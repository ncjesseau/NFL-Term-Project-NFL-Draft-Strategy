import pandas as pd
import streamlit as st
import altair as alt

# -----------------------
# PAGE SETUP
# -----------------------
st.set_page_config(page_title="NFL Draft Strategy Dashboard", layout="wide")

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/draft_strategy.csv")
    return df

df = load_data()

# Clean column names (fix Excel spacing issues)
df.columns = [col.strip().lower().replace("-", "_") for col in df.columns]
def map_position(pos):
    if pos in ["c", "g"]:
        return "IOL"
    elif pos in ["de", "olb"]:
        return "EDGE"
    elif pos in ["s", "saf"]:
        return "S"
    elif pos in ["nt", "dt"]:
        return "IDL"
    elif pos in ["ilb", "lb"]:
        return "LB"
    elif pos in ["t", "ot"]:
        return "T"
    else:
        return pos.upper()  # keep original but clean

df["position_group"] = df["position"].str.lower().apply(map_position)

# -----------------------
# TITLE + DESCRIPTION
# -----------------------
st.title("NFL Draft Strategy Dashboard")

st.markdown("""
This dashboard helps decision-makers evaluate which NFL draft strategies generate the strongest outcomes.

Use the filters on the left to explore performance, efficiency, and reliability across positions and draft rounds.
""")

# -----------------------
# SIDEBAR FILTERS
# -----------------------
st.sidebar.header("Filters")

positions = sorted(df["position_group"].dropna().unique())
selected_positions = st.sidebar.multiselect(
    "Select positions",
    positions,
    default=positions
)

rounds = sorted(df["round"].dropna().unique())
selected_rounds = st.sidebar.multiselect(
    "Select rounds",
    rounds,
    default=rounds
)

metric = st.sidebar.selectbox(
    "Metric for comparison",
    ["w_av", "value_per_pick", "games", "seasons_started"]
)

# -----------------------
# FILTER DATA
# -----------------------
filtered_df = df[
    (df["position_group"].isin(selected_positions)) &
    (df["round"].isin(selected_rounds))
].copy()

if filtered_df.empty:
    st.warning("No data matches your filters.")
    st.stop()

# -----------------------
# OVERVIEW METRICS
# -----------------------
st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Players", len(filtered_df))
col2.metric("Avg Weighted AV", round(filtered_df["w_av"].mean(), 2))
col3.metric("Avg Games", round(filtered_df["games"].mean(), 2))
col4.metric("Avg Seasons Started", round(filtered_df["seasons_started"].mean(), 2))

st.markdown("---")

# -----------------------
# CHART 1: POSITION VALUE
# -----------------------
st.subheader("1. Average Performance by Position")

position_summary = (
    filtered_df.groupby("position_group", as_index=False)
    .agg(
        avg_w_av=("w_av", "mean"),
        avg_value_per_pick=("value_per_pick", "mean"),
        avg_games=("games", "mean"),
        avg_seasons_started=("seasons_started", "mean"),
        players=("player_name", "count")
    )
    .sort_values("avg_w_av", ascending=False)
)

chart1 = alt.Chart(position_summary).mark_bar().encode(
    x=alt.X("position_group:N", sort="-y", title="Position"),
    y=alt.Y("avg_w_av:Q", title="Average Weighted AV"),
    tooltip=[
        "position_group",
        "avg_w_av",
        "avg_value_per_pick",
        "avg_games",
        "avg_seasons_started",
        "players"
    ]
).properties(height=400)

st.altair_chart(chart1, use_container_width=True)

st.markdown("""
This chart shows which positions tend to generate the highest overall player value.
""")

st.markdown("---")

# -----------------------
# CHART 2: HEATMAP
# -----------------------
st.subheader("2. Position Value by Draft Round")

round_position_summary = (
    filtered_df.groupby(["round", "position_group"], as_index=False)
    .agg(avg_metric=(metric, "mean"))
)

chart2 = alt.Chart(round_position_summary).mark_rect().encode(
    x=alt.X("round:O", title="Round"),
    y=alt.Y("position_group:N", title="Position"),
    color=alt.Color("avg_metric:Q", title=f"Avg {metric}"),
    tooltip=["round", "position_group", "avg_metric"]
).properties(height=450)

st.altair_chart(chart2, use_container_width=True)

st.markdown(f"""
This heatmap shows how positions perform across rounds using **{metric}**.
""")

st.markdown("---")

# -----------------------
# CHART 3: SCATTER
# -----------------------
st.subheader("3. Reliability vs Value")

chart3 = alt.Chart(filtered_df).mark_circle(size=70).encode(
    x=alt.X("games:Q", title="Games Played"),
    y=alt.Y("w_av:Q", title="Weighted AV"),
    color=alt.Color("position_group:N", title="Position"),
    tooltip=[
        "player_name",
        "position_group",
        "round",
        "pick",
        "games",
        "w_av",
        "seasons_started"
    ]
).interactive().properties(height=450)

st.altair_chart(chart3, use_container_width=True)

st.markdown("""
Players in the upper-right tend to combine durability and strong performance.
""")

st.markdown("---")

# -----------------------
# DECISION TOOL
# -----------------------
st.subheader("4. Decision Support Tool")

decision_round = st.selectbox(
    "Select a draft round",
    sorted(df["round"].dropna().unique())
)

decision_goal = st.selectbox(
    "Select your priority",
    [
        "Maximize value",
        "Find efficient picks",
        "Prioritize reliability"
    ]
)

decision_df = df[df["round"] == decision_round].copy()

if decision_goal == "Maximize value":
    decision_summary = (
        decision_df.groupby("position_group", as_index=False)
        .agg(score=("w_av", "mean"))
        .sort_values("score", ascending=False)
    )
    explanation = "highest average performance"

elif decision_goal == "Find efficient picks":
    decision_summary = (
        decision_df.groupby("position_group", as_index=False)
        .agg(score=("value_per_pick", "mean"))
        .sort_values("score", ascending=False)
    )
    explanation = "best value relative to draft position"

else:
    decision_summary = (
        decision_df.groupby("position_group", as_index=False)
        .agg(score=("games", "mean"))
        .sort_values("score", ascending=False)
    )
    explanation = "most reliable players"

top_positions = decision_summary.head(3)

st.write(f"""
For **Round {decision_round}**, the strongest positions based on **{explanation}** are:
""")

st.dataframe(top_positions, use_container_width=True)

st.info("""
Use this tool as a guide to inform draft strategy decisions.
It highlights historical trends rather than making definitive predictions.
""")

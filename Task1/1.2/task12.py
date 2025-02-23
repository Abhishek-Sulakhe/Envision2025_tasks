import streamlit as st
import pandas as pd

# Function to filter players
def filter_players(position, budget, df):
    filtered_df = df[df["player_positions"].str.contains(position, na=False, case=False)]
    filtered_df = filtered_df[filtered_df["value_eur"] <= budget]
    sorted_df = filtered_df.sort_values(by="overall", ascending=False)
    return sorted_df[["short_name", "player_positions", "overall", "potential", "value_eur"]]

# Streamlit App
st.title("Football Player Selection App")

# Load data
df = pd.read_csv("fifa22.csv")
# User Inputs
position = st.selectbox("Select Player Position", df['player_positions'].dropna().unique())
budget = st.number_input("Enter Budget (in Euros)", min_value=100000, value=100000000, step=100000)

if st.button("Find Players"):
    result = filter_players(position, budget, df)
    if not result.empty:
        st.write("### Matching Players:")
        st.dataframe(result)
    else:
        st.write("No players found within the given budget.")
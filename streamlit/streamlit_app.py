import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load and preprocess data
@st.cache_data
def load_data():
    try:
        df = pd.read_json('data/pl_data_dt.json')
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        df['year'] = df['date'].dt.year  # Add year column
        return df
    except FileNotFoundError as e:
        st.error(f"Data file missing: {e}")
        st.stop()

df = load_data()
teams = sorted(df['home_team'].unique())
years = sorted(df['year'].unique())  # Get all unique years

# Team Analysis Tab
selected_team = st.selectbox("Select Team for Analysis", teams)

if selected_team:
    team_data = df[(df['home_team'] == selected_team) | (df['away_team'] == selected_team)]
    if team_data.empty:
        st.error(f"No data available for {selected_team}")
    else:
        selected_year = st.select_slider("Select Year", options=years)
        year_data = team_data[team_data['year'] == selected_year]

        if year_data.empty:
            st.error(f"No data available for {selected_team} in {selected_year}")
        else:
            st.subheader(f"{selected_team} Performance in {selected_year}")
            
            # Add round range selection
            min_round, max_round = st.select_slider(
                "Select Round Range",
                options=list(range(1, 39)),
                value=(1, 38)
            )
            
            round_data = year_data[(year_data['round'] >= min_round) & (year_data['round'] <= max_round)]
            
            if round_data.empty:
                st.error(f"No data available for {selected_team} in rounds {min_round}-{max_round}")
            else:
                st.subheader(f"Performance from Round {min_round} to {max_round}")

                col1, col2 = st.columns(2)

                with col1:
                    # Goals trend over time
                    goals_fig = go.Figure()
                    goals_fig.add_trace(go.Scatter(
                        x=round_data['round'],
                        y=round_data.apply(lambda x: x['home_goals'] if x['home_team'] == selected_team else x['away_goals'], axis=1),
                        mode='lines+markers',
                        name="Goals"
                    ))
                    goals_fig.update_layout(
                        title=f"{selected_team} - Goals ({selected_year}, Rounds {min_round}-{max_round})",
                        xaxis_title="Round",
                        yaxis_title="Goals"
                    )
                    st.plotly_chart(goals_fig)

                with col2:
                    # Shot efficiency trend
                    shot_efficiency_fig = go.Figure()
                    shot_efficiency_fig.add_trace(go.Scatter(
                        x=round_data['round'],
                        y=round_data.apply(lambda x: x['home_shot_efficiency'] if x['home_team'] == selected_team 
                                        else x['away_shot_efficiency'], axis=1),
                        mode='lines+markers',
                        name="Shot Efficiency"
                    ))
                    shot_efficiency_fig.update_layout(
                        title=f"{selected_team} - Shot Efficiency ({selected_year}, Rounds {min_round}-{max_round})",
                        xaxis_title="Round",
                        yaxis_title="Shot Efficiency"
                    )
                    st.plotly_chart(shot_efficiency_fig)

                # Average performance bar
                avg_goals = round_data.apply(
                    lambda x: x['home_goals'] if x['home_team'] == selected_team else x['away_goals'], axis=1).mean()
                avg_shot_efficiency = round_data.apply(
                    lambda x: x['home_shot_efficiency'] if x['home_team'] == selected_team else x['away_shot_efficiency'], axis=1).mean()

                avg_fig = go.Figure(data=[
                    go.Bar(name="Goals", x=["Goals"], y=[avg_goals]),
                    go.Bar(name="Shot Efficiency", x=["Shot Efficiency"], y=[avg_shot_efficiency])
                ])
                avg_fig.update_layout(
                    title=f"{selected_team} - Averages (Rounds {min_round}-{max_round})",
                    yaxis_title="Average Value",
                    barmode='group'
                )
                st.plotly_chart(avg_fig)

                # Performance metrics
                metrics = st.columns(4)
                with metrics[0]:
                    st.metric("Average Goals", f"{avg_goals:.2f}")

                with metrics[1]:
                    avg_shots = round_data.apply(
                        lambda x: x['home_shots'] if x['home_team'] == selected_team else x['away_shots'], axis=1).mean()
                    st.metric("Average Shots", f"{avg_shots:.2f}")

                with metrics[2]:
                    shot_accuracy = round_data.apply(
                        lambda x: x['home_shots_on_goal'] / x['home_shots'] if x['home_team'] == selected_team 
                        else x['away_shots_on_goal'] / x['away_shots'], axis=1).mean()
                    st.metric("Shot Accuracy", f"{shot_accuracy:.2%}")

                with metrics[3]:
                    danger_ratio = round_data.apply(
                        lambda x: x['home_danger_ratio'] if x['home_team'] == selected_team 
                        else x['away_danger_ratio'], axis=1).mean()
                    st.metric("Danger Ratio", f"{danger_ratio:.2%}")
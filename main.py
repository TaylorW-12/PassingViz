import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns
import streamlit as st
import csv

df=pd.read_csv('Womendata.csv')


# Drawing the pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor('#22312b')

# Plot passing lines
for idx, row in df.iterrows():
    if row['pass_outcome'] == 'Incomplete':
        plt.plot(
            [row['x'], row['endX']],
            [row['y'], row['endY']],
            color='green'
        )

for idx, row in df.iterrows():
    if row['pass_outcome'] == 'Out':
        plt.plot(
            [row['x'], row['endX']],
            [row['y'], row['endY']],
            color='blue'
        )

for idx, row in df.iterrows():
    if row['pass_outcome'] == 'Complete':
        plt.plot(
            [row['x'], row['endX']],
            [row['y'], row['endY']],
            color='purple'
        )


plt.gca().invert_yaxis()
plt.show()
print(df)

# Streamlit App Layout
st.title("Pass Visualization (2023 International Women's World Cup- Spain vs Sweden) App")
st.sidebar.header("Filters")

# Dropdown for pass outcome
pass_outcome = st.sidebar.selectbox("Select Pass Outcome", ['Incomplete', 'Out'])

# Dropdown for player selection
player = st.sidebar.selectbox("Select Player (Spain's Roster)", ['All'] + df['player'].unique().tolist())

# Slider for time range
time_range = st.sidebar.slider("Select Time Range (minutes)", min_value=0, max_value=90, value=(0, 90))

# Filter data based on selections
filtered_df = df[df['pass_outcome'] == pass_outcome]

if player != 'All':
    filtered_df = filtered_df[filtered_df['player'] == player]

filtered_df = filtered_df[(filtered_df['minute'] >= time_range[0]) & (filtered_df['minute'] <= time_range[1])]

# Draw pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(10, 7))
fig.set_facecolor('#22312b')

# Plot passes
for _, row in filtered_df.iterrows():
    plt.plot(
        [row['x'], row['endX']],
        [row['y'], row['endY']],
        color='green',
        linewidth=2,
        alpha=0.7
    )

st.pyplot(fig)



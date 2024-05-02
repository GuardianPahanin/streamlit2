import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('athlete_events.csv')
    return data

df = load_data()

# Title
st.title('Olympic Athletes Dataset Explorer')

# Introduction
st.write('This app allows you to explore the Olympic athletes dataset.')

# Data Summary
st.write(f'The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.')

# Data Preview
if st.checkbox('Show Data Preview'):
    st.write(df.head())

# Unique Teams
teams = df['Team'].unique()

st.sidebar.title('Filter Data')
# Data Filtering
team = st.sidebar.selectbox('Team', teams)

filtered_df = df[df['Team'] == team]

# Unique Seasons, Sports, and Medals based on the selected Team
filtered_seasons = filtered_df['Season'].unique()
filtered_sports = filtered_df['Sport'].unique()
filtered_medals = filtered_df['Medal'].unique()

# Data Filtering based on the selected Team
season = st.sidebar.selectbox('Season', filtered_seasons)
sport = st.sidebar.selectbox('Sport', filtered_sports)
medal = st.sidebar.selectbox('Medal', filtered_medals)

filtered_df = filtered_df[(filtered_df['Season'] == season) &
                          (filtered_df['Sport'] == sport) &
                          (filtered_df['Medal'] == medal)]

# Data Visualization
st.write(f'Number of rows after filtering: {filtered_df.shape[0]}')
if st.checkbox('Show Filtered Data'):
    st.write(filtered_df)

# Line Chart - All Data
if st.checkbox('Show Line Chart - All Data'):
    all_data_line = df.groupby('Year').size()
    st.line_chart(all_data_line)

# Line Chart - Filtered Data
if st.checkbox('Show Line Chart - Filtered Data'):
    filtered_data_line = filtered_df.groupby('Year').size()
    st.line_chart(filtered_data_line)

# Histogram - Distribution of Athlete Ages
st.write('### Distribution of Athlete Ages')
st.hist(filtered_df['Age'], bins=20, edgecolor='black')
st.pyplot()

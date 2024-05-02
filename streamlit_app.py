import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Unique Teams and Sports
teams = df['Team'].unique()
sports = df['Sport'].unique()

st.sidebar.title('Filter Data')
# Data Filtering
sex = st.sidebar.selectbox('Sex', ['M', 'F'])
age = st.sidebar.slider('Age', min_value=10, max_value=100, value=(10, 100))
team = st.sidebar.selectbox('Team', teams)
year = st.sidebar.slider('Year', min_value=df['Year'].min(), max_value=df['Year'].max(), value=(df['Year'].min(), df['Year'].max()))
season = st.sidebar.selectbox('Season', ['Summer', 'Winter'])
sport = st.sidebar.selectbox('Sport', sports)
medal = st.sidebar.selectbox('Medal', ['Gold', 'Silver', 'Bronze', 'NA'])

# Filtered Data
filtered_df = df[
    (df['Sex'] == sex) &
    (df['Age'] >= age[0]) & (df['Age'] <= age[1]) &
    (df['Team'] == team) &
    (df['Year'] >= year[0]) & (df['Year'] <= year[1]) &
    (df['Season'] == season) &
    (df['Sport'] == sport) &
    (df['Medal'] == medal)
]

# Data Visualization
st.write(f'Number of rows after filtering: {filtered_df.shape[0]}')
if st.checkbox('Show Filtered Data'):
    st.write(filtered_df)

# Line Chart - Number of Athletes Over Time (All Data)
st.write('### Number of Athletes Over Time (All Data)')
line_data_all = df.groupby('Year').size()
st.line_chart(line_data_all)

# Line Chart - Number of Athletes Over Time (Filtered Data)
st.write('### Number of Athletes Over Time (Filtered Data)')
line_data_filtered = filtered_df.groupby('Year').size()
st.line_chart(line_data_filtered)

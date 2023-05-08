import streamlit as st
import pandas as pd
import numpy as np
import csv
import pickle

st.set_page_config(
    page_title="UK-AU FTA Summary",
)

st.title('See Summaries of the UK-AU FTA')

## user inputs
#read in topics and provide as a list of options in a dropdown
with open('topic_dict.pkl', 'rb') as f:
    topics = pickle.load(f)
topic = st.selectbox(
    'Select a topic to see a summary for.',
    list(topics.values()))
#create slider to allow probablility to be selected
prob = st.slider('Select minimum probability that text relates a topic before it is included in the summary.', min_value = 0.0,
                           max_value = 1.0, value = 0.9, step = 0.01)

## read in data to be used
my_df = pd.read_csv('article_topics.csv')

#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done! (using st.cache_data)")

#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(my_df)
    st.write(topics)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)


#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)

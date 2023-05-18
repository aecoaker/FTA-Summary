import streamlit as st
import pandas as pd
import numpy as np
import csv
import pickle

st.set_page_config(
    page_title="UK-AU FTA Summary",
)

st.title('Summarise the UK-AU Free Trade Agreement')
st.subheader('Generate summaries of the FTA for different topics')

## user inputs
#read in topics and provide as a list of options in a dropdown
with open('topic_dict.pkl', 'rb') as f:
    topics = pickle.load(f)
topic = st.selectbox(
    'Select a topic to see a summary for.',
    list(topics.values()))
t = list(topics.keys())[list(topics.values()).index(topic)]

#create slider to allow probablility to be selected
#prob = st.slider('Select the lowest probability that text relates to this topic before it is summarised.', min_value = 0.0,
#                           max_value = 1.0, value = 0.8, step = 0.2)

## read in summaries from CSV
#then just need to select correct one according to use input


st.subheader('Top Level Summary')
#abstrative summarisation here
with open('summaries.pkl', 'rb') as f:
    summaries = pickle.load(f)
st.markdown(summaries[t])

st.subheader('In Depth Summary')
#summaries from chunks here
with open('pre_recursive_summaries.pkl', 'rb') as f:
    pre_recursive_summaries = pickle.load(f)
st.markdown(pre_recursive_summaries[t])

st.subheader('Source')
st.markdown('The summaries regarding "' + str(topic) + '" are sources from the\nfollowing chapters and articles in the FTA.')
#list chapters and articles here




#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done! (using st.cache_data)")

#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(article_text_chunks)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)


#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)

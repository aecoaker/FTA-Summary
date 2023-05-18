import streamlit as st
import pandas as pd
import numpy as np
import csv
import pickle

st.set_page_config(
    page_title="UK-AU FTA Summary",
)

st.title('Summarise the UK-AU Free Trade Agreement (FTA)')
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
st.markdown('The summaries regarding "' + str(topic) + '" are sourced from the\nfollowing chapters and articles in the FTA:')
#bring in the topic classification
article_topics = pd.read_csv('article_topics.csv')
articles = article_topics[article_topics[('prob_t' + str(t))] >= 0.9]
#some styling to do present this nicely
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
#print this
st.table(articles[['Chapter', 'Article']])

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
#create slider to allow probablility to be selected
prob = st.slider('Select the lowest probability that text relates to this topic before it is summarised.', min_value = 0.0,
                           max_value = 1.0, value = 0.9, step = 0.01)

## read in data to be used 
articles_df = pd.read_csv('article_topics.csv')
#filter to get articles relevant to user selection
t = list(topics.keys())[list(topics.values()).index(topic)]
articles_to_sum = articles_df[articles_df[('prob_t' + str(t))] >= prob]
#put text into one string and then split out according to length limits
article_text = ' '.join(articles_to_sum['Article Text'])
def summary_chunks(text):
    chunks = []
    words = text.split()
    for i in range(0, len(words), 700):
      chunks.append(" ".join(words[i:i+700]))
    return chunks
article_text_chunks = summary_chunks(article_text)

## summarise the chunks
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
tokeniser = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
inputs = [tokeniser.batch_encode_plus([text],return_tensors='pt') for text in article_text_chunks]
summary_ids = [model.generate(i['input_ids'], early_stopping=True) for i in inputs]



#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done! (using st.cache_data)")

#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(article_text_chunks)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)


#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)

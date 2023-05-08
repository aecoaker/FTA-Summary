import streamlit as st
import pandas as pd
import numpy as np
import csv
import pickle

st.set_page_config(
    page_title="UK-AU FTA Summary",
)

st.title('FAQs - Summarise the UK-AU FTA')

st.subheader('Where do the topics come from?')
st.write("""The topics were generated from the text using a method called \'Latent Dirichlet Allocation\' (LDA). This is a
         statistical form of Natural Language Processing which considers the frequency of different words with different
         texts or parts of text (in this case articles). Words that appear together frequently are assumed to form a 'topic'
         together. We begin by assuming there are a number of topics, in this case 20, and that the distribution of words
         within a topic, and the distribution of topics within a text both follow Dirichlet distributions. The model then
         uses the observed frequencies to fit the distributions and thus deduces the potential topics. The titles of these 
         topics must be assigned manually and this was done by the author. 
         After this has been done, each text/piece of text (in this case each article within the FTA) has a topic (or topics) 
         associated with it. Alongside these are probabilities that indicated, based on the observed frequencies, how likely an
         article is to belong to a topic. The slider in the summariser allows a minimum limit for this probability to be set. 
         At 0, any article that may belong to that topic, even if it has a low probability of doing so, will be summarised. 
         Conversely, at 1, only articles that definetely belong to a topic are summarised. """)

st.subheader('How is the text summarised?')
st.write("""Streamlit is **_really_ cool**.""")

st.subheader('Who might use this?')
st.write("""Streamlit is **_really_ cool**.""")
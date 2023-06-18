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
         topics must be assigned manually and this was done by the author.""")
st.write("""After this has been done, each text/piece of text (in this case each article within the FTA) has a topic (or topics) 
         associated with it. Alongside these are probabilities that indicated, based on the observed frequencies, how likely an
         article is to belong to a topic. The slider in the summariser allows a minimum limit for this probability to be set. 
         At 0, any article that may belong to that topic, even if it has a low probability of doing so, will be summarised. 
         Conversely, at 1, only articles that definetely belong to a topic are summarised.""")

st.subheader('How is the text summarised?')
st.write("""Once a subset of the text from the FTA has been selected as belonging to a particular topics, it is summarised using
         a model called 'BART'. This is a neural network which moved data through 'neurons' which manipulate it according to many 
         millions of parameters in an attempt to replicate the mammalian brain.""")
st.write("""Neural Networks are the most modern technique used in Natural Language Processing and continue to make waves in popular
         culture with advancements freqently making the news. That said, they do have their limits, in particular BART is limited in
         the length of text that it can take as input. This is approximately 1000 words. In order to meet this, the subset of text
         is split into chunks, each of these is summarised, and those summarisations themselves are joined together and summarised.
         This results in the 'in-depth' and 'top-level' summarisations respectively.""")

st.subheader('Who might use this?')
st.write("""Free Trade Agreements are long and complex texts, designed to go into detail about all possible ways that ways that
         states can restrict the ways in which they trade. This is necessary from a legislative point of view but makes them
         difficult to navigate for citizens who need to know how they apply to them and their business. A such, providing simple 
         summaries of these texts that are relevant to users is a matter of public good.""")

st.subheader('Why are only some in-depth summaries shown?')
st.write("""Some topics contain more text than others, because of this, some shorter topics have in-depth summaries that are quite short. 
            Therefore only in-depth summaries that are significantly longer and more detailed than the top level summaries are printed.""")
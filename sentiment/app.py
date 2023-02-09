import streamlit as st
from textblob import TextBlob
st.header('Sentiment Analysis')
st.image('sentiment.jpg')
text=st.text_input(label="Enter your text")
if TextBlob(text).sentiment[0]>0:
    sent='Positive 😊'
elif TextBlob(text).sentiment[0]==0:
    sent='Neutral 😐'
else:
    sent='Negative 🙁'
if st.button('Get sentiment'):
        st.text(f'The sentiment for this text is {sent}')



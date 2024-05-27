import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.write("Favorite Song")
x = st.text_input("Song", "A Lot's Gonna Change")

def getSongStats(song: str):
    '''
    Using the song name, this function will return the song's stat and listening history by utilizing an API

    Returns a DataFrame and a histogram of the listening history
    '''

    #TODO: Implement API call
    songData = pd.DataFrame({'Song Name': [song], 'Rating': [5], 'Artist': ['Weyes Blood']})
    listeningHistory = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Number of listens': [1000, 2000, 1500]})

    return songData, listeningHistory

if st.button("Click Me"):
    st.write(f"Your favorite song is `{x}`")
    data, listeningHistory = getSongStats(x)
    st.write(data)

    st.line_chart(data = listeningHistory, x = 'Date', y = 'Number of listens')

# -*- coding:utf-8 -*-
import streamlit as st 
import pandas as pd 

@st.cache_data
def load_data():
    train = pd.read_csv("dataset/train.csv")
    return train

def main():
    st.title("Hello World!")
    st.title("Hello World!!")

    train = load_data()
    st.dataframe(train)

if __name__ == "__main__":
    main()
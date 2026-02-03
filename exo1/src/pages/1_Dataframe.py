import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/quotes.csv")

st.set_page_config(page_title="Dataframe and basic analysis", page_icon=":books:")
st.title("Dataframe and basic analysis")

st.dataframe(df, hide_index=True)

def get_null_values(df : pd.DataFrame) -> pd.DataFrame:
    return df.isnull().sum()

def get_quote_by_year(df : pd.DataFrame) -> pd.DataFrame:
    """Get the number of quotes by year"""
    return df.groupby("year").size()

def sort_quote_by_length(df : pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="quote", key=lambda x: x.str.len())

def get_quotes_that_contain(df : pd.DataFrame, word : str) -> pd.DataFrame:
    return df[df.quote.str.contains(word, case=False)]

st.write("Null values : ", get_null_values(df))

st.write("Number of rows : ", len(df))

st.write("Number of columns : ", len(df.columns))

st.write(f"Year with the most quotes : {get_quote_by_year(df).idxmax()} with {get_quote_by_year(df).max()} quotes")
st.write(f"Year with the least quotes : {get_quote_by_year(df).idxmin()} with {get_quote_by_year(df).min()} quotes")

st.write("Longest quote : ", sort_quote_by_length(df).iloc[-1])
st.write("Shortest quote : ", sort_quote_by_length(df).iloc[0])

st.write("Quotes that contain 'Victor Hugo' : ", get_quotes_that_contain(df, "Victor Hugo"))

st.write("Quotes that contain 'Pokémon' : ", get_quotes_that_contain(df, "Pokémon"))


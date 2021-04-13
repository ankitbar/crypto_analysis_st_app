import streamlit as st
from datetime import datetime
import coinapi_functions as cf
import graph_utils as gu
import json
import requests
import pandas as pd
import plotly.graph_objects as go
import os

st.title('Cryptocurrency Analysis')

conversion_from = st.sidebar.selectbox(
    "Conversion From",
    ("LTC", "BTC", "XRP","ETH")
)

conversion_to = st.sidebar.selectbox(
    "Conversion To",
    ("INR","USD","GBP")
)

date_from = st.sidebar.date_input(
	"Start Date"
)

date_to = st.sidebar.date_input(
	"End Date"
)

data_freq_unit = st.sidebar.selectbox(
	"Data Frequency (Unit)",
	("SEC","MIN","HRS","DAY","MTH","YRS")
)

timeperiod_dict = {"SEC":[1,2,3,4,5,6,10,15,20,30],"MIN":[1,2,3,4,5,6,10,15,20,30],"HRS":[1,2,3,4,6,8,12],"DAY":[1,2,3,5,7,10],"YRS":[1,2,3,4,5]}

data_freq_val = st.sidebar.selectbox(
	"Data Frequency (Value)",
	timeperiod_dict[data_freq_unit]
)


num_records = st.sidebar.number_input("Max records",1,100000)

# Pre-evaluation input processing
data_freq = str(data_freq_val) + data_freq_unit
time_start = date_from.strftime("%Y-%m-%d") + "T00:00:00"
time_end = date_to.strftime("%Y-%m-%d") + "T00:00:00"

# Read in the API key
api_key = st.secrets['api_key']

# Get data and display charts
if st.button("Get Data"):
	result_df = cf.get_ohlcv_data(conversion_from,conversion_to,data_freq,time_start,time_end,num_records,api_key)
	fig = gu.create_candlestick_chart(result_df,conversion_from,conversion_to)
	st.write(fig)
else:
	st.write("Get going, user!")
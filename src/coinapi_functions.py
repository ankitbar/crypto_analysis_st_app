import json
import requests
import pandas as pd
import datetime as dt

# Store api key, base url etc

# api_key = ""
# conversion_from = "LTC"
# conversion_to = "GBP"
# period_id = "1DAY"
# time_start = "2020-12-01T00:00:00"
# time_end = "2020-12-24T00:00:00"
# num_records = 100000

# Function to get Order High Low Close Value data from coinapi

def get_ohlcv_data(conversion_from,conversion_to,period_id,time_start,time_end,num_records,api_key):

    ohlcv_url = "https://rest.coinapi.io/v1/ohlcv/"
    request_url = ohlcv_url + conversion_from + "/" + conversion_to + "/history?" + "period_id=" + period_id + "&time_start=" + time_start + "&time_end=" + time_end + "&limit="+str(num_records)
    headers = {"X-CoinAPI-Key" : api_key}
    response = requests.get(request_url, headers = headers)
    if(response.status_code == 429):
        # API response
        return("Too many requests.")
    response_text = json.loads(response.text)
    # print(response_text)
    return(pd.DataFrame.from_records(response_text))
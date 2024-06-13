import inspect
import textwrap
import streamlit as st
from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts
import pandas as pd
import json
import random
import os.path
import requests


import ast





def main():
    st.title("SF Racial Justice Act")
    
    # st.divider()
    
    with st.sidebar:
        toggle = ("11351","11351.5","11352","11375","11378","11351|11351.5|11352|11375|11378")
        
        ch = st.selectbox(
            label="Select Type",
            options=toggle,
        )
        status_options = ('filed','booked','convicted','1385 PC - Guilty Plea to Other Charge')

        

    df = pd.read_csv("analysis_dashboard.csv")
    df["race_distribution_dict"] = df["race_distribution_dict"].apply(lambda x: ast.literal_eval(x))
    x1 = list(df[(df['status'] == 'filed') & (df['charge'] == '11351')]["race_distribution_dict"].iloc[0].keys())
    y1= {}
    for y in status_options:
        fil = df[(df['status'] == y) & (df['charge'] == ch)]
        x2 = []
        for x in x1:
            if x in fil["race_distribution_dict"].iloc[0].keys():
                x2.append(fil["race_distribution_dict"].iloc[0][x])
            else:
                x2.append(0)
        y1[y] = x2
    
    st.markdown("Selected Charge - **"+ch+"**")
    options = {
        "tooltip": {"trigger": "item", "axisPointer": {"type": "shadow"}, "order" : "valueDesc"},
        "legend": {"type" : "plain", "top" : 2,
                   "textStyle": {"fontSize" : 18, 'color' : 'white' }
                  },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {},
        "yAxis": {
            "axisLabel" : {
                 "fontWeight" : "bolder",
                 "fontSize" : 18,
                "color": "white"
            },
            "data": x1
        },
        
        
        "series": [
            {
                "name": "Booked charges",
                "type": "bar",
                "stack": "total",
                "label": {
                    "show": True,
                    "position" : "center",
                    "color" : "white"
                         },
                "data": y1['booked'],
            },
            
       
            {
                "name": "Filed Charges",
                "type": "bar",
                "stack": "total",
                "label": {
                    "show": True,
                    "position" : "center",
                    "color" : "white"
                         },
                "data": y1['filed'],
            },
            
       
            {
                "name": "Convicted Charges",
                "type": "bar",
                "stack": "total",
                "label": {
                    "show": True,
                    "position" : "center",
                    "color" : "white"
                         },
                "data": y1['convicted'],
            },

            {
                "name": '1385 PC - Guilty Plea to Other Charge',
                "type": "bar",
                "stack": "total",
                "label": {
                    "show": True,
                    "position" : "center",
                    "color" : "white"
                         },
                "data": y1['1385 PC - Guilty Plea to Other Charge'],
            },
            
        ],
        }
    st_echarts(options=options, height="600px",width="500px")


       
if __name__ == "__main__":
    st.set_page_config(
        page_title="RJA", page_icon=":chart_with_upwards_trend:"
    )
    main()
    

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
    st.title("California Racial Justice Act")
    
    # st.divider()
    
    with st.sidebar:
        toggle = ("11351","11351.5","11352","11375","11378")
        
        ch = st.selectbox(
            label="Select Type",
            options=toggle,
        )
        status_options = ('filed','booked','convicted','1385 PC - Guilty Plea to Other Charge')
        stage = st.selectbox(
            label="Select stage",
            options=status_options,
        )
        

    df = pd.read_csv("analysis_dashboard.csv")
    df["race_distribution_dict"] = df["race_distribution_dict"].apply(lambda x: ast.literal_eval(x))
    fil = df[(df['status'] == stage) & (df['charge'] == ch)]
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
            "data": list(fil["race_distribution_dict"].iloc[0].keys())
        },
        
        
        "series": [
            {
                "name": "Annual Eligible Caseload",
                "type": "bar",
                "stack": "total",
                "label": {
                    "show": True,
                    "position" : "center",
                    "color" : "white"
                         },
                "data": list(fil["race_distribution_dict"].iloc[0].values()),
            },
            
        ],
        }
    st_echarts(options=options, height="500px")


       
if __name__ == "__main__":
    st.set_page_config(
        page_title="RJA", page_icon=":chart_with_upwards_trend:"
    )
    main()
    


#from collections import namedtuple
#import altair as alt
#import math
import pandas as pd
#import streamlit as st

"""
# Dataframe Viewer
"""

url = 'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv'
df = pd.read_csv(url, index_col=0)

df

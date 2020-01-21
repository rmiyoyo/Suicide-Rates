import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('master.csv')
fig = px.line(df, x = 'country', y = 'suicides_no', title='Number of suicdes')
fig.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

csv_data = pd.read_csv('master.csv')
fig = px.line(csv_data, x = 'country', y = 'suicides_no', title='Number of suicdes')
fig.show()

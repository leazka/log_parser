from parser import parser
import plotly.express as px
import pandas as pd

for i in range(1, 7):
    list_of_diffs = parser(i)
    df = pd.DataFrame(list_of_diffs)
    fig = px.line(df, x='ts', y='diff', title='Difference in time for joint %s' % i)
    fig.show()

from statsmodels.graphics.tsaplots import plot_acf
import plotly.express as px
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Solar Energy Generation Analysis Plotting -- Michael Burak')

plotly_df = pd.read_csv("plotly_df.csv")

fig = px.scatter(plotly_df, x="Timestamp", y="Megawatthours",
                 title="Net generation from solar for US Lower 48, 07-2018 to current",
                 labels={"Timestamp": ""})

fig.update_traces(marker=dict(
    size=4,
    color="black",
    colorscale='Viridis',
    showscale=True
))

st.plotly_chart(fig, use_container_width=True)

st.title("Pandas to Plotly Lag Plot POC")
pd.plotting.lag_plot(plotly_df['Megawatthours'])
fig = plt.gcf()
st.plotly_chart(fig)

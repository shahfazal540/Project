import seaborn as sns
import matplotlib as plt
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv(r"C:\Users\A2Z\Desktop\Project\Dashboard\Data\shopping_trends.csv")

st.title("Customer Feedback")
st.sidebar.header("Filter Options")


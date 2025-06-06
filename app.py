
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load the segmented data
df = pd.read_csv("customer_segments.csv")

# Sidebar - filter by cluster
st.sidebar.title("Segment Selector")
clusters = sorted(df["Cluster"].unique())
selected_cluster = st.sidebar.selectbox("Choose a Segment", clusters)

# Filtered data
filtered_df = df[df["Cluster"] == selected_cluster]

st.title("Customer Segmentation Dashboard")
st.write(f"## Segment {selected_cluster} Overview")

# Summary stats
st.write(filtered_df.describe())

# Revenue distribution
st.subheader("Monthly Revenue Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df["MonthlyRevenue"], kde=True, ax=ax)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os

# --- LOGIN SECTION START ---
USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "1234")

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()
# --- LOGIN SECTION END ---

# Your original app starts here
# Load the segmented data
df = pd.read_csv("customer_segments.csv")

# Sidebar - filter by cluster
st.sidebar.title("Segment Selector")
clusters = sorted(df["Cluster"].unique())
selected_cluster = st.sidebar.selectbox("Choose a Segment", clusters)

# Filtered data
filtered_df = df[df["Cluster"] == selected_cluster]

st.title("Customer Segmentation Dashboard")
st.write(f"## Segment {selected_cluster} Overview")

# Summary stats
st.write(filtered_df.describe())

# Revenue distribution
st.subheader("Monthly Revenue Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df["MonthlyRevenue"], kde=True, ax=ax)
st.pyplot(fig)

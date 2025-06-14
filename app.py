import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

# --- User Authentication Setup ---
# Password hashing
hashed_passwords = stauth.Hasher(['1234']).generate()

# Config dictionary
credentials = {
    'usernames': {
        'swati': {
            'name': 'Swati Sharma',
            'password': hashed_passwords[0]
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    'customer_dashboard',   # cookie name
    'abcdef',               # key
    cookie_expiry_days=1
)

# Login
name, authentication_status, username = authenticator.login('Login', 'main')

# --- Authenticated App ---
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f"Welcome {name}!")

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

elif authentication_status == False:
    st.error("Username or password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")

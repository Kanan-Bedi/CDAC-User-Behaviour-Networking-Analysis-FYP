import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up Blob Storage connection
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@st.cache_data
def load_data():
    # Access the blob client
    container_name = "ueba"  # Replace with your container name
    blob_name = "updated_final_4.2.csv"  # Replace with your blob name (CSV file)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Download CSV data directly into a DataFrame
    with blob_client.download_blob() as blob_data:
        data = pd.read_csv(blob_data)
    return data

data = load_data()

# Splitting the dataset into features and target
X = data.drop(columns=['malicious'])
y = data['malicious']

# Title and description
st.title("User and Entity Behavior Analytics (UEBA) Dashboard")
st.write("This dashboard provides insights into user and entity behavior to help detect anomalies and insider threats.")

# Sidebar to choose visualization
action_choice = st.sidebar.selectbox("Choose an analysis to view:", ("Data Summary", "Anomaly Distribution", "Feature Analysis", "Time-based Behavior Analysis"))

if action_choice == "Data Summary":
    st.subheader("Dataset Summary")
    st.write("Basic statistics of the dataset, including feature summary and target variable distribution.")
    st.write(data.describe())
    st.write("Shape of the dataset:", data.shape)
    st.write("Columns in the dataset:", data.columns.tolist())
    st.write("Distribution of Malicious Labels:")
    st.bar_chart(data['malicious'].value_counts())

elif action_choice == "Anomaly Distribution":
    st.subheader("Anomaly Distribution")
    st.write("Visualizing the distribution of anomalies detected in the dataset.")
    fig, ax = plt.subplots()
    sns.countplot(x=y, palette='viridis', ax=ax)
    ax.set_title("Distribution of Malicious vs Non-Malicious Instances")
    ax.set_xlabel("Malicious (1 = Yes, 0 = No)")
    ax.set_ylabel("Count")
    st.pyplot(fig)

elif action_choice == "Feature Analysis":
    st.subheader("Feature Analysis")
    st.write("Explore the relationships between different features in the dataset.")
    feature = st.selectbox("Select a feature to analyze:", X.columns)
    fig, ax = plt.subplots()
    sns.histplot(X[feature], kde=True, ax=ax, color='blue')
    ax.set_title(f"Distribution of {feature}")
    ax.set_xlabel(feature)
    st.pyplot(fig)

    st.write("Correlation with Malicious Label:")
    correlation = data[[feature, 'malicious']].corr().iloc[0, 1]
    st.write(f"Correlation between {feature} and Malicious: {correlation:.2f}")

elif action_choice == "Time-based Behavior Analysis":
    st.subheader("Time-based Behavior Analysis")
    st.write("Analyzing user behavior over time to identify potential anomalies.")
    if 'day' in data.columns:
        day_counts = data['day'].value_counts().sort_index()
        st.line_chart(day_counts)
        st.write("This chart shows the number of activities performed on each day, which helps in identifying unusual activity spikes.")
    else:
        st.write("The dataset does not contain a 'day' column for time-based analysis.")

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.write("1. Save this code as `app.py`.")
st.sidebar.write("2. Run: `streamlit run app.py` in your terminal.")
st.sidebar.write("3. Use the sidebar to select an analysis to view.")

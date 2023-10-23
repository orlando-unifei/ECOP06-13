import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data from the web (replace 'your_data_url.csv' with the actual URL)
data_url = 'https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv'
df = pd.read_csv(data_url)

st.set_page_config("Hospital Management","https://unifei.edu.br/wp-content/themes/twentytwelve-child/img/cabecalho/logo-unifei-oficial.png")

# Create a Streamlit web app
st.title("Blood Pressure Analysis")

# Sidebar for user input
st.sidebar.header("Filters")
selected_gender = st.sidebar.selectbox("Select Gender:", ["All", "Female", "Male"])
selected_age_group = st.sidebar.selectbox("Select Age Group:", ["All", "30-45", "46-59", "60+"])

# Function to parse age groups
def parse_age_group(age_group):
    if age_group == "30-45":
        return (30, 45)
    elif age_group == "46-59":
        return (46, 59)
    elif age_group == "60+":
        return (60, 120)  # Assuming 120 as a maximum age
    else:
        return (0, 120)  # Default to all ages

# Filter the data based on user selection
filtered_df = df.copy()
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["sex"] == selected_gender]
if selected_age_group != "All":
    min_age, max_age = parse_age_group(selected_age_group)
    filtered_df = filtered_df[filtered_df["agegrp"] == selected_age_group]
    
# Main content
st.subheader("Selected Data:")
st.write(filtered_df)

# Plot blood pressure before and after
if not filtered_df.empty:
    fig, ax = plt.subplots()
    for group, data in filtered_df.groupby("sex"):
        bp_before = data["bp_before"]
        bp_after = data["bp_after"]
        ax.scatter(bp_before, bp_after, label=group)
    ax.set_xlabel("Blood Pressure Before")
    ax.set_ylabel("Blood Pressure After")
    ax.set_title("Blood Pressure Before vs. After")
    ax.legend()
    st.subheader("Blood Pressure Scatter Plot:")
    st.pyplot(fig)
else:
    st.warning("No data available for the selected filters.")
import streamlit as st
import pandas as pd
from preprocessor import (
    load_generation_data,
    load_weather_data,
    daily_production_distribution,
    daily_production_density_per_source,
    average_daily_ac_dc_power,
    total_production_distribution,
    daily_total_ac_dc_power,
    weekly_production,
    temperature_trends,
    daily_avg_temp_irradiation,
    daily_min_max_temp,
    correlation_temp_irradiation,
)

# Set up the main dashboard
st.set_page_config(page_title="Solar Power Plant Dashboard", layout="wide")

# Title and description
st.title("Solar Power Plant Analysis Dashboard")
st.write("This dashboard allows you to explore power generation and weather data from two solar power plants in India.")

st.image("PLANT ANALYSIS (1).png", caption="Solar Power Plant Analysis logo",  width=400, use_column_width=50)

# Load the datasets
generation_data_plant_1 = load_generation_data('Plant_1_Generation_Data.csv')
weather_data_plant_1 = load_weather_data('Plant_1_Weather_Sensor_Data.csv')
generation_data_plant_2 = load_generation_data('Plant_2_Generation_Data.csv')
weather_data_plant_2 = load_weather_data('Plant_2_Weather_Sensor_Data.csv')

# Sidebar for dataset selection
st.sidebar.title("Select Data")
dataset_selection = st.sidebar.radio(
    "Select dataset:",
    ("Generation Data - Plant 1", "Weather Data - Plant 1", 
     "Generation Data - Plant 2", "Weather Data - Plant 2")
)

# Sidebar for multiselect options
if dataset_selection == "Generation Data - Plant 1":
    st.sidebar.subheader("Select Analysis for Plant 1 Generation Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Daily Production Distribution",
            "Daily Production Density per Source",
            "Average Daily AC/DC Power",
            "Total Production Distribution",
            "Daily Total AC/DC Power",
            "Weekly Production",
        ],
    )
    df = generation_data_plant_1
elif dataset_selection == "Weather Data - Plant 1":
    st.sidebar.subheader("Select Analysis for Plant 1 Weather Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Temperature Trends",
            "Daily Average Temperatures and Irradiation",
            "Daily Min/Max Ambient Temperature",
            "Correlation Between Ambient Temperature and Irradiation",
        ],
    )
    df = weather_data_plant_1
elif dataset_selection == "Generation Data - Plant 2":
    st.sidebar.subheader("Select Analysis for Plant 2 Generation Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Daily Production Distribution",
            "Daily Production Density per Source",
            "Average Daily AC/DC Power",
            "Total Production Distribution",
            "Daily Total AC/DC Power",
            "Weekly Production",
        ],
    )
    df = generation_data_plant_2
else:
    st.sidebar.subheader("Select Analysis for Plant 2 Weather Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Temperature Trends",
            "Daily Average Temperatures and Irradiation",
            "Daily Min/Max Ambient Temperature",
            "Correlation Between Ambient Temperature and Irradiation",
        ],
    )
    df = weather_data_plant_2

# Display selected options
for option in options:
    if option == "Daily Production Distribution":
        st.subheader("Daily Production Distribution")
        daily_prod_dist = daily_production_distribution(df)
        st.write(daily_prod_dist)

    elif option == "Daily Production Density per Source":
        st.subheader("Daily Production Density per Source")
        density_per_source = daily_production_density_per_source(df)
        st.write(density_per_source)

    elif option == "Average Daily AC/DC Power":
        st.subheader("Average Daily AC/DC Power")
        avg_power = average_daily_ac_dc_power(df)
        st.write(avg_power)

    elif option == "Total Production Distribution":
        st.subheader("Total Production Distribution")
        total_dist = total_production_distribution(df)
        st.write(total_dist)

    elif option == "Daily Total AC/DC Power":
        st.subheader("Daily Total AC/DC Power")
        daily_totals = daily_total_ac_dc_power(df)
        st.write(daily_totals)

    elif option == "Weekly Production":
        st.subheader("Weekly Production")
        weekly_prod = weekly_production(df)
        st.write(weekly_prod)

    elif option == "Temperature Trends":
        st.subheader("Temperature Trends")
        temp_trends = temperature_trends(df)
        st.write(temp_trends)

    elif option == "Daily Average Temperatures and Irradiation":
        st.subheader("Daily Average Temperatures and Irradiation")
        avg_temp_irradiation = daily_avg_temp_irradiation(df)
        st.write(avg_temp_irradiation)

    elif option == "Daily Min/Max Ambient Temperature":
        st.subheader("Daily Min/Max Ambient Temperature")
        min_max_temp = daily_min_max_temp(df)
        st.write(min_max_temp)

    elif option == "Correlation Between Ambient Temperature and Irradiation":
        st.subheader("Correlation Between Ambient Temperature and Irradiation")
        correlation = correlation_temp_irradiation(df)
        st.write(correlation)

# Visualization options
st.sidebar.header("Select Graphs")
graph_options = []
for option in options:
    if option == "Daily Production Distribution":
        graph_options.append("Daily Production Distribution Graph")
    elif option == "Daily Production Density per Source":
        graph_options.append("Daily Production Density per Source Graph")
    elif option == "Average Daily AC/DC Power":
        graph_options.append("Average Daily AC/DC Power Graph")
    elif option == "Total Production Distribution":
        graph_options.append("Total Production Distribution Graph")
    elif option == "Daily Total AC/DC Power":
        graph_options.append("Daily Total AC/DC Power Graph")
    elif option == "Weekly Production":
        graph_options.append("Weekly Production Graph")
    elif option == "Temperature Trends":
        graph_options.append("Temperature Trends Graph")
    elif option == "Daily Average Temperatures and Irradiation":
        graph_options.append("Daily Average Temperatures and Irradiation Graph")
    elif option == "Daily Min/Max Ambient Temperature":
        graph_options.append("Daily Min/Max Ambient Temperature Graph")
    elif option == "Correlation Between Ambient Temperature and Irradiation":
        graph_options.append("Correlation Graph")

selected_graphs = st.sidebar.multiselect("Select graphs to display:", graph_options)

# Show selected graphs
if "Daily Production Distribution Graph" in selected_graphs:
    st.subheader("Daily Production Distribution Graph")
    st.line_chart(daily_production_distribution(df)['DAILY_YIELD'])

if "Daily Production Density per Source Graph" in selected_graphs:
    st.subheader("Daily Production Density per Source Graph")
    density_data = daily_production_density_per_source(df)
    st.bar_chart(density_data.set_index('SOURCE_KEY')['DAILY_YIELD'])

if "Average Daily AC/DC Power Graph" in selected_graphs:
    st.subheader("Average Daily AC/DC Power Graph")
    avg_power_data = average_daily_ac_dc_power(df)
    st.write(avg_power_data)

if "Total Production Distribution Graph" in selected_graphs:
    st.subheader("Total Production Distribution Graph")
    total_dist_data = total_production_distribution(df)
    st.bar_chart(total_dist_data.set_index('SOURCE_KEY')['DAILY_YIELD'])

if "Daily Total AC/DC Power Graph" in selected_graphs:
    st.subheader("Daily Total AC/DC Power Graph")
    daily_totals_data = daily_total_ac_dc_power(df)
    st.line_chart(daily_totals_data.set_index('DATE'))

if "Weekly Production Graph" in selected_graphs:
    st.subheader("Weekly Production Graph")
    weekly_prod_data = weekly_production(df)
    st.line_chart(weekly_prod_data.set_index('WEEK'))

if "Temperature Trends Graph" in selected_graphs:
    st.subheader("Temperature Trends Graph")
    temp_trends_data = temperature_trends(df)
    st.line_chart(temp_trends_data.set_index('DATE'))

if "Daily Average Temperatures and Irradiation Graph" in selected_graphs:
    st.subheader("Daily Average Temperatures and Irradiation Graph")
    avg_temp_irradiation_data = daily_avg_temp_irradiation(df)
    st.line_chart(avg_temp_irradiation_data.set_index('DATE'))

if "Daily Min/Max Ambient Temperature Graph" in selected_graphs:
    st.subheader("Daily Min/Max Ambient Temperature Graph")
    min_max_temp_data = daily_min_max_temp(df)
    st.line_chart(min_max_temp_data.set_index('DATE'))

if "Correlation Graph" in selected_graphs:
    st.subheader("Correlation Between Ambient Temperature and Irradiation Graph")
    correlation_data = correlation_temp_irradiation(df)
    st.line_chart(correlation_data)

# Display additional information
st.sidebar.header("Additional Information")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)

st.sidebar.text("Powered by Streamlit")

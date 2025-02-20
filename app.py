import mysql.connector
import streamlit as st
import googlemaps
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection
def create_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Google Maps API setup
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))

# Streamlit App
def main():
    st.title("Uber-like App")
    st.write("This is a simple Uber-like application.")

    # Example of using Google Maps API
    location = st.text_input("Enter a location")
    if location:
        geocode_result = gmaps.geocode(location)
        st.write(geocode_result)

    # Example of interacting with MySQL database
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        st.write(row)

if __name__ == "__main__":
    main()
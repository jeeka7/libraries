import streamlit as st
import mysql.connector
st.write("Library management System")

# Initialize connection.
conn = mysql.connector.connect(host='ip-172-31-25-66',database='sql12629961',password='C6iCpjmcus',user='sql12629961')

if conn.is_connected():
    st.write("Connection established")

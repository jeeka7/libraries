import streamlit as st
import mysql.connector
st.write("Library management System")

# Initialize connection.
conn = mysql.connector.connect(host='sql12.freemysqlhosting.net',database='sql12629961',password='C6iCpjmcus',user='sql12629961')

if conn.is_connected():
    st.write("Connection established")
cursor = conn.cursor()
cursor.execute("SELECT * FROM library")
data = cursor.fetchall()
count = cursor.rowcount
st.write("total rows obtained",count)
for row in data:
    print(row)

conn.close()

import streamlit as st
import mysql.connector
st.write("Library management System")

# Initialize connection.
conn = mysql.connector.connect(host='sql12.freemysqlhosting.net',database='sql12629961',password='C6iCpjmcus',user='sql12629961')

if conn.is_connected():
    st.write("Connection established")
cursor = conn.cursor()
query1 = "Select * from library"
cursor.execute(query1)
data = cursor.fetchall()
count = cursor.rowcount
st.write("total rows obtained",count)
for row in data:
    st.write(row)
conn = st.experimental_connection("sql")
df = conn.query("select * from library")
st.dataframe(df)
st.write(df)
conn.close()

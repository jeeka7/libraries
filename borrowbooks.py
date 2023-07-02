import streamlit as st
st.write("Library management System")

mydb=mysql.connector.connect(
host="ip-172-31-25-66"
user="sql12629961"
password="C6iCpjmcus"
database="sql12629961"
)
mycursor=mydb.cursor()
st.write("connection to free database successful")

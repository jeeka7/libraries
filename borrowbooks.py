import streamlit as st
import mysql.connector
import pandas as pd
st.write("Library management System")

# Initialize connection.
conn = mysql.connector.connect(host='sql12.freemysqlhosting.net',database='sql12629961',password='C6iCpjmcus',user='sql12629961')

if conn.is_connected():
    st.write("Connection established")
cursor = conn.cursor()
query1 = "Select * from library"
cursor.execute(query1)
data = cursor.fetchall()
df = pd.DataFrame(data)
dict = {0:'Bookname',1:'Renewaldate',2:'renewalsleft',3:'Libraryname',4:'issuedate',5:'daysleft',6:'fine'}
df.rename(columns = dict, inplace = True)
st.write(df)

conn.close()

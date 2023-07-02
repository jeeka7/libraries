import streamlit as st
st.write("Library management System")
conn = st.experimental_connection('sql12629961', type='sql')
books = conn.query('select * from library')
st.dataframe(books)

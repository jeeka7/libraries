import streamlit as st
st.write("Library management System")

# Initialize connection.
conn = st.experimental_connection('sql12629961', type='sql')

# Perform query.
df = conn.query('SELECT * from library;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.bookname} has a :{row.fine}:")

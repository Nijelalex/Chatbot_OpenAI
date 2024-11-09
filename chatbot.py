import streamlit as st

#Upload PDF File
st.header("Chatbot")

with st.sidebar:
    st.title("Documents Pane")
    file=st.file_uploader("Upload a PDF file", type="pdf")
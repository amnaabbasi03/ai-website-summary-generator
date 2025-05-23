import streamlit as st
from summarizer import get_clean_text_from_url, generate_summary

st.title("AI Website Summary Generator")
st.write("Get a clear summary and key topics from any webpage.")

url = st.text_input("Enter Website URL:")

if url:
    with st.spinner("Fetching and summarizing..."):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        text = get_clean_text_from_url(url)
        if text.startswith("Error"):
            st.error(text)
        else:
            summary = generate_summary(text)
            st.subheader("Summary")
            st.write(summary)


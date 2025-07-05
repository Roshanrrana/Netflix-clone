import streamlit as st
import os

def load_html():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    st.set_page_config(page_title="Netflix Clone", page_icon="🎬", layout="wide")
    st.title("Netflix Clone Demo")

    html_content = load_html()
    st.markdown(html_content, unsafe_allow_html=True)

    st.markdown("---")
    st.write("This is a **static frontend clone** – not connected to any backend.")
    st.info("To add streaming data or interactive features, consider integrating TMDb via API + Streamlit components.")

if __name__ == "__main__":
    main()

import streamlit as st

# Load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML content as raw string
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Main app
def main():
    st.set_page_config(page_title="Netflix Clone", layout="wide")

    local_css("style.css")  # Apply your CSS styling

    # Render the HTML as-is inside Streamlit
    html_content = load_html()
    st.components.v1.html(html_content, height=5000, scrolling=True)

if __name__ == "__main__":
    main()

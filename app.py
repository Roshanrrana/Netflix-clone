import streamlit as st

# Sample data (simulate a movie catalog)
movies = [
    {
        "title": "Stranger Things",
        "genre": "Sci-Fi",
        "poster": "https://upload.wikimedia.org/wikipedia/en/f/f7/Stranger_Things_season_4.jpg"
    },
    {
        "title": "Breaking Bad",
        "genre": "Crime, Drama",
        "poster": "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png"
    },
    {
        "title": "The Witcher",
        "genre": "Fantasy",
        "poster": "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Witcher_title_card.png"
    },
]

def show_movie(movie):
    st.image(movie["poster"], width=200)
    st.subheader(movie["title"])
    st.caption(f"Genre: {movie['genre']}")

def main():
    st.set_page_config(layout="wide", page_title="Netflix Clone", page_icon=":clapper:")
    st.title("🎬 Netflix Clone App")
    st.write("Welcome to your streaming platform!")

    # Movie Gallery
    st.markdown("## 📺 Popular Shows")
    cols = st.columns(len(movies))
    for col, movie in zip(cols, movies):
        with col:
            show_movie(movie)

    # Filter section
    st.markdown("---")
    st.markdown("## 🔍 Find a Show")
    search = st.text_input("Search by title")

    if search:
        results = [m for m in movies if search.lower() in m["title"].lower()]
        if results:
            st.success(f"Found {len(results)} result(s):")
            for movie in results:
                show_movie(movie)
        else:
            st.warning("No results found.")

if __name__ == "__main__":
    main()

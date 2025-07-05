# movie_info_app.py

import streamlit as st
import requests
import matplotlib.pyplot as plt

st.title("🎬 Movie Info Finder")
movie_name = st.text_input("Enter a movie name:")

if movie_name:
    api_key = "62f4c6cb"  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        st.header(data["Title"])
        poster_url = data["Poster"]
        if poster_url != "N/A":
            st.image(poster_url)
        else:
            st.warning("No poster available for this movie.")
        st.markdown(f"**Year**: {data['Year']}")
        st.markdown(f"**Genre**: {data['Genre']}")
        st.markdown(f"**IMDb Rating**: {data['imdbRating']}")
        st.markdown(f"**Plot**: {data['Plot']}")
        
        # Ratings Visualization
        ratings = data.get("Ratings", [])
        if ratings:
            sources = [r['Source'] for r in ratings]
            values = [float(r['Value'].replace('%','').replace('/10','').replace('/100','')) for r in ratings]
            fig, ax = plt.subplots()
            ax.barh(sources, values, color='orange')
            ax.set_xlabel('Rating')
            ax.set_title('Ratings from Different Sources')
            st.pyplot(fig)
    else:
        st.error("Movie not found! Try another.")

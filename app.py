import streamlit as st
import pickle
import pandas as pd
import requests
movies_dict = pickle.load(open('movies.pkl','rb'))
similarity =  pickle.load(open('similarity.pkl','rb'))

def fetech_poster(movie_id):
    try:
        movie_url = "https://api.themoviedb.org/3/movie/{}?api_key=94eeb0d6b80a6aaccb1d8cbde938d4e3&language=en=US".format(movie_id)
        response =  requests.get(movie_url).json()
        if(response['poster_path']!=None):
            return "https://image.tmdb.org/t/p/w500/"+response['poster_path']
    except():
        return " "
def recommend(movie):
    recommended_movies = []
    movie_posters =[]
    movie_index = movies[movies['title'] == movie].index[0]
    similarity_indices = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[1:6]
    for i in similarity_indices:
        recommended_movies.append(movies.iloc[i[0]]['title'])
        movie_posters.append(fetech_poster(movies.iloc[i[0]]['id']))
    return recommended_movies,movie_posters


movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('select any movie',(movies['title'].values))

if st.button('Recommend'):
    move_names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(move_names[0])
        try:
            st.image(posters[0])
        except:
            st.header("poster not available")
    with col2:
        st.text(move_names[1])
        try:
            st.image(posters[1])
        except:
            st.header("poster not available")
    with col3:
        st.text(move_names[2])
        try:
            st.image(posters[2])
        except:
            st.header("poster not available")
    with col4:
        st.text(move_names[3])
        try:
            st.image(posters[3])
        except:
            st.header("poster not available")
    with col5:
        st.text(move_names[4])
        try:
            st.image(posters[4])
        except:
            st.header("poster not available")
print("executon is successful")

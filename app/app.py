import streamlit as st
import pickle
import numpy as np
import pandas as pd

def recommend(book):
  book_ind = books[books["title"]==book].Ind
  mentioned_book = similarity[book_ind][0]
  similar_books = sorted(list(enumerate(mentioned_book)),key=lambda X:X[1],reverse=True)[1:6]
  L=[]
  for i in similar_books:
    L.append(books.iloc[i[0]].title)
  return L

def display_book(title, link_text, link_url):
    html_string = f"<div style='display: flex; align-items:center; justify-content:space-between; padding: 2px 30px; width:700px';><h1 style='font-size: 20px;'>{title}</h1><div><a href='{link_url}'>{link_text}</a></div></div>"
    st.write(html_string, unsafe_allow_html=True)


# Example usage:


similarity = pickle.load(open("../exports/similarity.pkl",'rb'))
books_dict = pickle.load(open("../exports/booksDict.pkl",'rb'))

books = pd.DataFrame(books_dict)

st.title('Books Recommendation System')

book = st.selectbox('Enter the name of the book: ',books['title'].values)

recommended_books = recommend(book)

col1,col2 = st.columns(2)



with col1:
    if st.button('Recommend',type="primary"):
        for i in recommended_books:
            links = books[books["title"] == i].URL.values[0]
            display_book(f"{i}","See Book",links)

with col2:
    if st.button('Clear'):
        for i in recommended_books:
            st.write()






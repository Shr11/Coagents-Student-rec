import streamlit as st



st.title("Student Recommendation System")
analytics = st.slider("Analytics (1-5)", 1, 5, value=3)
coding = st.slider("Coding (1-5)", 1, 5, value=3)
aptitude = st.slider("Aptitude (1-5)", 1, 5, value=3)

if st.button("Recommend"):
    st.success(f"Your recommended stream is Computer Science!")

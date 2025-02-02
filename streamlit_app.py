import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.set_page_config(page_title="Wellness Web Weaver", layout="wide")

    st.title("🌿 Wellness Web Weaver")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data", "User_preference"])

    if page == "Home":
        show_home()
    elif page == "Data":
        show_dashboard()
    elif page == "User_preference":
        show_pref()

def show_home():
    st.header("Welcome to Wellness Web Weaver")
    st.write("This is a fully converted Python & Streamlit version of your original web app.")
    st.write("\n---\n")
    st.image("https://source.unsplash.com/800x400/?wellness,health")

def show_dashboard():
    st.header("📊 Dashboard")
    st.write("Interactive wellness analytics and charts will go here.")

    st.subheader("Example Chart")

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Metric A', 'Metric B', 'Metric C']
    )
    st.line_chart(data)

def show_pref():
    st.header("⚙️ User Settings")
    st.write("Customize your wellness experience here.")

    user_name = st.text_input("Enter your name:")
    st.write(f"Hello, {user_name}!")

    st.write("Allergies")

    a_nuts = st.checkbox("Nuts")
    a_gluten = st.checkbox("gluten")
    a_egg = st.checkbox("Egg")

    like = []
    likes = st.text_input("Enter food preference")
    if likes == 'x' :
        like.append(likes)
    
    st.write(f"{like} ")
    
    deficiency = st.text_input("Enter nutrient deficiency")

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")


main()

import streamlit as st
import pandas as pd
import numpy as np
#import chatapi

like = []

def main():
    st.set_page_config(page_title="Wellness Web Weaver", layout="wide")

    st.title("🌿 Wellness Web Weaver")
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["Home", "Data", "User_preference"])

    if page == "Home":
        show_home()
    elif page == "Data":
        show_dashboard()
    elif page == "User_preference":
        show_pref()

def show_home():
    st.header("Welcome to Wellness Web Weaver")
    st.write("An app that make recipe depending on your need")
    st.write("\n---\n")
    st.image("https://source.unsplash.com/800x400/?wellness,health")
    if st.button("Create recipe"):
        #answer = "can you make multiple recipe with these ingredient?"
        #Append answer with list of ingredient
        #prompt = chatapi.get_ai_response(answer)
        #st.write(f"{prompt}")
        print("hello world")

    

def show_dashboard():
    st.header("📊 Dashboard")
    st.write("Interactive wellness analytics and charts will go here.")

    st.subheader("Example Chart")

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Metric A', 'Metric B', 'Metric C']
    )
    st.line_chart(data)

    # Create sample recipe data
    recipe_data = {
        'Recipe': ['Chicken Salad', 'Pasta Carbonara', 'Greek Yogurt Bowl', 'Salmon with Rice', 'Vegetable Stir Fry'],
        'Calories': [350, 650, 280, 450, 300]
    }

    # Create DataFrame
    df = pd.DataFrame(recipe_data)

    # Create title and description
    st.title('Recipe Calorie Dashboard')
    st.write('Visualize the calorie content of different recipes')

    # Create bar chart
    st.bar_chart(data=df.set_index('Recipe')['Calories'])

def show_pref():
    st.header("⚙️ User Settings")
    st.write("Customize your wellness experience here.")

    user_name = st.text_input("Enter your name:")
    st.write(f"Hello, {user_name}!")

    st.write("Allergies")

    a_nuts = st.checkbox("Nuts")
    a_gluten = st.checkbox("gluten")
    a_egg = st.checkbox("Egg")

    global like
    likes = st.text_input("Enter food preference")
    like = like.append(likes)

    st.write(f"{like} ")

    deficiency = st.text_input("Enter nutrient deficiency")

 
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

    #answer = "do you like potato?"
    #prompt = chatapi.get_ai_response(answer)

    st.write(f"something,{prompt}")


main()
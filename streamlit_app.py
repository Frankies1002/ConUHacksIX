import streamlit as st
import pandas as pd
import numpy as np
import chatapi
import pymongo


# Use session_state to store preferences persistently
if "likes" not in st.session_state:
    st.session_state.likes = []

def setlikes(item):
    """Append a user preference to session state."""
    st.session_state.likes.append(item)

def getlikes():
    """Retrieve user preferences from session state."""
    return st.session_state.likes

def main():
    st.set_page_config(page_title="Wellness Web Weaver", layout="wide")

    st.title("🌿 Wellness Web Weaver")
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["Home", "Data", "User Preference"])

    if page == "Home":
        show_home()
    elif page == "Data":
        show_dashboard()
    elif page == "User Preference":
        show_pref()

def show_home():
    """Display the home page with recipe generation."""
    st.header("Welcome to Wellness Web Weaver")
    st.write("An app that makes recipes depending on your needs.")
    st.write("\n---\n")
    st.image("https://source.unsplash.com/800x400/?wellness,health")

    if st.button("Create recipe"):
        ingredients = getlikes()
        if ingredients:
            answer = "Create a recipe with these ingredients and allergies:\n\n"
            answer += ", ".join(ingredients)
            
            # Get AI-generated recipe
            response = chatapi.get_ai_response(answer)  # Ensure chatapi is correctly implemented
            st.write(f"### AI-Generated Recipe:\n{response}")
        else:
            st.warning("Please enter some preferences before generating a recipe.")

def show_dashboard():
    # MongoDB connection URI (Replace with your actual URI)
    mongo_uri = "mongodb+srv://toca:jmeFGCz3HqgtGOIu@cluster0.tln4p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)

    # Select database and collection
    db = client["mongodbVSCodePlaygroundDB"]  # Replace with your database name
    collection = db["food_nutrition"]  # Replace with your collection name

    # Fetch data (convert cursor to list of dictionaries)
    data = list(collection.find())

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # Drop MongoDB default '_id' field if not needed
    df.drop(columns=['_id'], inplace=True, errors='ignore')

    # Display the DataFrame
    print(df)

def show_pref():
    """Display user preferences and settings."""
    st.header("⚙️ User Settings")
    st.write("Customize your wellness experience here.")

    user_name = st.text_input("Enter your name:", key="user_name")
    if user_name:
        st.write(f"Hello, {user_name}!")

    st.write("Allergies:")
    allergies = {
        "Nuts": st.checkbox("Nuts"),
        "Gluten": st.checkbox("Gluten"),
        "Egg": st.checkbox("Egg"),
    }

    like = st.text_input("Enter food preference:", key="food_pref")

    if st.button("Save Settings"):
        if like:
            setlikes(like)

        for allergy, selected in allergies.items():
            if selected:
                setlikes(f"{allergy} allergy")

        st.success("Settings saved successfully!")
        st.write(f"### Current Preferences:\n{getlikes()}")

main()

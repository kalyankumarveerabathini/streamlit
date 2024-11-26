import streamlit as st

st.title("welcome")
st.write("Iam kalyan kumar veerabathini.")
import streamlit as st

# Title and Header
st.title("Welcome to My Website!")
st.header("Explore Interactive Features")

# Text
st.write("This is a simple website built with Streamlit.")

# Input and Interaction
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to my website.")

# Displaying a Chart
import streamlit as st
import pandas as pd
import numpy as np

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if pages == "Home":
    st.title("Welcome to My Portfolio Website!")
    st.image("https://via.placeholder.com/800x200?text=Streamlit+Website", use_column_width=True)
    st.write("""
    Hi there! This is a simple interactive website built using **Streamlit**.  
    Navigate through the sidebar to learn more about me and my work.
    """)

    # Display a simple metric
    st.metric(label="Happy Visitors", value="1234", delta="+12")

    # Interactive chart
    st.subheader("Visitor Trends")
    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["Page Views", "Unique Visitors", "Sign-ups"]
    )
    st.line_chart(data)

# About Me Page
elif pages == "About Me":
    st.title("About Me")
    st.image("https://via.placeholder.com/150", width=150)
    st.write("""
    Hello! I'm **John Doe**, a passionate software developer and data enthusiast.  
    I specialize in creating web apps and data-driven solutions.
    """)

    # Skills
    st.subheader("Skills")
    skills = ["Python", "Data Analysis", "Machine Learning", "Web Development", "Cloud Computing"]
    st.write(", ".join(skills))

# Projects Page
elif pages == "Projects":
    st.title("Projects")
    st.write("Here are some of my featured projects:")

    # Project 1
    st.subheader("1. Data Analysis Dashboard")
    st.write("A dashboard that visualizes key metrics and trends using Streamlit.")
    st.image("https://via.placeholder.com/600x300", caption="Dashboard Preview")

    # Project 2
    st.subheader("2. Machine Learning Model")
    st.write("An ML model to predict customer churn based on historical data.")
    st.image("https://via.placeholder.com/600x300", caption="Model Output Example")

# Contact Page
elif pages == "Contact":
    st.title("Contact Me")
    st.write("Fill out the form below to get in touch!")

    # Form Inputs
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Submit"):
        if name and email and message:
            st.success("Thank you for reaching out! I'll get back to you soon.")
        else:
            st.error("Please fill out all fields.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit.")



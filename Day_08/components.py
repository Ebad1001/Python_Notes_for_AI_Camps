# !python -m streamlit run file.py
import streamlit as st

# Sidebar
st.sidebar.title("Sidebar title")
choice = st.sidebar.radio("Select a view:", ["Home", "About", "Contact"])

# Headings
st.title(f"{choice} Page")      # main title
st.header("This is a Header")   # section header
st.write("---")

# Body Texts
st.text("- **Some text**")     # to display plain text
st.write("- **Some text**")    # more versatile than text, can handle (dataframes, markdowns, etc.)
st.write("---")

# Special Messages, Colorful texts
st.header("Colored messages")
st.success("Success msgs are in Green")
st.error("Error msgs are in Red")
st.warning("Warning msgs are in Yellow")
st.info("Info msgs are in Blue")
st.write("---")

# Text input
st.header("Text input")
name = st.text_input("Enter your name")

# Number input
st.header("Number input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=50)

# Button, on click events
st.header("Button")
if st.button("Show Details"):
    st.write(f"Your name is {name} and your age is {age}")
st.write("---")

# Slider
st.header("Slider")
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {value}")
st.write("---")

# Checkbox
st.header("Checkbox")
value = st.checkbox("Show Text")
st.write(f"Checkbox value: {value}")
st.write("---")

# Radio
st.header("Radio")
value = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"Radio value: {value}")
st.write("---")

# Selectbox
st.header("Selectbox")
value = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selectbox value: {value}")
st.write("---")

# Multiselect
st.header("Multiselect")
value = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Multiselect value: {value}")
st.write("---")

# Table
import pandas as pd
st.header("Dataframe Tables")
df = pd.DataFrame({"A": [1, 2, 3], "B": [5, 6, 4], "C": [9, 7, 8]})
st.write(df)
st.write("---")


# Load images from URL
st.header("Image from URL")
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png"
st.image(img_url, caption="Image from URL")
st.write("---")

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)
st.write("---")

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
st.video(video_url)
st.write("---")
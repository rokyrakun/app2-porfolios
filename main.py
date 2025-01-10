import streamlit as st

st.set_page_config(page_title="Rob Ballard", page_icon=":smiley:", layout="wide")

col1, col2 = st.columns(2) #create 2 columns

with col1: #open a column
    st.image("images/profile.jpg")

with col2:
    st.title("Rob Ballard")
    content = """Hello, my name is Rob Ballard.  This is me and my wife in December, 2024.  I am a former Computer Science major and COBOL programmer learning my first new programming language in over 30 years.  I have relished the experience, and honestly had forgotten how much I enjoy coding.  Please look over my portfolio, and if there is something you'd like me to code for you, please send me a message on the contact page.
    """
    st.info(content)
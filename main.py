import streamlit as st
#pandas is a streamlit module to process .csv files
import pandas as pd


st.set_page_config(page_title="Rob Ballard", page_icon=":smiley:", layout="wide")

col1, col2 = st.columns(2) #create 2 columns

with col1: #open a column
    st.image("images/profile.jpg")

with col2:
    st.title("Rob Ballard")
    content = """Hello, my name is Rob.  This is me and my wife in December, 2024.  I am a former Computer Science major and COBOL programmer learning my first new programming language in over 30 years.  I have relished the experience, and honestly had forgotten how much I enjoy coding.  Please look over my portfolio, and if there is something you'd like me to code for you, please send me a message on the contact page.
    """
    st.info(content)

#better to use a multi-line string variable, and then apply use that variable in your st.write statement
#when entering free-form text which may expand to > 1 line.  in this case it didn't, but concept still worksl
content2 = """
<b>Below you can find some of the apps I have built in Python.  Feel free to contact me!</b>
"""
#add html tags here.  only works on st.write lines
#when the code is unindented, as it is here, it will stand on its own
#outside the context of the two columns in page setup.  i kinda guessed that part, but it worked.
st.write(content2, unsafe_allow_html=True)

#create two additional columns (which confuses me a little)
#again ... this code processes chronologically
col3, col4 = st.columns(2)

#sep = seperator
#df = data frame
df = pd.read_csv("data.csv", sep=";")

#must use an index, and the data itsef for intterrows
#return a pandas series, which you can then process (title below)
#df[:10] .. first 10 rows
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])










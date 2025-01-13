import streamlit as st
from send_email import send_email


st.header("Contact Me")

with st.form(key="email_form"):  #key is mandatory.  not using it
    user_email = st.text_input("Your email address")
    message_area = st.text_area("Your message")
    #this string is formatted per RFC 5322 (standard email) protocol
    #if it isn't formatted exactly like this, you won't get the desired output.
    #everything after the blank line is placed in the body of the email
    #hence, the sender's email in body so you can double-click and send
    message_out = f"""\
Subject:  New email from {user_email}

From: {user_email} 
{message_area}  
"""
    button = st.form_submit_button("Send")
    if button:
        send_email(message_out)
        #st.info message to user once processing is complete
        #st.info output is always in a nice colored box
        st.info("Your email was sent successfully!")




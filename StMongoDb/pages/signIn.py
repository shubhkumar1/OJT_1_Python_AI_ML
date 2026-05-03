import streamlit as st
import time as t
from datetime import date
import pymongo as dbc
from dotenv import load_dotenv
import os


load_dotenv()

dbKey = os.getenv("DB_KEY")

dbClient = dbc.MongoClient(f"{dbKey}")

myDb = dbClient["Python_OJT"]
db = myDb["Student_info"]

tab1, tab2 = st.tabs(["Sign In", "Reset Password"], )

with tab1:
    st.title("Sign In", text_alignment="center")

    with st.form("Student Sign In"):
        email = str(st.text_input("Enter your Email-ID...")).lower()
        password = str(st.text_input("Enter your Password", placeholder="Enter your DOB (YYYY-MM-DD) if you haven't changed your password, e.g.- 2001-01-01", type="password"))

        if st.form_submit_button("Sign In", width="stretch"):
            st.write("Loading...")
            t.sleep(1)
            value = 0

            res = db.find({"$and" : [{"email" : email}, {"password" : password}]})

            for x in res:
                value = 1
                st.session_state['name'] = x["name"]
                st.session_state['email'] = x["email"]
                st.session_state['password'] = x["password"]
                st.switch_page("pages/profile.py")


            if value == 0:
                st.error("Invalid Credentials...")

        
with tab2:

    st.title("Password Reset", text_alignment="center")

    @st.dialog("Password Reset")
    def passwordReset():
        newPassword = str(st.text_input("Enter your new password", type='password'))
        if st.button("Save"):

            db.update_one({"email" : email}, {"$set" : {"password" : newPassword}})

            st.success("Password Reset successfully Baby...")
            t.sleep(1.5)
            st.rerun()


    with st.form("Password Reset"):
        email = st.text_input("Enter your E-mail...")
        dob = str(st.date_input("Enter your Date", min_value = date(2000, 1, 1), max_value=date(2025, 1, 1),value=None))

        if st.form_submit_button("Next"):
            st.write("Verifying your info...")

            res = db.find_one({"$and": [{"email": email}, {"dob": dob}]})
            value = 0

            if res:
                value = 1
                passwordReset()

            if value == 0:
                st.error("Invalid Credentials...")


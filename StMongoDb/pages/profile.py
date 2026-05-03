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


if 'name' not in st.session_state:
    st.error("Please sign in...")
    st.write("Switching to Sign In page...")
    t.sleep(2)
    st.switch_page("pages/signIn.py")

name = st.session_state['name']
email = st.session_state['email']
password = st.session_state['password']

c1, c2 = st.columns([10, 1])

c1.title("Profile Page Settings", text_alignment="center")
if c2.button("", icon=":material/logout:"):
    st.session_state.clear()
    st.rerun()

st.header(f"Welcome {name}")


@st.dialog("Profile")
def profile():

    res = db.find({"$and": [{"email" : email}, {"password" : password}]})


    for x in res:
        st.code(f"Name: {x["name"]}", language='css')
        st.code(f"Department: {x["dept"]}", language='css')
        st.code(f"Roll: {x["roll"]}", language='css')
        st.code(f"DOB: {x["dob"]}", language='css')
        st.code(f"Gender: {x["gender"]}", language='css')
        st.code(f"E-mail: {x["email"]}", language='css')
        st.code(f"Contact-Time: {x["ftime"]}", language='css')
        st.code(f"Address: {x["address"]}", language='css')
        st.image(image=x["web_cam"], caption="Profile photo", width="stretch")



@st.dialog("Edit your Profile")
def edit():

    setValue = ""

    value = str(st.selectbox("Choose your field to update", options=["Name", "Dept", "Roll", "Dob", "Gender", "Email", "Address", "Profile Photo"], index=None, placeholder="Select Field")).lower()

    if value == "name" or value == "roll" or value == "email":
        setValue = str(st.text_input(f"Update your {value}"))

    if value == "dept":
        setValue = st.selectbox("Update your Department: ", options=["BBA", "BCA", "IT", "CS", "MCA", "AI/ML"], index=None, placeholder="Select Department")
        
    if value == "dob":
        setValue = str(st.date_input("Update your DOB: ", min_value=date(2000, 1, 1), max_value=date(2025, 1, 1), value=None))

    if value == "gender":
        setValue = st.radio("Update Gender", ["Male", "Female"])

    if value == "address":
        setValue = str(st.text_area(f"Update your {value}"))

    if value == "profile photo":
        value = "web_cam"
        web_cam_data = st.camera_input("Update Photo: ")
        if web_cam_data:
            setValue = web_cam_data.getvalue()


    if st.button("Save", width="stretch"):
        if value and setValue:
            db.update_one({"email": email}, {"$set": {value: setValue}})
            st.success("Update successfully")

            if value == "name":
                st.session_state["name"] = setValue

            if value == "email":
                st.session_state["email"] = setValue

            t.sleep(1.5)
            st.rerun()
        
        else:
            st.error("Please check your input field carefully Baby...")




@st.dialog("Change Password")
def changePassword():
    newPassword = str(st.text_input("Enter your new Password", type="password"))
    if st.button("Change"):

        db.update_one({"email": email}, {"$set": {"password": newPassword}})
        st.success("Password change successfully Baby...")
        t.sleep(2)
        st.session_state.clear()
        st.switch_page("pages/signIn.py")



@st.dialog("Delete")
def deleteProfile():
    st.error("Are you ready to delete your profile?")

    if st.button("Delete Profile", type="primary"):
        db.delete_one({"email": email})
        st.success("Profile deleted successfully")
        t.sleep(1.5)
        st.session_state.clear()
        st.switch_page("pages/signUp.py")


if st.button("See your Profile", width="stretch"):
    profile()

if st.button("Edit your Profile", width="stretch"):
    edit()

if st.button("Change your Password", width="stretch"):
    changePassword()

if st.button("Delete your Profile", width="stretch"):
    deleteProfile()


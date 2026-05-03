import streamlit as st
from datetime import date
import time
import pymongo as dbc
from dotenv import load_dotenv
import os


load_dotenv()

dbKey = os.getenv("DB_KEY")

dbClient = dbc.MongoClient(f"{dbKey}")

myDb = dbClient["Python_OJT"]
db = myDb["Student_info"]

st.title("Please Create your Profile", width="stretch", text_alignment="center")

@st.dialog("Preview")
def previewInfo():
    
    st.code("Name: " + name, language='css')
    st.code("Department: " + dept, language='css')
    st.code("Roll-No: " + roll, language='css')
    st.code("DOB: " + dob, language='css')
    st.code("Gender: " + gender, language='css')
    st.code("Email: " + email, language='css')
    st.code("Contact-Time: " + ftime, language='css')
    st.code("Address: " + address, language='css')
    st.code("Profile-Photo: ", language='css')
    if web_cam:
        st.image(image = web_cam, caption="Profile Photo")
    else:
         st.error("Please Click Photo")

    if st.button("Save"):
        if name and dept and roll and dob and gender and email and ftime and address and web_cam:

            db.insert_one({"name": name, "dept": dept, "roll": roll, "dob": dob, "gender": gender, "email": email, "ftime": ftime, "address": address, "web_cam": web_cam.getvalue(), "password": dob})
            
            st.success("Save successfully Baby...")
            time.sleep(2)
            st.switch_page("pages/signIn.py")
        else:
            st.error("Please Check & fill correctly...")


with st.form("Student Form"):
    name = st.text_input("Enter your Name: ")
    dept = str(st.selectbox("Enter your Department: ", options=["BBA", "BCA", "IT", "CS", "MCA", "AI/ML"], index=None, placeholder="Select Department"))
    roll = st.text_input("Enter your Roll No.: ")
    dob = str(st.date_input("Enter your DOB: ", min_value=date(2000, 1, 1), max_value=date(2025, 1, 1), value=None))
    gender = st.radio("Gender", ["Male", "Female"])
    email = str(st.text_input("Enter your Mail: ")).lower()
    ftime = str(st.time_input("Enter favorable time to contact: ", value=None))
    address = st.text_area("Enter your Address: ")
    web_cam = st.camera_input("Click Photo: ")

    if st.form_submit_button("Preview", icon=":material/preview:"):
        previewInfo()
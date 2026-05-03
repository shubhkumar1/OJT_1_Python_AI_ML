# Streamlit & Database Integration: From SQL to NoSQL

## Developer Profile
* **Name:** Shubham Kumar
* **Department:** BCA
* **College:** Marwari College Ranchi
* **Role:** OJT Intern (AI/ML)
* **Faculty Name:** Dr. Kunal Gupta
---

## 🚀 Project Overview
This project documents my learning journey and implementation of database integration using **Streamlit**. It tracks the evolution from using traditional Relational Databases (SQL) to modern Document-based NoSQL databases (MongoDB).

## 🛠️ Phase 1: Streamlit with SQL (XAMPP)
Initially, I explored the integration of Python's Streamlit framework with a local SQL environment.
* **Environment:** Used **XAMPP Server** to host a local MySQL database.
* **Implementation:** Connected Streamlit apps to MySQL to perform CRUD (Create, Read, Update, Delete) operations using libraries like `mysql-connector-python`.

## 🍃 Phase 2: Transition to MongoDB
After mastering the SQL workflow, I shifted focus to **MongoDB** to handle unstructured data and flexible schemas.

### 1. Local Environment Setup
* **Mongo Shell (mongosh):** Downloaded and configured the MongoDB Shell to interact with the database via the terminal.
* **CLI Learning:** Mastered essential commands for database management:
    * `show dbs` - List available databases.
    * `use <db_name>` - Switch context to a specific database.
    * `db.collection.insertOne()` - Add new records.
    * `db.collection.find()` - Retrieve data.
* **Local Connection:** Successfully connected the Streamlit application to a local MongoDB instance using mongosh command.

### 2. Cloud Integration with MongoDB Atlas
To make the application more scalable and accessible, I migrated the local database to the cloud.
* **Platform:** **MongoDB Atlas**.
* **Configuration:** Set up a "Shared Cluster" which provides a **512MB free tier** online database.
* **Connectivity:** Implemented the connection string using `pymongo` to bridge the Streamlit frontend with the Atlas cloud cluster.

## 📦 Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **SQL Server:** XAMPP (MySQL)
* **NoSQL Database:** MongoDB (Local & Atlas)
* **Tools:** Mongo Shell (mongosh), Compass
* **Language:** Python

## 📖 Key Learnings
* Understanding the difference between relational tables and JSON-like document storage.
* Managing database security and connection strings for cloud environments.
* Building interactive data-driven dashboards with real-time database updates.

## Live URL
* **Link:** [https://mind-stuff.streamlit.app/](https://mind-stuff.streamlit.app/)

---

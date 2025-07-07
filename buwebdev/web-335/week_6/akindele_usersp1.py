"""
Title: akindele_usersp1.py
Author: Joseph Akindele
Date: July 6, 2025
Description: Python program that connects to MongoDB and performs various operations.
"""

from pymongo import MongoClient
import certifi

# Load system certificate authority
ca = certifi.where()

# Updated MongoDB connection using certifi CA file
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@web335db.t68oxva.mongodb.net/web335DB?retryWrites=true&w=majority",
    tls=True,
    tlsCAFile=ca
)

# Access the database
db = client['web335DB']


# Display all users
print("\n-- DISPLAYING DOCUMENTS FROM users COLLECTION --")
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

# Find user by employeeId
print("\n-- DISPLAYING DOCUMENT WHERE employeeId IS 1011 --")
print(db.users.find_one({"employeeId": "1011"}))

# Find user by lastName
print("\n-- DISPLAYING DOCUMENT WHERE lastName IS Mozart --")
print(db.users.find_one({"lastName": "Mozart"}))
"""
Title: akindele_usersp2.py
Author: Joe Akindele
Date: July 13, 2025
Description: This program performs CRUD operations using Python and MongoDB.
"""

from pymongo import MongoClient
from datetime import datetime, timezone
import certifi

# Use certifi's CA bundle explicitly
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@web335db.t68oxva.mongodb.net/web335DB?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)

db = client["web335DB"]
#  Create a new user document
new_user = {
    "firstName": "Joe",
    "lastName": "Akindele",
    "employeeId": "2025",
    "email": "joe.akindele@love.com",
    "dateCreated": datetime.now(timezone.utc)
}

# Insert the document
user_id = db.users.insert_one(new_user).inserted_id
print("\n User created with _id:", user_id)


print("\n📄 Fetched user after creation:")
print(db.users.find_one({"employeeId": "2025"}))

#  Update email
db.users.update_one(
    {"employeeId": "2025"},
    {"$set": {"email": "akindele.joe@love.com"}}
)
print("\n Updated user email:")
print(db.users.find_one({"employeeId": "2025"}))

#  Delete the user
delete_result = db.users.delete_one({"employeeId": "2025"})
print(f"\n User deleted. Deleted count: {delete_result.deleted_count}")

#  Verify deletion
print("\n Fetch deleted user (should be None):")
print(db.users.find_one({"employeeId": "2025"}))

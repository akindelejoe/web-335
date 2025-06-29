// akindele-assignment5.2.js
// Author: Joe Akindele
// Date: June 29, 2025
// Assignment 5.2 - Projections

// Add a new user to the collection
db.users.insertOne({
    firstName: "Ada",
    lastName: "Okoro",
    email: "Adaokoro@gmail.com",
    age: 25
  });
  
  // Confirm Ada was added
  db.users.find({ email: "Adaokoro@gmail.com" });
  
  // Insert Mozart if not already present
  db.users.insertOne({
    firstName: "Wolfgang",
    lastName: "Mozart",
    email: "wolfgang.mozart@gmail.com",
    age: 35
  });
  
  // Update Mozart’s email
  db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@gmail.com" } }
  );
  
  // Confirm Mozart’s email was updated
  db.users.find({ lastName: "Mozart" });
  
  // Projection: Show only first name, last name, and email
  db.users.find({}, { _id: 0, firstName: 1, lastName: 1, email: 1 });
  
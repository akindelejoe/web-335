// Assignment 6.2 - Aggregate Queries
// Author: Joseph Akindele

// Aggregate query joining houses and students
db.houses.aggregate([
    {
      $lookup: {
        from: "students",
        localField: "studentId",
        foreignField: "_id",
        as: "studentInfo"
      }
    }
  ]).pretty()
  
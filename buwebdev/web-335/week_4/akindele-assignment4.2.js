// Display all users
db.users.find().pretty()

// Display user with email jbach@me.com
db.users.find({ email: "jbach@me.com" }).pretty()

// Display user with last name Mozart
db.users.find({ lastName: "Mozart" }).pretty()

// Display user with first name Richard
db.users.find({ firstName: "Richard" }).pretty()

// Display user with employeeId 1010
db.users.find({ employeeId: "1010" }).pretty()

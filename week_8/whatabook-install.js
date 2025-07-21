const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://admin:Lovedontcostathing1@cluster0.tjjeq2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();
    const db = client.db("whatabook");

    // Drop database if exists
    await db.dropDatabase();

    // Insert books
    await db.collection("books").insertMany([
      {
        bookId: "1",
        title: "Clean Code",
        price: 39.99,
        author: {
          authorId: "a1",
          name: "Robert C. Willian"
        },
        genre: "Software Engineering"
      },
      {
        bookId: "2",
        title: "Atomic Habits",
        price: 24.99,
        author: {
          authorId: "a2",
          name: "James Clifford"
        },
        genre: "Self-help"
      }
    ]);

    // Insert customer with wishlist
    await db.collection("customers").insertOne({
      customerId: "c1",
      name: "Jackson Niklas",
      wishlist: ["1", "2"]
    });

    console.log("Data inserted successfully!");
  } catch (err) {
    console.error("Error:", err);
  } finally {
    await client.close();
  }
}

run();

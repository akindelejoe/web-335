const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://admin:Lovedontcostathing1@cluster0.tjjeq2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();
    const db = client.db("whatabook");
    const books = db.collection("books");

    console.log("1. List of all books:");
    const allBooks = await books.find().toArray();
    console.log(allBooks);

    console.log("\n2. Books by genre (e.g., 'Self-help'):");
    const byGenre = await books.find({ genre: "Self-help" }).toArray();
    console.log(byGenre);

    console.log("\n3. Books by author name (e.g., 'Robert C. Martin'):");
    const byAuthor = await books.find({ "author.name": "Robert C. Martin" }).toArray();
    console.log(byAuthor);

    console.log("\n4. Book by bookId = '1':");
    const byId = await books.findOne({ bookId: "1" });
    console.log(byId);

  } catch (err) {
    console.error(" Query Error:", err);
  } finally {
    await client.close();
  }
}

run();

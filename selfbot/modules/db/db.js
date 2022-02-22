const { MongoClient } = require("mongodb");

// start DB

class DB {
  constructor() {
    let client = new MongoClient(
      "mongodb+srv://cojored:conrad12@cluster0.u4l9r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    );
    client.connect();
    this.client = client;
  }
}
module.exports = DB;

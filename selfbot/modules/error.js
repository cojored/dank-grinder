const discord = require("discord.js-selfbot");
const DB = require("./db/db.js");
/**
 * Error tracking w/db
 * @param {DB} dbclient
 * @param {discord.Client} client
 */
async function error(dbclient, client) {
  fails = dbclient.db("fails").collection("fails");
  oldfails = await fails.findOne({ token: client.token });
  // Check db for existing fails
  if (oldfails) {
    // Add another fail
    fails.updateOne(
      { token: client.token },
      {
        $set: {
          amount: Number(oldfails.amount + 1),
        },
      }
    );
    // if there are more than 2 fails kill it
    if (oldfails.amount >= 2) {
      fails.deleteOne({ token: client.token });
      process.exit(0);
    }
  } else {
    // otherwise insert the first fail
    fails.insertOne({ token: client.token, amount: Number(1) });
  }
}

module.exports = error;

const discord = require("discord.js-selfbot");
const DB = require("./db/db.js");
/**
 * Tracks Earnings
 * @param {discord.Message} response
 * @param {DB} dbclient
 * @param {Number} ownerID
 */
function trackEarnings(response, dbclient, ownerID) {
  setTimeout(function () {
    // Fetch the dank memer message
    response.channel.messages.fetch(response.id).then(async function (message) {
      //regex checking to get cash earned
      earned = message.embeds[0].description
        .toString()
        .match(/⏣ ?[0-9],?[0-9]{1,}/g);
      //proccessing amount earned
      if (earned[0]) {
        earned = Number(
          earned[0].replace("⏣", "").replace(",", "").replace(" ", "")
        );
      } else {
        earned = 0;
      }
      //update db with amount earned
      earnings = dbclient.db("userdata").collection("earnings");
      ownerEarnings = await earnings.findOne({ uid: ownerID });
      if (ownerEarnings) {
        earnings.updateOne(
          {
            uid: ownerID,
          },
          {
            $set: { earned: Number(ownerEarnings.earned) + Number(earned) },
          }
        );
      } else {
        earnings.insertOne({ uid: ownerID, earned: Number(earned) });
      }
    });
  }, 2000);
}

module.exports = trackEarnings;

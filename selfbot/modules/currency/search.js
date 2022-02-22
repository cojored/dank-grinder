const discord = require("discord.js-selfbot");
const DB = require("../db/db.js");
const click_button = require("../fetch/click_button.js");
const error = require("../error.js");
const trackEarnings = require("../trackEarnings.js");

/**
 * Runs the search command
 * @param {DB} dbclient
 * @param {discord.Client} client
 * @param {discord.Channel} channel
 * @param {Number} randomTimeout
 * @param {Number} ownerID
 */
function search(dbclient, client, channel, randomTimeout, ownerID) {
  setTimeout(() => {
    // say pls search
    channel.send("pls search").then(function (m) {
      // await a reply
      m.channel
        .awaitMessages((x) => x.author.id === "270904126974590976", {
          max: 1,
          time: 15000,
          errors: ["time"],
        })
        .then((resp) => {
          //get response
          response = resp.first();
          // are there buttons?
          if (!response.components[0].components) return;
          //select a random button
          option =
            response.components[0].components[
              Math.floor(
                Math.random() * response.components[0].components.length
              )
            ];
          // click the button
          click_button(response, option, client.token)
            .then(() => {
              fails = dbclient.db("fails").collection("fails");
              //delete fails
              fails.deleteOne({ token: client.token });
              //proccess amount earned
              trackEarnings(response, dbclient, ownerID);
            })
            .catch(() => {
              //ERROR!!!
              error(dbclient, client);
            });
        })
        .catch(() => {
          //ERROR!!!
          error(dbclient, client);
        });
    }, randomTimeout);
  });
}
module.exports = search;

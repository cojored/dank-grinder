const fetch = require("node-fetch");
const create_id = require("../createId.js");
function click_button(response, option, token) {
  // create the data sent to discord
  data = {
    application_id: response.author.id,
    channel_id: response.channel.id,
    message_id: response.id,
    // real session id
    session_id: response.client.ws.shards.first().sessionID,
    data: {
      component_type: option.type,
      custom_id: option.custom_id,
    },
    guild_id: response.guild.id,
    message_flags: 0,
    // calculate nonce
    nonce: `${
      (Math.round(Date.now() / 1000) * 1000 - 1420070400000) * 4194304
    }`,
    type: 3,
  };
  // return a promise for error tracking and stuff
  return new Promise((resolve, reject) => {
    // send request
    fetch("https://discord.com/api/v9/interactions", {
      method: "POST",
      headers: {
        Authorization: `${token}`,
        "Content-Type": "application/json",
        Connection: "keep-alive",
      },
      body: JSON.stringify(data),
    }).then((res) => {
      //check response status
      if (res.status === 204) {
        // good response resolve
        resolve(true);
      } else {
        //else reject
        reject("Invalid Response");
      }
    });
  });
}

module.exports = click_button;

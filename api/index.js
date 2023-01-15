const express = require("express");
const fetch = require("node-fetch");
const discord = require("discord.js-selfbot");
const app = express();

const invites = {
  944306502578085928: "qr7pYXjS",
  944306568399302736: "cJTpdnEtUJ",
  944306638117036132: "gjJtV3vSvA",
};

app.use(express.json());

app.post("/getUid", function (req, res) {
  const client = new discord.Client();

  client.on("ready", async function () {
    await res.send(client.user.id);
    client.destroy();
  });

  client.login(req.body.token);
});

app.post("/joinGuild", function (req, res) {
  fetch(
    `https://discord.com/api/v9/invites/${
      invites[Number(req.body.guild)]
    }?inputValue=https%3A%2F%2Fdiscord.gg%2F${
      invites[Number(req.body.guild)]
    }&with_counts=true&with_expiration=true`,
    { headers: { Authorization: req.body.token }, method: "GET" }
  ).then((resp) => {
    if (resp.status === 200) {
      return res.status(200).send("OK");
    } else {
      return res.status(500).send("uh oh");
    }
  });
});

app.post("/validateToken", function (req, res) {
  const client = new discord.Client();

  client.on("ready", async function () {
    await res.send("OK");
    client.destroy();
  });

  try {
    client.login(req.body.token);
  } catch (error) {
    res.status(500).send("Invalid");
  }
});

app.listen(6000);

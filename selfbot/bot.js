const Discord = require("discord.js-selfbot");
const client = new Discord.Client();
const DB = require("./modules/db/db.js");
const currency = require("./modules/currency/currency.js");
const db = new DB().client;

client.on("ready", () => {
  guild = client.guilds.cache.get(process.argv[4]);
  channel = guild.channels.cache.get(process.argv[5]);
  currency.search(
    db,
    client,
    channel,
    Math.random() * (10000 - 5000) + 5000,
    Number(process.argv[3])
  );
  setInterval(() => {
    guild = client.guilds.cache.get(process.argv[4]);
    channel = guild.channels.cache.get(process.argv[5]);
    currency.search(
      db,
      client,
      channel,
      Math.random() * (10000 - 5000) + 5000,
      Number(process.argv[3])
    );
  }, 30000);
});

client.on("message", function (message) {
  if (
    message.author.id != "694644198531661844" &&
    message.author.id != "934080564686913546"
  )
    return;
  if (message.content === ".searchTest") {
    currency.search(
      db,
      message.client,
      message.channel,
      100,
      Number(process.argv[3])
    );
  }
  if (message.content === ".stop") {
    process.exit(0);
  }
});

client.login(process.argv[2]);

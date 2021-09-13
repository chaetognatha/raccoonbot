# raccoonbot
This is a discord bot that you can run after installing the packages discord.py, dotenv and textblob!
You also need to have an api key in a .env file!
This very simple bot will just read any message on all channels where it has read/write perms and if it sees Spanish, it will post a translation to English after that message.
I initially wrote this using googletrans, but found that textblob was more reliable.

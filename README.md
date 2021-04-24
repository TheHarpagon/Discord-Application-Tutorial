![PyPI - Status](https://img.shields.io/pypi/status/discord.py) ![PyPI](https://img.shields.io/pypi/v/discord.py)
# Discord Bot Tutorial

A tutorial on how to make a [Discord](https://discord.com) Bot with the [`discord.py`](https://discordpy.readthedocs.io/en/latest/index.html) library along with a 24/7 uptime. This project should take anywhere from `15` to `45` minutes.

&NewLine;
## Platforms

Make sure you sign up for the following platforms before proceeding. Since this project will be completely in the cloud, there are no installations necessary for this project.
- [Discord](https://discord.com)
- [Replit](https://replit.com)
- [UptimeRobot](https://uptimerobot.com)

&NewLine;
## Getting Started (Discord)
This is the platform where your bot will operate


### Creating a Server
This is where you will create the platform for your bot to function on

- Go [here](https://discord.com/channels/@me)
- Read this [short article](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-) and create your server 
- Name the server `Replit Bot Testing`

### Creating the Application
This is where you will create an application for your bot

- Go to the [Discord Developer Portal](https://discord.com/developers/)
- Click `New Application`
- Name it `Replit Bot`


### <a id = "ctb"></a> Creating the Bot
This where you make the bot for your application
- Go to the `🧩 Bot` section
- Click `Add Bot`
- Click `Copy` under `Click to Reveal Token`
- **Paste and store this token** in a text file on your device (will be used later)

### Inviting the Bot
You will need to invite the bot to a Server in order to make it function

- Go to the `🏠 General Information` section
- Click `Copy` under `Application ID`
- Go [here](https://scarsz.me/authorize) and paste the Application ID
- Select your previously made server and click `Authorize`
- Once done, go back to Discord to check for confirmation

<img src = "https://i.gyazo.com/2dac3d0c16820e3ac67224ee24765f07.png" height = auto width = 350>

<img src = "https://i.gyazo.com/31c1545235e10a8a146e3c3e73905764.png" height = auto width = 500>

&NewLine;
## Getting Started (Replit)
This is the platform where you will host and run the code for the bot

### Creating a Repl
- Go [here](https://replit.com)
- Make a new repl
- Select [Python](https://www.python.org/) as the language
- Name it "Discord Application" or anything else you want

<img src = "https://i.gyazo.com/cc3f733bf2241e59a41545e0ea662235.png" height = auto width = 350>

### Adding files
- Add a `keepAlive.py` file as shown below

<img src = "https://i.gyazo.com/019f84f992dcab6c6e8b7611e6389d92.gif" height = auto width = 200>

- Create an environment variable as shown below and use your previously saved token for the value
- If you do not have your token, go back [here](#ctb) and retrieve it

<img src = "https://i.gyazo.com/4a2db12daa2935ca4a75ea62ff91d277.gif" height = auto width = 200>

&NewLine;
## Booting Up

You will now implement the necessary tools to boot up the bot

### `main.py`
This code will be the framework of your bot. It contains a few commands and events to demonstrate the layout of the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) library usage. You can add more commands/events later as you read through the [documentation](https://discordpy.readthedocs.io/en/latest/index.html). For now, **paste this [code](https://github.com/TheHarpagon/Discord-Application-Tutorial/blob/master/main.py) into your repl's `main.py` file.**

### `keepAlive.py`
This code that will allow your application to run 24/7. Paste it into your repl's `keepAlive.py` file

```py
from flask import Flask
from threading import Thread
import random

app = Flask("")
@app.route("/")

def home():
  return("Online!")

def run():
  app.run(host = "0.0.0.0", port = random.randint(2000, 9000))

def keepAlive():
  thread = Thread(target = run)
  thread.start()
```

&NewLine;
## Uptime Robot
The last step of this tutorial is to set up the [UptimeRobot](https://uptimerobot.com) monitor

- Click `▶️ Run` on the top of your repl
- Copy the URL in the top right of your screen (mine was `https://Replit-Bot.hdadhich01.repl.co`)
- Go to your UptimeRobot [dashboard](https://uptimerobot.com/dashboard?ref=website-header#mainDashboard) and add a new monitor
- Fill out the fields as shown below, and use your own repl's URl for the empty field

<img src = "https://i.gyazo.com/5e610702f186982b07560a75e073861e.png" height = auto width = 350>

Click `Create Monitor`, and that's it. You have completed building your Discord Bot!

&NewLine;
## Testing it Out
Go to your previously created server and test out the following commands.
- `!help` - displays a list of all commands
- `!hello` - says hello back
- `!ping` - displays the application latency
- `!predict <question>` - predicts the outcome of your question
- `!color <hexCode>` - displays the given color code in an embed
- `!dm <user> <message>` - sends a direct message to the specified user

<img src = "https://i.gyazo.com/e56c903d8ba61444976c93a37bb66b8a.png" height = auto width = 750>

&NewLine;
## Support
If you encountered any issues, feel free to direct message me on my Discord found [here](https://dsc.bio/TheHarpagon)!

![PyPI - Status](https://img.shields.io/pypi/status/discord.py) ![PyPI](https://img.shields.io/pypi/v/discord.py)
# Discord Application Tutorial

A tutorial on how to make a [Discord](https://discord.com) Application with the [`discord.py`](https://discordpy.readthedocs.io/en/latest/index.html) library. The application will be hosted on [Replit](https://replit.com) with [UptimeRobot](https://uptimerobot.com) to ensure a 24/7 uptime. The duration of this project is from `15` to `45` minutes.

&NewLine;
## Platforms

Make sure you sign up for the following platforms before proceeding. There are no installations needed for this project.
- [Discord](https://discord.com)
- [Replit](https://replit.com)
- [UptimeRobot](https://uptimerobot.com)

&NewLine;
## Getting Started (Discord)

This is the platform where your application will operate.

### Creating a Server
This server is where your application will function.

- Go [here](https://discord.com/channels/@me)
- Read this [short article](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-) and create your server 
- Name the server "Application Testing" or anything you want

### Creating an Application
This is where you will make the Discord application.
- Go to the [Discord Developer Portal](https://discord.com/developers/)
- Click "New Application"
- Name it "Replit Application" or anything else you want


### <a id = "cabf"></a> Creating an Application Account
This where you make the Discord account for the Application.
- Click the "🧩 Bot" section on the left hand side
- Click "Add Bot"
- Click "Copy" under "Click to Reveal Token"
- **Paste and store this token** in a text file on your device (will be used later)

### Inviting the Application
You will need to invite the application to a Server in order to make it function
- Click the "🏠 General Information" section on the left hand side
- Click "Copy" under "Client ID"
- Go [here](https://scarsz.me/authorize) and paste the Client ID
- Select the server you made before
- Once done, go back to Discord to check for confirmation

<img src = "https://i.gyazo.com/5706d17ac6b1f62c59e913d77c75233a.png" height = auto width = 350>

<img src = "https://i.gyazo.com/67ba588a9aece7b778b9e9f112aee7b3.png" height = auto width = 500>

&NewLine;
## Getting Started (Replit)

[Replit](https://replit.com) is the platform where you will host and run the code for the application.

### Creating a Repl
- Make a new repl
- Select [Python](https://www.python.org/) as the language
- Name it "Discord Application" or anything else you want

<img src = "https://i.gyazo.com/3638191cc3810c3624ac6e17968b1ed7.png" height = auto width = 350>

### Adding files
- Add a `.env` and `keepAlive.py` file as shown below

<img src = "https://i.gyazo.com/26b79017e4ab327bfb7b1f051cdc8118.gif" height = auto width = 350>

&NewLine;
## Booting Up

Once finished with the setup process above, you will implement the necessary tools to boot up the application.

### `main.py`
This code will be the framework of your application. It contains a few commands and events to demonstrate the layout of the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) library usage. You can add more commands/events later as you read through the [docs](https://discordpy.readthedocs.io/en/latest/index.html).

For now, paste this [code](https://github.com/TheHarpagon/Discord-Application-Tutorial/blob/master/main.py) into your `main.py` file in your previously create repl

### `.env`
Now you will use your previously saved token. This token authenticates and allows you to control the application. Anyone with your token can manipulate your application. If you did not save your token, refer to this [section](#cabf).

Go to the `.env` file in your repl and type in the following with your token after the equal sign
```
token = 
```

### `keepAlive.py`
This is the file that will allow your application to run 24/7. Paste the following code into your `keepAlive.py` file.

```python
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
The last step of this tutorial is to set up the [UptimeRobot](https://uptimerobot.com) dashboard. 
- Click "▶️ Run" on the top of your repl
- Your application is now running, you can go back to your server and look at the right hand side
- Copy the URL in the top right of your screen (mine was `https://Discord-Application.hdadhich01.repl.co`)
- Go to your UptimeRobot [dashboard](https://uptimerobot.com/dashboard?ref=website-header#mainDashboard) and add a new monitor
- Fill out the fields as such, pasting your URL in its corresponding field:

<img src = "https://i.gyazo.com/27925cee6e140fb30d677436d76639d2.png" height = auto width = 350>

Click "Create Monitor", and that's it. You have completed building your Discord Application!

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

If you encountered any errors, feel free to direct message me on my Discord [here](https://dsc.bio/TheHarpagon)!

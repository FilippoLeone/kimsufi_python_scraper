# Kimsufi scraper

This script allows the user to be alerted when the availability changes over time for the Kimsufi servers.

**NOTE** A Telegram channel is already set up and it's running this script!

![alt text](https://telegram.org/img/t_logo.png "Telegram Channel") 

Join now: https://t.me/kimsufi_alert 

The script will run every hour and it will send a message in the channel when the availability changes.

# How to use the script

Download FireFox and [Gecko](https://github.com/mozilla/geckodriver/releases)

Clone the repository: `git clone https://github.com/FilippoLeone/kimsufi_python_scraper.git`

Create a file called `credentials.py` with the following structure:
- `firefox_path = r''`
This path will be your gecko executable file, note that you will still need to install firefox to get this running.
- `telegram_token = ''`
Fill this value with your Telegram bot API key, you can get this key from the `BotFather`
- `telegram_channel = ''`  
This value is your channel, create one and add your bot inside, example value for this field `@kimsufi_alert_channel`

Now you need to create a Python virtual environment with `python -m venv <directory>` 

You can now install the dependencies with `pip -r install requirements.txt`

This script was tested with `python 3.7` but it should work for python3+, tested on both Windows & Ubuntu server.

# Help wanted! 

Let's refactor the code and make this a bit prettier! Feel free to send me a pull request :)

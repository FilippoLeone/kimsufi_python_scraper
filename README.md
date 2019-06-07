# Kimsufi scraper

This script allows the user to be alerted when the availability changes over time for the Kimsufi servers. 
A Telegram channel is already set up and if you just want to get this information you can join by following this link: https://t.me/kimsufi_alert, the script will run every hour and it will send a message in the channel when the availability changes.

# How to use the script

Create a file called credentials.py with the following structure:
- `firefox_path = r''`
This path will be your gecko executable file, note that you will still need to install firefox to get this running.
- `telegram_token = ''`
Fill this value with your Telegram bot API key, you can get this key from the `BotFather`
- `telegram_channel = ''`  
This value is your channel, create one and add your bot inside, example value for this field `@kimsufi_alert_channel`

This script was tested with `python 3.7` but it should work for python3+, tested on both Windows & Ubuntu server.

# Help wanted! 

Let's refactor the code and make this a bit prettier! Feel free to send me a pull request :)

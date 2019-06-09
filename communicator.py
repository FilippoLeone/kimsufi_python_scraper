import requests
from logger import Logger
import message_strings as loginfo
import credentials

class Communicator:
    logType = 'CommunicatorLog'

    def __init__(self):
        self.Logger = Logger(Communicator.logType)

    def telegram_message(self, message, channel, parse_mode='markdown'):
        """
        This method sends a message into a channel from a Telegram bot with a get request. 
        """
        response = requests.get(
                f'https://api.telegram.org/bot{credentials.telegram_token}/sendMessage?chat_id={channel}&text={message}&parse_mode={parse_mode}'
        )
        if response.status_code == 200:
            self.Logger.log(loginfo.REQUEST_SUCCEED)
        else:
            self.Logger.log(loginfo.REQUEST_FAIL + response.status_code)

    def send_mail(self):
        """
        Unimplemented. Please consider implementing this method in a pull request.
        """
        pass
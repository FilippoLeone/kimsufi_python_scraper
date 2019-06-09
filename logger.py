import datetime
import message_strings as loginfo
import json

class Logger:

    def __init__(self, logType='default'):
        self.logType = logType

    def log(self, message):
        """
        Logs the a message into logfile.txt along with a timestamp & log type.
        """
        timestamp = datetime.datetime.now().isoformat()
        try:
            with open('logfile.txt','a') as logfile:
                logfile.write(f"{timestamp} - {self.logType} : {message}\n")
        except FileNotFoundError:
            with open('logfile.txt', 'w') as logfile:
                logfile.write(f"{timestamp} - {self.logType} : {message}\n")

    def log_json(self, json_dict):
        """
        Writes json from a python dict inside serverlog.json
        """
        with open('serverlog.json', 'w', encoding='utf8') as jsonlog:
            jsonlog.write(json.dumps(json_dict, ensure_ascii=False, indent=4)) 
        self.log(loginfo.JSON_SAVE)
            
    def get_json(self):
        """
        Returns json data from serverlog.json in a python dict
        """
        try:
                with open('serverlog.json', 'r', encoding='utf8') as serverlog:
                        jsondata = json.load(serverlog)
                self.log(loginfo.JSON_GET)
                return jsondata
        except FileNotFoundError:
                self.log(loginfo.JSON_GET_FAIL)
                return False        

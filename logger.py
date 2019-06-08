import datetime
import message_strings as loginfo
import json

class Logger:
    def __init__(self):
        self.type = 'Logger'

    def log(self, message, type):
        timestamp = datetime.datetime.now().isoformat()
        try:
            with open('logfile.txt','a') as logfile:
                logfile.write(f"{timestamp} - {type} : {message}\n")
        except FileNotFoundError:
            with open('logfile.txt', 'w') as logfile:
                logfile.write(f"{timestamp} - {type} : {message}\n")

    def log_json(self, json_dict):
        with open('serverlog.json', 'w', encoding='utf8') as jsonlog:
            jsonlog.write(json.dumps(json_dict, ensure_ascii=False, indent=4)) 
        self.log(loginfo.JSON_SAVE, self.type)
            
    def get_json(self):
        try:
                with open('serverlog.json', 'r', encoding='utf8') as serverlog:
                        jsondata = json.load(serverlog)
                self.log(loginfo.JSON_GET, self.type)
                return jsondata
        except FileNotFoundError:
                self.log(loginfo.JSON_GET_FAIL, self.type)
                return False        

import requests

class LintBotFunction:
     def __init__(self,push_str):
        self.push_str = push_str
        self.url = "https://asia-east1-catproject-338203.cloudfunctions.net/pushfunction?message="
          
     def push_message(self):
        requests.get(self.url + self.push_str)
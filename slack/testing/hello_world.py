# testing script
import requests
import sys
sys.path.append('../../../keys')
from keys import Keychain

class Tester:

    def __init__(self):
        self.time_taken = 0

    def post(self, slack_webhook):
        payload = {"text":"Hello, World!"}
        requests.post(slack_webhook, json=payload)


if __name__ == '__main__':
    
    kc = Keychain()
    bot_testing_webhook = kc.get('bot_testing_webhook')
    t1 = Tester()
    t1.post(bot_testing_webhook)

# testing script
import requests
import sys

class Tester:

    def __init__(self):
        self.time_taken = 0

    def post(self, slack_webhook):
        payload = {"text":"Hello, World!"}
        requests.post(slack_webhook, json=payload)


if __name__ == '__main__':
    
    bot_testing_webhook = sys.argv[1]
    t1 = Tester()
    t1.post(bot_testing_webhook)

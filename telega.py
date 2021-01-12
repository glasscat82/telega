import requests, sys, json, re

class Telega():
    """simple class for telegram, minimum set of API for sending and changing messages in telegrams"""
    def __init__(self, token = "you_token_telegram_bot", path = "", filename = "data.json"):
        self.token = token
        self.path = path
        self.filename = filename

    @staticmethod
    def p(text, *args):
        print(text, *args, sep=' / ', end='\n')

    # rounding?!, in 3m python banking rounding to the nearest integer; (
    @staticmethod
    def int_r(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    def sendMessage(self, chat_id, text='Meow!', parse_mode='html', reply_markup={}, token_bot=None):
        token_bot = self.token if token_bot is None else token_bot
        data = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}

        if len(reply_markup) > 0:
            data['reply_markup'] = json.dumps(reply_markup)

        r = requests.post(
            url = f'https://api.telegram.org/bot{token_bot}/sendMessage',
            data = data,
            ).json()
        return r

    # core.telegram.org/bots/api#updating-messages
    def editMessageText(self, chat_id, message_id, text='bla', parse_mode='html', reply_markup={}, token_bot=None):
        token_bot = self.token if token_bot is None else token_bot
        data = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode': parse_mode}

        if len(reply_markup) > 0:
            data['reply_markup'] = json.dumps(reply_markup)

        r = requests.post(
            url = f'https://api.telegram.org/bot{token_bot}/editMessageText',
            data = data,
            ).json()
        return r
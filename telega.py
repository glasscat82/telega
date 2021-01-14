import requests, sys, json, re

class Telega():
    """simple class for telegram, minimum set of API for sending and changing messages in telegrams"""
    def __init__(self, token = "you_token_telegram_bot", path = "", filename = "data.json"):
        self.token = token
        self.path = path
        self.filename = filename

    # --------- The help functions ------ #

    @staticmethod
    def p(text, *args):
        print(text, *args, sep=' / ', end='\n')

    @staticmethod
    def parse_text(text):
        pattern = r'/\w+'
        key = re.search(pattern, text)
        if key != None:
            g = key.group()
            return g[1:].lower()
        else:
            return False

    # rounding?!, in 3m python banking rounding to the nearest integer ;(
    @staticmethod
    def int_r(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    @staticmethod
    def array_chunk(array, size):
        res = []
        num = len(array)/size
        count_size = int(num + (0.5 if num > 0 else -0.5))
        for index, cp in enumerate(range(count_size), 1):
            res.append(array[cp*size: index*size])
        return res

    @staticmethod
    def write_json(data, filename=f'{self.path}/data.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def load_json(filename=f'{self.path}/data.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        return {}

    # --------- The telegram functions ------ #

    # core.telegram.org/bots/api#sendmessage
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
    def editMessageText(self, chat_id, message_id, text='Meow!', parse_mode='html', reply_markup={}, token_bot=None):
        token_bot = self.token if token_bot is None else token_bot
        data = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode': parse_mode}

        if len(reply_markup) > 0:
            data['reply_markup'] = json.dumps(reply_markup)

        r = requests.post(
            url = f'https://api.telegram.org/bot{token_bot}/editMessageText',
            data = data,
            ).json()
        return r
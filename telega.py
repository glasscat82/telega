import requests, sys, json, re, math

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
        count_size = math.ceil(len(array)/size)
        for index, cp in enumerate(range(count_size), 1):
            res.append(array[cp*size: index*size])
        return res

    def write_json(self, data, filename=None):
        filename = f'{self.path}/data.json' if filename is None else filename
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_json(self, filename=None):
        filename = f'{self.path}/data.json' if filename is None else filename
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        return {}

    # --------- The telegram functions ------ #

    # Returns basic information about the bot in form of a User object.
    def getMe(self, token_bot=None):
        token_bot = self.token if token_bot is None else token_bot
        r = requests.post(url=f'https://api.telegram.org/bot{token_bot}/getMe').json()
        return r

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
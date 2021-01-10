import requests, sys, json, re

class Telega():
    """simple class for telegram, minimum set of API for sending and changing messages in telegrams"""
    def __init__(self, token="you_token_telegram_bot"):
        self.token=token

    @staticmethod
    def p(text, *args):
        print(text, *args, sep=' / ', end='\n')
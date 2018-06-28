import requests

from config import BOT


class Bot:
    @staticmethod
    def notify(message):
        requests.get(
            'https://api.telegram.org/%s/sendMessage' % BOT['token'],
            params={'chat_id': BOT['chat'], 'text': message, 'parse_mode': 'HTML'}
        )

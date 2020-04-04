import os

import requests


class Bot:
    @staticmethod
    def notify(message):
        requests.get(
            'https://api.telegram.org/%s/sendMessage' % os.getenv('BOT_TOKEN'),
            params={'chat_id': os.getenv('BOT_CHAT'), 'text': message, 'parse_mode': 'HTML'}
        )

#! /usr/bin/env python3

import os
import re

from bot import Bot
from cian import Cian
from db import DB
from distance import Distance

if __name__ == '__main__':
    regex = re.compile('([0-9.]+ руб.)')

    cian = Cian(os.getenv('CIAN_URL'))
    ads = cian.get_ads()
    db = DB()
    for ad in ads:
        _, created = db.get_or_create(ad)
        if created:
            walk = Distance.calc(ad.address)
            matches = re.search(regex, ad.price)
            if matches:
                price = matches.group()
            else:
                price = ad.price

            if walk['value'] >= 2040:
                continue

            message = '%s, %s, %s\n%s' % (
                '<b>%s от офиса</b> ' % walk['text'] if walk['value'] else ' ',
                ad.address,
                '<b>%s</b>' % price,
                ad.url
            )
            Bot.notify(message)
    db.conn.close()

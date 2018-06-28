#! /usr/bin/env python3

from bot import Bot
from db import DB
from cian import Cian
from config import CIAN_URLS
from distance import Distance


if __name__ == '__main__':
    for url in CIAN_URLS:
        cian = Cian(url)
        ads = cian.get_ads()
        db = DB()
        for ad in ads:
            _, created = db.get_or_create(ad)
            if created:
                walk = Distance.calc(ad.address)
                message = '%s-ка%sна %s, %s\n%s' % (
                    ad.rooms,
                    ' в <b>%s от офиса</b> ' % walk['text'] if walk['value'] else ' ',
                    ad.address,
                    ad.price,
                    ad.url
                )
                Bot.notify(message)
        db.conn.close()

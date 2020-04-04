import os

import psycopg2

from cian import Ad


class DB:
    def __init__(self, dsn=os.getenv('DB_DSN')):
        self.conn = psycopg2.connect(dsn)

    def get_or_create(self, ad: Ad):
        c = self.conn.cursor()
        c.execute("SELECT * FROM ads WHERE ad_id=%s", (ad.id,))
        if c.fetchone():
            created = False
            c.execute(
                "UPDATE ads SET rooms=%s, address=%s, price=%s, phones=%s, description=%s, url=%s WHERE ad_id=%s",
                (ad.rooms, ad.address, ad.price, ad.phones, ad.description, ad.url, ad.id)
            )
        else:
            created = True
            c.execute(
                "INSERT INTO ads(ad_id, rooms, address, price, phones, description, url) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                ad
            )
        c.close()
        self.conn.commit()
        return ad, created

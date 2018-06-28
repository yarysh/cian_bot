import sqlite3

from cian import Ad
from config import DB_PATH


class DB:
    def __init__(self, db=DB_PATH):
        self.conn = sqlite3.connect(db)

    def get_or_create(self, ad: Ad):
        c = self.conn.cursor()
        c.execute("SELECT * FROM ads WHERE ad_id=?", (ad.id,))
        if c.fetchone():
            created = False
            c.execute(
                "UPDATE ads SET rooms=?, address=?, price=?, phones=?, description=?, url=? WHERE ad_id=?",
                (ad.rooms, ad.address, ad.price, ad.phones, ad.description, ad.url, ad.id)
            )
        else:
            created = True
            c.execute(
                "INSERT INTO ads(ad_id, rooms, address, price, phones, description, url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                ad
            )
        c.close()
        self.conn.commit()
        return ad, created

import collections

import requests
import xlrd


Ad = collections.namedtuple('Ad', ['id', 'rooms', 'address', 'price', 'phones', 'description', 'url'])


class Cian:
    def __init__(self, url):
        self.url = url

    def _download_xlsx(self):
        resp = requests.get(
            self.url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.0 Safari/537.36'},
            # proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'},
        )
        if resp.status_code != 200: return None
        with open('tmp/cian.xlsx', 'wb') as f:
            f.write(resp.content)
        return f.name

    def get_ads(self):
        ads = []
        xlsx = xlrd.open_workbook(self._download_xlsx())
        sheet = xlsx.sheet_by_index(0)

        indexes = {
            'id': {'field': 'ID  объявления', 'index': None},
            'rooms': {'field': 'Количество комнат', 'index': None},
            'address': {'field': 'Адрес', 'index': None},
            'price': {'field': 'Цена', 'index': None},
            'phones': {'field': 'Телефоны', 'index': None},
            'description': {'field': 'Описание', 'index': None},
            'url': {'field': 'Ссылка на объявление', 'index': None},
        }
        header = sheet.row_values(0)
        for key, val in indexes.items():
            try:
                indexes[key]['index'] = header.index(val['field'])
            except ValueError:
                return ads

        for row in range(1, sheet.nrows):
            data = sheet.row_values(row)
            ads.append(
                Ad(
                    id=data[indexes['id']['index']],
                    rooms=data[indexes['rooms']['index']],
                    address=data[indexes['address']['index']],
                    price=data[indexes['price']['index']],
                    phones=data[indexes['phones']['index']],
                    description=data[indexes['description']['index']],
                    url=data[indexes['url']['index']],
                )
            )
        return ads

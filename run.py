import requests
import sys
import pyexcel

from retrying import retry
from requests.exceptions import RequestException


def is_request_exception(e):
    return issubclass(type(e), RequestException)


class Epidemic:
    def __init__(self):
        self.url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
            "Referer": "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"
        }

    @retry(retry_on_exception=is_request_exception, wrap_exception=False, stop_max_attempt_number=3)
    def get_data(self):
        r = requests.get(self.url, headers=self.headers)
        if r.status_code != 200:
            raise Exception('No data Error.')
        else:
            data = r.json()
            if data['msg'] == u'成功':
                data = data['data']
            else:
                print(u'爬取失败')
                sys.exit(0)
            self.save_data(data)

    def save_data(self, data):
        # China
        content = {}
        china = [['date',
                  'today-confirm', 'today-suspect', 'today-heal', 'today-dead', 'today-severe', 'today-storeConfirm',
                  'today-input',
                  'total-confirm', 'total-suspect', 'total-heal', 'total-dead', 'total-severe', 'total-input',
                  'extData', 'lastUpdateTime']]
        china_day_list = data['chinaDayList']
        for d in china_day_list:
            china.append([d['date'], d['today']['confirm'], d['today']['suspect'], d['today']['heal'],
                          d['today']['dead'], d['today']['severe'], d['today']['storeConfirm'],
                          d['today']['input'] if 'input' in d['today'] else '',
                          d['total']['confirm'], d['total']['suspect'], d['total']['heal'], d['total']['dead'],
                          d['total']['severe'], d['total']['input'], d['extData'], d['lastUpdateTime']])
        content['China'] = china

        # today
        provinces = data['areaTree'][2]['children']
        for d in provinces:
            name = d['name']
            today = [['id', 'name', 'lastUpdateTime',
                      'today-confirm', 'today-suspect', 'today-heal', 'today-dead', 'today-severe', 'today-storeConfirm',
                      'total-confirm', 'total-suspect', 'total-heal', 'total-dead', 'total-severe']]
            for c in d['children']:
                today.append([c['id'], c['name'], c['lastUpdateTime'],
                              c['today']['confirm'], c['today']['suspect'], c['today']['heal'], c['today']['dead'],
                              c['today']['severe'], c['today']['storeConfirm'], c['total']['confirm'],
                              c['total']['suspect'], c['total']['heal'], c['total']['dead'], c['total']['severe']])
            content[name] = today

        book = pyexcel.get_book(bookdict=content)
        book.save_as("output.xlsx")


if __name__ == '__main__':
    epidemic = Epidemic()
    epidemic.get_data()

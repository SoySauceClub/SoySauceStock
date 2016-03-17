import string

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class YahooEarningDateScraper(object):
    yahoo_finance_url_part = 'http://finance.yahoo.com/q?s='

    def __init__(self, thread_waiting_seconds):
        self.waiting_seconds = thread_waiting_seconds

    def fetch_earning_date(self, stock):
        request_url = self.yahoo_finance_url_part + stock
        driver = webdriver.Firefox()
        driver.implicitly_wait(self.waiting_seconds)
        driver.get(request_url)

        event_div = driver.find_element_by_id('table1')

        inner_text = event_div.text.split('\n')
        driver.close()
        for index in range(len(inner_text)):
            if('Earnings' in inner_text[index]):
                earnDateFullText = inner_text[index]
                earnDateValue = earnDateFullText[15:]
                return earnDateValue
        return ''


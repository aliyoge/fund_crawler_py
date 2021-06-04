# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

req = requests.get("http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=000033&topline=10&year=2021&month=3")

text = req.text

text = text.replace('var apidata={ content:"', '')

pattern = re.compile(r'",arryear:.*')

html = re.sub(pattern, '', text)

soup = BeautifulSoup(html,'lxml')

trs = soup.table.tbody.find_all("tr")[0:3]

for tr in trs:
    tds = tr.find_all("td")
    print(tds[1].string)
    print(tds[8].string)

# select poscode, posname, count(*) as count, cast(sum(poscost) as int) from fund group by poscode, posname order by count desc limit 10;
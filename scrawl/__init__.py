# -*- coding: utf-8 -*-

"""

    PythonBase.scrawl
    ~~~~~~~~~~~~~~~~~

    stamaimer 08/29/16

"""

import requests
from lxml import html


url = "http://zhaoren.idtag.cn/samename/searchName!pmbyrepeatlist.htm"

xpath = "//div[@class='top-right-lb']/ul/li/p/text()"

response = requests.get(url)

if response.status_code == requests.codes.ok:

    tree = html.fromstring(response.content)

    elements = tree.xpath(xpath, smart_strings=0)

    for element in elements:

        print element.split('.')[1]

else:

    print response.reason



# -*- coding:utf-8 -*-

import os


class Config(object):
    DEBUG = True
    # 获取VAL_HOST环境变量，如果没有返回true
    VAL_HOST = os.getenv("VAL_HOST", "true")
    FORBITDDEN = []
    HOST = ["127.0.0.1:8080"]
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    WEBSITE = dict(
        IS_RUNNING=True,
        TOKEN='',
        AUTHOR_LATEST_COUNT=5,
    )

    SCHEDULED_DICT = dict(
        SPIDER_INTERVAL=int(os.getenv('SPIDER_INTERVAL', 60)),
    )

    # Engine config
    URL_PHONE = 'https://m.baidu.com/s'
    URL_PC = 'http://www.baidu.com/s'
    BAIDU_RN = 15
    SO_URL = "https://www.so.com/s"
    BY_URL = "https://www.bing.com/search"
    DUCKGO_URL = "https://duckduckgo.com/html"

    REMOTE_SERVER = {
        'proxy_server': 'http://0.0.0.0:8002/'
    }

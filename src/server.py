# -*- coding:utf-8 -*-
import aiocache
import os
import sys
import datetime

from sanic import Sanic
from sanic.response import html, redirect
from sanic_session import RedisSessionInterface

from src.config import LOGGER, CONFIG
from src.database.redisbase import RedisSession
from src.views import md_bp,novel_bp

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Sanic(__name__)
app.session_interface = None
app.blueprint(md_bp)
app.blueprint(novel_bp)


@app.listener("before_server_start")
def init_cache(app, loop):
    LOGGER.info("Start aiocahe")
    app.config.from_object(CONFIG)
    REDIS_DICT = CONFIG.REDIS_DICT
    aiocache.settings.set_defaults(class_="aiocache.RedisCache",
                                   endpoint=REDIS_DICT.get('REDIS_ENDPOINT', 'localhost'),
                                   port=REDIS_DICT.get('REDIS_PORT', 6379),
                                   db=REDIS_DICT.get('CACHE_DB', 0),
                                   password=REDIS_DICT.get('REDIS_PASSWORD', None),
                                   loop=loop, )
    LOGGER.info("Start reids pool")
    redis_session = RedisSession()
    app.get_redis_pool = redis_session.get_redis_pool
    app.session_interface = RedisSessionInterface(app.get_redis_pool,
                                                  cookie_name="novel_sid",
                                                  expiry=30 * 24 * 60 * 60)


@app.middleware('request')
async def add_session_to_request(request):
    print(request.headers)
    # host = request.headers.get('host', None)
    user_agent = request.headers.get('user-agent', None)
    if user_agent:
        user_ip = request.headers.get('X-Forwarded-For')
        LOGGER.info('user ip is:{}'.format(user_ip))
        if user_ip in CONFIG.FORBITDDEN:
            return html('<h3>网站正在维护中.....</h3>')
        if CONFIG.WEBSITE['IS_RUNNING']:
            await app.session_interface.open(request)
        else:
            return html('<h3>网站正在维护中.....</h3>')
    else:
        return html('<h3>网站正在维护中.....</h3>')


@app.middleware('response')
async def save_session(request, response):
    if request.path == '/operate/login' and request['session'].get('user', None):
        await app.session_interface.save(request, response)
        response.cookies['novel_sid']['expires'] = datetime.datetime.now() + datetime.timedelta(days=30)
    elif request.path == '/register':
        try:
            response.cookies['reg_index'] = str(request['session']['index'][0])
        except KeyError as e:
            LOGGER.error(e)


if __name__ == "__main__":
    app.run(host="127.0.0.1", workers=2, port=8081, debug=CONFIG.DEBUG)

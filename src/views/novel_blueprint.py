# -*- coding:utf-8 -*-

from sanic import Blueprint
from sanic.response import html, text, redirect
from jinja2 import Environment, PackageLoader, select_autoescape

from src.config import CONFIG

novel_bp = Blueprint('novel_blueprint')
novel_bp.static('/static/novels', CONFIG.BASE_DIR + '/static/novels')

# jinja2 config
env = Environment(loader=PackageLoader('views.novel_blueprint', '../templates/novels'),
                  autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@novel_bp.route('/')
async def index(request):
    user = request['session'].get('user', None)
    search_ranking = []
    if user:
        return template('index.html', title='小说搜索引擎', is_login=1, user=user,
                        search_ranking=search_ranking)
    else:
        return template('index.html', title='小说搜索引擎', is_login=0,
                        search_ranking=search_ranking)

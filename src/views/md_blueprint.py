# -*- coding:utf-8 -*-

from sanic import Blueprint
from sanic.response import html, text, redirect
from jinja2 import Environment, PackageLoader, select_autoescape

from src.config import CONFIG

md_bp = Blueprint('rank_blueprint', url_prefix='md')
md_bp.static('/static/md', CONFIG.BASE_DIR + '/static/md')

# jinja2 config
env = Environment(loader=PackageLoader('views.md_blueprint', '../templates/md'),
                  autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@md_bp.route('/')
async def index(request):
    user = request['session'].get('user', None)
    novel_head = ['#', '小说名', '搜索次数']
    first_type_title = '搜索排行'
    first_type = []
    search_ranking = []
    if user:
        return template('index.html', title='acer_novel', is_login=1, user=user,
                        search_ranking=search_ranking, first_type=first_type,
                        first_type_title=first_type_title, novel_head=novel_head, is_owl=1)
    else:
        return template('index.html', title='acer_novel', is_login=0,
                        search_ranking=search_ranking, first_type=first_type,
                        first_type_title=first_type_title, novel_head=novel_head, is_owl=1)

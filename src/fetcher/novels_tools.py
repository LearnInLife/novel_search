# -*- coding:utf-8 -*-

from importlib import import_module


async def get_novels_info(class_name, novels_name):
    """
    :param class_name: 搜索引擎名
    :param novels_name: 小说名
    :return:
    """
    novels_module = import_module('src.fetcher.{}.{}_novels'.format('novels_factory', class_name))
    novels_info = await novels_module.start(novels_name)
    return novels_info

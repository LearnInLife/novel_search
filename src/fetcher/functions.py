# -*- coding:utf-8 -*-

import os
import aiofiles
import random
from src.config import CONFIG


async def _get_data(filename, default=''):
    root_folder = os.path.dirname(os.path.dirname(__file__))
    user_agents_files = os.path.join(os.path.join(root_folder, "data"), filename)

    try:
        async with aiofiles.open(user_agents_files, mode='r') as f:
            data = [_.strip() for _ in await f.readlines()]
    except:
        data = [default]
    return data


async def get_random_user_agent():
    return random.choice(await _get_data('user_agents.txt', CONFIG.USER_AGENT))

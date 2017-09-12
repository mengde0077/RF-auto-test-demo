# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-09-01 16:52:29
# @Last Modified by:   caolinming
# @Last Modified time: 2017-09-04 17:56:28

import os

from NdolLibrary.redisKeywords import RedisKeywords
from NdolLibrary.mysqlKeywords import MysqlKeywords
from NdolLibrary.otherKeywords import OtherKeywords

__version_file_path__ = os.path.join(os.path.dirname(__file__), 'VERSION')
__version__ = open(__version_file_path__, 'r').read().strip()


class NdolLibrary(RedisKeywords, MysqlKeywords, OtherKeywords):
    """
    用于 8天 自动化测试 辅助支持库
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
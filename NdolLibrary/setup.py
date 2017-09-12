# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-09-01 16:48:07
# @Last Modified by:   caolinming
# @Last Modified time: 2017-09-04 18:08:21

import os
from setuptools import setup, find_packages

__version_file_path__ = os.path.join(os.path.dirname(__file__), 'src/NdolLibrary', 'VERSION')
__version__ = open(__version_file_path__, 'r').read().strip()

setup(
	name = 'NdolLibrary',
	version = __version__,
	author = '8dol_tester',
	description = '用于robot framework 测试支持，包括 redis操作',
	packages = find_packages('src'),
	package_dir = {'':'src'},
	package_data = {
		'':['*.py'],
		'':['*']
	},
	install_requires = [
        "redis"
    ]
)
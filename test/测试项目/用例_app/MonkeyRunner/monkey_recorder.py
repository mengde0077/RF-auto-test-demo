# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2016-07-22 11:21:57
# @Last Modified by:   caolinming
# @Last Modified time: 2016-07-22 11:31:03

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

device = mr.waitForConnection()

recorder.start(device)
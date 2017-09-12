# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-07-03 09:18:35
# @Last Modified by:   caolinming
# @Last Modified time: 2017-07-03 09:19:20
# Linux 解决设备掉线问题：软件方案 之 Python 实现
# https://testerhome.com/topics/9219

import usb
import fire


class AdbUSB(object):
    def list(self):
        for d in usb.core.find(find_all=True):
            if d.serial_number:
                print '%s\t%s' %(d.serial_number, d.product)

    def reset(self, serial):
        devices = {}
        for d in usb.core.find(find_all=True):
            if d.serial_number:
                devices[d.serial_number] = d

        ok_serials = []
        for sn in devices.keys():
            if sn.startswith(serial):
                ok_serials.append(sn)

        if len(ok_serials) == 1:
            serial = ok_serials[0]
            d = devices.get(serial)
            try:
                d.reset()
            except usb.core.USBError:
                pass
        elif len(ok_serials) == 0:
            print 'No device serial number is', serial
        else:
            print 'Too many device matched', serial


if __name__ == '__main__':
    fire.Fire(AdbUSB)
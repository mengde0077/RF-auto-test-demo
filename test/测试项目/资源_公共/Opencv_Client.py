#coding:utf-8

import json
import requests



class nodecvSample:

    def __init__(self, host):
        self.host = host

    def getresult(self, files):
        url = self.host + '/opencv/findpairs'
        res = requests.post(url, files=files)
        try:
            jsonres = json.loads(res.text)
            match_res=jsonres["match"]
            if match_res["result"] == True:
                print "Match"
                print 'Screenshot image width: ' + str(match_res["width"])
                print 'Screenshot image height: ' + str(match_res["height"])
                print 'Match rectangle corner1: ('+str(match_res["match_x1"])+','+ str(match_res["match_y1"])+')'
                print 'Match rectangle corner2: ('+str(match_res["match_x2"])+','+ str(match_res["match_y2"])+')'
            else:
                print "Not Match"
        except:
            print "Exception"
        return res.text

if __name__ == '__main__':
    sample = nodecvSample('http://192.168.100.57:9900')
    print sample.getresult({
        'image1': ('macaca_logo.png', open('./image/macaca_logo.png', 'rb')),
        'image2': ('macaca.png', open('./image/macaca.png', 'rb'))
    })

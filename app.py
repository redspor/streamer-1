import requests
from flask import Flask
from flask import request
import re
app = Flask(__name__)

@app.route('/getstream',methods=['GET'])
def getstream():  # put application's code here
    param = request.args.get("param")
    if param == "getts":
        source = request.url
        source = source.replace('https://streamer.herokuapp.com/getstream?param=getts&source=','')
        source = source.replace('http://127.0.0.1:5000/getstream?param=getts&source=','')
        source = source.replace('%2F','/')
        source = source.replace('%3F','?')
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'tr-TR,tr;q=0.9',
            'origin': 'https://lite-1x163215.top',
            'referer': 'https://lite-1x163215.top/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        ts = requests.get(source,headers=headers)
        return ts.content
    if param == "getm3u8":
        videoid = request.args.get("videoid")
        veriler = {"AppId": "3", "AppVer": "1025", "VpcVer": "1.0.11", "Language": "tr", "Token": "", "VideoId": videoid}
        r = requests.post("https://lite-1x163215.top/cinema",json=veriler)
        if "FullscreenAllowed" in r.text:
            veri = r.text
            return veri
            veri = re.findall('"URL":"(.*?)"',veri)
            veri = veri[0].replace("\/", "/")
            veri = veri.replace('edge3','edge10')
            veri = veri.replace('edge4','edge10')
            veri = veri.replace('edge2','edge10')
            if "m3u8" in veri:
                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR, tr;q = 0.9",
                    "origin": "https://lite-1x163215.top",
                    "referer": "https://lite-1x163215.top/",
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
                }
                anadomain = veri.split("mediaplaylist")
                anadomain = anadomain[0]
                '''tsal = requests.get(veri,headers=headers)
                tsal = tsal.text.replace(videoid,anadomain+videoid)'''
                tsal = tsal.replace('https://','https://streamer.herokuapp.com/getstream?param=getts&source=https://')
                return tsal
        else:
            return "Veri yok"

if __name__ == '__main__':
    app.run()


import requests
from flask import Flask
from flask import request
import regex
app = Flask(__name__)

@app.route('/getstream',methods=['GET'])
def getstream():  # put application's code here
    param = request.args.get("param")
    if param == "getts":
        source = request.url
        source = source.replace('https://streamer-rxlz.onrender.com/getstream?param=getts&source=','')
        source = source.replace('%2F','/')
        source = source.replace('%3F','?')
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'tr-TR,tr;q=0.9',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
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
                tsal = requests.get(veri,headers=headers)
                tsal = tsal.text.replace(videoid,anadomain+videoid)
                tsal = tsal.replace('https://','https://streamer-rxlz.onrender.com/getstream?param=getts&source=https://')
                return tsal
        else:
            return "Veri yok"

if __name__ == '__main__':
    app.run()


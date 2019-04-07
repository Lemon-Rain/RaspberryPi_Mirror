# -*- coding:utf-8 -*-

import requests
import json
import baiduAI
import play

# api接口
apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'


def fun():
    text = baiduAI.get_text()
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "潮州",
                    "province": "广东",
                    "street": "饶平"
                }
            }
        },
        "userInfo": {
            "apiKey": "40cf626301264cd7a7dbfa5ddaf7007d",
            "userId": "288892"
        }
    }

    data = json.dumps(data)
    result = requests.post(apiUrl, data=data).json()

    print(result['results'][0]['values']['text'])
    baiduAI.get_audio(result['results'][0]['values']['text'])


fun()
play.play()

import requests
import logging
import json

class Message():
    '''
    用于信息推送
    '''
    def __init__(self, url):
        self.url = url

    def send(self, message):
        requests.post(self.url, json={"message": message})

        
class DingDingMessage():
    '''
    钉钉机器人推送
    '''
    def __init__(self, url,keyword):
        self.url = url
        self.keyword = keyword

    def send(self, message):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        message_body={
            "msgtype": "markdown",
            "markdown": {
                "title": str(self.keyword),
                "text": "信息内容\n" + message
            },
            "at": {
                "atMobiles": [],
                "isAtAll": False
            }
        }
        send_data=json.dumps(message_body)
        ret = requests.post(self.url, headers=headers, data=send_data)
        ret_json = ret.json()
        if ret_json['errmsg'] == "ok":
            logging.info("信息推送成功")
            return 0
        else:
            logging.error("信息推送失败")
            return -1
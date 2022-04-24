from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()  # 登录微信


def send_news():
    try:
        my_friend = bot.friends().search(u'j1145390891')[0]  # 好友的微信号，可以在获取好友列表中找
        my_friend.send(u"知道吗，你是最最最最美的女孩纸!")  # 描述自己修改
        t = Timer(1, send_news)  # 设置发送时间间隔
        t.start()
    except:
        my_friend = bot.friends().search('执愛。婷＾＿＾')[0]  # 自己的微信号
        my_friend.send(u"今天消息发送失败了")  # 描述自己修改


if __name__ == "__main__":
    send_news()

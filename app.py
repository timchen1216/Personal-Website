import re, sqlite3
from flask import Flask, render_template, url_for, request
import discord

client = discord.Client()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dcbot')
def dcbot():
    #調用 event 函式庫
    @client.event
    #當機器人完成啟動時
    async def on_ready():
        print('目前登入身份：', client.user)

    @client.event
    #當有訊息時
    async def on_message(message):
        #排除自己的訊息，避免陷入無限循環
        if message.author == client.user:
            return
        #如果包含 ping，機器人回傳 pong
        if message.content == '%港港脆脆叉':
            await message.channel.send('瀧瀧皮皮燒')
        if message.content == '%毛豆皮俠':
            await message.channel.send(file=discord.File('毛豆皮俠.jpg'))
        if message.content == '%嘲諷毛豆皮俠':
            await message.channel.send(file=discord.File('毛豆皮俠.png'))
        if message.content == '%我好愛你':
            await message.channel.send(file=discord.File('我好愛你.jpeg'))
        if message.content == '%嘲諷閃電賴正達':
            await message.channel.send(file=discord.File('閃電賴正達.png'))
        if message.content == '%閃電賴正達':
            await message.channel.send(file=discord.File('閃電賴正達.jpg'))
        if message.content == '%高哥斯拉菲':
            await message.channel.send(file=discord.File('高哥斯拉菲.jpg'))
        if message.content == '%關鍵跑票':
            await message.channel.send(file=discord.File('關鍵跑票.png'))


    client.run('OTk4OTQ5NzAyMzc4NzE3MzA3.GKyEKv.qvuCI8jBzQ4Jd6NBfNVVfHKFw68DKwJMJwckV0') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

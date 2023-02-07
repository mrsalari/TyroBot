<p align="center">
    <br>
    <b>Rubika Bot Self Library for Python</b>
    <br>
</p>

## Rubika

> A fast, beautiful and very powerful library for making your own robots in Rubika

``` python
from TyroBot import Bot, Message

bot = Bot('TOKEN')

for msg in bot.on_message():
    m = Message(msg)
    if m.text() == 'Hello':
        bot.reply(msg, 'Hello from TyroBot Library')
```

**Tyrobot is** is an easy, fast and unofficial [rubika](https://rubika.ir) self bot library. 
It enables you to easily interact with the main Telegram API through a user account (custom client) using Python.

### Key Features

- **Ready**: Install rubika with pip and start building your applications right away.
- **Easy**: Makes the rubika API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by aiohttp instead of requests.
- **Powerful**: Full access to Rubika's API to execute any official client action and more.

### Installing

``` bash
pip3 install TyroBot
```

This is not an official rubika product. It is not affiliated with nor endorsed by rubika Inc.

© 2022 Mohammad Saeed Salari
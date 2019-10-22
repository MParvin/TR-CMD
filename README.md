# TSMB
Telegram Server Manager Bot - Safe &amp; Easy run command in your RaspberryPi, PC or server from every where.

# How to install and use:
 1. To begin, you'll need an Access Token. If you already read and followed [Introduction to the API](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API), you can use the one you generated then. If not: To generate an Access Token, you have to talk to @BotFather and follow a few simple steps ([described here](https://core.telegram.org/bots#6-botfather)). You should really read the introduction first, though.
 Source: [Your first bot from python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
 
 2 . First install some dependencies:
 ```bash
  sudo pip install -r requirements.txt
  ```
  Best way is use Virtualenv:
  ```bash
  virtualenv -p python3 .env
  source .env/bin/activate
  pip install requirements.txt
  ```
  Install these package for using htop command:
  #### In debian base:
  ```bash
  apt-get install htop aha
  ```
  #### In RHEL base:
  ```bash
  yum install htop
  git clone https://github.com/theZiz/aha.git
  cd aha
  make
  make install
  ```
 
 3. After create your bot and get your Token from botFather, send some text(more than two message) to your bot and use this command to find your chat_id:
  ```bash
  curl -X POST https://api.telegram.org/bot[YOUR-TOKEN]/getUpdates
  ```
  example:
  ```bash
  curl -X POST https://api.telegram.org/bot193025875:AAHZ3hIanIau-Hg04B-mZREFBjLl6GvM9fk/getUpdates
  ```
  Output:
  ```
  {"ok":true,"result":[{"update_id":124681718,
"message":{"message_id":2888,"from":{"id":131728488,"is_bot":false,"first_name":"Mohammad","last_name":"Parvin","username":"mmparvin","language_code":"en-US"},"chat":{"id":131728488,"first_name":"Mohammad","last_name":"Parvin","username":"mmparvin","type":"private"},"date":1523988641,"text":"HHHHHHHHHHH"}}]}
  ```
Put your chat_id and Token(in step1) in config.
 3. Make executable tsmb.py file:
 ```bash
 chmod +x tsmb.py
 ```
 4. Run file:
 ```bash
 ./tsmb.py
 ```
## Sample of htop output:
To get a snapshot of htop, send `/htop` command to bot, output will be like this:

![htop output](https://github.com/MParvin/TSMB/blob/master/htop_output.png?raw=true)
 
## Updates:
 * For more security all response will be sent to the Admin.

## Todo:
* Change admin check structure
* Add debug section, for getting more report
* Use error function in all command functions
* Find best way for detecting interactive commands like htop
* Add one function for all interactive commands

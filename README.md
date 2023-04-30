# Telegram Server Manager Bot

The Telegram Server Manager Bot is a tool that allows you to remotely manage your Raspberry Pi, PC, or server using Telegram. With this bot, you can run commands from anywhere using your smartphone or computer, without needing to log in to your server directly. This can be especially useful if you want to check on your server's status, restart a service, or troubleshoot an issue while you're away from your desk.

## Prerequisites

To use the Telegram Server Manager Bot, you will need the following:

* A Telegram account.
* A Telegram bot token. You can generate this by talking to @BotFather on Telegram.
* Python 3.x installed on your RaspberryPi, PC, or server.


## Installation

1. Clone this repository to your RaspberryPi, PC, or server.

2. Install the required dependencies by running `pip install -r requirements.txt` in the terminal.

3. Rename config.example to config and replace YOUR_TOKEN with your Telegram bot token, YOUR_CHAT_ID with your Telegram chat ID, and ADMIN_CID with the chat ID of the admin who is authorized to execute commands.

4. Make the bot.py file executable by running chmod +x bot.py in the terminal.

5. Run the bot by running ./bot.py in the terminal.


## Usage

To use the Telegram Server Manager Bot, simply open Telegram and start a chat with your bot. Only the admin can execute commands, so make sure to add the admin chat ID to the configuration file. You can then run any of the built-in commands or enter any Linux command that you want to run on your RaspberryPi, PC, or server.

It also supports the following commands:

```bash
  /ping8: Pings 8.8.8.8 and returns the results.

  /top: Runs the top command and returns the results.

  /htop: Runs the htop command and returns the results.

  /help - Shows help and usage information.
```

** You can also run any Linux command by simply entering it in the Telegram chat with the bot.

## Contributions

Contributions to this project are welcome! If you have ideas for new features or improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
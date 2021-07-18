#!/bin/bash

## Set default commands
pipCommand="pip"
pythonCommand="python"
useBale=0

## Display help for commands
showHelp() {
    echo -e "Autoinstall usage: $0 [option..]\n
   	-b, --bale		For install bale api instead of Telegram API \n
	  -h, --help		This help message\n
	  -d, --debug		Enable bash debug\n
	  -i, --interactive	Install requirements for interactive commands\n
	  -u, --useful		Install useful commands\n
	  -3, --python3		Use python3 instead of Python2\n
    "
    exit 0
}

## Use virtualenv
useVenv() {
    ## Create virtual environment
    virtualenv -p $pythonCommand venv
    ## Activate virtual environment
    source venv/bin/activate
}


useBaleAPI() {
    ## Change telegram API URL to Bale API URL
    find ./ -name bot.py -exec sed -i 's/api\.telegram\.org/tapi.bale.ai/mg' {} \;
}


## to use interactive commands like htop we need these packages
installAha() {
    [ -f "/etc/debian_version" ] && apt-get update && apt-get install -y aha && return 0
    (git clone https://github.com/theZiz/aha.git && cd aha && make && make install return 0) || ( echo "cannot install aha, please use -d to debug \nPlease submit an issue here:\n https://github.com/MParvin/TSMB/issues/new" && exit 1)

}

## Install useful commands
installUsefulCMD() {
    echo "Installing htop, please wait a moment..."
    yum install -y htop &> /dev/null ||  apt install -y htop &> /dev/null
}

configureBot(){
    echo -e "To configure your bot, you must have a Telegram or Bale token\n
		How to create Telegram bot: https://core.telegram.org/bots#3-how-do-i-create-a-bot\n
    How to create Bale bot: https://devbale.ir/quick-start\n"
    read -p "Enter your bot token here:"

    telegramToken=$REPLY

    echo -e "Get chat_id and enter here:\n
		To get chat_id do:
			- In telegram:\n start a chat with @id_chatbot
			- In Bale:\n start a chat with chatid_bot
    "
    chatId=$REPLY
}

while :
do
    case "$1" in
        -b | --bale)
            which virtualenv &> /dev/null || (echo "Cannot use Bale without virtualenv, please run \"pip install virtualenv\" before run this script with -b option" && exit 1)
            useBale = "True"
            break
            ;;
        -h | --help)
            showHelp
            exit 0
            ;;
        -d | --debug)
            set -x
            break
            ;;
        -i | --interactive)
            installAha
            break
            ;;
        -u | --useful)
            installUsefulCMD
            break
            ;;
        -3 | --python3)
            pythonCommand="python3"
            pipCommand="pip3"
            break
            ;;
        *)
            break
            ;;

    esac
done


## Check is python installed
which $pythonCommand &> /dev/null || (echo "Please install python, and run this script again" && exit 1)
## Check is pip installed
which $pipCommand &> /dev/null || (echo -e "Please install pip, and run this script again\n
				In Debian base system for python2.* use apt-get install python-pip\n
for python3.* use apt-get install python3-pip" && exit 1)

## Install virtualenv if is not installed
(which virtualenv &> /dev/null && useVenv) || read -p "Do you want to install virtualenv(y/n)? " -n 1 -r
## User accepted
[[ ! $REPLY =~ ^[yY]$ ]] && $pipCommand install virtualenv --user && useVenv

## Install requirements
([ -f requirements.txt ] && $pipCommand install -r requirements.txt) || echo "Could not find requirements.txt, please clone complete this repository from here:\nhttps://github.com/MParvin/TSMB/, \nthen run Autoinstall.sh"
if [ "$useBale" -eq 1 ]
then
    useBaleAPI
fi


read -p "Do you want to configure your bot now(y/n)?"
if [ $REPLY =~ ^[yY] ]
then
    configureBot
else
    echo -e "To use this bot, first change variables in \".env\" file\n
		then executable bot script \"chmod +x bot.py \"
    and run it: \"./bot.py \""
fi

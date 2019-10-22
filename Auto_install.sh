#!/bin/bash

## Set default commands
pipCommand="pip"
pythonCommand="python"

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
virtualenv -p $pythonCommand venv 
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

## Install htop
installHtop() {
	yum install -y htop &> /dev/null ||  apt install -y htop &> /dev/null
}



while :
  do
     case "$1" in
	     -b | --bale)
		     which virtualenv &> /dev/null || (echo "Cannot use Bale without virtualenv" && exit 1)
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
		     installHtop
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
which virtualenv &> /dev/null || read -p "Do you want to install virtualenv(y/n)? " -n 1 -r
([[ ! $REPLY =~ ^[yY]$ ]] && $pipCommand install virtualenv  && useVenv) || (echo "")

([ -f requirements.txt ] && pip install -r requirements) || echo "Cannot find requirements.txt, please clone complete this repository from here:\nhttps://github.com/MParvin/TSMB/, \nthen run Autoinstall.sh"
if [ "$useBale" -eq "True"]
then
	useBaleAPI
fi


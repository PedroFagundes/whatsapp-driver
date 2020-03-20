# Instruções para configurar um novo servidor para o WebWhatsDriver #

## Pacotes ##
### virtualenv ###
`sudo apt update`
`sudo apt install python3-pip`
`pip3 install virtualenv`

### firefox ###
`sudo apt-get install firefox xvfb`

`sudo apt-get purge firefox`

`wget https://ftp.mozilla.org/pub/firefox/releases/61.0.2/linux-x86_64/pt-BR/firefox-61.0.2.tar.bz2`

`tar -xjf firefox-*.tar.bz2`

`sudo mv firefox /opt/`

`rm firefox-*.tar.bz2`

tar xvzf geckodriver-v0.24.0-linux64.tar.gz

*OPTIONAL* - `sudo mv /usr/bin/firefox /usr/bin/firefox_old`

`sudo ln -s /opt/firefox/firefox /usr/bin/firefox`

## Criando ambiente virtual ##
`mkdir /envs`
`virtualenv /envs/webwhatsdriver`

## Clonando projeto e instalando dependencias ##
`mkdir /webapps && cd /webapps`
`git clone https://github.com/PedroFagundes/azbot-webwhatsdriver.git`
`cd azbot-webwhatsdriver && source /envs/webwhatsdriver/bin/activate`
`pip install -r requirements.txt`


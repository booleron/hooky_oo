# twitter-random-haiku-bot
### About
Bot that parse random haiku and send it to Twitter every 3 hours
### Deployment
* Create a new virtual environment in terminal:
```shell
virtualenv --python=python3.5 venv
```
* Make your environment active and install requirements:
```shell
source venv/bin/activate
pip install -r requirements.txt
```
* Fill environment variables in start.sh with your data from https://apps.twitter.com 
* Make start.sh executable and run it:
```
chmod +x start.sh
./start.sh
```

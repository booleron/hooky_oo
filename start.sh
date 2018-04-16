#!/bin/bash
export LOG_NAME='haiku_random_bot'
export CONSUMER_KEY=''
export CONSUMER_SECRET=''
export ACCESS_TOKEN=''
export ACCESS_TOKEN_SECRET=''

. venv/bin/activate && python bot.py && sleep 30m
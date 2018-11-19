#!/usr/bin/env bash

cd /usr/local/topevent
exec env/bin/gunicorn events.wsgi -c deploy/gunicorn.conf.py

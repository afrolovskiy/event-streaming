#!/usr/bin/env bash

cd /usr/local/topevent
exec env/bin/gunicorn topevent.wsgi -c deploy/gunicorn.conf.py

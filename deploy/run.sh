#!/usr/bin/env bash

cd /usr/local/event-streaming
exec env/bin/gunicorn topevent.wsgi -c deploy/gunicorn.conf.py

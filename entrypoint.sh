#!/bin/bash
cd coursework
gunicorn coursework.wsgi:application --bind 0.0.0.0:$PORT
#!/bin/bash
service nginx restart
gunicorn -b localhost:8085 -w 2 arteliasite.wsgi
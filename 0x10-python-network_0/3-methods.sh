#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sX OPTIONS "$1" | grep -o '<h1>.*</h1>'

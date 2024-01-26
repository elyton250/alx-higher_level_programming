#!/bin/bash
#this is the json post
curl -s -X POST -H "Content-type: application/json" -d "$(cat "$2")" "$1"

#!/bin/bash
#this sends a requesst and gets the body from the passed Ip
curl -s "$1" | wc -c

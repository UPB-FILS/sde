#!/bin/sh
read text
echo "Content-type: text/plain; charset=utf-8"
echo "Server: Awesome server"
echo "Age: 3502"
echo ""
echo "Message $text received"
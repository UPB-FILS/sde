#!/bin/sh
read text
echo "Content-type: text/plain; charset=utf-8"
echo "Age: 3500"
echo ""
echo "Message $text received from $usr"
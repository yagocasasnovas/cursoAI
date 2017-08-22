#!/bin/bash

python GameManager.py &
PID1=$!

wait $PID1
echo 'hola'








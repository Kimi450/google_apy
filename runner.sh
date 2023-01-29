#!/bin/bash

mkdir logs 2>/dev/null

FILE=$1; unbuffer ./$FILE | tee logs/log_$(echo $FILE | cut -d "." -f 1)_$(date +"%Y%m%d_%H%M%S")

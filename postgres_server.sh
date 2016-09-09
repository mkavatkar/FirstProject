#!/bin/bash
if [[ $1 = "start" ]]; then
    pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
elif [[ $1 = "stop" ]]; then
    printf "stopping server\n"
    pg_ctl -D /usr/local/var/postgres stop -s -m fast
else
    printf "Wrong arguments passed, Following are the options: \n"
    printf "1. start\n"
    printf "2. stop\n"
fi

#!/bin/bash

for ((i = 0; i < 1050; i++)); do
    x=$(mysql -uisucon -pisucon isubata -Ns -e "select name from image where id = ${i};")
    echo "name: $x"
    if [[ ${#x} -eq 0 ]]; then
        echo "no name"
        continue
    fi
    mysql -uisucon -pisucon isubata -Ns -e "select data INTO DUMPFILE '/var/lib/mysql-files/${x}' from image where name = '${x}' limit 1;"
done

#!/bin/bash
HOSTNAME="localhost"
PORT="3306"
USERNAME="root"
PASSWORD="admin"

DB_NAME="jinbag"
TABLE_NAME="user_profile"

select_sql="select id from ${TABLE_NAME}"
mysql -h${HOSTNAME}  -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DB_NAME} -e "${select_sql}" >> res

cat res | while read line;do
echo $line
done
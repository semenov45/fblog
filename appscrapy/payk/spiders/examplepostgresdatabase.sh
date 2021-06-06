#!/bin/bash
cd /fblog/appscrapy/payk/spiders/



scrapy crawl zhabrcom


wait



password='Password'
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt = replace(descrypt, '\r\n',' ')"
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt = replace(descrypt, '[',' ')"
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt = replace(descrypt, ']',' ')"
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt_text = replace(descrypt_text, '\r\n',' ')"
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt_text = replace(descrypt_text, '[',' ')"
PGPASSWORD=$(echo $password) psql -h host -U user -d dbname -t -c "update zhabrcom set descrypt_text = replace(descrypt_text, ']',' ')"




echo 'update success return 0 '
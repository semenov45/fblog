#!/bin/bash
cd /app/appscrapy/payk/spiders/

source "absolute/path/venv/bin/activate"

scrapy crawl zhabrcom


wait




sqlite3 habr.db 'update zhabrcom set descrypt = replace(descrypt, "\r\n", "")'
sqlite3 habr.db 'update zhabrcom set descrypt = replace(descrypt, "[", "")'
sqlite3 habr.db 'update zhabrcom set descrypt = replace(descrypt, "]", "")'
sqlite3 habr.db 'update zhabrcom set descrypt_text = replace(descrypt_text, "[", "")'
sqlite3 habr.db 'update zhabrcom set descrypt_text = replace(descrypt_text, "]", "")'
sqlite3 habr.db 'update zhabrcom set descrypt_text = replace(descrypt_text, "\r\n", "")'


echo "update success return 0 "
<h1 align="center">Fblog</h1>
<p>cd fblog/appscrapy/payk/spiders/</p>
<p>Run</p>
python3 database.py
<p></p>
crontab -e  0 12 * * * /fblog/appscrapy/payk/spiders/examplepostgresdatabase.sh
<p>Or</p>
crontab -e  0 12 * * * /fblog/appscrapy/payk/spiders/examplesqlitedatabase.sh
<p>Run</p>
python3 wsgi.py
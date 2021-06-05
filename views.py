# -*- coding: utf-8 -*-

from flask import render_template,request,send_from_directory, current_app, make_response, url_for
from app import app,db
from database import Zhabrcom
from forms import SearchForm
import random
from datetime import datetime,timedelta
@app.route('/', methods=['GET','POST'], defaults={"page": 1}) 
@app.route('/<int:page>', methods=['GET','POST'])
def index(page):
    q = request.form.get('q')
    page = page
    per_page = 20
    
    invert = Zhabrcom.query.filter_by(id = random.randrange(200, 590, 2)).first()
    invertcenter = Zhabrcom.query.filter_by(id = random.randrange(600, 900, 2)).first()
    invertring = Zhabrcom.query.filter_by(id = random.randrange(0, 190, 2)).first()
    print("QQQQQQQQQQQQQQQ",page)
    if q:
        posts = Zhabrcom.query.filter(Zhabrcom.title.like('%'+ q+'%')).paginate(page,per_page)
        print("POST",posts)
        return render_template("index.html",q=q,posts=posts,invert=invert,invertcenter=invertcenter,invertring=invertring)

       
        #return render_template('index.html',posts=posts,invert=invert,invertcenter=invertcenter,invertring=invertring)
        #return render_template('search.html', form=form)
   
    else:
        posts = Zhabrcom.query.order_by(Zhabrcom.id).paginate(page,per_page)
        return render_template("index.html",posts=posts,invert=invert,invertcenter=invertcenter,invertring=invertring)

@app.route('/<slug>')
def detail(slug):
    post = Zhabrcom.query.filter_by(title = slug).first()
    invert = Zhabrcom.query.filter_by(id = random.randrange(200, 590, 2)).first()
    invertcenter = Zhabrcom.query.filter_by(id = random.randrange(600, 900, 2)).first()
    invertring = Zhabrcom.query.filter_by(id = random.randrange(0, 190, 2)).first()
    return render_template("single.html",post=post,invert=invert,invertcenter=invertcenter,invertring=invertring)


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



###################sitemap dinamic

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = []

    # get static routes
    # use arbitary 10 days ago as last modified date
    lastmod = datetime.now() - timedelta(days=10)
    lastmod = lastmod.strftime('%Y-%m-%d')
    for rule in current_app.url_map.iter_rules():
        # omit auth and admin routes and if route has parameters. Only include if route has GET method
        if 'GET' in rule.methods and len(rule.arguments) == 0 \
                and not rule.rule.startswith('/admin') \
                and not rule.rule.startswith('/auth') \
                and not rule.rule.startswith('/test'):
            pages.append(['https://fblog.pp.ua' + rule.rule, lastmod])

    # get dynamic routes
    posts = Zhabrcom.query.order_by(Zhabrcom.id).all()
    for post in posts:
        url = 'https://fblog.pp.ua' + url_for('.detail', slug=post.title)
        last_updated = datetime.now().strftime('%Y-%m-%d')
        pages.append([url, last_updated])


    sitemap_template = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_template)
    response.headers['Content-Type'] = 'application/xml'
    return response

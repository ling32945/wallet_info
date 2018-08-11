#!/usr/bin/env python
# coding=utf-8

import os
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from app.models import *
try:
    import simplejson as json
except:
    import json

    module_file = os.path.basename(__file__)
    module_name = module_file[0:module_file.find('.')]
    module = Blueprint(module_name, __name__)

def category_as_dict(category):
    return {'id': category.id, 'category': category.category, 'description': category.description}

@module.route('/')
def category_index():
    categories = Category.query.all()
    category_list = []
    for category in categories:
        category_list.append(category_as_dict(category))
    return render_template('category/index.html', data=category_list)
    #return jsonify(code=0, message='Category List', data=category_list)

@module.route('/add', methods=['GET', 'POST'])
def category_add():
    if request.method == 'GET':
        return render_template('category/add.html', data="")
    elif request.method == 'POST':
        category_type = request.form['category_type']
        category_des = request.form['category_des']
        category = Category(category_type, category_des)
        db.session.add(category)
        db.session.commit()
        #return jsonify(code=0, message='Category Created', data=category_as_dict(category))
        return redirect(url_for('category.detail', token=category.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    category = Category.query.filter(Category.id == token).first();
    print "Jae.Start"
    print request.script_root
    print request.path
    print "Jae.End"
    return render_template('category/detail.html', data=category_as_dict(category))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    category = Category.query.filter(Category.id == token).first();
    if request.method == 'GET':
        return render_template('category/update.html', data=category_as_dict(category))
    elif request.method == 'POST':
        category_type = request.form['category_type']
        category.category = category_type
        category_des = request.form['category_des']
        category.description = category_des
        db.session.commit()
        return redirect(url_for('category.detail', token=category.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    category = Category.query.filter(Category.id == token).first();
    if category is not None:
        db.session.delete(category)
        db.session.commit()
    return redirect(url_for('category.category_index'))

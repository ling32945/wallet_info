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

def factory_as_dict(factory):
    return {'id': factory.id, 'no': factory.no, 'name': factory.name , 'description': factory.description}

@module.route('/')
def index():
    factorys = Factory.query.all()
    factory_list = []
    for factory in factorys:
        factory_list.append(factory_as_dict(factory))
    return render_template('factory/index.html', data=factory_list)

@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('factory/add.html', data="")
    elif request.method == 'POST':
        no = request.form['no']
        name = request.form['name']
        description = request.form['factory_des']
        factory = Factory(no, name, description)
        db.session.add(factory)
        db.session.commit()
        return redirect(url_for('factory.detail', token=factory.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    factory = Factory.query.filter(Factory.id == token).first();
    return render_template('factory/detail.html', data=factory_as_dict(factory))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    factory = Factory.query.filter(Factory.id == token).first();
    if request.method == 'GET':
        return render_template('factory/update.html', data=factory_as_dict(factory))
    elif request.method == 'POST':
        no = request.form['no']
        factory.no = no
        name = request.form['name']
        factory.name = name
        description = request.form['factory_des']
        factory.description = description
        db.session.commit()
        return redirect(url_for('factory.detail', token=factory.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    factory = Factory.query.filter(Factory.id == token).first();
    if factory is not None:
        db.session.delete(factory)
        db.session.commit()
    return redirect(url_for('factory.index'))

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

def gender_as_dict(gender):
    return {'id': gender.id, 'sex': gender.sex , 'description': gender.description}

@module.route('/')
def index():
    genders = Gender.query.all()
    gender_list = []
    for gender in genders:
        gender_list.append(gender_as_dict(gender))
    return render_template('gender/index.html', data=gender_list)

@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('gender/add.html', data="")
    elif request.method == 'POST':
        sex = request.form['sex']
        description = request.form['gender_des']
        gender = Gender(sex, description)
        db.session.add(gender)
        db.session.commit()
        return redirect(url_for('gender.detail', token=gender.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    gender = Gender.query.filter(Gender.id == token).first();
    return render_template('gender/detail.html', data=gender_as_dict(gender))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    gender = Gender.query.filter(Gender.id == token).first();
    if request.method == 'GET':
        return render_template('gender/update.html', data=gender_as_dict(gender))
    elif request.method == 'POST':
        sex = request.form['sex']
        gender.sex = sex
        description = request.form['gender_des']
        gender.description = description
        db.session.commit()
        return redirect(url_for('gender.detail', token=gender.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    gender = Gender.query.filter(Gender.id == token).first();
    if gender is not None:
        db.session.delete(gender)
        db.session.commit()
    return redirect(url_for('gender.index'))

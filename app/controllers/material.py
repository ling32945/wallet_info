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

def material_as_dict(material):
    return {'id': material.id, 'material': material.material , 'description': material.description}

@module.route('/')
def index():
    materials = Material.query.all()
    material_list = []
    for material in materials:
        material_list.append(material_as_dict(material))
    return render_template('material/index.html', data=material_list)

@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('material/add.html', data="")
    elif request.method == 'POST':
        material_name = request.form['material']
        description = request.form['material_des']
        material = Material(material_name, description)
        db.session.add(material)
        db.session.commit()
        return redirect(url_for('material.detail', token=material.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    material = Material.query.filter(Material.id == token).first();
    return render_template('material/detail.html', data=material_as_dict(material))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    material = Material.query.filter(Material.id == token).first();
    if request.method == 'GET':
        return render_template('material/update.html', data=material_as_dict(material))
    elif request.method == 'POST':
        material_name = request.form['material']
        material.material = material_name
        description = request.form['material_des']
        material.description = description
        db.session.commit()
        return redirect(url_for('material.detail', token=material.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    material = Material.query.filter(Material.id == token).first();
    if material is not None:
        db.session.delete(material)
        db.session.commit()
    return redirect(url_for('material.index'))

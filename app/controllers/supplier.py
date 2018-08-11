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

def supplier_as_dict(supplier):
    return {'id': supplier.id, 'supplier': supplier.supplier , 'description': supplier.description}

@module.route('/')
def index():
    suppliers = Supplier.query.all()
    supplier_list = []
    for supplier in suppliers:
        supplier_list.append(supplier_as_dict(supplier))
    return render_template('supplier/index.html', data=supplier_list)

@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('supplier/add.html', data="")
    elif request.method == 'POST':
        supplier_name = request.form['supplier']
        description = request.form['supplier_des']
        supplier = Supplier(supplier_name, description)
        db.session.add(supplier)
        db.session.commit()
        return redirect(url_for('supplier.detail', token=supplier.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    supplier = Supplier.query.filter(Supplier.id == token).first();
    return render_template('supplier/detail.html', data=supplier_as_dict(supplier))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    supplier = Supplier.query.filter(Supplier.id == token).first();
    if request.method == 'GET':
        return render_template('supplier/update.html', data=supplier_as_dict(supplier))
    elif request.method == 'POST':
        supplier_name = request.form['supplier']
        supplier.supplier = supplier_name
        description = request.form['supplier_des']
        supplier.description = description
        db.session.commit()
        return redirect(url_for('supplier.detail', token=supplier.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    supplier = Supplier.query.filter(Supplier.id == token).first();
    if supplier is not None:
        db.session.delete(supplier)
        db.session.commit()
    return redirect(url_for('supplier.index'))

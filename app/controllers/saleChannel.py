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

def channel_as_dict(channel):
    return {'id': channel.id, 'name': channel.channel_name, 'description': channel.description}

@module.route('/')
def index():
    channels = SaleChannel.query.all()
    channel_list = []
    for channel in channels:
        channel_list.append(channel_as_dict(channel))
    return render_template('saleChannel/index.html', data=channel_list)

@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('saleChannel/add.html', data="")
    elif request.method == 'POST':
        name = request.form['channel_name']
        description = request.form['channel_des']
        channel = SaleChannel(name, description)
        db.session.add(channel)
        db.session.commit()
        return redirect(url_for('saleChannel.detail', token=channel.id))
    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    channel = SaleChannel.query.filter(SaleChannel.id == token).first();
    return render_template('saleChannel/detail.html', data=channel_as_dict(channel))

@module.route('/update/<token>', methods=['GET', 'POST'])
def update(token):
    channel = SaleChannel.query.filter(SaleChannel.id == token).first();
    if request.method == 'GET':
        return render_template('saleChannel/update.html', data=channel_as_dict(channel))
    elif request.method == 'POST':
        name = request.form['channel_name']
        channel.name = name
        description = request.form['channel_des']
        channel.description = description
        db.session.commit()
        return redirect(url_for('saleChannel.detail', token=channel.id))
    else:
        return('OK')

@module.route('/delete/<token>')
def delete(token):
    channel = SaleChannel.query.filter(SaleChannel.id == token).first();
    if channel is not None:
        db.session.delete(channel)
        db.session.commit()
    return redirect(url_for('saleChannel.index'))

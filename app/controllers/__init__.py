#!/usr/bin/env python
# coding=utf-8

import os
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
try:
    import simplejson as json
except:
    import json

module_file = os.path.basename(__file__)
module_name = module_file[0:module_file.find('.')]
module = Blueprint(module_name, __name__)


@module.route('/')
def index():
    return redirect(url_for('product.index'))


#@module.route('hello')
#def hello():
#    return jsonify(code=0, message='This is /hello')

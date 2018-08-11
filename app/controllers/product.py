#!/usr/bin/env python
# coding=utf-8

import os
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, current_app
from sqlalchemy.orm import aliased
from app import db
from app.models import *
import random

try:
    import simplejson as json
except:
    import json

module_file = os.path.basename(__file__)
module_name = module_file[0:module_file.find('.')]
module = Blueprint(module_name, __name__)


def product_as_dict(product):
    result = {}

    result["id"] = product.id
    result["image"] = product.image
    result["style_no"] = product.style_no
    result["item_no"] = product.item_no
    result["barcode"] = product.barcode

    if product.brand is not None and product.brand:
        result["brand"] = product.brand
    else:
        result["brand"] = ""

    if product.product_abbreviation is not None and product.product_abbreviation:
        result["product_abbreviation"] = product.product_abbreviation
    else:
        result["product_abbreviation"] = ""

    result["category_id"] = product.category_id
    result["gender_id"] = product.gender_id
    result["color"] = product.color
    result["main_material_id"] = product.main_material_id

    if product.vice_material_id is not None and product.vice_material_id:
        result["vice_material_id"] = product.vice_material_id
    else:
        result["vice_material_id"] = ""

    if product.interior_material_id is not None and product.interior_material_id:
        result["interior_material_id"] = product.interior_material_id
    else:
        result["interior_material_id"] = ""

    if product.exterior_structure is not None and product.exterior_structure:
        result["exterior_structure"] = product.exterior_structure
    else:
        result["exterior_structure"] = ""

    if product.interior_structure is not None and product.interior_structure:
        result["interior_structure"] = product.interior_structure
    else:
        result["interior_structure"] = ""

    if product.open_mode is not None and product.open_mode:
        result["open_mode"] = product.open_mode
    else:
        result["open_mode"] = ""

    if product.length is not None and product.length:
        result["length"] = product.length
    else:
        result["length"] = ""

    if product.width is not None and product.width:
        result["width"] = product.width
    else:
        result["width"] = ""

    if product.height is not None and product.height:
        result["height"] = product.height
    else:
        result["height"] = ""

    if product.weight is not None and product.weight:
        result["weight"] = product.weight
    else:
        result["weight"] = ""

    if product.supplier_id is not None and product.supplier_id:
        result["supplier_id"] = product.supplier_id
    else:
        result["supplier_id"] = ""

    if product.factory_price is not None and product.factory_price:
        result["factory_price"] = product.factory_price
    else:
        result["factory_price"] = ""

    if product.cost_price is not None and product.cost_price:
        result["cost_price"] = product.cost_price
    else:
        result["cost_price"] = ""

    if product.tag_price is not None and product.tag_price:
        result["tag_price"] = product.tag_price
    else:
        result["tag_price"] = ""

    if product.retail_price is not None and product.retail_price:
        result["retail_price"] = product.retail_price
    else:
        result["retail_price"] = ""

    if product.original_item_no is not None and product.original_item_no:
        result["original_item_no"] = product.original_item_no
    else:
        result["original_item_no"] = ""

    if product.feature is not None and product.feature:
        result["feature"] = product.feature
    else:
        result["feature"] = ""

    if product.comment is not None and product.comment:
        result["comment"] = product.comment
    else:
        result["comment"] = ""

    return result


@module.route('/')
def index():
    main_material = aliased(Material)
    vice_material = aliased(Material)
    interior_material = aliased(Material)
    query_result = db.session.query(
            Product,
            Category.category,
            Gender.sex,
            main_material.material,
            vice_material.material,
            interior_material.material,
            Supplier.supplier
        ).outerjoin(Category, Product.category_id == Category.id
        ).outerjoin(Gender, Product.gender_id == Gender.id
        ).outerjoin(main_material, Product.main_material_id == main_material.id
        ).outerjoin(vice_material, Product.vice_material_id == vice_material.id
        ).outerjoin(interior_material, Product.interior_material_id == interior_material.id
        ).outerjoin(Supplier, Product.supplier_id == Supplier.id
        ).all()

    print query_result

    result = []
    for obj in query_result:
        product = obj[0]

        data = product_as_dict(product)
        data["category"] = obj[1]
        data["gender"] = obj[2]
        data["main_material"] =  obj[3]
        data["vice_material"] =  obj[4]
        data["interior_material"] = obj[5]
        data["supplier"] = obj[6]

        result.append(data)

    print result
    return render_template('product/index.html', data = result)


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config.get('CUSTOM_ALLOWED_EXTENSIONS')


@module.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        result = {}

        categories = Category.query.all()
        category_list = []
        for category in categories:
            category_list.append({'id':category.id, 'name':category.category})
        result["category"] = category_list

        genders = Gender.query.all()
        gender_list = []
        for gender in genders:
            gender_list.append({'id':gender.id, 'name':gender.sex})
        result["gender"] = gender_list

        materials = Material.query.all()
        material_list = []
        for material in materials:
            material_list.append({'id':material.id, 'name':material.material})
        result["material"] = material_list

        suppliers = Supplier.query.all()
        supplier_list = []
        for supplier in suppliers:
            supplier_list.append({'id':supplier.id, 'name':supplier.supplier})
        result["supplier"] = supplier_list

        wallet_image = "sample_wallet_" + str(random.randint(0,2)) + ".jpg"
        result["image"] = wallet_image


        return render_template('product/add.html', data=result)
    elif request.method == 'POST':
        print "\nAdd Form Data:"
        print request.form
        print request.files
        print current_app.config.get('CUSTOM_ALLOWED_EXTENSIONS')
        print current_app.config.get('CUSTOM_UPLOAD_FOLDER')

        # check if the post prequest has the required fields
        if request.form is None or not request.form:
            current_app.logger.warn('uploaded form fields is empty')
            return redirect(request.url)

        valid_form = True
        error_msg = 'required fields '
        if request.form['style_no'] is None or not request.form['style_no']:
            valid_form = False
            error_msg = error_msg + 'style_no, '
        if request.form['item_no'] is None or not request.form['item_no']:
            valid_form = False
            error_msg = error_msg + 'item_no, '
        if request.form['barcode'] is None or not request.form['barcode']:
            valid_form = False
            error_msg = error_msg + 'barcode, '

        if not valid_form:
            error_msg = error_msg + 'of uploaded from is empty'
            current_app.logger.warn(error_msg)
            return redirect(request.url)


        # check if the post request has the file part
        if 'input-pd' not in request.files:
            current_app.logger.warn('No file of input-pd in uploaded files')
            return redirect(request.url)

        upload_file = request.files['input-pd']
        # if user does not select file, browser also
        # submit a empty part without filename
        if upload_file.filename == '':
            current_app.logger.warn('No selected file in uploaded files')
            return redirect(request.url)

        if upload_file and allowed_file(upload_file.filename):
            filename = request.form['item_no'] + os.path.splitext(upload_file.filename)[-1]
            upload_file.save(os.path.join(current_app.config.get('CUSTOM_UPLOAD_FOLDER'), filename))
            #return redirect(url_for('uploaded_file', filename=filename))

        style_no = request.form['style_no']
        item_no = request.form['item_no']
        barcode = request.form['barcode']
        brand = request.form['brand']
        product_abbreviation = request.form['product_abbreviation']
        category_id = request.form['category']
        gender_id = request.form['gender']
        color = request.form['color']
        main_material_id = request.form['main_material']
        vice_material_id = request.form['vice_material']
        interior_material_id = request.form['interior_material']
        exterior_structure = request.form['exterior_structure']
        interior_structure = request.form['interior_structure']
        open_mode = request.form['open_mode']
        length = request.form['length']
        width = request.form['width']
        height = request.form['height']
        weight = request.form['weight']
        supplier_id = request.form['supplier']
        factory_price = request.form['factory_price']
        cost_price = request.form['cost_price']
        tag_price = request.form['tag_price']
        retail_price = request.form['retail_price']
        original_item_no = request.form['original_item_no']
        image = filename
        #feature =
        #comment =


        product = Product(image, style_no, item_no, barcode,
            category_id, gender_id, color, main_material_id,
            brand, product_abbreviation,
            vice_material_id, interior_material_id,
            exterior_structure, interior_structure, open_mode,
            length, width, height, weight,
            supplier_id, factory_price, cost_price, tag_price, retail_price, original_item_no
            );

        db.session.add(product)
        db.session.commit()
        #return redirect(url_for('factory.detail', token=factory.id))



        return redirect(url_for('product.index'))

    else:
        return("OK")

@module.route('/detail/<token>')
def detail(token):
    main_material = aliased(Material)
    vice_material = aliased(Material)
    interior_material = aliased(Material)
    query_result = db.session.query(
            Product,
            Category.category,
            Gender.sex,
            main_material.material,
            vice_material.material,
            interior_material.material,
            Supplier.supplier
        ).outerjoin(Category, Product.category_id == Category.id
        ).outerjoin(Gender, Product.gender_id == Gender.id
        ).outerjoin(main_material, Product.main_material_id == main_material.id
        ).outerjoin(vice_material, Product.vice_material_id == vice_material.id
        ).outerjoin(interior_material, Product.interior_material_id == interior_material.id
        ).outerjoin(Supplier, Product.supplier_id == Supplier.id
        ).filter(Product.id == token).first()


    product = query_result[0]
    data = product_as_dict(product)

    data["category"] = query_result[1]
    data["gender"] = query_result[2]
    data["main_material"] =  query_result[3]
    data["vice_material"] =  query_result[4]
    data["interior_material"] = query_result[5]
    data["supplier"] = query_result[6]

    if not os.access(os.path.join(current_app.config.get('CUSTOM_UPLOAD_FOLDER'), data["image"]), os.F_OK) or not os.access(os.path.join(current_app.config.get('CUSTOM_UPLOAD_FOLDER'), data["image"]), os.R_OK):
        data["image"] = "sample_not_exist.jpg"
        current_app.logger.warn('Wallet image {} not found'.format(data["image"]))


    return render_template('product/detail.html', data = data)

##@module.route('/update/<token>', methods=['GET', 'POST'])
##def update(token):
##    factory = Factory.query.filter(Factory.id == token).first();
##    if request.method == 'GET':
##        return render_template('factory/update.html', data=factory_as_dict(factory))
##    elif request.method == 'POST':
##        no = request.form['no']
##        factory.no = no
##        name = request.form['name']
##        factory.name = name
##        description = request.form['factory_des']
##        factory.description = description
##        db.session.commit()
##        return redirect(url_for('factory.detail', token=factory.id))
##    else:
##        return('OK')
##
##@module.route('/delete/<token>')
##def delete(token):
##    factory = Factory.query.filter(Factory.id == token).first();
##    if factory is not None:
##        db.session.delete(factory)
##        db.session.commit()
##    return redirect(url_for('factory.index'))

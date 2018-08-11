#!/usr/bin/env python
# coding=utf-8

from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    style_no = db.Column(db.String(10), nullable=False)
    item_no = db.Column(db.String(10), unique=True, index=True, nullable=False)
    barcode = db.Column(db.String(32), unique=True, index=True, nullable=False)
    brand = db.Column(db.String(45), nullable=True)
    product_abbreviation = db.Column(db.String(45), nullable=True)
    category_id = db.Column(db.Integer, nullable=False)
    gender_id = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(8), nullable=False)
    main_material_id = db.Column(db.Integer, nullable=False)
    vice_material_id = db.Column(db.Integer, nullable=True)
    interior_material_id = db.Column(db.Integer, nullable=True)
    exterior_structure = db.Column(db.String(45), nullable=True)
    interior_structure = db.Column(db.String(45), nullable=True)
    open_mode = db.Column(db.String(12), nullable=True)
    length = db.Column(db.Numeric(4,2), nullable=True)
    width = db.Column(db.Numeric(4,2), nullable=True)
    height = db.Column(db.Numeric(4,2), nullable=True)
    weight = db.Column(db.Numeric(6,2), nullable=True)
    supplier_id = db.Column(db.Integer, nullable=True)
    factory_price = db.Column(db.Numeric(8,2), nullable=True)
    cost_price = db.Column(db.Numeric(8,2), nullable=True)
    tag_price = db.Column(db.Numeric(8,2), nullable=True)
    retail_price = db.Column(db.Numeric(8,2), nullable=True)
    original_item_no = db.Column(db.String(10), nullable=True)
    image = db.Column(db.String(45), nullable=True)
    feature = db.Column(db.String(45), nullable=True)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, image, style_no, item_no, barcode,
            category_id, gender_id, color, main_material_id,
            brand = None, product_abbreviation = None,
            vice_material_id = None, interior_material_id = None,
            exterior_structure = None, interior_structure = None, open_mode = None, length = None, width = None, height = None, weight = None,
            supplier_id = None, factory_price = None, cost_price = None, tag_price = None, retail_price = None, original_item_no = None,
            feature = None, comment = None):

        self.image  = image
        self.style_no = style_no
        self.item_no = item_no
        self.barcode = barcode

        if brand is not None and brand:
            self.brand = brand
        else:
            self.brand = None

        if product_abbreviation is not None and product_abbreviation:
            self.product_abbreviation = product_abbreviation
        else:
            self.product_abbreviation = None

        self.category_id = category_id
        self.gender_id = gender_id
        self.color = color
        self.main_material_id = main_material_id

        if vice_material_id is not None and vice_material_id:
            self.vice_material_id = vice_material_id
        else:
            self.vice_material_id = None

        if interior_material_id is not None and interior_material_id:
            self.interior_material_id = interior_material_id
        else:
            self.interior_material_id = None

        if exterior_structure is not None and exterior_structure:
            self.exterior_structure = exterior_structure
        else:
            self.exterior_structure = None

        if interior_structure is not None and interior_structure:
            self.interior_structure = interior_structure
        else:
            self.interior_structure = None

        if open_mode is not None and open_mode:
            self.open_mode = open_mode
        else:
            self.open_mode = None

        if length is not None and length:
            self.length = length
        else:
            self.length = None

        if width is not None and width:
            self.width = width
        else:
            self.width = None

        if height is not None and height:
            self.height = height
        else:
            self.height = None

        if weight is not None and weight:
            self.weight = weight
        else:
            self.weight = None

        if supplier_id is not None and supplier_id:
            self.supplier_id = supplier_id
        else:
            self.supplier_id = None

        if factory_price is not None and factory_price:
            self.factory_price = factory_price
        else:
            self.factory_price = None

        if cost_price is not None and cost_price:
            self.cost_price = cost_price
        else:
            self.cost_price = None

        if tag_price is not None and tag_price:
            self.tag_price = tag_price
        else:
            self.tag_price = None

        if retail_price is not None and retail_price:
            self.retail_price = retail_price
        else:
            self.retail_price = None

        if original_item_no is not None and original_item_no:
            self.original_item_no = original_item_no
        else:
            self.original_item_no = None

        if feature is not None and feature:
            self.feature = feature
        else:
            self.feature = None

        if comment is not None and comment:
            self.comment = comment
        else:
            self.comment = None


    def __repr__(self):
        return '<Product Name %r>' % self.product_abbreviation


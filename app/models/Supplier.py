#!/usr/bin/env python
# coding=utf-8

from app import db

class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supplier = db.Column(db.String(12), unique=True, index=True, nullable=False)
    description = db.Column(db.String(36), nullable=True)

    def __init__(self, supplier, description=None):
        self.supplier = supplier
        self.description = description

    def __repr__(self):
        return '<supplier %r>' % self.supplier


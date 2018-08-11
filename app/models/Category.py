#!/usr/bin/env python
# coding=utf-8

from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(12), unique=True, index=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def __init__(self, category=None, description=None):
        self.category = category
        self.description = description

    def __repr__(self):
        return '<category %r>' % self.category


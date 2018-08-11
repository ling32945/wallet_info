#!/usr/bin/env python
# coding=utf-8

from app import db

class Material(db.Model):
    __tablename__ = 'material'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    material = db.Column(db.String(8), unique=True, index=True, nullable=False)
    description = db.Column(db.String(24), nullable=True)

    def __init__(self, material, description=None):
        self.material = material
        self.description = description

    def __repr__(self):
        return '<material %r>' % self.material


#!/usr/bin/env python
# coding=utf-8

from app import db

class Factory(db.Model):
    __tablename__ = 'factory'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(12), unique=True, index=True, nullable=False)
    name = db.Column(db.String(12), nullable=True)
    description = db.Column(db.String(36), nullable=True)

    def __init__(self, no, name=None, description=None):
        self.no = no
        self.name = name
        self.description = description

    def __repr__(self):
        return '<no %r>' % self.no


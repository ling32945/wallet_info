#!/usr/bin/env python
# coding=utf-8

from app import db

class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sex = db.Column(db.String(6), unique=True, index=True, nullable=False)
    description = db.Column(db.String(24), nullable=True)

    def __init__(self, sex, description=None):
        self.sex = sex
        self.description = description

    def __repr__(self):
        return '<sex %r>' % self.sex


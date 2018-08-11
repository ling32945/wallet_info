#!/usr/bin/env python
# coding=utf-8

from app import db

class SaleChannel(db.Model):
    __tablename__ = 'sale_channels'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    channel_name = db.Column(db.String(8), unique=True, index=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def __init__(self, channel_name=None, description=None):
        self.channel_name = channel_name
        self.description = description

    def __repr__(self):
        return '<channel name %r>' % self.channel_name


# -*- coding: utf-8 -*-
from portfolio import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1024), index=True)
    imgSrc = db.Column(db.String(250))
    github = db.Column(db.String(250))
    weblink = db.Column(db.String(250))

    def __repr__(self):
        return '<Title {}>'.format(self.title)


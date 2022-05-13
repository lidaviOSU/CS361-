from application import db
from application.models import MSDS
from flask import render_template, jsonify,json


def searchdb(query):
    data = MSDS.query.filter(MSDS.name.contains(query) | MSDS.comments.contains(query) | MSDS.vendor.contains(query) | MSDS.internal.contains(query) | MSDS.user.contains(query) | MSDS.year.contains(query) | MSDS.cas.contains(query))
    return data
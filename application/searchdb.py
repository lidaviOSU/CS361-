from application import db,jsonify
from application.models import MSDS
import json

def searchdb(query):
    data = MSDS.query.filter(MSDS.name.contains(query) | MSDS.comments.contains(query) | MSDS.vendor.contains(query) | MSDS.internal.contains(query) | MSDS.user.contains(query) | MSDS.year.contains(query) | MSDS.cas.contains(query))
    results = []
    for datas in data:
        dictionary = {"id": datas.id,"name": datas.name, "comments": datas.comments, "vendor":datas.vendor, "internal": datas.internal, "user": datas.user, "year": datas.year, "cas": datas.cas}
        results.append(dictionary)
    return results

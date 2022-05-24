from flask import Flask, Response, request
from flaskext.mysql import MySQL
import csv
import io
import pymysql
from application.searchdb import searchdb
from application import app
from sqlalchemy import create_engine


@app.route('/download-csv/<query>', methods=["GET"])
def download_csv(query):
    if query:
        result = searchdb(query)
        if not result:
            return "nothing to download"

        output = io.StringIO()
        writer = csv.writer(output)

        line = ['MY DATA']
        writer.writerow(line)

        for r in result:
            line = []
            attribute = ""
            for element in r:
                attribute += str(element) + ':' + str(r[str(element)])
                attribute += ','
            line.append(attribute[:-1])
            writer.writerow(line)

        output.seek(0)

        return Response(output, mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=my_csv.csv"})
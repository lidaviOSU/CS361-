from flask import Flask, Response, render_template, request, redirect
from flaskext.mysql import MySQL
import csv
import io
import pymysql
from db_setup import create_connection, app

@app.route('/download-csv/<query>', methods=['GET'])
def download_csv(query):
    db_connection = create_connection()
    cursor = db_connection.cursor()
    if request.method == 'GET':
        cursor.execute(query)
        result = cursor.fetchall()

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
                attribute += str(element)
                attribute += ','
            line.append(attribute[:-1])
            writer.writerow(line)

        output.seek(0)

        return Response(output, mimetype="text/csv",
                headers={"Content-Disposition": "attachment;filename=my_csv.csv"})
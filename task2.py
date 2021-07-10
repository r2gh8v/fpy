#!/usr/bin/python3


from flask import Flask, request as flask_request

import logging, os
# logging.getLogger().setLevel(logging.INFO)

# import schema.sql
from db import *
from scheduler import *



print("here")



app = Flask(__name__)
app.logger.setLevel(logging.INFO)

app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

try:
    os.makedirs(app.instance_path)
except OSError:
        pass

def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


init_app(app)




@app.route("/")
def index():
    return "Hello World!"


@app.route("/videos", methods=["GET"])
def get_videos():
	# request = flask_request.get_json()
	offset = flask_request.args.get('offset') or 0
	message = "success"

	try:
		offset = int(offset)
	except Exception as e:
		return {"error": "offset has to be string"}
	print(offset)

	final_result = []


	db = get_db()

	for row in db.execute('SELECT * FROM vid LIMIT 2 OFFSET ?', (str(offset))):
 		final_result.append(row)

	if not final_result:
 		message = "Offset might be larger than the data set size."

	return {"next_offset": offset+2, "videos": final_result, "message":message}


@app.route("/search", methods=["GET"])
def get_videos_by_search():
	title = flask_request.args.get('title')
	description = flask_request.args.get('description')

	db = get_db()
	final_result = []

	if not title and not description:
		return {"error": "No search params mentioned!"}


	if title:
		for row in db.execute("SELECT * FROM vid WHERE title like ?", ('%'+title +'%',)):
 			final_result.append(row)
	if description:
		for row in db.execute("SELECT * FROM vid WHERE description like ?", ('%'+description +'%',)):
 			final_result.append(row)


	return {"videos": final_result, "message": "success"}





if __name__ == "__main__":
    app.run(debug=True, port = 5000, host='0.0.0.0')

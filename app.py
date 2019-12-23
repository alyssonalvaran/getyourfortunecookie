from flask import Flask, render_template, send_from_directory
from random import randrange


app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
	# open cookie sayings file
	file_path = "static/temp/cookie-sayings.txt"
	with open(file_path, "r") as f:
		sayings = f.read()
		sayings_list = sayings.split("\n")
		f.close()

	# pick random fortune
	random_num = randrange(len(sayings_list))
	fortune = sayings_list[random_num]

	return render_template("index.html", **locals())

@app.route("/cookie-sayings/")
def send_cookie_sayings():
	return app.send_static_file("temp/cookie-sayings.txt")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
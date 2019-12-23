from flask import Flask, render_template, request, send_from_directory

from sayings import get_random_saying, overwrite_saying


app = Flask(__name__, static_url_path="")

@app.route("/", methods=["GET", "POST"])
def home():
	file_path = "static/temp/cookie-sayings.txt"

	# get random saying and index
	saying, index = get_random_saying(file_path)

	if request.method == "POST":
		# get form data
		saying_input = request.form.get("sayingInput")
		overwrite_saying(file_path, index, saying_input)

	return render_template("index.html", **locals())

@app.route("/cookie-sayings/")
def send_cookie_sayings():
	return app.send_static_file("temp/cookie-sayings.txt")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
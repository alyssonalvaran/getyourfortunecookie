from flask import Flask, render_template, request, send_from_directory
from random import randrange


app = Flask(__name__, static_url_path="")

@app.route("/", methods=["GET", "POST"])
def home():
	file_path = "static/temp/cookie-sayings.txt"

	# open cookie sayings file
	f = open(file_path, "r")
	sayings = f.read()
	sayings_list = sayings.split("\n")
	f.close()

	# pick random fortune
	random_num = randrange(len(sayings_list))
	fortune = sayings_list[random_num]

	if request.method == "POST":
		# get form data
		fortune_input = request.form.get("fortuneInput")
		if fortune_input != "":
			# overwrite old saying
			sayings_list[random_num] = fortune_input
			
			f = open(file_path, "w")
			f.write("\n".join(sayings_list))
			f.close()

	return render_template("index.html", **locals())

@app.route("/cookie-sayings/")
def send_cookie_sayings():
	return app.send_static_file("temp/cookie-sayings.txt")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
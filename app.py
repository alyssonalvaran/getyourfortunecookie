from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
	with open("static/temp/cookie-sayings.txt", "r") as f:
		details = f.read()
		print(details)
		f.close()

	return render_template("index.html", **locals())

@app.route("/cookie-sayings/")
def send_cookie_sayings():
	return app.send_static_file('temp/cookie-sayings.txt')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
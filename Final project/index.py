from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path="/static")

#Route to serve static files
@app.route("/static/<path:path>")
def get_file(path):
    return send_from_directory("static", path)

#Default route
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def default(path):
    return "<h1>Welcome!</h1>"

if __name__ == "__main__":
    app.run()
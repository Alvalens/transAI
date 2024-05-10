from flask import Flask, render_template, request, jsonify, send_from_directory


DATASET_FILE_PATH = "uploads/dataset.csv"
MODEL_FILE_PATH = "model.pkl"

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/")
def index():
    return render_template("pages/index.html")


# route config
@app.route("/public/<path:subdir>/<path:filename>")
def serve_static(subdir, filename):
    # Define the base directory for static files
    base_dir = "public"

    # Construct the full directory path
    directory = f"{base_dir}/{subdir}"

    # Serve the file from the specified directory
    return send_from_directory(directory, filename)


if __name__ == "__main__":
    app.run(debug=True)

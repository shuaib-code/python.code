from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # List all files in the root directory except app.py and index.html
    files = [f for f in os.listdir('./templates') if os.path.isfile(f) and f not in ['app.py', 'index.html']]
    return render_template('index.html', files=files)

@app.route('/file/<filename>')
def download_file(filename):
    # Serve the requested file
    return send_from_directory('.', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

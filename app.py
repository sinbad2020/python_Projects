from flask import Flask, render_template, request, jsonify
import os

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    target_dir = os.path.join(os.getcwd(), "uploads")# مسار مطلق

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    file = os.path.join(target_dir, request.files['file'].filename)
    request.files['file'].save(file)

    return jsonify({"message": "File uploaded successfully."})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

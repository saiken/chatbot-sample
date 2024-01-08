from flask import Flask, render_template, jsonify
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/api/sendMessage', methods=['POST'])
def sendMessage():
    return jsonify({"role": "assistant", "message": "すごくいいですね"})

if __name__ == "__main__":
    app.run()

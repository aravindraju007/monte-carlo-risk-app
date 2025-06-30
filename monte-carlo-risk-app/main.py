from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run', methods=['POST'])
def run_analysis():
    username = request.form['username']
    service = request.form['service']
    resources = request.form['resources']
    shots = request.form['shots']
    history = request.form['history']
    signal = request.form['signal']
    return render_template("results.html", data={
        "username": username,
        "service": service,
        "resources": resources,
        "shots": shots,
        "history": history,
        "signal": signal
    })

@app.route('/audit')
def audit():
    return render_template("audit.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ecological-footprint-analysis/templates/interactive_sdgi_map.html')
def interactive_map():
    return render_template('interactive_sdgi_map.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
from flask import Flask

app = Flask(__name__)

@app.route('/global_ecological_footprint')
def global_ecological_footprint():
    return "Global Ecological Footprint Data"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

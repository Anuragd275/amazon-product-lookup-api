from flask import *
from api import get_item_details

# Initiate the application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/product/<asin>', methods=['GET'])
def search_by_pid(asin):
    result =  get_item_details(asin)
    return jsonify(result)
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
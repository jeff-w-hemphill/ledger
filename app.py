
from flask import Flask, current_app, render_template, request, redirect, jsonify
import json
from json import JSONEncoder
from datetime import date
from script import loan, Entry


app = Flask(__name__)
app.app_context().push()
with app.app_context():
    print(current_app.name)
        
# in-memory
buckets = []
loans = []
loans.append(loan.to_json())

@app.route('/')
def index():
    return render_template('index.html', loan = loan)

@app.route('/ledger/buckets', methods=['GET','POST'])
def create_buckets():
    if request.method == 'GET':
        return jsonify(buckets)
    else:
        try:
            bucket = request.form['identifier']
            buckets.append(bucket)
            return jsonify(buckets)
        except:
            return 'Error posting buckets'

@app.route('/ledger/buckets/sum', methods=['GET'])
def sum():
    try:
        ids = request.args['bucketids'].split(',')
        response = {}
        for id in ids:
            response[id] = 0
            for item in loan.entries:
                if id == item.bucketId:
                    response[id] += item.value
    except:
        return 'Error summing buckets'
        
    return response




@app.route('/ledger/entries', methods=['GET', 'POST'])
def entries():
    if request.method == 'GET':
        for l in loans:
            l = json.loads(l)
           
            if l['id'] == int(request.args['loanId']):
                return l
            
        return 'error, enter valid loanId'
    else:
        data = request.get_json()
        # confused about how this endpoint works. Are we supposed to also receive loanId as used by other endpoint?
        
        return request.data
    


if __name__ == "__main__":
    app.run(debug=True)
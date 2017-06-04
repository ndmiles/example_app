from flask import redirect, Flask, json, render_template, request, session, url_for, send_from_directory

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    test_dict = {'first_name': first_name, 'last_name': last_name}
    json_data = json.dumps(test_dict)
    print(json_data)
    return redirect(url_for('hello',data=json_data), code=303)

@app.route('/hello/', methods=['GET'])
def hello():
    tmp = request.args['data']
    data = json.loads(tmp)
    first_name = data['first_name']
    last_name = data['last_name']
    return render_template('hello.html',name=first_name+' '+last_name)


if __name__ =="__main__":
     app.run(debug=True)

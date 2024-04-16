from flask import Flask, render_template, request, redirect, url_for
from text_classificaion import classify_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    prediction = ''
    if request.method == 'POST':
        message = request.form['message']
        # check message is empty
        if message == '':
            return redirect(url_for('index'))

        else:
            prediction = classify_text(message)
    elif request.method == 'GET' and request.args.get('clear') == 'true':
        message = ''
        prediction = ''
    return render_template('index.html',message=message, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

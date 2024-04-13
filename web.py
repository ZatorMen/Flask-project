from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('registration.html', encoding='utf-8') as f:
            return ''.join(f.readlines())
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
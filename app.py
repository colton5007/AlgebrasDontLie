from flask import Flask
from flask import send_file, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def landing():
    return open('index.html').read()

@app.route("/explore", methods=['GET', 'POST'])
def explore():
    if request.method == 'POST':
        print(request.form)
        ctype = request.form['ctype']
        return open('explore.html').read().replace('###', ctype)
    else:
        return open('explore.html').read().replace('###', '')

if __name__ == '__main__':
      app.run(host='localhost', port=8080)
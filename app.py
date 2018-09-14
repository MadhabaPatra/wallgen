from flask import Flask, request, send_file, url_for, redirect, render_template
import os
import wallgen
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        print(request.form['side'])
        if request.form['side']:
            side = int(request.form['side'])
            shift = side//10
            side += shift*2
            points = wallgen.genPoints(100,100,side)
            img = wallgen.genWall(points, side, shift)
            img.save('static/wall.png')
            return send_file('static/wall.png', mimetype="image/png")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('',port),app)
    http_server.serve_forever()
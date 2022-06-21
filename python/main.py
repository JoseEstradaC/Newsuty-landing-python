from flask import Flask,render_template,jsonify,request,send_from_directory
from opengraph import OpenGraph
app = Flask(__name__)
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')
    
@app.route('/assets/<path>')
def send_report(path):
    return send_from_directory('static/assets', path)

@app.route('/link', methods=['GET'])
def getParser():
    og = OpenGraph(url=request.args.get('url'))
    return jsonify(
        title=og.title,
        url=og.url,
        url_image=og.image
    )
    
if __name__=="__main__":
    app.run()
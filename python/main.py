from flask import Flask,render_template,jsonify,request
from opengraph import OpenGraph
app = Flask(__name__)
def root():
    return render_template('index.html')

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
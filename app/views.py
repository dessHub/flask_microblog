from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname":"dess"}
    post = [{'author':{'nickname':'creig'},'body':'its a beutifull day'},{'author':{'nickname':'ben'},'body':'Flask is awesom'}]
    return render_template('index.html',title='Home',user=user,post=post)

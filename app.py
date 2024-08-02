from flask import Flask ,render_template,request   
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///task.db'
db = SQLAlchemy(app)

class Routine(db.Model):
    Sno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=True)
    desc =  db.Column(db.String(500),nullable=True)
    date =  db.Column(db.DateTime,default = datetime.now())
    def __repr__(self):
        return f"{self.Sno} -- {self.title}"

@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        title = request.form['Title']
        desc = request.form['Desc']
        print("post")
        task = Routine(title =title, desc=desc)
        db.session.add(task)
        db.session.commit()
    alltask = Routine.query.all()
    return render_template('index.html',alltask = alltask)

@app.route('/index')
def index():
    return 'this is an index page'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
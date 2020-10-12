from flask import Flask , request, render_template , url_for
from flask import redirect , session , flash , g, json , jsonify
from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms.validators import InputRequired , Length
from flask_sqlalchemy import SQLAlchemy
import sqlite3 


app = Flask(__name__)
app.secret_key = 'session'

DATABASE = "path/to/PhotoCoordinates.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


class LoginForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min =16, max= 16, message= 'name must be exactly 16 characters long and must be jpg.')])
    lot = StringField('longitude', validators=[InputRequired(), Length(min =16, max= 16, message= 'lan must be exactly 16 characters long')])
    lan = StringField('lanitude', validators=[InputRequired(), Length(min =17, max= 17 , message= 'lon must be exactly 16 characters long.')])

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/geodata_get_request', methods=['GET', 'POST'])
def index():
    with open("route.json", "r") as read_file:
            data = json.load(read_file)
            
    return render_template('jsofile.html')
        
      


@app.route('/geodata_post_request', methods=['GET', 'POST'])
def form():
    
    form = LoginForm()
    if form.validate_on_submit():
        validate_name= request.form['name'] 
        validate_lot= request.form['lot']
        validate_lan= request.form['lan']
        db.execute("INSERT INTO PhotoCoordinates (name, lot, lan)  VALUES (?,?,?)" ,(validate_name, validate_lot, validate_lan))
        db.commit()
        return render_template('views.html', mydata=mydata)
    return render_template('form.html', form = form)

@app.route('/views',  methods=['GET', 'POST'])
def views():
    data = PhotoCoordinates.query.all()
    return render_template('views.html')



if __name__ == '__main__':
    app.run(debug = True)
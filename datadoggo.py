from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, \
                    DateTimeField, RadioField, SelectField, \
                    TextField, TextAreaField, SelectField)
from wtforms.validators import DataRequired

import os 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd

# configuration
#DATABASE = '/tmp/flaskr.db'
#SECRET_KEY = 'development key'
#USERNAME = 'admin'
#PASSWORD = 'default'
#Creating the application
app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'

#sql database section
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#Database Models
class Doggo(db.Model):
    __tablename__ = 'Dogs'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64))
    breed= db.Column(db.String(64))
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"Name: {self.name}, Breed: {self.breed}"

db.create_all() #not really sure for this one (come back to review)

class InfoForm(FlaskForm):
    d_choices = [('Affenpinscher', 'Affenpinscher'), ('Australian Silky Terrier', 'Australian Silky Terrier'), ('Australian Terrier', 'Australian Terrier'), \
    ('Bichon Avanese', 'Bichon Avanese'), ('Bichon Frise', 'Bichon Frise'), ('Bohemian Terrier', 'Bohemian Terrier'), \
    ('Bolognese','Bolognese'), ('Border Terrier','Border Terrier'), ('Boston Terrier','Boston Terrier'), ('Brussels Griffon', 'Brussels Griffon'), \
    ('Cairn Terrier', 'Cairn Terrier'), ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'), ('Chihuahua', 'Chihuahua'),\
    ('Chinese Crested Dog', 'Chinese Crested Dog'), ('Chinese Imperial Chin', 'Chinese Imperial Chin'), ('Chinese Temple Dog', 'Chinese Temple Dog'),\
    ('Coton de tulear', 'Coton de tulear'), ('Czech Terrier', 'Czech Terrier'), ('Dachshund', 'Dachshund'), ('Dandie Dinmont Terrier', 'Dandie Dinmont Terrier'),\
    ('English Toy Spaniel', 'English Toy Spaniel'), ('German Hunting Terrier', 'German Hunting Terrier'), ('Griffon Belge', 'Griffon Belge'), ('Griffon Brabancon', 'Griffon Brabancon'),\
    ('Hairless Dog', 'Hairless Dog'), ('Italian Greyhound', 'Italian Greyhound'), ('Jack Russel Terrier', 'Jack Russel Terrier'), ('Japanese Spaniel (Chin)', 'Japanese Spaniel (Chin)'),\
    ('Japanese Spitz', 'Japanese Spitz'), ('Lakeland Terrier', 'Lakeland Terrier'), ('Lhasa Apso', 'Lhasa Apso'), ('Little Lion Dog', 'Little Lion Dog'), \
    ('Maltese','Maltese'), ('Manchester Terrier', 'Manchester Terrier'), ('Miniature Pinscher', 'Miniature Pinscher'), ('Miniature Schnauzer', 'Miniature Schnauzer'),\
    ('Norfolk Terrier', 'Norfolk Terrier'), ('Norwegian Lundehund','Norwegian Lundehund'), ('Norwich Terrier', 'Norwich Terrier'), ('Papillon','Papillon'), ('Pekingnese', 'Pekingnese'), \
    ('Pomeranian','Pomeranian'), ('Poodle (Toy / Miniature)', 'Poodle (Toy / Miniature)'), ('Pug', 'Pug'), ('Schipperkee', 'Schipperkee'), ('Scottish Terrier', 'Scottish Terrier'),\
    ('Sealyham Terrier', 'Sealyham Terrier'), ('Shetland Sheepdog', 'Shetland Sheepdog'), ('Shih Tzu', 'Shih Tzu'), ('Silky Terrier', 'Silky Terrier'), \
    ('Small Continental Spaniel', 'Small Continental Spaniel'), ('Small English Terrier', 'Small English Terrier'), ('Small Spitz', 'Small Spitz'), \
    ('Smooth Fox Terrier', 'Smooth Fox Terrier'), ('Tibetan Spaniel', 'Tibetan Spaniel'), ('Toy Fox Terrier', 'Toy Fox Terrier'), ('Toy Terrier', 'Toy Terrier'),\
    ('Volpino Italiano', 'Volpino Italiano'), ('Welsh Terrier', 'Welsh Terrier'), ('West Highland Terrier', 'West Highland Terrier'), \
    ('Wire-Haired Fox Terrier', 'Wire-Haired Fox Terrier'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Mixed','Mixed'), ('Unknown','Unknown')]
    name = StringField("Name: ",validators=[DataRequired()])
    breed = SelectField("Breed: ", choices=d_choices,validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/information', methods=['GET','POST'])
def show_info():
    form= InfoForm()
    if form.validate_on_submit():
        #id = form.id.data
        new_entry = Doggo(form.name.data, form.breed.data)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('show_stats'))
    return render_template('infoform.html', form=form)

@app.route('/statistics')
def show_stats():
    stats = Doggo.query.all()
    legend = 'Dog Count'
    labels = ['Affenpinscher', 'Australian Silky Terrier', 'Australian Terrier', 'Bichon Avanese', 'Bichon Frise', 'Bohemian Terrier', 'Bolognese', 'Border Terrier', 'Boston Terrier', 'Brussels Griffon', 'Cairn Terrier', 'Cavalier King Charles Spaniel', 'Chihuahua', 'Chinese Crested Dog', 'Chinese Imperial Chin', 'Chinese Temple Dog', 'Coton de tulear', 'Czech Terrier', 'Dachshund', 'Dandie Dinmont Terrier', 'English Toy Spaniel', 'German Hunting Terrier', 'Griffon Belge', 'Griffon Brabancon', 'Hairless Dog', 'Italian Greyhound', 'Jack Russel Terrier', 'Japanese Spaniel (Chin)', 'Japanese Spitz', 'Lakeland Terrier', 'Lhasa Apso', 'Little Lion Dog', 'Maltese', 'Manchester Terrier', 'Miniature Pinscher', 'Miniature Schnauzer', 'Norfolk Terrier', 'Norwegian Lundehund', 'Norwich Terrier', 'Papillon', 'Pekingnese', 'Pomeranian', 'Poodle (Toy / Miniature)', 'Pug', 'Schipperkee', 'Scottish Terrier', 'Sealyham Terrier', 'Shetland Sheepdog', 'Shih Tzu', 'Silky Terrier', 'Small Continental Spaniel', 'Small English Terrier', 'Small Spitz', 'Smooth Fox Terrier', 'Tibetan Spaniel', 'Toy Fox Terrier', 'Toy Terrier', 'Volpino Italiano', 'Welsh Terrier', 'West Highland Terrier', 'Wire-Haired Fox Terrier', 'Yorkshire Terrier', 'Mixed', 'Unknown']
    values = [0] * len(labels)
    for infoline in stats:
        infoline = str(infoline)
        for index in range(len(labels)):
            if infoline.split(sep=",")[1][8:] == labels[index]:  #getting 2nd element which is the breed
                values[index] += 1

    return render_template('stats.html', stats=stats, legend=legend, labels=labels, values=values)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404






if __name__ == '__main__':
    app.run()
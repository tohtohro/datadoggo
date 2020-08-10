from flask import Flask, render_template 
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, \
                    DateTimeField, RadioField, SelectField, \
                    TextField, TextAreaField, SelectField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY']= 'mysecretkey'

class InfoForm(FlaskFom):
    choices = [1. Affenpinscher,Australian Silky Terrier,Australian Terrier ,Bichon Avanese ,Bichon Frise
,Bohemian Terrier,Bolognese,Border Terrier,Boston Terrier,Brussels Griffon,Cairn Terrier,Cavalier King Charles Spaniel
,Chihuahua,Chinese Crested Dog,Chinese Imperial Chin,Chinese Temple Dog,Coton de tulear,Czech Terrier,Dachshund
,Dandie Dinmont Terrier,English Toy Spaniel,German Hunting Terrier,Griffon Belge,Griffon Brabancon,Hairless Dog
,Italian Greyhound,Jack Russel Terrier,Japanese Spaniel (Chin),Japanese Spitz,Lakeland Terrier
,Lhasa Apso,Little Lion Dog,Maltese,Manchester Terrier,Miniature Pinscher,Miniature Schnauzer,Norfolk Terrier,Norwegian Lundehund
,Norwich Terrier,Papillon,Pekingnese,Pomeranian,Poodle (Toy / Miniature),Pug,Schipperkee,Scottish Terrier
,Sealyham Terrier,Shetland Sheepdog,Shih Tzu,Silky Terrier,Small Continental Spaniel,Small English Terrier
,Small Spitz,Smooth Fox Terrier,Tibetan Spaniel,Toy Fox Terrier,Toy Terrier
,Volpino Italiano,Welsh Terrier,West Highland Terrier,Wire-Haired Fox Terrier,Yorkshire Terrier]

    breed = SelectField("What is your Breed?", choices=validators=[])
    submit = SubmitField('Submit')

@app.route()
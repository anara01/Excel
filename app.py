from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def data():
	data = pd.read_excel('good.xlsx')
	return render_template('index.html', data=data)


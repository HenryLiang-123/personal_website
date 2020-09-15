from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
#when there is a / detected in the url, this function gets run
def home_page():
    return render_template('./index.html')

@app.route('/<string:page_name>')
#when there is a / detected in the url, this function gets run
#page name suffix (use when needed)
def html_page(page_name):
    return render_template(page_name)

# @app.route('/about')
# #when there is a / detected in the url, this function gets run
# def about():
#     return render_template('./about.html')


def write_to_database(data):
	with open('database.txt', mode = 'a') as database:
		name = data['name']
		email = data['email']
		message = data['message']
		file = database.write(f'\n{name},{email},{message}')

def write_to_csv(data):
	with open('database.csv', newline = '', mode = 'a') as database2:
		name = data['name']
		email = data['email']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter = ",", quotechar = '"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			 return 'did not save to database'
	else:
		return 'error'


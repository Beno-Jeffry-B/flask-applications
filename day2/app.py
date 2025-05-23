'''
    --> render_template 
    --> data transfer to templates

PROBLEM STATMENT:
    Create a system for receptionists to view and manage patients who come in for appointments.




Note
    --> if u are having .html pages then put them templates {same spelling} flask automatically searches and redirects them.
    --> For Custom Template Folder

    make sure add a extra parameter in Flask()

    for eg:
        -->  app = Flask(__name__, template_folder='html_pages')


   -->   
    return render_template("index.html",  name = "Beno Jeffry")  # expects keyword args not regular args

    
'''


from flask import Flask ,render_template
app = Flask(__name__)



@app.route('/')
def homepage():
    return "homepage"



@app.route('/dashboard')
def dashboard():
    appointments = [
        {
            'id': 1,
            'name': 'Ravi Kumar',
            'time': '10:00 AM',
            'doctor': 'Dr. Meena Sharma',
            'status': 'Waiting'
        },
        {
            'id': 2,
            'name': 'Priya Iyer',
            'time': '10:30 AM',
            'doctor': 'Dr. Arjun Patel',
            'status': 'Checked In'
        },
        {
            'id': 3,
            'name': 'Sathish N',
            'time': '11:00 AM',
            'doctor': 'Dr. Meena Sharma',
            'status': 'Waiting'
        },
        {
            'id': 4,
            'name': 'Kavitha R',
            'time': '11:30 AM',
            'doctor': 'Dr. Arjun Patel',
            'status': 'Waiting'
        }]
    
    return render_template('index.html',appointments=appointments)
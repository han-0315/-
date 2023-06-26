from flask import Flask, render_template
from views import home, about, contact, submit_contact_form

app = Flask(__name__)

# Routes
app.add_url_rule('/', view_func=home)
app.add_url_rule('/about', view_func=about)
app.add_url_rule('/contact', view_func=contact, methods=['GET', 'POST'])
app.add_url_rule('/submit_contact_form', view_func=submit_contact_form, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)

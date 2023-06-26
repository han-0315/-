from flask import render_template, request, redirect, url_for
from models import BlogPost, ContactFormSubmission
from forms import ContactForm

# Dummy data
blog_posts = [
    BlogPost(title='First post', content='This is my first blog post', author='John Doe', date='2021-01-01'),
    BlogPost(title='Second post', content='This is my second blog post', author='John Doe', date='2021-01-02'),
    BlogPost(title='Third post', content='This is my third blog post', author='John Doe', date='2021-01-03')
]

def home():
    return render_template('home.html', blog_posts=blog_posts)

def about():
    return render_template('about.html')

def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)

def submit_contact_form():
    form = ContactForm(request.form)
    if form.validate():
        submission = ContactFormSubmission(name=form.name.data, email=form.email.data, message=form.message.data)
        # TODO: Save submission to database or send email
        return redirect(url_for('home'))
    else:
        return render_template('contact.html', form=form)

from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Form submitted successfully!")
            # Process form data
        else:
            flash("Form validation failed. Please correct the errors.")
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

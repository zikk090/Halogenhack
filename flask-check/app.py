from flask import Flask, render_template, request
from spam_filter import is_spam, SPAM_WORDS, classifier, vectorizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        email = request.form['email']
        email_vector = vectorizer.transform([email])
        prediction = classifier.predict(email_vector)[0]

        if prediction == 'spam':
            return "This email is a spam email."
        else:
            return "This email is not a spam email."
    else:
        return "Method not allowed. Please use a POST request."

if __name__ == '__main__':
    app.run(debug=True)

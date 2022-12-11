# Import the necessary libraries
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define a list of common spam words and phrases
SPAM_WORDS = [
    "viagra",
    "free money",
    "work from home",
    "get rich quick",
    "lose weight fast",
    "nigerian prince",
    "make millions",
    "lottery winner",
]

# Define a function to check if an email is spam
def is_spam(email, spam_words):
    """
    Check if an email is spam by checking if it contains any of the spam words or phrases in the provided list.

    :param email: The email to check (string)
    :param spam_words: A list of spam words and phrases to check for (list of strings)
    :return: True if the email is spam, False if it is not spam
    """

    # Convert the email to lowercase
    email = email.lower()

    # Compile a regular expression pattern to match any of the spam words or phrases
    spam_pattern = re.compile("|".join(spam_words))

    # Check if any of the spam words or phrases are in the email
    if spam_pattern.search(email):
        return True

    # Check if the email contains any suspicious patterns
    if re.search(r"\$\d+", email) or re.search(r"\d+\$", email):
        return True

    # Check if the email contains a Google Drive attachment from an unknown sender
    if "google drive" in email and "attachment" not in email and "contact" not in email:
        return True

    # If none of the spam words or patterns were found, return False
    return False

# Define the training data
emails = [
    ("Hi, I'm a Nigerian prince and I need your help to transfer millions of dollars. Please send me your bank account information.", "spam"),
    ("Congratulations! You have won the lottery! Please send me your personal details to claim your prize.", "spam"),
    ("Hello, I'm a friend of your friend and I have a great business opportunity for you. You can make millions from the comfort of your own home. Let me know if you're interested.", "spam"),
    ("Hi, I'm a software engineer and I'm looking for a job. I have attached my resume for your review. Please let me know if you have any job openings.", "not spam"),
    ("Hello, I'm a health coach and I'm offering a special discount on my weight loss program. You can lose 10 pounds in just 2 weeks. Contact me for more information.", "spam"),
    ("Hi, I'm a researcher and I'm conducting a survey on the effectiveness of spam filters. Can you please help by answering a few questions?", "not spam"),
]

# Create a CountVectorizer to convert emails into numerical feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([email for email, label in emails])
y = [label for email, label in emails]

# Train a Multinomial Naive Bayes classifier on the data
classifier = MultinomialNB()
classifier
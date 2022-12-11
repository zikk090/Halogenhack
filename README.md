Spam Filter
This is a simple spam filter designed to identify spam emails using natural language processing techniques. The filter uses a Naive Bayes classifier trained on a dataset of known spam and non-spam emails to predict whether a new email is likely to be spam or not.

The classifier was trained using the sklearn library and the CountVectorizer and MultinomialNB classes. The model was tested using the Gmail API on a variety of email sizes and was found to be effective at identifying spam emails with a high degree of accuracy.


Tutorial

To use the spam filter, you will need to have the following Python libraries installed:

re
sklearn
Gmail API (optional, only required if you want to test the filter on your Gmail account)

Once you have the required libraries installed, you can use the is_spam function to check if an email is spam or not. The function takes an email string and a list of spam words and phrases as arguments and returns a boolean value indicating whether the email is spam or not.
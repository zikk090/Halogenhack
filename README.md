## Spam Filter
This project is a submission for the Halogen hackathon by **Ezinne Faith Kalu (ekalu.fk@gmail.com)**. The goal of this project is to build a spam filter that can accurately classify incoming emails as spam or not spam.

## Installation
To run this project on your local machine, follow these steps:

+ Clone the repository: git clone https://github.com/username/spam-filter.git
+ Install the required dependencies: 
```shell
 pip install -r 
``` 
requirements.txt
+ Run the Flask app: 
```bash
python3 app.py
```

## Usage
Once the Flask app is running, open your web browser and navigate to http://localhost:5000/. You should see a form where you can enter an email message to check if it's spam or not.

## Project Structure
**app.py**: The Flask app that serves the web interface for the spam filter.
**spam_filter.py**: The Python module that contains the machine learning model for the spam filter.
**templates/**: A directory containing the HTML templates for the Flask app.

## Credits
The spam filter was built using the scikit-learn machine learning library, and the Flask web framework was used to serve the web interface. The spam dataset used to train the model was obtained from the UCI Machine Learning Repository.


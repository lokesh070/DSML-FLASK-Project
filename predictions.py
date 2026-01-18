from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

model = open('artefacts/classifier.pkl', 'rb')
clf  = pickle.load(model)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def pinger():
    return {'Message': 'This is a Hello Message from version2'}

@app.route("/predict", methods=['POST'])
def predict():
    loan_request = request.get_json() #get the data in JSON format
    if loan_request['Gender']=='Male':
        Gender = 0
    else:
        Gender = 1

    if loan_request['Married']=='No':
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_request['ApplicantIncome']
    LoanAmount = loan_request['LoanAmount']
    Credit_History = loan_request['Credit_History']

    input_data = [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]]
    prediction = clf.predict(input_data) ## [[]]

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Accepted"

    return {'Loan Approval Status': pred}


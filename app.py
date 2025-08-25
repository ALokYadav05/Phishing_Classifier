from flask import Flask, request, render_template
import joblib
import numpy as np
import boto3
import os
from db import save_prediction 

app = Flask(__name__, template_folder="templates")

# -------------------------------
# Loading Model from S3
# -------------------------------
BUCKET_NAME = "phishing-classifier-model"   
MODEL_KEY = "random_forest_model.pkl"  
LOCAL_MODEL_PATH = "model.pkl"    

# Download model from S3
s3 = boto3.client('s3')
s3.download_file(BUCKET_NAME, MODEL_KEY, LOCAL_MODEL_PATH)

# Load the model
model = joblib.load(LOCAL_MODEL_PATH)

# flask routes

@app.route('/')
def home():
    return render_template("index2.html")  

@app.route('/predict', methods=['POST'])
def predict():
    try:
        columns = [
            "Submitting_to_email", "having_At_Symbol", "URL_Length", "HTTPS_token",
            "Google_Index", "Abnormal_URL", "Statistical_report", "double_slash_redirecting",
            "Shortining_Service", "on_mouseover", "Redirect", "Prefix_Suffix", "Iframe",
            "RightClick", "Request_URL", "having_IP_Address", "Domain_registeration_length",
            "SSLfinal_State", "having_Sub_Domain", "Links_in_tags", "URL_of_Anchor",
            "SFH", "age_of_domain", "web_traffic", "DNSRecord", "Page_Rank",
            "Links_pointing_to_page"
        ]

        features = [int(request.form.get(col, 0)) for col in columns]
        final_input = np.array(features).reshape(1, -1)

        prediction = model.predict(final_input)[0]
        result = "Phishing Website" if prediction == 1 else "Legitimate Website"

        # Save to MongoDB
        save_prediction(
            url=request.form.get("url", "N/A"), 
            features=dict(zip(columns, features)), 
            prediction=result
        )

        return render_template("index2.html", prediction_text=f"Result : {result}")
    
    except Exception as e:
        return f"Error : {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

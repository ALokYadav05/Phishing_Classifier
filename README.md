# Phishing Classifier Web App

**End-to-end phishing URL classifier** : trained an ML model from scratch, performed basic EDA, containerized the Flask app using Docker, deployed it on AWS EC2, and hosted the trained model on S3.


---

##  Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Setup & Run Locally](#setup--run-locally)
- [Deployment on AWS](#deployment-on-aws)
- [Demonstration](#demonstration)
- [Proof of Deployment](#proof-of-deployment)
- [AWS Cleanup & Billing](#aws-cleanup--billing)
- [Technologies Used](#technologies-used)
- [About Me](#about-me)
- [License](#license)

---

## Overview
This project showcases a phishing-detection web application:
- Trained an ML model from scratch (performed data exploration and model training)
- Containerized the app with Docker
- Deployed the Flask application on AWS EC2
- Stored and loaded the trained model from Amazon S3
- Documented and cleaned up all AWS resources (EC2, S3, etc.) to avoid incurring charges
- Included screenshot proof of deployment, and cleaned up AWS resources post-demo
---

## Architecture
Simple and modular architecture ensures the app is portable, scalable, and demonstrable.

---

## Features
- URL phishing classification using an ML model
- Lightweight Flask web UI for testing
- Dockerized setup for seamless deployment
- AWS EC2 hosting with model accessible on S3
- Responsive cleanup of AWS resources to avoid charges
- Video and screenshots included as proof of deployment

---

## Setup & Run Locally
```bash
git clone https://github.com/your-username/phishing-classifier.git
cd phishing-classifier
docker build -t phishing-classifier .
docker run -d -p 5000:5000 phishing-classifier
```
#Access the app via http://localhost:5000


## Deployment on AWS
- Deployed Docker container on an EC2 instance.
- Mapped port 80 (EC2) to port 5000 (container)
- Fetched model assets from S3 within the container.
- App was publicly accessible and fully functional via the EC2 public IP.

## Proof of Deployment
- Screenshots include:
- App reachable via public IP
- Prediction result displayed in UI
- docker ps confirming the container is running
- EC2 Console showing active instance during demo

## Screenshots :##

<img width="1919" height="907" alt="Screenshot 2025-08-28 125511" src="https://github.com/user-attachments/assets/b8dffe99-48db-4b96-b3f5-3489652ecde8" />
<img width="1894" height="324" alt="Screenshot 2025-08-28 125713" src="https://github.com/user-attachments/assets/1993056e-879e-4d29-8bd8-3d23876b02da" />

<img width="1906" height="970" alt="Screenshot 2025-08-28 124926" src="https://github.com/user-attachments/assets/98d30b75-5b9a-445e-bfc7-eb035386de27" />
<img width="1904" height="971" alt="Screenshot 2025-08-28 125111" src="https://github.com/user-attachments/assets/393952b0-ce27-4237-a975-a5134d5dde1d" />




## AWS Cleanup & Billing
- To prevent unwanted costs:
- EC2 instance terminated
- EBS volumes deleted
- Elastic IPs released
- S3 bucket contents deleted

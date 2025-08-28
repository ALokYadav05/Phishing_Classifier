# Phishing Classifier Web App

**End-to-end phishing URL classifier** using a pre-trained ML model, containerized with Docker, deployed on AWS EC2, with model stored in S3.

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
- Uses a **pre-trained ML model** (no EDA needed; already preprocessed and encoded)
- Deployed as a **Docker container** running on an AWS EC2 instance
- Model files hosted on **S3**
- Proves full **end-to-end functionality**: Model → Container → Cloud deployment

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
Access the app via http://localhost:5000
```

##Deployment on AWS
- Deployed Docker container on an EC2 instance.
- Mapped port 80 (EC2) to port 5000 (container)
- Fetched model assets from S3 within the container.
- App was publicly accessible and fully functional via the EC2 public IP.

##Proof of Deployment
- Screenshots include:
- App reachable via public IP
- Prediction result displayed in UI
- docker ps confirming the container is running
- EC2 Console showing active instance during demo

<img width="1919" height="902" alt="Screenshot 2025-08-28 125542" src="https://github.com/user-attachments/assets/b077a89a-af8e-4e18-9494-9b66a76dfd92" />
<img width="1919" height="907" alt="Screenshot 2025-08-28 125511" src="https://github.com/user-attachments/assets/b8dffe99-48db-4b96-b3f5-3489652ecde8" />
<img width<img width="1894" height="324" alt="Screenshot 2025-08-28 125713" src="https://github.com/user-attachments/assets/5d4509f3-9c0d-4e46-91a3-b35096f32fe5" />
="1904" height="971" alt="Screenshot 2025-08-28 125111" src="https://github.com/user-attachments/assets/05f55089-cfdc-41e9-a3bc-a9b774a0e794" />
<img width="1906" height="970" alt="Screenshot 2025-08-28 124926" src="https://github.com/user-attachments/assets/ae4c5f6d-8df2-4a8d-9b2d-061813894060" />


##AWS Cleanup & Billing
- To prevent unwanted costs:
- EC2 instance terminated
- EBS volumes deleted
- Elastic IPs released
- S3 bucket contents deleted

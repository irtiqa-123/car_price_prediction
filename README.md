# Car Price Prediction App

A simple machine learning project that predicts the price of used cars based on input features. The project includes a complete ML pipeline, a FastAPI app for predictions, and Dockerization for easy deployment and sharing.

---

## **Project Overview**

This project demonstrates....

- **ML Pipeline**: Data ingestion → Preprocessing → Model Training → Evaluation  
- **FastAPI App**: Provides an API and interface to input car details and get predicted prices.  
- **Docker**: Containerized app for easy deployment and sharing.  
- **Optional CI/CD**: Can be integrated with GitHub Actions for automatic builds and deployment.

---

## **Folder Structure**

car_price_prediction/
├── data/ # CSV dataset (vehicle_data.csv)
├── models/ # Trained model will be saved here
├── src/ # Python scripts
│ ├── data_ingest.py # Load CSV, preview data
│ ├── preprocess.py # Encode categorical features, split train/test
│ ├── train.py # Train ML model
│ ├── evaluate.py # Evaluate model and save metrics
│ └── app.py # FastAPI API for predictions
├── Dockerfile # Containerize the app
├── requirements.txt # Python dependencies
└── README.md

## **Setup Instructions**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/car_price_prediction.git
cd car_price_prediction
2. Install Python Dependencies (optional if running locally)
bash
pip install -r requirements.txt
3. Run the FastAPI App Locally
bash
uvicorn src.app:app --reload
Open your browser: http://127.0.0.1:8000

Test the endpoints with Postman or the browser form.

4. Docker Setup (Recommended)
Build Docker Image
bash
docker build -t car:latest .
Run Docker Container
bash
docker run -p 8000:8000 car:latest
Open your browser: http://localhost:8000

Push Docker Image to Docker Hub
bash
docker login
docker tag car:latest mirirtiqa/car:latest
docker push mirirtiqa/car:latest
Team members can now run:
bash
docker pull mirirtiqa/car:latest
docker run -p 8000:8000 mirirtiqa/car:latest
ML Pipeline
Data Ingestion: Load the dataset (vehicle_data.csv) into Python.

Preprocessing: Encode categorical variables, handle missing values, split train/test.

Training: Train a regression model to predict car prices.

Evaluation: Calculate metrics (RMSE, R²) and save model in /models.

Using the API
Endpoint: /predict
Method: POST
Input Example (JSON):

json
Copy code
{
  "year": 2018,
  "mileage": 30000,
  "fuel": "Petrol",
  "transmission": "Manual",
  "owner": "First"
}
Output Example:

json
Copy code
{
  "prediction": 2878
}
Output is in ₹ (Indian Rupees).

Optional: CI/CD
Can be integrated with GitHub Actions to automatically:

Build Docker image on push

Push updated image to Docker Hub

Deploy to cloud server (EC2, Render, Railway, etc.)

Team Access
Developers/QA: Pull Docker image from Docker Hub and run locally.

Team Lead/Manager: Can see running app via public URL or inspect Docker image.

Users: Interact via API or frontend form.

Technologies Used
Python 3.11

FastAPI

scikit-learn, pandas, numpy

Docker & Docker Hub
CI/CD for Car Price Prediction App
Overview

This project uses GitHub Actions to implement Continuous Integration (CI) and Continuous Deployment (CD) for the car-price-app Docker container. Every change pushed to the main branch triggers the workflow to automatically build and push the Docker image to DockerHub.

Workflow Steps

Trigger

The workflow runs automatically on push to the main branch.

Can also be manually triggered from the Actions tab.

Checkout Code

The workflow first checks out the latest code from the repository using actions/checkout@v3.

Setup Python & Install Dependencies

Uses actions/setup-python to install Python.

Installs required packages from requirements.txt.

Docker Login

Logs into DockerHub using GitHub Secrets:

DOCKERHUB_USERNAME → your DockerHub username

DOCKERHUB_TOKEN → DockerHub Access Token

This ensures secure login for pushing images.

Build Docker Image

Builds the Docker image using your Dockerfile.

Tags the image: mirirtiqa/car-price-app:latest.

Push Docker Image to DockerHub

Pushes the newly built image to DockerHub automatically.

Secrets Required
Secret Name	Description
DOCKERHUB_USERNAME	DockerHub username (mirirtiqa)
DOCKERHUB_TOKEN	DockerHub Access Token
How It Works

Make changes in the repo and push to main.

GitHub Actions runs the workflow: builds & pushes Docker image.

EC2 or any server can pull the latest image from DockerHub to deploy.

This ensures automation — you don’t need to manually rebuild or push Docker images every time you update the code.

Future Improvements
Add a polished frontend using HTML/CSS or Streamlit

Integrate CI/CD pipeline for automated builds and deployment

Deploy on cloud (Render, Railway, AWS ECS/Fargate) for public access

License
MIT License

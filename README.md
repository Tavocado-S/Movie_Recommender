# Movie Recommendation System

## TL;DR
End-to-end MLOps project for a Netflix-style movie recommendation system using the MovieLens dataset.  
Built a reproducible machine learning workflow with MySQL, Airflow, MLflow, FastAPI, Docker Compose, and Streamlit.  
Best model: SVD collaborative filtering with cold-start fallback and experiment tracking for model comparison and promotion.

## Problem
Recommendation systems help users discover relevant content in large catalogs and are widely used in digital platforms such as Netflix, Spotify, and e-commerce applications. A key challenge is to generate personalized recommendations efficiently while handling sparse user-item interactions and cold-start scenarios for new users.

This project addresses that challenge by building a collaborative filtering recommendation system with a production-oriented workflow, including retraining, tracking, API serving, and a user-facing interface.

## Objective
- Build a movie recommendation engine based on user-item rating interactions.
- Train and evaluate a collaborative filtering model for personalized recommendations.
- Handle cold-start scenarios with a fallback recommendation strategy.
- Create a reproducible MLOps pipeline for training, tracking, deployment, and monitoring.

## My Contribution

## My Contribution

This project was completed in a team setting as part of the DataScientest Machine Learning Engineering training.

My main contribution covered the end-to-end ML workflow, including:
- implementation of the MySQL database layer for storing ratings and movie data
- data pipeline development
- experiment tracking and comparison with MLflow
- retraining workflow orchestration with Airflow
- integration of recommendation logic into the application workflow
- contribution to reproducibility and end-to-end execution with Docker Compose

## Data
- **Source:** MovieLens 20M dataset
- **Content:** user ratings, movie metadata, and auxiliary files
- **Scale:** ~20 million ratings, ~138k users, ~27k movies
- **Sample mode:** reduced sample dataset used for faster development and demonstration

## Approach
- Stored ratings and movie data in a **MySQL** database
- Used **SVD collaborative filtering** on the user-item matrix
- Implemented **cold-start fallback** using popular/highly rated movies
- Created a retraining workflow with **Airflow**
- Used **MLflow** for experiment tracking, model comparison, and model promotion
- Exposed predictions and recommendations through a **FastAPI** service
- Built a **Streamlit** frontend for interactive exploration and demo use
- Containerized the full stack with **Docker Compose**

## Results
- **Model:** SVD collaborative filtering
- **Evaluation metrics (sample run):**
  - RMSE: ~0.90
  - MAE: ~0.68
- **Cold-start handling:** popularity-based fallback for users without rating history
- **Prediction range:** clipped to realistic movie rating bounds

## Why this project matters
This project demonstrates more than model training: it shows how a machine learning solution can be integrated into a reproducible and operational workflow. The focus includes data handling, model lifecycle management, automated retraining, API delivery, and an interactive interface—key capabilities for turning data science into practical business solutions.

## Architecture
- **Data layer:** MovieLens dataset stored in MySQL
- **Modeling:** SVD collaborative filtering for user-movie recommendations
- **Orchestration:** Airflow DAG for retraining on new batch data
- **Experiment tracking:** MLflow for metrics, artifacts, and model promotion
- **Serving:** FastAPI for recommendation and prediction endpoints
- **Frontend:** Streamlit app for interactive usage
- **Deployment:** Docker Compose for local end-to-end execution

## My contribution
This project was completed in a team setting as part of the DataScientest Machine Learning Engineering training. My contribution focused on building the end-to-end analytical workflow, including data pipeline development, model training and evaluation, experiment tracking, workflow automation, API integration, and user-facing delivery through interactive tools.

## Repository structure
- `notebooks/` — exploratory analysis notebook
- `src/` — reusable Python modules for data preparation, training, and prediction
- `airflow/dags/` — retraining workflow
- `api/` — FastAPI application for recommendations and predictions
- `streamlit/` — Streamlit frontend
- `docker-compose.yml` — local orchestration of the full system
- `requirements.txt` — project dependencies
- `scripts/bootstrap.py` - downloads data, creates database and tables

## How to run

**Prerequisites:** Docker Desktop, Git, and free local ports for the application services.

1. Clone the repository
2. Build and start the full stack:
docker compose up -d --build
3. Run the bootstrap that downloads data and setup database:
python scripts/bootstrap.py
4. verify that tables were created:
  docker compose exec -T mysql-ml mysql -uapp -pmysql -hmysql-ml -D movielens -e "SHOW TABLES;"
5. Verify inside MySQL the number of rows of tables
 run: 
 - docker compose exec -T mysql-ml mysql -N -B -uapp -pmysql -hmysql-ml -D movielens -e "SELECT COUNT(*) FROM ratings;" 
 Note: Ratings rows should be 0 
 - docker compose exec -T mysql-ml mysql -N -B -uapp -pmysql -hmysql-ml -D movielens -e "SELECT COUNT(*) FROM movies;"
 Note: Movies rows should be 6730

6. Verify UIs are reachable, call in your explorer the next local hosts: 
 - FastAPI: http://localhost:8000/docs User: admin Password: secret 
 - MLflow UI: http://localhost:5001 
 - Airflow UI: http://localhost:8080 user: recommender password: BestTeam
 - Streamlit: http://localhost:8501

6. Run experiments from Airflow UI

## Example use case
- A user rates a few movies
- The model identifies latent preference patterns from similar users and items
- The API returns personalized recommendations
- If the user has no rating history, the system falls back to popular/highly rated movies

## Technical stack
- Programming: Python
- Database: MySQL
- ML / Modeling: SVD collaborative filtering
- Experiment tracking: MLflow
- Workflow orchestration: Airflow
- API: FastAPI
- Frontend: Streamlit
- Containerization: Docker Compose

## Future improvements
- Extend the recommendation logic with hybrid filtering approaches
- Improve cold-start handling with content-based features
- Add automated testing and monitoring for production scenarios
- Improve model evaluation with ranking metrics such as Precision@K or Recall@K
- Deploy the system to a cloud environment

## Notes
This project was developed as part of the DataScientest Machine Learning Engineering program and is presented here as a portfolio project focused on end-to-end ML system design, reproducibility, and deployment-oriented thinking.

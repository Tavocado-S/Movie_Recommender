from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def run(cmd, cwd=None):
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}")

def main():
    print("=== BOOTSTRAP: MOVIE RECOMMENDER DEMO SETUP ===")

    # 1. Generate dataset sample
    run('docker compose exec airflow-webserver bash -lc "cd /opt/airflow/repo && python src/data/make_dataset.py"', cwd=ROOT)

    # 2. Verify raw files
    ratings_path = ROOT / "data" / "raw" / "ml-20m" / "ratings.csv"
    movies_path = ROOT / "data" / "raw" / "ml-20m" / "movies.csv"
    if not ratings_path.exists():
        raise FileNotFoundError(f"Missing file: {ratings_path}")
    if not movies_path.exists():
        raise FileNotFoundError(f"Missing file: {movies_path}")
    print("✓ Raw dataset files found")

    # 3. Split ratings into incoming batches
    run(r'python .\src\data\split_ratings_into_batches.py', cwd=ROOT)

    # 4. Create schema
    run('docker compose exec airflow-webserver bash -lc "python /opt/airflow/repo/src/data/create_database_mysql.py --init-schema"', cwd=ROOT)

    # 5. Load movies table
    run('docker compose exec airflow-webserver bash -lc "python /opt/airflow/repo/src/data/create_database_mysql.py --load-movies /opt/airflow/repo/data/sample/movies_sample.csv"', cwd=ROOT)

    print("\n=== BOOTSTRAP COMPLETE ===")
    print("Next step: Trigger the Airflow DAG `retrain_on_new_batch` to ingest the first batch and train the model.")
    print("Open:")
    print("- FastAPI docs: http://localhost:8000/docs")
    print("- MLflow UI:    http://localhost:5001")
    print("- Airflow UI:   http://localhost:8080")
    print("- Streamlit UI: http://localhost:8501")

if __name__ == "__main__":
    main()
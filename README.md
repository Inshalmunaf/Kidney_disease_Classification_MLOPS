# Kidney_disease_Classification_MLOPS


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Inshalmunaf/Kidney_disease_Classification_MLOPS
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow Tracking with DagsHub 📊

This project uses [MLflow](https://mlflow.org/) for experiment tracking, integrated with [DagsHub](https://dagshub.com/) to host the MLflow server.

### Prerequisites

1.  **DagsHub Account:** Make sure you have a DagsHub account and have created a repository for this project.
2.  **Install `dagshub` library:** Ensure the library is installed in your environment:
    ```bash
    pip install dagshub
    ```

### Configuration using .env File 🔒

We use a .env file to securely manage DagsHub connection details (repository owner and name) without committing them to Git.

1) Create .env File: In the root directory of the project, create a file named .env.

2) Add Variables: Add your DagsHub repository details to the .env file:

3) Add .env to .gitignore: Ensure your .gitignore file includes the line .env to prevent accidentally committing your secrets.

Add the following Python code near the beginning of your evaluation script (e.g., in `04_model_evaluation.ipynb` or `model_evaluation_with_mlflow.py`), **before** any `mlflow` commands:

```python
import dagshub
import os
from dotenv import load_dotenv

load_dotenv()

REPO_OWNER = os.getenv('DAGSHUB_REPO_OWNER')
REPO_NAME = os.getenv('DAGSHUB_REPO_NAME')

dagshub.init(repo_owner= REPO_OWNER, repo_name= REPO_NAME, mlflow=True)
# ------------------------------------


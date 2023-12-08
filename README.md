the-impact-of-news-information-acquisitionn-and-cognitoin
==============================

We investigated whether the acquisition and cognition of new information impact university students' satisfaction with societal conditions, economic situations, and personal life, as well as the specific aspects through which such influence occurs. We provide guidance and fully replicable code to reproduce our research findings. Our data were sourced from the Chinese National Survey Data Archive's 2019 survey on the social attitudes of university students. After cleaning and filtering the data, we conducted Ordinary Least Squares (OLS) regression, revealing significant impacts of information news sources and interest in the news on various aspects of university students' satisfaction. Consequently, our findings demonstrate that the channels through which news is obtained do indeed influence the current satisfaction levels.
see [walk through](https://github.com/youchuanyi/the-Impact-of-News-Information-Acquisition-and-Cognition/blob/master/walkthrough.ipynb "walk through")

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Figures and tables
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.

    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── descriptive_data.py
    │   │   └── __init__.py
    



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Requirements
------------
First, make sure you navigate to the project directory.
```bash
cd the-impact-of-news-information-acquisitionn-and-cognitoin
```
Then, you can load the required environment variables in `requirements.txt` 
### Create and activate a virtual environment.
```bash
python -m venv .venv
source .venv/bin/activate
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
never forget to activate the environments whenever you work on the projects.

Data Cleaning
------------
We translated the Chinese version of the questionnaire into English, which can be found in `survey.md ` in the interim folder. By screening the questions in the questionnaire and selecting 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9' as our controlled variables, and 'Q13', 'Q14', 'Q15_A8' as our independent variables, we explored their effects on the three dependent variables'Q10', 'Q11', and 'Q12'.

**Load and Process Raw Data:**
```bash
python src/data/__init__.py load
```
**Save Cleaned Data:**
The cleaned data is saved in the data/processed directory.

Data Analysis
------------

**Ordinary Least Squares (OLS) Modeling:**
We utilized Ordinary Least Squares (OLS) regression to investigate the impact of three explanatory variables on three response variables. 
```bash
python models/regression_model.py 
```
**Ordered Logistic Regression for Robustness Checks:**
To ensure the robustness of our findings, we conducted robustness checks using Original Logistic Regression. The logistic regression scripts are available in the models/robustness.py directory:
```bash
python models/robustness.py
```

Results
------------
turn to [walkthrough](./walkthrough.ipynb) for results.

Docker
------------

**Dockerization:**

This project has been Dockerized for easy deployment and reproducibility. Follow the steps below to run the project using Docker.

**Prerequisites:**

Make sure you have [Docker](https://www.docker.com/get-started) installed on your machine.

### Build Docker Image
```bash
docker build -t the-impact-of-news-information-acquisition-and-cognition

```
### Run Docker Container
```bash
docker run -it the-impact-of-news-information-acquisition-and-cognition 

```



# COVID-19 cases in Spain
## Udacity nanodegree "Data scientist", project 2 ("Create a data dashboard")

### General data
Autor: Christoph Wagner
Date of publication: 16/05/2020

### Software used for the project

Software versions:
- Jupyter Notebook Server 6.0.3
- Python 3.8 (64 bit)

Python libraries used in the project:
- pandas
- plotly
- json
- flask

Javascript libraries used in the project:
- bootstrap
- jquery

### Motivation for the project
In this small project, I created a web app for displaying the COVID-19 related cases and fatalities in the regions of Spain between 02/03/2020 and 29/04/2020.
The data are part of the UNCOVER COVID-19 challenge from the Roche Data Science Coalition (downloaded from kaggle.com). 
The dataset has been preprocessed using a Jupyter notebook and then displayed in a web app using the Plotly and Bootstrap frameworks. 
The web app has been created using Flask and is published on the Heroku cloud platform using Gunicorn HTTP server.
Purpose of this project was self-training in web development (related to Data Science topics).

### Files in the repository
- README.md									README file 
- data_preparation.ipynb					Jupyter notebook for initial data preprocessing
- original_data					
	- covid19-spain-cases.csv				Downloaded COVID-19 dataset from kaggle.com (Original format)
	- covid19-spain-cases_transformed.csv	Transformed version of dataset
- webapp	
	- covid_spain_app.py					Python script for definition of web app
	- data									Data for webapp
	- wrangling_scripts/wrangle_data.py		Python script for creation of plotly diagrams
	- covid_spain_app
		- static							Images
		- templates							Webpage definition
	- routes.py								Routing definition and filling of web app with plotly graphs

URL to web app on Heroku:



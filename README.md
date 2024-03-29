# Sample size in healthcare NLP
This repository lists out the codes and queries used in conducting a simulation to make recommendations on sample sizes for training data used in healthcare NLP.
**This work is currently in progress and updates are being made to the queries and simulations based on reviewer feedback**

# Interactive Dashboard of Results:

[WORK IN PROGRESS - Streamlit app](https://jayachaturvedi-sample-size-in-healthcare-nlp-dashboard-poic0t.streamlit.app/)

[GOOGLE SHEETS APP](https://docs.google.com/spreadsheets/d/1_XssYdseh44vNAa-UqMp8rlJNVMib-7KTbtAfmc47xE/edit?usp=sharing)

# Details of files

*SQL_queries*: 
This file has all the SQL queries used to extract the data from MIMIC database. The hypertension (HTN) data was extracted from a local instance of the MIMIC-III database. The diabetes data was extracted from an instance of MIMIC-III on Google Cloud's BigQuery service.

*creating_dataset_for_classifier.ipynb*:
This python file has code for combining the HTN and non-HTN data, as well as diabetes and non-diabetes data, for final use in the building of classifier models.

*demographic_distributions.ipynb*:
This python file contains code to generate and analyse demographic distributions amongst the data collected.

*samplesize_build_classifiers_incl_bert.ipynb*:
This python file contains code used to generate the different classifiers and the different variations in parameters, like sample size and class proportions. This includes both BERT and non-BERT classifiers. Please bear in mind that this notebook is a bit messy, but I have tried to somewhat clean it up so it is decent-ish for now!

*results folder*:
This folder contains results for all sample sizes and class proportions.

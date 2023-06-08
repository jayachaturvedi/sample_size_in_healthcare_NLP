#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:49:54 2023

@author: jayachaturvedi
"""

import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Define the classifier performance results
classifier_scores = {
    'Decision Tree': 0.8,
    'KNN': 0.9,
    # Add more classifiers and their scores here
}

# Define the sample size options
sample_sizes = [500, 1000, 2000]

# Define the class proportion options
class_proportions = {
    '50/50': (0.5, 0.5),
    '60/40': (0.6, 0.4),
    '70/30': (0.7, 0.3),
    # Add more class proportions here
}

def generate_line_graph(sample_size, class_proportion):
    # Perform any necessary calculations or data processing here
    # In this example, we'll simply retrieve the score for each classifier
    
    # Retrieve the class proportions
    class_proportion_label = f"{class_proportion[0]*100}/{class_proportion[1]*100}"
    
    # Retrieve the scores for each classifier
    classifier_labels = []
    classifier_scores_values = []
    for classifier, score in classifier_scores.items():
        classifier_labels.append(classifier)
        classifier_scores_values.append(score)
    
    # Generate the line graph
    plt.plot(classifier_labels, classifier_scores_values, marker='o')
    plt.xlabel('Classifier')
    plt.ylabel('F1-Score (weighted average)')
    plt.title(f'Performance Results for Sample Size: {sample_size}, Class Proportion: {class_proportion_label}')
    plt.xticks(rotation=45)
    plt.ylim(0, 1)  # Set the y-axis limits
    
    # Display the graph in Streamlit
    st.pyplot()

# Create the Streamlit app
st.title('Interactive Dashboard')
sample_size = st.selectbox('Select Sample Size:', sample_sizes)
class_proportion = st.selectbox('Select Class Proportion:', list(class_proportions.keys()))

# Retrieve the class proportion values based on the selected label
selected_class_proportion = class_proportions[class_proportion]

# Generate and display the line graph based on the selected options
generate_line_graph(sample_size, selected_class_proportion)

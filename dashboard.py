#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:49:54 2023

@author: jayachaturvedi
"""

import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


classifier_scores_by_options = {
    '200_10/90': {'LR': '0.91', 'NB': '0.91', 'RF': '0.91', 'DT': '0.88', 'SVC': '0.91', 'lSVC': '0.91', 'SGD': '0.91', 'KNN': '0.91'}, 
    '200_20/80': {'LR': '0.79', 'NB': '0.72', 'RF': '0.73', 'DT': '0.82', 'SVC': '0.73', 'lSVC': '0.79', 'SGD': '0.79', 'KNN': '0.84'}, 
    '200_30/70': {'LR': '0.65', 'NB': '0.73', 'RF': '0.71', 'DT': '0.55', 'SVC': '0.73', 'lSVC': '0.64', 'SGD': '0.65', 'KNN': '0.67'}, 
    '200_40/60': {'LR': '0.58', 'NB': '0.61', 'RF': '0.40', 'DT': '0.45', 'SVC': '0.56', 'lSVC': '0.58', 'SGD': '0.62', 'KNN': '0.54'}, 
    '200_50/50': {'LR': '0.53', 'NB': '0.62', 'RF': '0.35', 'DT': '0.53', 'SVC': '0.48', 'lSVC': '0.49', 'SGD': '0.59', 'KNN': '0.57'}, 
    '400_10/90': {'LR': '0.89', 'NB': '0.88', 'RF': '0.89', 'DT': '0.89', 'SVC': '0.89', 'lSVC': '0.88', 'SGD': '0.87', 'KNN': '0.90'}, 
    '400_20/80': {'LR': '0.73', 'NB': '0.73', 'RF': '0.73', 'DT': '0.73', 'SVC': '0.73', 'lSVC': '0.73', 'SGD': '0.73', 'KNN': '0.73'}, 
    '400_30/70': {'LR': '0.74', 'NB': '0.73', 'RF': '0.67', 'DT': '0.74', 'SVC': '0.73', 'lSVC': '0.73', 'SGD': '0.73', 'KNN': '0.68'}, 
    '400_40/60': {'LR': '0.62', 'NB': '0.62', 'RF': '0.56', 'DT': '0.50', 'SVC': '0.64', 'lSVC': '0.64', 'SGD': '0.64', 'KNN': '0.56'}, 
    '400_50/50': {'LR': '0.58', 'NB': '0.65', 'RF': '0.65', 'DT': '0.49', 'SVC': '0.65', 'lSVC': '0.58', 'SGD': '0.62', 'KNN': '0.65'}, 
    '500_10/90': {'LR': '0.93', 'NB': '0.94', 'RF': '0.93', 'DT': '0.88', 'SVC': '0.93', 'lSVC': '0.93', 'SGD': '0.92', 'KNN': '0.94'}, 
    '500_20/80': {'LR': '0.85', 'NB': '0.74', 'RF': '0.71', 'DT': '0.72', 'SVC': '0.79', 'lSVC': '0.86', 'SGD': '0.83', 'KNN': '0.85'}, 
    '500_30/70': {'LR': '0.76', 'NB': '0.74', 'RF': '0.72', 'DT': '0.72', 'SVC': '0.75', 'lSVC': '0.76', 'SGD': '0.72', 'KNN': '0.73'}, 
    '500_40/60': {'LR': '0.71', 'NB': '0.67', 'RF': '0.58', 'DT': '0.66', 'SVC': '0.69', 'lSVC': '0.70', 'SGD': '0.67', 'KNN': '0.66'}, 
    '500_50/50': {'LR': '0.69', 'NB': '0.68', 'RF': '0.63', 'DT': '0.72', 'SVC': '0.67', 'lSVC': '0.65', 'SGD': '0.64', 'KNN': '0.62'}, 
    '600_10/90': {'LR': '0.80', 'NB': '0.80', 'RF': '0.80', 'DT': '0.78', 'SVC': '0.80', 'lSVC': '0.80', 'SGD': '0.80', 'KNN': '0.82'}, 
    '600_20/80': {'LR': '0.81', 'NB': '0.69', 'RF': '0.69', 'DT': '0.75', 'SVC': '0.81', 'lSVC': '0.82', 'SGD': '0.84', 'KNN': '0.82'}, 
    '600_30/70': {'LR': '0.76', 'NB': '0.72', 'RF': '0.62', 'DT': '0.77', 'SVC': '0.76', 'lSVC': '0.76', 'SGD': '0.74', 'KNN': '0.79'}, 
    '600_40/60': {'LR': '0.64', 'NB': '0.62', 'RF': '0.57', 'DT': '0.55', 'SVC': '0.63', 'lSVC': '0.63', 'SGD': '0.64', 'KNN': '0.60'}, 
    '600_50/50': {'LR': '0.69', 'NB': '0.64', 'RF': '0.64', 'DT': '0.66', 'SVC': '0.63', 'lSVC': '0.67', 'SGD': '0.64', 'KNN': '0.69'}, 
    '800_10/90': {'LR': '0.92', 'NB': '0.86', 'RF': '0.86', 'DT': '0.90', 'SVC': '0.88', 'lSVC': '0.92', 'SGD': '0.90', 'KNN': '0.88'}, 
    '800_20/80': {'LR': '0.84', 'NB': '0.81', 'RF': '0.80', 'DT': '0.80', 'SVC': '0.83', 'lSVC': '0.84', 'SGD': '0.80', 'KNN': '0.82'}, 
    '800_30/70': {'LR': '0.77', 'NB': '0.77', 'RF': '0.71', 'DT': '0.76', 'SVC': '0.77', 'lSVC': '0.78', 'SGD': '0.76', 'KNN': '0.79'}, 
    '800_40/60': {'LR': '0.65', 'NB': '0.62', 'RF': '0.58', 'DT': '0.63', 'SVC': '0.64', 'lSVC': '0.66', 'SGD': '0.65', 'KNN': '0.64'}, 
    '800_50/50': {'LR': '0.69', 'NB': '0.72', 'RF': '0.70', 'DT': '0.66', 'SVC': '0.72', 'lSVC': '0.65', 'SGD': '0.58', 'KNN': '0.64'}, 
    '1000_10/90': {'LR': '0.82', 'NB': '0.83', 'RF': '0.83', 'DT': '0.79', 'SVC': '0.83', 'lSVC': '0.84', 'SGD': '0.83', 'KNN': '0.86'}, 
    '1000_20/80': {'LR': '0.82', 'NB': '0.77', 'RF': '0.74', 'DT': '0.76', 'SVC': '0.79', 'lSVC': '0.82', 'SGD': '0.83', 'KNN': '0.81'}, 
    '1000_30/70': {'LR': '0.70', 'NB': '0.71', 'RF': '0.66', 'DT': '0.64', 'SVC': '0.72', 'lSVC': '0.70', 'SGD': '0.67', 'KNN': '0.67'}, 
    '1000_40/60': {'LR': '0.66', 'NB': '0.59', 'RF': '0.58', 'DT': '0.66', 'SVC': '0.59', 'lSVC': '0.65', 'SGD': '0.67', 'KNN': '0.59'}, 
    '1000_50/50': {'LR': '0.67', 'NB': '0.71', 'RF': '0.68', 'DT': '0.59', 'SVC': '0.68', 'lSVC': '0.66', 'SGD': '0.65', 'KNN': '0.67'}, 
    '2000_10/90': {'LR': '0.88', 'NB': '0.85', 'RF': '0.84', 'DT': '0.84', 'SVC': '0.87', 'lSVC': '0.88', 'SGD': '0.88', 'KNN': '0.88'}, 
    '2000_20/80': {'LR': '0.83', 'NB': '0.80', 'RF': '0.73', 'DT': '0.77', 'SVC': '0.82', 'lSVC': '0.83', 'SGD': '0.84', 'KNN': '0.82'}, 
    '2000_30/70': {'LR': '0.76', 'NB': '0.76', 'RF': '0.72', 'DT': '0.74', 'SVC': '0.78', 'lSVC': '0.76', 'SGD': '0.76', 'KNN': '0.74'}, 
    '2000_40/60': {'LR': '0.72', 'NB': '0.70', 'RF': '0.64', 'DT': '0.64', 'SVC': '0.70', 'lSVC': '0.73', 'SGD': '0.72', 'KNN': '0.72'}, 
    '2000_50/50': {'LR': '0.67', 'NB': '0.62', 'RF': '0.61', 'DT': '0.66', 'SVC': '0.66', 'lSVC': '0.66', 'SGD': '0.64', 'KNN': '0.65'}, 
    '3000_10/90': {'LR': '0.91', 'NB': '0.86', 'RF': '0.86', 'DT': '0.85', 'SVC': '0.90', 'lSVC': '0.91', 'SGD': '0.89', 'KNN': '0.90'}, 
    '3000_20/80': {'LR': '0.81', 'NB': '0.78', 'RF': '0.75', 'DT': '0.74', 'SVC': '0.79', 'lSVC': '0.81', 'SGD': '0.80', 'KNN': '0.77'}, 
    '3000_30/70': {'LR': '0.77', 'NB': '0.72', 'RF': '0.66', 'DT': '0.71', 'SVC': '0.77', 'lSVC': '0.78', 'SGD': '0.77', 'KNN': '0.74'}, 
    '3000_40/60': {'LR': '0.68', 'NB': '0.64', 'RF': '0.59', 'DT': '0.64', 'SVC': '0.69', 'lSVC': '0.68', 'SGD': '0.68', 'KNN': '0.68'}, 
    '3000_50/50': {'LR': '0.69', 'NB': '0.63', 'RF': '0.61', 'DT': '0.64', 'SVC': '0.71', 'lSVC': '0.69', 'SGD': '0.66', 'KNN': '0.66'}, 
    '4000_10/90': {'LR': '0.89', 'NB': '0.84', 'RF': '0.84', 'DT': '0.85', 'SVC': '0.88', 'lSVC': '0.89', 'SGD': '0.88', 'KNN': '0.85'}, 
    '4000_20/80': {'LR': '0.81', 'NB': '0.80', 'RF': '0.73', 'DT': '0.76', 'SVC': '0.81', 'lSVC': '0.81', 'SGD': '0.79', 'KNN': '0.81'}, 
    '4000_30/70': {'LR': '0.77', 'NB': '0.73', 'RF': '0.65', 'DT': '0.70', 'SVC': '0.78', 'lSVC': '0.78', 'SGD': '0.76', 'KNN': '0.74'}, 
    '4000_40/60': {'LR': '0.71', 'NB': '0.62', 'RF': '0.55', 'DT': '0.67', 'SVC': '0.68', 'lSVC': '0.71', 'SGD': '0.70', 'KNN': '0.66'}, 
    '4000_50/50': {'LR': '0.70', 'NB': '0.66', 'RF': '0.64', 'DT': '0.68', 'SVC': '0.70', 'lSVC': '0.69', 'SGD': '0.69', 'KNN': '0.69'}, 
    '5000_10/90': {'LR': '0.91', 'NB': '0.89', 'RF': '0.87', 'DT': '0.87', 'SVC': '0.91', 'lSVC': '0.91', 'SGD': '0.90', 'KNN': '0.90'}, 
    '5000_20/80': {'LR': '0.83', 'NB': '0.81', 'RF': '0.76', 'DT': '0.78', 'SVC': '0.83', 'lSVC': '0.82', 'SGD': '0.82', 'KNN': '0.81'}, 
    '5000_30/70': {'LR': '0.78', 'NB': '0.75', 'RF': '0.67', 'DT': '0.73', 'SVC': '0.77', 'lSVC': '0.77', 'SGD': '0.75', 'KNN': '0.76'}, 
    '5000_40/60': {'LR': '0.75', 'NB': '0.72', 'RF': '0.63', 'DT': '0.72', 'SVC': '0.76', 'lSVC': '0.74', 'SGD': '0.74', 'KNN': '0.71'}, 
    '5000_50/50': {'LR': '0.73', 'NB': '0.69', 'RF': '0.66', 'DT': '0.69', 'SVC': '0.76', 'lSVC': '0.73', 'SGD': '0.72', 'KNN': '0.70'}
    # Add more combinations of sample size and class proportion here
}



sample_sizes = [200, 400, 600, 800, 1000, 2000, 3000, 4000, 5000]
class_proportions = {
    '50/50': (0.5, 0.5),
    '40/60': (0.4, 0.6),
    '30/70': (0.3, 0.7),
    '20/80': (0.2, 0.8),
    '10/90': (0.1, 0.9)
    # Add more class proportions here
}

#for key in classifier_scores_by_options.keys():
    #parts = key.split('_')
    #sample_sizes.append(parts[0])
    #class_proportions.append(parts[1])
    


def generate_line_graph(sample_size, class_proportion):
    # Retrieve the class proportion label
    class_proportion_label = f"{int(class_proportion[0]*100)}/{int(class_proportion[1]*100)}"
    
    # Generate a unique key for the selected options
    options_key = f"{sample_size}_{class_proportion_label}"
    
    # Retrieve the scores for the selected options
    classifier_scores = classifier_scores_by_options[options_key]
    
    # Retrieve the classifier labels and scores
    classifier_labels = list(classifier_scores.keys())
    classifier_scores_values = list(classifier_scores.values())
    
    # Generate the line graph
    plt.ylim(0.20, 0.90)  # Set the y-axis limits
    plt.plot(classifier_labels, classifier_scores_values, marker='o')
    plt.xlabel('Classifier')
    plt.ylabel('F1-Score (weighted average)')
    plt.title(f'Performance Results for Sample Size: {sample_size}, Class Proportion: {class_proportion_label}')
    plt.xticks(rotation=45)
   
    
    # Display the graph in Streamlit
    #st.pyplot()
    st.pyplot(plt.gcf())
    
    
    



st.title('Interactive Dashboard \nHypertension Diagnosis')   
# Add text using st.write()
st.write("Please select a sample size and class proportion below to see results for all classifiers.") 
sample_size = st.selectbox('Select Sample Size:', sample_sizes)
class_proportion = st.selectbox('Select Class Proportion:', class_proportions)




# Retrieve the class proportion values based on the selected label
selected_class_proportion = class_proportions[class_proportion]

# Generate and display the line graph based on the selected options
generate_line_graph(sample_size, selected_class_proportion)







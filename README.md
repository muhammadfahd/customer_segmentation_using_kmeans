# 🛍️ Customer Segmentation using K-Means Clustering
This project is a customer segmentation analysis using K-means clustering. The goal is to divide customers into distinct groups based on their annual income and spending score to help businesses make targeted marketing decisions.
This repo contain following 
* [Unsuervised Learning K-means Clustering in Detail](./unsupervised%20learning%20kmeans%20clustering.md)
* Implementing k-means clustering using 
  * Built from scratch 
  * using scikit library
* [Building a project with customer segmentation](./customer_Segmentation.ipynb)
* Streamit Lit App
---
## 🧑‍💻 K-Means Clustering Algorithm
K-means clustering is an unsupervised machine learning algorithm used to partition data into K distinct clusters. The objective of the algorithm is to minimize the within-cluster variance, so the points within each cluster are as similar as possible.
For detailed checkout [here](./unsupervised%20learning%20kmeans%20clustering.md)

--- 

## 🧑‍💻 Implementation
1. **K-Means Clustering from Scratch**
We start by implementing K-means clustering from scratch to understand the internal workings of the algorithm [here](./k_measn_from_scratch.py)
<br>
2. **Using Built-in Library (Scikit-Learn)**
To simplify the clustering process, we also use the built-in KMeans algorithm from Scikit-Learn [here](./k_means_using_scikit.py)

---

#  Mini Project - Customer Segmenation 
In this project, we use K-means clustering to perform customer segmentation. The dataset contains 200 rows and 5 columns representing customer data, including:

* **Annual Income (in thousands)**: Customer's annual income in thousands of dollars.
* **Spending Score (1 to 100)** :A score assigned to customers based on their spending behavior.
* **Age** : Customer’s age.
* **Gender** : Gender of the customer (optional for segmentation).
* **Customer ID** :  Unique identifier for each customer.

📊 **Steps Performed**:
* Exploratory Data Analysis (EDA)
* Visualization of clusters
* K-means clustering implementation
* Model Saving for prediction

---
## 🚀 Streamlit UI
We created a Streamlit app to provide an interactive user interface for predicting customer clusters. Users can input their annual income and spending score, and the app will display:

* The predicted cluster
* The cluster meaning (e.g., high spenders, low spenders)
* Visualizations of the cluster distribution
* Recommended actions based on the cluster

---
## 🛠️ Technologies Used
**Python**: Programming language for implementing machine learning algorithms.
**Scikit-Learn**: Library for machine learning models (K-means clustering).
**Streamlit**: Framework to create the interactive web app.
**Matplotlib**: Library for visualizations.
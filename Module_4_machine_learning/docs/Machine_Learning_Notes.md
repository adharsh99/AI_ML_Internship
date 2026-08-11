# Machine Learning Notes

## Module 4 - Machine Learning Fundamentals

## 1. What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions without being explicitly programmed for every task.

Machine Learning is commonly used for:

- Prediction
- Classification
- Recommendation
- Fraud detection
- Image recognition
- Sales forecasting
- House price prediction

---

## 2. Types of Machine Learning

There are three main types of Machine Learning:

### 1. Supervised Learning

The model learns from data where the correct output is already known.

Examples:

- House price prediction
- Student score prediction
- Email spam classification

### 2. Unsupervised Learning

The model finds patterns or groups in data without predefined output labels.

Examples:

- Customer segmentation
- Clustering
- Pattern discovery

### 3. Reinforcement Learning

The model learns by interacting with an environment and receiving rewards or penalties.

Examples:

- Game-playing AI
- Robotics
- Autonomous systems

---

## 3. Supervised Learning

Our House Price Prediction project uses Supervised Learning.

The dataset contains:

### Input Features

- Area
- Bedrooms
- Bathrooms
- Age

### Output

- House Price

The model learns the relationship between the input features and the known house prices.

---

## 4. Regression

Regression is a Machine Learning technique used to predict continuous numerical values.

Examples:

- House price prediction
- Salary prediction
- Sales prediction
- Temperature prediction

House Price Prediction is a regression problem because the output is a numerical price.

---

## 5. Classification

Classification is used when the output belongs to a category or class.

Examples:

- Spam or Not Spam
- Pass or Fail
- Disease or No Disease
- Setosa, Versicolor, or Virginica

Classification and regression are both common supervised learning techniques.

---

## 6. Machine Learning Workflow

A basic Machine Learning workflow consists of:

1. Collect the dataset
2. Understand the dataset
3. Clean the data
4. Explore the data
5. Visualize the data
6. Select features
7. Select target
8. Split the data
9. Create the model
10. Train the model
11. Make predictions
12. Evaluate the model
13. Make predictions on new data

---

## 7. Dataset

For the House Price Prediction project, the dataset contains information about houses.

The main columns are:

| Column | Meaning |
|---|---|
| Area | House size in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Age | Age of the house in years |
| Price | House price |

---

## 8. Features

Features are the input variables given to the Machine Learning model.

In our project:

```text
Area
Bedrooms
Bathrooms
Age
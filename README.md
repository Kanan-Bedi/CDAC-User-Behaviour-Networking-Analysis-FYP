# CDAC-User-Behaviour-Networking-Analysis-FYP


## Project Overview:
The project focuses on developing an intelligent system for detecting insider threats by analyzing user behavior within a network. Insider threats pose significant risks as they involve individuals with privileged access to sensitive information. The project addresses the challenge of identifying malicious activities within highly imbalanced datasets, a common issue in current machine learning approaches.

## Objectives:
Insider Threat Detection: Develop a machine learning model that detects anomalies in user behavior indicative of potential insider threats using the CERT insider threat dataset.
Model Performance Evaluation: Conduct a comparative analysis of different models, evaluate their performance on the original and augmented CERT dataset.
Research Analysis: Explore existing trends, challenges, and future research directions in the insider threat detection domain.

## Dataset:
The project utilizes the CERT insider threat dataset, which simulates various insider threat scenarios. The dataset includes multiple files such as psychometric data, email activity, device usage, logon events, and more, providing comprehensive information on user activities across different environments.

## Methodology:
Behavioral Fingerprinting: Develop algorithms to create unique fingerprints for user sessions based on static (e.g., user ID) and dynamic (e.g., session duration) attributes.
Anomaly Detection: Implement machine learning algorithms (e.g., K-Means, DBSCAN) to detect deviations from normal user behavior in real-time.
System Integration: Seamlessly integrate the detection system with existing security infrastructure (e.g., SIEM, FIM) for enhanced security monitoring.

## Development & Implementation:
Data Collection: Collect data from network traffic, system logs, and application usage.
Preprocessing: Normalize data, handle missing values, and extract behavioral features using Python, Pandas, and Scikit-learn.
Model Training: Train deep learning models (e.g., LSTM-CNN, Bidirectional LSTM-CNN) using TensorFlow or Keras, followed by validation and hyperparameter tuning.
Deployment: Deploy the system using Docker and Kubernetes for scalability.

## Testing & Optimization:
The system's effectiveness will be evaluated using various metrics, such as Precision, Recall, F1-Score for the deep learning models, and Silhouette Score and Davies-Bouldin Index for clustering algorithms.

## Data Flow and Model Lifecycle
![Project Workflow](https://github.com/Kanan-Bedi/CDAC-User-Behaviour-Networking-Analysis-FYP/blob/main/MlOps%20Workflow.jpeg?raw=true)

- **Data flows**: From Azure Blob to preprocessing pipelines where tokenization (for BERT/RoBERTa) and scaling (for traditional ML) are applied.
- **Model training**: Includes supervised, unsupervised, deep learning, and transfer learning models, with real-time monitoring.
- **Continuous monitoring**: Involves logging and alerting for model drift and performance degradation.
- **Automated retraining and redeployment**: Triggered when the performance drops below a certain threshold.

## Project Outcome:
The successful implementation of this project will result in a robust User Behavior Analytics system capable of detecting insider threats, with potential scalability for larger environments and integration with advanced visual analytics tools.

 ## Conclusion:
This project aims to enhance network security by using advanced machine learning techniques to monitor and analyze user behavior, adding an additional layer of protection against insider threats. The system is designed to be scalable, accurate, and integrative, with future prospects for further refinement of anomaly detection algorithms.

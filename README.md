# Kubernetes Streamlit Dashboard

This project demonstrates the deployment of a Python-based Streamlit dashboard on a Kubernetes cluster using **Minikube** inside **WSL2**.  
It simulates a production-style setup — with containerized application, declarative manifests, and a service to expose the app — but runs locally for learning and portfolio purposes.

## Tech Stack
- **Python 3.11** — App development
- **Streamlit** — Web application framework
- **pandas**, **numpy**, **matplotlib** — Data manipulation and visualization
- **Docker** — Containerization
- **Kubernetes** — Container orchestration
- **Minikube** — Local Kubernetes cluster
- **WSL2** — Linux environment on Windows

## Features
- Deployment defined via Kubernetes YAML manifests
- NodePort service for external access to the dashboard
- Interactive dashboard with KPI metrics, chart, and user-controlled parameters
- Runs entirely inside WSL2 for a production-like workflow# streamlit-dashboard-k8s
Deploying a dashboard app to Kubernetes

## Live Demo Screenshot

![Dashboard Screenshot](screenshot.png)

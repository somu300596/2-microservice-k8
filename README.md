# Microservices Application with Docker, Kubernetes, Helm, ArgoCD, and Istio

## Table of Contents
- [Introduction](#introduction)
- [Architecture Overview](#architecture-overview)
- [Pre-requisites](#pre-requisites)
- [Setup Instructions](#setup-instructions)
  - [1. Application Setup](#1-application-setup)
  - [2. Docker Setup](#2-docker-setup)
  - [3. Kubernetes Setup](#3-kubernetes-setup)
  - [4. Helm Deployment](#4-helm-deployment)
  - [5. ArgoCD Setup](#5-argocd-setup)
  - [6. Istio Service Mesh Setup](#6-istio-service-mesh-setup)
---

## Introduction

This repository demonstrates a complete microservices-based application deployed using Docker, Kubernetes, Helm, ArgoCD for continuous delivery, and Istio for service mesh and observability. The project contains two microservices:
- `order-service`: Responsible for handling order-related operations.
- `user-service`: Provides user-related data and services.

This project highlights modern DevOps practices including containerization, orchestration, CI/CD automation, and service observability.

---

## Architecture Overview

1. **Microservices** (`order-service` and `user-service`) interact via HTTP.
2. **Docker** is used to containerize the services.
3. **Kubernetes** is used to manage deployments and scaling.
4. **Helm** handles the deployment of Kubernetes manifests.
5. **ArgoCD** is used for continuous delivery and GitOps workflows.
6. **Istio** is added to provide service mesh features such as observability, traffic management, and security.

---

## Pre-requisites

Ensure you have the following tools installed before starting:

1. **Docker** (for building images): [Install Docker](https://docs.docker.com/get-docker/)
2. **Minikube** or a Kubernetes cluster: [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
3. **Helm** (for deploying charts): [Install Helm](https://helm.sh/docs/intro/install/)
4. **ArgoCD** (for CI/CD): [Install ArgoCD](https://argo-cd.readthedocs.io/en/stable/getting_started/)
5. **Istio** (for service mesh): [Istio Setup Guide](https://istio.io/latest/docs/setup/)

---

## Setup Instructions

### 1. Application Setup

Clone the repository and navigate to the root directory:

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Docker Setup
Each service has its own Dockerfile for containerization.
1. Build the Docker images:

    Navigate to each service directory and build the Docker images:
    ```bash
    cd order-service
    docker build -t <username>/order-service:latest .
    cd ../user-service
    docker build -t <username>/user-service:latest .
    ```
2. Push the images to your Docker registry (replace <username> with your    Docker Hub username or your private registry):
    ```bash
    docker push <username>/order-service:latest
    docker push <username>/user-service:latest
    ```
3. Verify if the images are in the public repository
4. Run the Docker images locally to test them before deploying to Kubernetes:
    ```bash
    docker run -d -p 5001:5001 --name order-service <username>/order-service:latest
    docker run -d -p 5000:5000 --name user-service <username>/  user-service:latest
    ```
Now you have Docker images for both services ready for deployment.

### 3. Kubernetes Setup

1. Start **minikube**
    ```bash
    minikube start
    ```
2. Deploy the mainfest file under the user-service and order-service folder
    ```bash
    kubectl apply -f user-service/mainfest.yml
    kubectl apply -f order-service/mainfest.yml
    ```
3. Verify is the related pods are present.

### 4. Helm Setup

1. Make sure Helm is installed.
2. Instead of doing the k8 manually, we can have them in form of templates or helm charts.
3. To deploy them, you can execute the below commands:
    ```bash
    helm install user-service .\user-service-helm
    helm install order-service .\order-service-helm
    ```

### 5. ARGOCD Setup

#### Install ArgoCD

If you haven't installed ArgoCD yet, follow these steps to set it up on your Kubernetes cluster:

1. **Install ArgoCD** using the following command:

   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

2. **Access the ArgoCD Server**

    Expose the ArgoCD API server using a LoadBalancer or NodePort. For testing, you can use the following command to expose it via a NodePort:

    ```bash
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```
    You can now access the ArgoCD UI at http://localhost:8080.
    
3. **Get the Initial Admin Password**

    To retrieve the initial admin password, use the following command:

    ```bash
    kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
    ```
4. **Login to ArgoCD**

    1. Open your browser and navigate to http://localhost:8080.
    2. Log in using the username admin and the password retrieved in the previous step.

5. **Add Your Git Repository**
    After logging in, add your Git repository containing the Kubernetes manifests for your applications:

    1. Go to Settings > Repositories > Connect Repo using HTTPS.
    2. Enter the repository URL and credentials if needed.

6. **Create an Application**

    1. Click on New App in the ArgoCD UI.

    2. Fill in the application details:

        1. Application Name: (e.g., order-service, user-service)
        2. Project: Default
        3. Repository URL: Your Git repository URL
        4. Revision: HEAD
        5. Path: The path to the application manifests in the repository
        6. Cluster: https://kubernetes.default.svc
        7. Namespace: The namespace where you want to deploy the application

        Click Create to set up the application.

7. **Sync the Application**
    Once the application is created, click on it in the ArgoCD UI.
    Click on the Sync button to deploy the application to your Kubernetes   cluster.

### 6. Istio Service Mesh Setup

#### Install Istio

1. Install Istio on your Minikube cluster using the following command:

   ```bash
   minikube addons enable istio
   ```
2. Verify Istio installation by checking the pods in the istio-system       namespace:

    ```bash
    kubectl get pods -n istio-system
    ```

#### Enable Kiali
Enable the Kiali add-on to monitor the Istio service mesh and verify:

    minikube addons enable istio
    kubectl get pods -n istio-system

#### Access Kiali Dashboard
Access the Kiali Dashboard using port forwarding:

    kubectl port-forward svc/kiali -n istio-system 20001:20001
    
Open your browser and navigate to http://localhost:20001 to access the Kiali dashboard.

Navigate to the Kiali dashboard and check for services, traffic flows, and metrics.

Troubleshoot any issues using the visualizations provided by Kiali.


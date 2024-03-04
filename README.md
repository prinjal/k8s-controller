# Kubernetes Pod Event Controller

This Python-based Kubernetes controller listens for pod events across all namespaces in a Kubernetes cluster and prints a simple message for each event. It's designed as an example to demonstrate how to interact with the Kubernetes API using Python.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or newer
- pip (Python package installer)
- Access to a Kubernetes cluster (Minikube, kind, or any cloud-based Kubernetes service)
- `kubectl` command-line tool (for testing purposes)

## Installation

Follow these steps to set up the project environment:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/kubernetes-pod-event-controller.git
    cd kubernetes-pod-event-controller
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Ensure your `kubectl` is configured to interact with your Kubernetes cluster. For Minikube, simply start your cluster with `minikube start`, and `kubectl` will automatically be configured to use it.

## Running the Controller

To run the controller, execute:

```bash
python controller.py
```

## Testing

To test the controller, you can use `kubectl` to create, update, and delete pods in your cluster. Execute the following commands in your terminal:

```bash
# Create a Pod
kubectl run test-pod --image=nginx --restart=Never

# Delete the Pod
kubectl delete pod test-pod
```


### Notes for Customization:

- **Repository URL**: Replace `https://github.com/yourusername/kubernetes-pod-event-controller.git` with the actual URL of your GitHub repository.
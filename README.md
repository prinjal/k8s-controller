# Kubernetes Pod Event Controller

This Python-based Kubernetes controller listens for pod events across all namespaces in a Kubernetes cluster and prints a simple message for each event. It's designed as an example to demonstrate how to interact with the Kubernetes API using Python.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or newer
- pip (Python package installer)
- Access to a Kubernetes cluster (Minikube, kind, or any cloud-based Kubernetes service)
- `kubectl` command-line tool (for testing purposes)


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
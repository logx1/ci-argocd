#!/bin/bash
k3d cluster delete mycluster
k3d cluster create mycluster --servers 1 --agents 1 --port 8000:8000@loadbalancer
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

kubectl create namespace argocd
kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443

#!/bin/bash
# Lab 03 – Safe Minikube Image Load Script
# Author: le3arn2code
# Purpose: Load large Docker images into Minikube safely (low-RAM friendly)

IMAGE_NAME="mnist_model:latest"
TAR_NAME="mnist_model.tar"
REQUIRED_RAM_MB=6000

echo "🔍 Checking available memory..."
AVAILABLE_MB=$(free -m | awk '/Mem:/ {print $2}')
echo "🧠 System RAM detected: ${AVAILABLE_MB} MB"

if [ "$AVAILABLE_MB" -lt "$REQUIRED_RAM_MB" ]; then
  echo "⚠️ Low memory (<6GB). Using safe two-step method."
  echo "🧹 Cleaning old Minikube instance..."
  minikube stop >/dev/null 2>&1
  minikube delete >/dev/null 2>&1

  echo "🚀 Starting lightweight Minikube..."
  minikube start --memory=2500mb

  echo "💾 Saving Docker image locally..."
  sudo docker save "$IMAGE_NAME" -o "$TAR_NAME"

  echo "📦 Loading image into Minikube..."
  minikube image load "$TAR_NAME"

  echo "✅ Verification inside Minikube:"
  minikube image ls | grep mnist_model
else
  echo "✅ Sufficient memory available. Using direct image load."
  minikube image load "$IMAGE_NAME"
fi

echo "🎯 Completed: Safe Minikube Image Load executed successfully."

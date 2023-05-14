#!/bin/bash

# Default URL
model_url="https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin"

# Default uninstall option
uninstall=false

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --custom_model_url) model_url="$2"; shift ;;
        --uninstall) uninstall=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [ "$uninstall" = true ] ; then
    echo "Uninstalling..."
    rm -rf LocalAI
    rm -rf Auto-GPT
    exit 0
fi

# Check if the directory exists, if not clone the repository
if [ ! -d "LocalAI" ]; then
  git clone https://github.com/go-skynet/LocalAI
fi

cd LocalAI
make build
wget $model_url -O models/gpt-3.5-turbo
cd ..

# Check if on macOS, if so install extra prerequisites using brew
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install cmake go
fi

cp .env.template Auto-GPT/.env

# Check if the directory exists, if not clone the repository
if [ ! -d "Auto-GPT" ]; then
  git clone -b stable https://github.com/Significant-Gravitas/Auto-GPT.git
fi

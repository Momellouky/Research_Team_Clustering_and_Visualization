#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: Pip is not installed. Please install pip before proceeding."
    exit 1
fi

# Install dependencies
pip install numpy pandas nltk gensim gpt4all scikit-learn matplotlib plotly umap bokeh bertopic sentence-transformers hdbscan


# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Done. Dependencies installed successfully."
else
    echo "Error: Failed to install dependencies."
fi

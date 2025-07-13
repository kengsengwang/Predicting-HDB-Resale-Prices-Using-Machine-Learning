#!/bin/bash

# === Define root project folder ===
ROOT_DIR="Predicting-HDB-Resale-Prices-Using-Machine-Learning"
cd "$HOME/Documents/$ROOT_DIR" || exit

echo "✅ Setting up directory structure..."

# === Create required folders ===
mkdir -p .github
mkdir -p src

# === Move files to src/ ===
mv src/*.py src/ 2>/dev/null  # move Python files if not already in place

# === Move Jupyter Notebook ===
mv eda.ipynb . 2>/dev/null

# === Create empty files if they don't exist ===
touch README.md requirements.txt run.sh

# === Summary ===
echo "✅ Project structure created:"
echo "├── .github/"
echo "├── src/ (contains Python ML pipeline files)"
echo "├── README.md"
echo "├── eda.ipynb"
echo "├── requirements.txt"
echo "└── run.sh"

echo "🚀 Done!"

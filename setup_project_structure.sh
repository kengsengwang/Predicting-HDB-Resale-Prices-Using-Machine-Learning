#!/bin/bash

echo "� Running setup from: $(pwd)"
echo "✅ Creating folders if not exist..."

# === Step 1: Create required folders ===
mkdir -p src
mkdir -p .github

# === Step 2: Move Python files to src/ if not already moved ===
echo "� Moving Python files to src/ ..."
find . -maxdepth 1 -type f -name "*.py" -exec mv {} src/ \;

# === Step 3: Create essential files if missing ===
echo "� Creating placeholder files if missing..."

touch README.md
touch requirements.txt
touch run.sh
touch .gitignore

# === Step 4: Summary ===
echo "✅ Project structure is now:"
echo "├── src/                # All Python scripts"
echo "├── .github/            # GitHub workflows (optional)"
echo "├── eda.ipynb           # EDA notebook stays in root"
echo "├── requirements.txt"
echo "├── run.sh"
echo "├── README.md"
echo "└── .gitignore"

echo "� Setup complete!"


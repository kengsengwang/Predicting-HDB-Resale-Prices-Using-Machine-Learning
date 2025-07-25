#!/bin/bash

echo "ν³ Running setup from: $(pwd)"
echo "β Creating folders if not exist..."

# === Step 1: Create required folders ===
mkdir -p src
mkdir -p .github

# === Step 2: Move Python files to src/ if not already moved ===
echo "νΊ Moving Python files to src/ ..."
find . -maxdepth 1 -type f -name "*.py" -exec mv {} src/ \;

# === Step 3: Create essential files if missing ===
echo "ν³ Creating placeholder files if missing..."

touch README.md
touch requirements.txt
touch run.sh
touch .gitignore

# === Step 4: Summary ===
echo "β Project structure is now:"
echo "βββ src/                # All Python scripts"
echo "βββ .github/            # GitHub workflows (optional)"
echo "βββ eda.ipynb           # EDA notebook stays in root"
echo "βββ requirements.txt"
echo "βββ run.sh"
echo "βββ README.md"
echo "βββ .gitignore"

echo "νΎ Setup complete!"


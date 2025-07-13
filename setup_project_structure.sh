#!/bin/bash

echo "í³ Running setup from: $(pwd)"
echo "âœ… Creating folders if not exist..."

# === Step 1: Create required folders ===
mkdir -p src
mkdir -p .github

# === Step 2: Move Python files to src/ if not already moved ===
echo "íºš Moving Python files to src/ ..."
find . -maxdepth 1 -type f -name "*.py" -exec mv {} src/ \;

# === Step 3: Create essential files if missing ===
echo "í³ Creating placeholder files if missing..."

touch README.md
touch requirements.txt
touch run.sh
touch .gitignore

# === Step 4: Summary ===
echo "âœ… Project structure is now:"
echo "â”œâ”€â”€ src/                # All Python scripts"
echo "â”œâ”€â”€ .github/            # GitHub workflows (optional)"
echo "â”œâ”€â”€ eda.ipynb           # EDA notebook stays in root"
echo "â”œâ”€â”€ requirements.txt"
echo "â”œâ”€â”€ run.sh"
echo "â”œâ”€â”€ README.md"
echo "â””â”€â”€ .gitignore"

echo "í¾‰ Setup complete!"


Absolutely! Here's a complete and polished `README.md` tailored to your GitHub project on **Predicting HDB Resale Prices Using Machine Learning**. It includes:

* 🔹 Project overview
* 📊 Dataset info
* 🧹 Preprocessing
* 🤖 Models used
* 🚀 How to run
* 📈 Results
* ✅ Requirements

---

### ✅ Recommended `README.md`

```markdown
# 🏠 Predicting HDB Resale Prices Using Machine Learning

This project builds a machine learning pipeline to **predict HDB resale flat prices in Singapore** based on historical transaction data. The goal is to explore key factors influencing pricing and build a predictive model that can assist buyers, sellers, and policymakers.

---

## 📂 Project Structure

```

.
├── data/                   # Contains original and cleaned CSV files
├── src/                    # Python modules for preprocessing, training, etc.
├── eda.ipynb               # Exploratory Data Analysis in Jupyter Notebook
├── run.sh                  # Shell script to run the full pipeline
├── requirements.txt        # Python dependencies
├── README.md               # This file

````

---

## 📊 Dataset

The dataset used is the public HDB resale transactions dataset available from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices).

### Key Features:
- `month`: Transaction date
- `town`: HDB town
- `flat_type`, `flat_model`, `storey_range`
- `floor_area_sqm`
- `lease_commence_date`
- `remaining_lease`
- `resale_price` (target)

---

## 🧹 Data Preprocessing

Handled in `src/data_preprocessing.py`:
- Converted `storey_range` to numerical format
- Converted `remaining_lease` to months
- Created `flat_age` feature
- Handled missing values and encoding of categorical variables

---

## 🤖 Models Implemented

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- Deep Neural Network (optional extension)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kengsengwang/Predicting-HDB-Resale-Prices-Using-Machine-Learning.git
cd Predicting-HDB-Resale-Prices-Using-Machine-Learning
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
bash run.sh
```

---

## 📈 Evaluation Metrics

Used in `src/evaluate_model.py`:

* RMSE (Root Mean Squared Error)
* R² Score
* Visualizations of predicted vs actual prices

---

## 🔍 EDA Highlights (see `eda.ipynb`)

* Strong positive correlation between floor area and resale price
* Older flats tend to sell at lower prices (flat age matters)
* Resale price varies significantly across different towns and flat models

---

## ✅ Requirements

See `requirements.txt`, which includes:

* pandas
* numpy
* scikit-learn
* xgboost
* catboost
* matplotlib, seaborn
* jupyter

---

## ✍️ Author

**Wang Keng Seng**
🔗 [GitHub Profile](https://github.com/kengsengwang)

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).



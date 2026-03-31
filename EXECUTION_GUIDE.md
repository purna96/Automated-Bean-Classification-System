# 🫘 Dry Bean Classification - Execution Guide

## Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Jupyter Notebook
```bash
jupyter notebook Bean_Classification.ipynb
```
- **Execution Time:** 10-20 minutes (includes model training and hyperparameter tuning)
- **Output:** Generates visualization plots + saves trained models

### Step 3: Launch the Streamlit App
```bash
streamlit run bean_classifier_app.py
```
- **Opens automatically** in your default browser
- **URL:** `http://localhost:8501`

---

## What Happens When You Run the Notebook

### Output Generated:
1. **Visualizations:**
   - Class distribution charts (bar + pie)
   - Feature histograms and boxplots (16 features)
   - Correlation heatmap
   - Model performance comparisons
   - Confusion matrices
   - Feature importance plots

2. **Console Output:**
   - Dataset shape and statistics
   - Missing values report
   - Outlier detection results
   - Model training progress
   - Performance metrics for all algorithms
   - Hyperparameter tuning results
   - Best model selection

3. **Saved Files:**
   ```
   ✓ best_rf_model.pkl (trained model)
   ✓ scaler.pkl (feature scaler)
   ✓ label_encoder.pkl (class encoder)
   ✓ feature_columns.txt (feature names)
   ```

---

## What the Streamlit App Does

### Input Section (Left):
- 16 numeric input fields with realistic ranges
- Sliders or number inputs for bean measurements
- Default values based on dataset statistics

### Output Section (Right):
- **Prediction Result:**
  - Predicted bean type (green highlighted)
  - Confidence percentage (e.g., 96.5%)
  - Bean description

- **Probability Chart:**
  - Bar chart showing all 7 bean types
  - Probability distribution
  - Detailed table with percentages

---

## Notebook Sections Explained

### 📊 Section 1: Data Loading
```python
# Loads Dry_Beans_Dataset.xlsx
# Displays: shape, head(), info(), describe()
# Time: ~5 seconds
```

### 📈 Section 2: EDA
```python
# Class distribution analysis
# Feature histograms and boxplots
# Correlation heatmap
# Time: ~30 seconds
```

### 🔍 Section 3: Missing Values & Outliers
```python
# Checks for null values
# Z-score and IQR outlier detection
# Results: Usually no missing values
# Time: ~10 seconds
```

### 🧹 Section 4: Preprocessing
```python
# Label encoding for target variable
# Feature scaling with StandardScaler
# Stratified train-test split (80-20)
# Time: ~5 seconds
```

### 🤖 Section 5: Model Building
```python
# Trains 7 different classifiers:
#   - Logistic Regression
#   - Decision Tree
#   - Random Forest
#   - SVM
#   - KNN
#   - Naive Bayes
#   - Gradient Boosting
# Cross-validation: 5 folds
# Time: ~2-3 minutes (longest section)
```

### ⚖️ Section 6: SMOTE
```python
# Applies SMOTE for class balancing
# Retrains selected models
# Compares performance before/after
# Time: ~1 minute
```

### 👁️ Section 7: Evaluation
```python
# Classification reports
# Confusion matrices
# Overfitting analysis
# Time: ~20 seconds
```

### 🔧 Section 8: Hyperparameter Tuning
```python
# GridSearchCV for Random Forest
# Tests various parameter combinations
# Finds optimal configuration
# Time: ~5 minutes
```

### 📊 Section 9: Comparison
```python
# Creates model comparison table
# Visualizes performance differences
# Identifies best model
# Time: ~10 seconds
```

### 💾 Section 10: Model Saving
```python
# Saves trained models and scalers
# Creates feature column reference
# Ready for deployment
# Time: ~2 seconds
```

---

## Expected Output Examples

### Notebook Console Output:
```
✓ All libraries imported successfully!

Dataset Shape: (13611, 17)

Class Distribution (%)
Seker        14.5%
Barbunya     12.3%
Bombay       10.2%
...

═══════════════════════════════════════════════════════
Training Logistic Regression...
Train Accuracy: 0.9234
Test Accuracy: 0.9156
Precision: 0.9142
...

═══════════════════════════════════════════════════════
🏆 BEST MODEL: Random Forest
   Test Accuracy: 0.9534
═══════════════════════════════════════════════════════
```

### Streamlit App Display:
```
🫘 Dry Bean Type Classification

[Input fields for 16 bean measurements]
[🚀 Classify Bean button]

═════════════════════════════════════════════════
✅ Predicted Bean Type
SEKER
Description: 🫘 Seker beans - Small, round shape
Confidence Score: 96.45%
═════════════════════════════════════════════════

📈 Prediction Probabilities
[Bar chart showing all 7 types]
[Detailed probability table]
```

---

## Troubleshooting

### Issue: "Model files not found" in Streamlit app
**Solution:** Run the notebook completely first to generate model files

### Issue: Notebook runs very slowly
**Solution:** This is normal for hyperparameter tuning. Patience required!
- Random Forest section: 5-10 minutes
- Total notebook: 15-25 minutes

### Issue: Streamlit app doesn't open
**Solution:** Check if port 8501 is available:
```bash
# Kill existing process if needed
# Or use different port:
streamlit run bean_classifier_app.py --server.port 8502
```

### Issue: Excel file not found
**Solution:** Ensure `Dry_Beans_Dataset.xlsx` is in the same directory

### Issue: Import errors
**Solution:** Reinstall all requirements:
```bash
pip install --upgrade -r requirements.txt
```

---

## Performance Expectations

| Component | Time |
|-----------|------|
| Data Loading | ~5 sec |
| EDA | ~30 sec |
| Preprocessing | ~5 sec |
| Model Training | ~2-3 min |
| SMOTE | ~1 min |
| Evaluation | ~20 sec |
| Hyperparameter Tuning | ~5 min |
| Rest of Analysis | ~30 sec |
| **Total Notebook** | **~10-15 min** |
| **Streamlit App** | **Real-time predictions (instant)** |

---

## Files Check List

Before running, ensure these files exist:
- ✅ `Dry_Beans_Dataset.xlsx` (dataset)
- ✅ `Bean_Classification.ipynb` (notebook)
- ✅ `bean_classifier_app.py` (streamlit app)
- ✅ `requirements.txt` (dependencies)
- ✅ `README.md` (documentation)

After running notebook, these should be created:
- ✅ `best_rf_model.pkl`
- ✅ `scaler.pkl`
- ✅ `label_encoder.pkl`
- ✅ `feature_columns.txt`

---

## Next Steps After Execution

1. ✅ Review notebook outputs and visualizations
2. ✅ Test Streamlit app with different bean measurements
3. ✅ Validate predictions against known bean types
4. ✅ Deploy to cloud (Streamlit Cloud, Heroku, etc.)
5. ✅ Collect user feedback for model improvement

---

## Advanced Tips

### Custom Predictions Programmatically:
```python
import joblib
import numpy as np

# Load saved model and scaler
model = joblib.load('best_rf_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Your bean measurements (16 features)
bean_data = np.array([[...your 16 values...]])
bean_scaled = scaler.transform(bean_data)

# Predict
prediction = model.predict(bean_scaled)[0]
confidence = model.predict_proba(bean_scaled)[0].max()
bean_type = label_encoder.inverse_transform([prediction])[0]

print(f"Predicted: {bean_type} (Confidence: {confidence*100:.2f}%)")
```

### Deploy to Streamlit Cloud:
```bash
# Push to GitHub, then:
# 1. Go to streamlit.io/cloud
# 2. Deploy from GitHub repository
# 3. Share public URL
```

---

**Status:** ✅ Complete and Ready to Run
**Version:** 1.0
**Last Updated:** 2025

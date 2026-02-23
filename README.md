# ML Home Assignment

A comprehensive machine learning project demonstrating various ML techniques including Exploratory Data Analysis (EDA), Regression, Classification, Support Vector Machines (SVM), and Neural Networks.

## 📚 Project Structure

The repository contains the following Jupyter notebooks:

### 1. **EDA.ipynb** - Exploratory Data Analysis
- Dataset overview and statistics
- Data visualization and distribution analysis
- Feature correlation studies
- Data quality and missing value assessment

### 2. **Regression.ipynb**
- Regression model development and evaluation
- Feature scaling and preprocessing
- Performance metrics and model comparison

### 3. **Classification.ipynb**
- Classification problem formulation
- Model training and validation
- Classification metrics (accuracy, precision, recall, F1-score)

### 4. **SVM.ipynb** - Support Vector Machines
- SVM classifier implementation
- Kernel selection and hyperparameter tuning
- Support Vector Machine performance analysis

### 5. **Neural Network.ipynb**
- Deep learning model architecture
- Network training and validation
- Loss curves and accuracy metrics

## 📦 Datasets

The project includes preprocessed datasets in pickle format:

- **Training Data:**
  - `X_train.pkl` - Training features
  - `X_train_scaled.pkl` - Scaled training features
  - `y_train.pkl` - Training targets

- **Validation Data:**
  - `X_val.pkl` - Validation features
  - `X_val_scaled.pkl` - Scaled validation features
  - `y_val.pkl` - Validation targets

- **Test Data:**
  - `X_test.pkl` - Test features
  - `X_test_scaled.pkl` - Scaled test features
  - `y_test.pkl` - Test targets

## 🤖 Models

Pre-trained models are included:

- `model.pkl` - Regression/Primary model
- `classification_model.pkl` - Classification model
- `scaler.pkl` - Feature scaler for preprocessing

## 🛠️ Web Application

The `Web_APP` directory contains deployment-ready code for serving the models.

## 🚀 Getting Started

1. Clone the repository
2. Install required dependencies: `pip install -r requirements.txt`
3. Open the Jupyter notebooks in order:
   - Start with `EDA.ipynb` for data understanding
   - Progress through regression and classification models
   - Explore advanced techniques (SVM, Neural Networks)

## 📊 Technologies Used

- Python 3
- Jupyter Notebooks
- Scikit-learn
- TensorFlow/Keras
- Pandas & NumPy
- Matplotlib & Seaborn

## 📝 License

This project is part of a machine learning home assignment.

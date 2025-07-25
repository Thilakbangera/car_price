# 🚗 Car Price Prediction App

A **Streamlit-based web application** that allows users to **predict the price of a used car** based on key features such as company, model, year, kilometers driven, and fuel type. The prediction is powered by a **pre-trained Linear Regression model**.

---

## 📂 Project Structure

```bash
car-price-prediction/
│
├── LinearRegressionModel.pkl     # Pre-trained ML model
├── Cleaned_car.csv               # Cleaned dataset with car listings
├── app.py                        # Main Streamlit app
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation (this file)
```

---

## 🔧 Features

* Interactive **dropdowns** for car company and model
* Input fields for:

  * Manufacturing **year**
  * **Kilometers** driven
  * **Fuel type**
* Real-time **price prediction**
* Session-based **history** of all predictions in the current session

---

## 🚀 How to Run the App

### ✅ Step 1: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, use this:

```txt
streamlit
pandas
scikit-learn
```

Install manually with:

```bash
pip install streamlit pandas scikit-learn
```

### ✅ Step 2: Run the App

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## 📊 Model Details

* **Type**: Linear Regression
* **Features used**:

  * `name` (Car model)
  * `company`
  * `year`
  * `kms_driven`
  * `fuel_type`
* **Training dataset**: `Cleaned_car.csv` (ensure it's in the same directory)

---

## 📋 Dataset: `Cleaned_car.csv`

This CSV should contain at least the following columns:

* `name` – Model name (e.g., Alto LXI)
* `company` – Car manufacturer (e.g., Maruti)
* `year` – Year of manufacture
* `kms_driven` – Total kilometers driven
* `fuel_type` – Fuel type (Petrol, Diesel, etc.)
* `price` – Target variable (used for training, optional during inference)

---

## 🖼️ App UI Preview

### Title

```
Car Price Prediction
Use this app to predict the price of a car based on its features.
```

### Input Fields

* Select Car Company
* Select Car Model
* Year
* Kilometers Driven
* Fuel Type

### Buttons

* `Predict Price`

### Output

* Predicted price (₹)
* Table of previous predictions in session

---

## 💾 Session Handling

* Streamlit `session_state` is used to **track previous predictions** during the app session.

---

## 🛠️ Notes

* Make sure `LinearRegressionModel.pkl` and `Cleaned_car.csv` exist in the same directory as `app.py`.
* Model must be trained with consistent preprocessing as expected by the input.

---

## 🧠 Future Improvements

* Add additional features like `transmission`, `owner type`, `location`
* Support **model retraining** from the UI
* Save predictions to a database or file
* Deploy on platforms like **Streamlit Cloud**, **Heroku**, or **Render**

---

## 🌐 Deployment

To deploy on **Streamlit Cloud**:

1. Push your project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and select `app.py`
4. Add `LinearRegressionModel.pkl` and `Cleaned_car.csv` to your GitHub repo
5. App will be deployed and hosted online for free!

---

## 👨‍💻 Author

**Thilak Bangera**

GitHub: [@Thilakbangera](https://github.com/Thilakbangera)

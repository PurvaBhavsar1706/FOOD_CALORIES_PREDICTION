# Food Calories Prediction 🍽️

## 🔍 Overview
`food_calories_prediction` is an AI-powered web application that predicts the calorie and nutritional content of food items using image classification. Users can register, log in, upload an image of food, and get details like calories, protein, fiber, and carbohydrates.

This project uses a pre-trained deep learning model (.h5) to recognize food items and provide nutrition facts. It’s ideal for fitness enthusiasts, diet planners, and anyone looking to monitor food intake.

---

## 💡 Features

- 🔐 User registration and login system (Flask + SQLite)
- 📷 Upload food image and get prediction using ML model
- 📊 Displays nutritional information (calories, protein, fiber, carbs)
- 📁 Stored image uploads in static folder
- 🖥️ Responsive UI using HTML, CSS, Bootstrap
- ✅ Lightweight and easy to deploy

---

## 🛠️ Technologies Used

| Component        | Technology                     |
|------------------|--------------------------------|
| Backend          | Python, Flask                  |
| Machine Learning | TensorFlow / Keras (.h5 model) |
| Database         | SQLite                         |
| Frontend         | HTML, CSS, Bootstrap           |
| Image Handling   | PIL, NumPy                     |

---

## 🧠 How It Works

1. **User Auth:** Users can register and log in securely.
2. **Upload Image:** User uploads a food image (e.g., pizza, mango).
3. **Prediction:** Image is processed by the pre-trained model (`food_model.h5`) to classify the food item.
4. **Nutrition Info:** Based on the classified item, the app fetches calorie and nutrition data (from a static dictionary or CSV file).
5. **Display Results:** Prediction and details are shown on the result page.

---

## 🗂️ Project Structure


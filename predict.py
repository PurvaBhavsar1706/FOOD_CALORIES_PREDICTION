from flask import Blueprint, render_template, request
import os
from PIL import Image
import numpy as np
import tensorflow as tf

predict = Blueprint('predict', __name__)
UPLOAD_FOLDER = 'static/uploads'

# Load trained model
model = tf.keras.models.load_model('model/food_model.h5')

# Must match your model's classes
class_labels = ['pizza', 'burger', 'mango', 'banana', 'salad', 'paneer', 'chapati', 'frankie', 'biryani', 'dal', 'apple','kiwi','papaya','pasta','sandwich']

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def real_predict(image_path):
    img_tensor = preprocess_image(image_path)
    prediction = model.predict(img_tensor)[0]
    class_index = np.argmax(prediction)
    label = class_labels[class_index]

    food_info = {
    'mango': {"calories": 60, "fiber": "1.6g", "protein": "0.8g", "carbs": "15g", "info": "Sweet and juicy fruit."},
    'banana': {"calories": 89, "fiber": "2.6g", "protein": "1.1g", "carbs": "23g", "info": "Energy-rich fruit."},
    'burger': {"calories": 295, "fiber": "1.5g", "protein": "17g", "carbs": "30g", "info": "Pattie sandwich."},
    'pizza': {"calories": 266, "fiber": "2.3g", "protein": "11g", "carbs": "33g", "info": "Cheesy delight."},
    'biryani': {"calories": 290, "fiber": "2g", "protein": "8g", "carbs": "38g", "info": "Spiced rice dish."},
    'chapati': {"calories": 104, "fiber": "3g", "protein": "3g", "carbs": "15g", "info": "Whole wheat Indian bread."},
    'paneer': {"calories": 265, "fiber": "0g", "protein": "18g", "carbs": "6g", "info": "Cottage cheese, rich in protein."},
    'frankie': {"calories": 220, "fiber": "2g", "protein": "7g", "carbs": "25g", "info": "Wrap filled with veggies or meat."},
    'dal': {"calories": 180, "fiber": "4g", "protein": "10g", "carbs": "22g", "info": "Protein-rich lentil curry."},
    'salad': {"calories": 90, "fiber": "2.5g", "protein": "2g", "carbs": "10g", "info": "Healthy mixed vegetables."},
    'apple': {"calories": 52, "fiber": "2.4g", "protein": "0.3g", "carbs": "14g", "info": "Crunchy and sweet red fruit."},
    'kiwi': {"calories": 41, "fiber": "2.1g", "protein": "0.8g", "carbs": "10g", "info": "Tangy green tropical fruit."},
    'papaya': {"calories": 43, "fiber": "1.7g", "protein": "0.5g", "carbs": "11g", "info": "Soft tropical fruit rich in enzymes."},
    'pasta': {"calories": 131, "fiber": "1.8g", "protein": "5g", "carbs": "25g", "info": "Italian wheat-based dish."},
    'sandwich': {"calories": 250, "fiber": "2g", "protein": "12g", "carbs": "30g", "info": "Two bread slices with filling."}
}


    return {
        "name": label.capitalize(),
        **food_info.get(label, {
            "calories": "Unknown", "fiber": "-", "protein": "-", "carbs": "-", "info": "No details found."
        })
    }

@predict.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

            prediction = real_predict(image_path)

            return render_template('result.html',
                                   image='/' + image_path,
                                   food_name=prediction['name'],
                                   calories=prediction['calories'],
                                   food_info=prediction['info'],
                                   fiber=prediction['fiber'],
                                   protein=prediction['protein'],
                                   carbs=prediction['carbs'])

    return render_template('home.html')

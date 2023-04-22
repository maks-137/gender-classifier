def predict():
    import sys
    import os

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    import tensorflow as tf
    from tensorflow.keras.preprocessing import image 

    img_path = sys.argv[1]

    model = tf.keras.models.load_model('model')

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255
    img_array = img_array.reshape(1, 224, 224, 3)

    prediction = model.predict(img_array, batch_size=1)
    label = 'Чоловік' if prediction > 0.5 else 'Жінка'
    
    print(label)




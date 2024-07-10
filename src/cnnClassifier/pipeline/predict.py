import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from pathlib import Path

class DogCat:
    def __init__(self, filename) -> None:
        self.filename = filename

    def predictiondogcat(self):
        # Load model
        model = load_model(Path("artifacts/training") / "model.h5")

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        # test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'dog'
            return [{'image': prediction}]
        else:
            prediction = 'cat'
            return [{'image': prediction}]
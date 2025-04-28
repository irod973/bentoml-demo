"""This module defines a BentoML service that uses a Keras model to classify
digits.
"""

import bentoml
import numpy as np
from bentoml.io import NumpyNdarray

BENTO_MODEL_TAG = "keras_model:latest"


classifier_runner = bentoml.keras.get(BENTO_MODEL_TAG).to_runner()

mnist_service = bentoml.Service("mnist_classifier", runners=[classifier_runner])


@mnist_service.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_data: np.ndarray) -> np.ndarray:
    return classifier_runner.predict.run(input_data)

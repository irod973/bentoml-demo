import json

import numpy as np
import numpy.typing as npt
import requests
from loguru import logger

from bentoml_demo.training import MNISTData, prepare_mnist_training_data

SERVICE_URL = "http://localhost:3000/classify"


def sample_random_mnist_data_point() -> tuple[npt.NDArray[np.float32], npt.NDArray[np.int32]]:
    mnist_data: MNISTData = prepare_mnist_training_data()
    random_index = np.random.randint(0, len(mnist_data.test_images))
    random_test_image = mnist_data.test_images[random_index]
    random_test_image = np.expand_dims(random_test_image, 0)
    return random_test_image, mnist_data.test_labels[random_index]


def make_request_to_bento_service(
    service_url: str, input_array: np.ndarray
) -> str:
    serialized_input_data = json.dumps(input_array.tolist())
    response = requests.post(
        service_url,
        data=serialized_input_data,
        headers={"content-type": "application/json"}
    )
    return response.text


def main():
    input_data, expected_output = sample_random_mnist_data_point()
    prediction = make_request_to_bento_service(SERVICE_URL, input_data)
    logger.info(f"Prediction: {prediction}")
    logger.info(f"Expected output: {expected_output}")


if __name__ == "__main__":
    main()

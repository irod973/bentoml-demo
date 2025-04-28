"""This module trains a ConvNet model built with Keras, for classifying
digits using the MNIST dataset.
"""

from pathlib import Path
from typing import NamedTuple

import numpy as np
import numpy.typing as npt
from tensorflow import keras

NUM_CLASSES = 10
INPUT_SHAPE = (28, 28, 1)
NUM_EPOCHS = 1



class MNISTData(NamedTuple):
    train_images: npt.NDArray[np.float32]
    train_labels: npt.NDArray[np.int32]
    test_images: npt.NDArray[np.float32]
    test_labels: npt.NDArray[np.int32]

def prepare_mnist_training_data() -> MNISTData:
    """Prepares training data for the model.

    Returns:
        MNISTData object containing
            - The training images,
            - The training labels,
            - The test images,
            - The test labels.
    """
    (train_images, train_labels), (
        test_images,
        test_labels,
    ) = keras.datasets.mnist.load_data()

    train_images = train_images.reshape(train_images.shape[0], *INPUT_SHAPE).astype(
        np.float32
    )
    test_images = test_images.reshape(test_images.shape[0], *INPUT_SHAPE).astype(
        np.float32
    )

    # Normalize the images to the range [0, 1]
    train_images /= 255.0
    test_images /= 255.0

    # One-hot encode the labels
    train_labels = keras.utils.to_categorical(train_labels, NUM_CLASSES)
    test_labels = keras.utils.to_categorical(test_labels, NUM_CLASSES)

    return MNISTData(train_images, train_labels, test_images, test_labels)


def build_convnet_model(input_shape: tuple, num_classes: int) -> keras.Model:
    """Builds a simple ConvNet model.

    Args:
        input_shape: The shape of the input data.
        num_classes: The number of classes to classify.

    Returns:
        A Keras model.
    """
    model = keras.models.Sequential(
        [
            keras.Input(shape=input_shape),
            keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu", padding="same"),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same"),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(num_classes, activation="softmax"),
        ]
    )

    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )

    return model


def train_model(
    model: keras.Model,
    mnist_data: MNISTData,
    num_epochs: int,
) -> keras.Model:
    """Trains a model.

    Args:
        model: The model to train.
        mnist_data: Data contanining
            train_images: The training images.
            train_labels: The training labels.
            test_images: The test images.
            test_labels: The test labels.
        num_epochs: The number of epochs to train for.
    Returns:
        The trained model.
    """
    model.fit(
        mnist_data.train_images,
        mnist_data.train_labels,
        epochs=num_epochs,
        validation_data=(mnist_data.test_images, mnist_data.test_labels),
    )
    return model


def save_model(model: keras.Model, model_save_path: Path) -> None:
    """Saves a model to a file.

    Args:
        model: The model to save.
        model_save_path: The file to save the model to.
    """
    model.save(model_save_path)


def main():
    """Trains a model for classifying digits using the MNIST dataset."""

    mnist_data: MNISTData = prepare_mnist_training_data()

    model = build_convnet_model(INPUT_SHAPE, NUM_CLASSES)

    model = train_model(
        model, mnist_data, NUM_EPOCHS
    )

    save_model(model, Path("model.keras"))


if __name__ == "__main__":
    main()

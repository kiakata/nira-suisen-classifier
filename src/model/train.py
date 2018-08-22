# coding: utf-8
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# local
from config import file_path


batch_size = 32
epochs = 32


def main():
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, input_shape=(128, 128, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        file_path.PREPROCESSED_TRAIN_DIR_PATH,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='categorical')

    validation_generator = test_datagen.flow_from_directory(
        # PREPROCESSED_VAL_DIR_PATH,
        file_path.PREPROCESSED_TRAIN_DIR_PATH,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='categorical')

    history = model.fit_generator(
        train_generator,
        samples_per_epoch=200,
        nb_epoch=epochs,
        validation_data=validation_generator,
        nb_val_samples=50)

    # from keras.utils import plot_model
    # plot_model(model, to_file="model.png", show_shapes=True)


if __name__ == '__main__':
    main()

from tensorflow import keras
from keras.datasets import mnist
from keras import layers

# make model
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
model = keras.Sequential([
    layers.Dense(512, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(optimizer="rmsprop",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255

model.fit(train_images, train_labels, epochs=5, batch_size=128)

# test model (predict the number 7)
test_digits = test_images[0:10]
predictions = model.predict(test_digits)
print(predictions[0])
predictions[0].argmax()
print(predictions[0][7])

# test model on new number
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"test_acc: {test_acc}")

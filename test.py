import os, io
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from keras import Sequential
from keras.layers import *
from keras.models import load_model
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# CREATING THE MODEL AND ITS TOPOLOGY
def createModelWithTopology():
    model = Sequential() # Sequential is one of two main Keras models (the other one is Model)

    # Topology 1:
    #model.add(Dense(4, activation='relu', kernel_initializer='random_normal', input_dim=columns))
    #model.add(Dense(4, activation='relu', kernel_initializer='random_normal'))
    #model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

    # Topology 2:
    model.add(Dense(8, kernel_initializer='random_normal', input_dim=columns))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dense(16, kernel_initializer='random_normal'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dense(32, kernel_initializer='random_normal'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dense(16, kernel_initializer='random_normal'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

    # Compiling the neural network
    # binary_crossentropy is used for calculation the loss function between actual output vs predicted output

    #edit this!
    learning_rate = 0.006
    custom_optimizer = keras.optimizers.Adam(learning_rate=learning_rate,name='Adam')
    model.compile(optimizer=custom_optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

# Set working directory to be a local directory (files will be taken from same directory as this script)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dataset = pd.read_csv('robocode_4robots.csv')
columns = dataset.shape[1] - 1

print("---------- first_5_rows --------------\n", dataset.head(5)) # Returns first n rows
print("---------- statistics_summary --------------\n", dataset.describe(include='all')) # Generate various summary statistics, excluding NaN values.

# creating input features and target variables
x = dataset.iloc[:,0:columns] # first argument: all rows; second argument: zero to twelve columns
y = dataset.iloc[:,columns]

# standardize different input scales
#sc = StandardScaler()
#x = sc.fit_transform(x)

# Split the data + validation data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# Once the model is created, you can config the model with losses and metrics with model.compile(),
# train the model with model.fit(), or use the model to do prediction with model.predict().
model = createModelWithTopology()

# Fit the model
#model.fit(x_train, y_train, batch_size=1, epochs=10)
#creating history variable for plot, based on model fit function https://keras.io/examples/structured_data/collaborative_filtering_movielens/
history = model.fit(
    x=x_train,
    y=y_train,
    batch_size=128,
    epochs=100,
    verbose=1,
    validation_data=(x_test, y_test),
)

# Return the loss value & metrics values for the model in test mode
eval_model=model.evaluate(x_train, y_train)
print("---------- eval_model --------------\n", eval_model)

# Predict output for our test dataset - make it a boolean based on its value
y_pred=model.predict(x_test)
y_pred=(y_pred>0.5)

# Check the accuracy of NN
# left-upper and right-down are the values we want (true-positive and true-negative)
# přidat i do prezentace
cm = confusion_matrix(y_test, y_pred)
print("---------- confusion_matrix --------------\n", cm)

#print plot in a new window after model learning
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
plt.show()

#save model do not forget to rename!
model.save(
    'savedModel_test.h5', #edit this!
    overwrite=True,
    include_optimizer=True,
)
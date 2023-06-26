from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import random

cl = list(range(10000))
cl_10 = random.sample(cl,30)

# print(cl_10)
# print(cl_10[0])

# MNIST 분류 모델 파일 불러오기
_, (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0 # 데이터 정규화

# 모델 불러오기
model = load_model('./data/mnist_model_adam_add3.h5')
model.summary()
model.evaluate(x_test, y_test, verbose=2)

i = 0
while i <=29:

    picks = cl_10[i]
    pick = [picks]
    y_prob = model.predict(x_test[pick], verbose=0) 
    predicted = y_prob.argmax(axis=-1)
    print("손글씨 이미지 예측값 : ", predicted)
    plt.imshow(x_test[picks], cmap="gray")
    plt.show()
    i += 1
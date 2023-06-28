#078일차-실습-1-해답-ver1
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, LSTM, SimpleRNN
#
#
# time step만큼(여기서는 15로 세팅함) 시퀀스 데이터 분리
def split_sequence(sequence, step):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_idx = i + step
        if end_idx > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_idx], sequence[end_idx]
        x.append(seq_x)
        y.append(seq_y)
    return np.array(x), np.array(y)

# sin 함수 학습 데이터 ❶
x = [i for i in np.arange(start=-10, stop=10, step=0.1)]  # 10에서 +10 사이의값을 배열xfmf 생성 
train_y = [np.sin(i) for i in x]  # 배열 x를 인수로 하여 sin함수를 동작하여 train_y를 구함

# 하이퍼파라미터 ❷
n_timesteps = 15    # 입력 시퀀스 길이 15 세팅  동글배기(노드)가 15개란 뜻 # 그림6-26
n_features = 1      # 입력 백터의 차원 1 세팅 

# 시퀀스 나누기 ➌
# train_x.shape => (samples, timesteps)
# train_y.shape => (samples)
train_x, train_y = split_sequence(train_y, step=n_timesteps)
    #split_sequence() 함수를 실행하면 입력시퀀스 x와 출력값 y가 반환됨
    # x와 y는  ❹ 블럭의 train_x.reshape() 함수의 인수로 사용됨 
print("shape x:{} / y:{}".format(train_x.shape, train_y.shape))

# RNN 입력 벡터 크기를 맞추기 위해 벡터 차원 크기 변경 ❹
# reshape from [samples, timesteps] into [samples, timesteps, features]
train_x = train_x.reshape(train_x.shape[0], train_x.shape[1], n_features)
            # ➌ 블럭의 결과값인 train_x.shape, train_y.shape을 
            # train_x.reshape() 함수의 인수로 사용함
print("train_x.shape = {}".format(train_x.shape))
print("train_y.shape = {}".format(train_y.shape))
os.system("pause")

# RNN 모델 정의 ❺ # 아래 명령문 하단의 주석참조
model = Sequential()
model.add(SimpleRNN(units=10, return_sequences=False, input_shape=(n_timesteps, n_features)))
        # return_sequences 속성은 RNN 계산 과정에서 은닉 상탯값을 출력할지 결정
        # 이 인자가 False 인 경우 마지막 시점의 메모리 셀에서만 결과를 출력함.
        # 반대로 True 인 경우 모든 RNN 계산 과정에서 결과를 출력함
        # return_sequences 인자는 다층구조의 RNN 모델이나 출력이 여러 개 인 
        # one-to-many와 many-to-many 구조를 위해 사용함
model.add(Dense(1))
model.add(Dense(1)) # 추가함1 
model.add(Dense(1)) # 추가함2
model.add(Dense(1)) # 추가함3 
model.add(Dense(1)) # 추가함4
#model.compile(optimizer='adam', loss='mse') # 유지함 optimizer='adam'
model.compile(optimizer='sgd', loss='mse') # 변경함 optimizer='sgd' 
#
# 모델 학습 ❻
np.random.seed(0)
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=5, mode='auto')
history = model.fit(train_x, train_y, epochs=1000, callbacks=[early_stopping])

# loss 그래프 생성 ❼
plt.plot(history.history['loss'], label="loss")
plt.legend(loc="upper right")
plt.show()

# 테스트 데이터셋 생성 ❽
test_x = np.arange(10, 20, 0.1)
calc_y = np.cos(test_x) # 테스트 정답 데이터

# RNN 모델 예측 및 로그 저장 ❾
test_y = calc_y[:n_timesteps]
for i in range(len(test_x) - n_timesteps):
    net_input = test_y[i : i + n_timesteps]
    net_input = net_input.reshape((1, n_timesteps, n_features))
    train_y = model.predict(net_input, verbose=0)
    print(test_y.shape, train_y.shape, i, i + n_timesteps)
    test_y = np.append(test_y, train_y)


# 예측 결과 그래프 그리기 ❿
plt.plot(test_x, calc_y, label="ground truth", color="orange")
plt.plot(test_x, test_y, label="predictions", color="blue")
plt.legend(loc='upper left')
plt.ylim(-2, 2)
plt.show()
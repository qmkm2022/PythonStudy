# import sys  
# sys.path.append(r"C:/workspace/chatbot"); from utils.Preprocess import Preprocess
# from models.intent.IntentModel import IntentModel

# p = Preprocess()

# intent = IntentModel(model_name='./chatbot/models/intent/intent_model.h5', proprocess=pow)
# query = "내일 오전 10시에 촐랭이밥 하나 포장이요."
# predict = intent.predict_class(query)
# predict_label = intent.labels[predict]

# print(query)
# print("의도 예측 클래스 : ", predict)
# print("의도 예측 레이블 : ", predict_label)

import sys  
sys.path.append(r"C:/workspace/chatbot"); from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='./chatbot/train_tools/dict/chatbot_dict.bin',
               userdic='./chatbot/utils/user_dic.tsv')

intent = IntentModel(model_name='./chatbot/models/intent/intent_model.h5', compile=False)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.compile(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)
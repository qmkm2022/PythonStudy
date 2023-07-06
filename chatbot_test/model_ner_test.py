import sys  
sys.path.append(r"C:/workspace/chatbot"); from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='./chatbot/train_tools/dict/chatbot_dict_3.bin',
               userdic='./chatbot/utils/user_dic.tsv')


ner = NerModel(model_name='./chatbot/models/ner/ner_model_cb.h5', proprocess=p)

query = "오늘 오전 13시 2분에 촐랭이밥 주문 하고 싶어요"

predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)


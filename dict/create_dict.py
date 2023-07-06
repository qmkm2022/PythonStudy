#
# 챗봇에서 사용하는 사전 파일 생성
#
import sys  
sys.path.append(r"C:/workspace/chatbot"); from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 헤더제거
    return data


# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('./chatbot/train_tools/dict/ccc2.txt')


# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess(word2index_dic='./chatbot/train_tools/dict/chatbot_dict_2.bin',
               userdic = './chatbot/utils/user_dic.tsv')
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])
    # keywords = p.get_keywords(pos, without_tag=True)
    # for k in keywords:
    #     dict.append(k)

# 사전에 사용될 word2index 생성
# 사전의 첫번 째 인덱스에는 OOV 사용
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("./chatbot/train_tools/dict/chatbot_dict_3.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()

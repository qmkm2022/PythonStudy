from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm

# 코사인 유사도 계산
def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# TDM 만들기
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}
    for word in word_dics:
        freq_mat[word] = 0
    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1
    return freq_mat

# 단어 벡터 만들기
def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec

# 문장입력1
def sentence1():
    print("3개 이상의 단어로 구성된 문장1을(를) 입력하세요")
    s_1 = input()
    print("문장1 : ", s_1)
    return s_1

# 문장입력2
def sentence2():
    print("3개 이상의 단어로 구성된 문장2을(를) 입력하세요")
    s_2 = input()
    print("문장2 : ", s_2)
    return s_2

s_1 = sentence1()
s_2 = sentence2()

# 형태소분석기를 이용해 단어 묶음 리스트 생성
komoran = Komoran()
bow1 = komoran.nouns(s_1)
bow2 = komoran.nouns(s_2)

# 단어 묶음 리스트를 하나로 합침
bow = bow1 + bow2

# 단어 묶음에서 중복제거해 단어 사전 구축
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)

# 문장 별 단어 문서 행렬 계산
freq_list1 = make_term_doc_mat(bow1, word_dics)
freq_list2 = make_term_doc_mat(bow2, word_dics)
print(freq_list1)
print(freq_list2)

# 문장 벡터 생성
doc1 = np.array(make_vector(freq_list1))
doc2 = np.array(make_vector(freq_list2))

print(doc1)
print(doc2)

# 코사인 유사도 계산
r1 = cos_sim(doc1, doc2)
print(r1)
from konlpy.tag import Komoran

# 문장입력1
def sentence1():
    print("3개 이상의 단어로 구성된 문장1을(를) 입력하세요")
    print("예:사람은 표유류에 속하는 동물이다")
    s_1 = input()
    print("문장1 : ", s_1)
    return s_1

# 문장입력2
def sentence2():
    print("3개 이상의 단어로 구성된 문장2을(를) 입력하세요")
    print("예:사람은 설치류에 속하는 동물이다")
    s_2 = input()
    print("문장2 : ", s_2)
    return s_2

# 어절 단위 n-gram
def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x + num_gram] for x in range(0,len(text) - num_gram + 1)]
    return tuple(ngrams)

# 유사도 계산
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt = cnt + 1
    return cnt/len(doc1)

s_1 = sentence1()
s_2 = sentence2()

# 형태소 분석기에서 명사(단어) 추출
komoran = Komoran()
bow1 = komoran.nouns(s_1)
bow2 = komoran.nouns(s_2)

# 단어 n-gram 토큰 추출
doc1 = word_ngram(bow1, 2) 
doc2 = word_ngram(bow2, 2)

# 추출된 n-gram 토큰 출력
print(doc1)
print(doc2)

# 유사도 계산
r1 = similarity(doc1, doc2)

# 계산된 유사도 출력
print(r1)
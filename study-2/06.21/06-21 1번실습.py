# 예제-5-1 2-gram 유사도 계산
from konlpy.tag import Komoran

# 어절 단위 n-gram 1
def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x + num_gram] for x in range(0,len(text) - num_gram + 1)]
    return tuple(ngrams)

# 유사도 계산 2
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt = cnt + 1
    return cnt/len(doc1)

# 문장정의
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학하였다'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학하였다'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었습니다.'

# 형태소 분석기에서 명사(단어) 추출 3
komoran = Komoran()
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 단어 n-gram 토큰 추출 4
doc1 = word_ngram(bow1, 4) # 2-gram 방식으로 추출 -> 2
doc2 = word_ngram(bow2, 4) # 3-gram 방식으로 추출 -> 3
doc3 = word_ngram(bow3, 4) # 4-gram 방식으로 추출 -> 4

# 추출된 n-gram 토큰 출력
print(doc1)
print(doc2)

# 유사도 계산
r1 = similarity(doc1, doc2) # 5
r2 = similarity(doc3, doc1) # 6

# 계산된 유사도 출력
print(r1)
print(r2)
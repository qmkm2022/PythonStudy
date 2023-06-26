#073일차-실습-1-해답
from konlpy.tag import Komoran
import numpy as np
komoran = Komoran()
text = "백화점에는 상품이 많아요"
text = "백화점에는 상품과 사람과 직원이 많아요" # 이 주석을 해제할 때 발생하는 결과를 직전의 결과와 비교하세요
text = "백화점에는 상품과 사람과 직원뿐 아니라 상품이 많아요" # 이 주석을 해제할 때 발생하는 결과를 직전의 결과와 비교--> 구름이 두 번 나왔지만 한 개만 리스트업 되었음 


# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)


# 단어 사전 구축 및 단어별 인덱스 부여
dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)
# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
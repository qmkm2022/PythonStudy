from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
# text = "오늘 날씨는 구름이 많아요."
# text = "오늘 날씨는 구름과 우주인이 많아요."
# text = "오늘 날씨는 구름과 우주인과 구름이 많아요."
# text = "오늘 점심은 라면과 김밥입니다."
# text = "병에 담긴 물은 정말 차가운 물입니다."
text = "날씨가 정말 덥습니다."

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
targets = list(dics.values( ))
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
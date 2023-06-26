# 사용자 단어 사전 형태소 분석 실습
from konlpy.tag import Komoran

komoran = Komoran(userdic='C:/Users/tjoeun/AppData/Local/Programs/Python/Python38/Lib/site-packages/konlpy/data/corpus/kobill//user_dic.tsv')

text_1 = " 들국화와 산울림 중 최고의 그룹은 누구일까"
text_2 = "들국화는 국화꽃과 다를까?"

pos_1 = komoran.pos(text_1)
pos_2 = komoran.pos(text_2)

print(pos_1)
print(pos_2)
# # 사용자 단어 사전 형태소 분석
# from konlpy.tag import Komoran

# komoran = Komoran(userdic='C:/Users/tjoeun/AppData/Local/Programs/Python/Python38/Lib/site-packages/konlpy/data/corpus/kobill//user_dic.tsv')
# text = "우리 챗봇은 엔엘피를 좋아해."
# pos = komoran.pos(text)
# print(pos)

from konlpy.tag import Komoran

#komoran = Komoran(userdic='./user_dic.tsv')
komoran = Komoran(userdic='C:/Users/tjoeun/AppData/Local/Programs/Python/Python38/Lib/site-packages/konlpy/data/corpus/kobill/user2.dic')
#text = "우리 챗봇은 엔엘피를 좋아해."
text = "우리 챗봇은 엔와이피를 뉴진스를 좋아해."
pos = komoran.pos(text)
print(pos)
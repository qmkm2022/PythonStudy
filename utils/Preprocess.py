from konlpy.tag import Komoran
import pickle
import jpype
from re import search


class Preprocess:
    def __init__(self, word2index_dic='', userdic=None):
        # 단어 인덱스 사전 불러오기
        if(word2index_dic != ''):
            f = open(word2index_dic, "rb")
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None

        # 형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사
        # 참조 : https://docs.komoran.kr/firststep/postypes.html
        # 관계언 제거, 기호 제거
        # 어미 제거
        # 접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기 POS 태거
    def pos(self, sentence):
        jpype.attachThreadToJVM()
        return self.komoran.pos(sentence)

    # 불용어 제거 후, 필요한 품사 정보만 가져오기
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

    # 키워드를 단어 인덱스 시퀀스로 변환
    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []

        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                # 해당 단어가 사전에 없는 경우, OOV 처리
                w2i.append(self.word_index['OOV'])
        return w2i
    
    # corpus.txt에서 특정단어가 들어가있는 문구를 대체하여 저장
    def replace_word(self, input_file, chage_file, target_word, replace_word):
        # 파일읽기
        with open(input_file, 'r', encoding='UTF-8') as file:
            content = file.readlines()
            es = []
            num=0
            # target_word가 들어간 문장만 찾아서 리스트로 정렬
            for i in list(content):
                if num > len(content):
                    break
                if search(target_word,i) and i:
                    num +=1
                    es.append(i)
            # 찾은 target_word가 들어간 문장들을 replace_word단어로 교체 후 저장
            es_new = []
            for i in es:
                temp = i.replace(target_word,replace_word)
                es_new.append(temp)
            str_es = ''.join(es_new)

            with open(chage_file, 'w', encoding='UTF-8') as file:
                file.write(str_es)

    # 2개의 txt 파일을 병합
    def merge_file(self, file1, file2, output_file):
        with open(file1, 'r', encoding='UTF-8') as file1:
            file1_content = file1.read()

        with open(file2, 'r', encoding='UTF-8') as file2:
            file2_content = file2.read()

        merge_content = file1_content + file2_content

        with open(output_file, 'w', encoding='UTF-8') as output_file:
            output_file.write(merge_content)

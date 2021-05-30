import nltk
from nltk.corpus import stopwords
from stanfordcorenlp import StanfordCoreNLP

NameAndLocation = ['adam', 'allan', 'andrew', 'anthony', 'austin', 'bill', 'bob', 'brandon', 'brian', 'charles',
               'chris', 'christopher',
               'daniel', 'david', 'dennis', 'donald', 'douglas', 'edward', 'eric', 'frank', 'george', 'henry',
               'james', 'jason', 'jeffrey',
               'jeshua', 'jim', 'john', 'joseph', 'keith', 'kenneth', 'kevin', 'mark', 'matthew', 'michael', 'mike',
               'nicholas', 'patrick',
               'paul', 'peter', 'phillip', 'reed', 'richard', 'robert', 'roy', 'ryan', 'sam', 'samuel', 'scott',
               'steven', 'thomas', 'tom',
               'william', 'anna', 'amy', 'andrea', 'barbara', 'catherine', 'cathy', 'charlotte', 'christina',
               'christine', 'daisy',
               'deborah', 'elizabeth', 'ellen', 'emily', 'hannah', 'helen', 'jacqueline', 'jane', 'jennifer',
               'jessica', 'joan', 'judy',
               'julia', 'julie', 'karen', 'katherine', 'kelly', 'laura', 'linda', 'lisa', 'maria', 'martha', 'mary',
               'maureen', 'melissa',
               'michelle', 'nancy', 'nicole', 'pam', 'pamela', 'phyllis', 'rachel', 'rebecca', 'samantha', 'sarah',
               'sharon', 'susan',
               'tina', 'tracy', 'wendy', 'london', 'england', 'liverpool', 'manchester', 'sheffield', 'birmingham',
               'coventry', 'leeds',
               'scotland', 'glasgow', 'edinburgh', 'wales', 'cardiff', 'belfast', 'ireland', 'dublin', 'australia',
               'canberra', 'queensland',
               'brisbane', 'north', 'south', 'west', 'east', 'wales', 'sydney', 'australia', 'adelaide', 'victoria',
               'melbourne', 'western',
               'perth', 'zealand', 'wellington', 'canada', 'ottawa', 'british', 'columbia', 'vancouver', 'toronto',
               'quebec', 'montreal',
               'america', 'washington', 'boston', 'chicago', 'atlanta', 'seattle', 'los', 'angeles', 'russia',
               'russian', 'egypt', 'australian',
               'austria', 'austrian', 'belgium', 'brazil', 'brazilian', 'britain', 'canadian', 'chaina', 'chinese',
               'denmark', 'danish', 'egyptian',
               'finland', 'finnish', 'france', 'french', 'greece', 'greek', 'hungary', 'hungarian', 'italy',
               'italian', 'japan', 'japanese', 'korea',
               'korean', 'mexico', 'mexican', 'irish', 'poland', 'polish', 'portugal', 'portugese', 'scotland',
               'scottish', 'africa', 'african',
               'spain', 'spanish', 'sweden', 'swedish', 'switzerland', 'swiss', 'netherlands', 'dutch', 'turkey',
               'turkish', 'uk', 'usa', 'american',
               'welsh', 'germany', 'german', 'rome', 'roman', 'thailand', 'thai', 'asia', 'asian', 'europe',
               'european', 'antarctica']
attribute = ['name', 'id', 'address', 'email', 'date', 'color', 'length', 'time', 'year', 'password','age','weight','height',
             'shape','size','position','speed','direction','username','password']
others = ['object', 'knowledge', 'idea', 'information', 'example', 'pdf', 'job', 'zip','git','github','mi','-s','https','service.py'
        ,'web','website','flask','url','html','www','python','software','http','com','pdf','zip','october','yes','//www.github.com',
        'oaps','seconds','javascripts','/search','/downvote/commentid','/upvote/commentid','/downvote/articleid','/subjects','e.g.',
          '']
special = ['~','!','@','#','%','^','&','/','*','(',')','+','<','>',',','.','[',']']

#save the result which has symbol 'nsubj'、'obj' and 'compound'.
# Example ('nsubj','谓语','主语'), ('obj','谓语','宾语'),('compound','词1','词2')
def dependency_parsing(string,tfidf_noun_top5):
    nlp = StanfordCoreNLP(r'D:\stanford-corenlp-4.2.0')
    dict = {}
    sents = nltk.sent_tokenize(string)
    for sent in sents:
        dependencyParsing = nlp.dependency_parse(sent)
        token = nltk.word_tokenize(sent)
        token_len = len(token)
        # print('Current sentence:'+str(sent))
        # print('Current word segmentation result:'+str(token))
        # # print(token_len)
        # print('Dependency parse result:'+str(dependencyParsing))
        # print('-'*150)
        predicate = 0
        class_index = 0
        classname = ''

        # select class name and add class name to dictionary
        for element in dependencyParsing:
            index_NN = element[2]
            if index_NN <= token_len:
                if 'nsubj' in element[0] and token[index_NN-1] in tfidf_noun_top5 and token[index_NN-1] not in dict:
                    dict[token[index_NN-1]] = {'attributes': [], 'methods': []}

        #select method name and add method name to right place in the dictionary
        for element in dependencyParsing:
            index_VB = element[2]
            if index_VB <= token_len:
                if 'nsubj' in element[0] and token[index_VB-1] in dict:
                    predicate = element[1]  # obj is the index of predicate
                    class_index = element[2]  # token[class_index-1]表示类名
                    classname = token[class_index - 1]
                if 'obj' == element[0] and element[1] == predicate and token[index_VB - 1] not in dict[classname]['methods']:
                    method_name = token[predicate - 1] + ' ' + token[index_VB - 1]
                    dict[classname]['methods'].append(method_name)

        #select attribute name and add attribute name to right place in the dictionary
        for element in dependencyParsing:
            index_MD = element[2]
            if index_MD <= token_len:
                if 'nsubj' in element[0] and token[index_MD - 1] in dict:
                    class_index = index_MD  # token[class_index-1]表示类名
                    classname = token[class_index - 1]
                    # print('classname is:')
                    # print(classname)
                    # print(dict)
                    # print(token)
                if classname is not '' and token[index_MD - 1] in attribute and token[index_MD-1] not in dict[classname]['attributes']:
                    # print(token[index_MD-1])
                    # print(dict[classname]['attributes'])
                    attribute_name = token[index_MD - 1]
                    dict[classname]['attributes'].append(attribute_name)
    return dict

#token[index-1] 表示句子分词结果数组中符号('obj','nsubj'...)对应的单词
def method_name_extraction(token,dependencyParsing):
    method_arr = []
    for element in dependencyParsing:
        index = element[2]
        class_index = 0
        if 'nsubj' in element[0] and token[index - 1] in dict:
            obj = element[1]  # obj is the index of predicate
            class_index = element[2]
        if 'obj' in element[0] and element[1] == obj and token[index-1] not in method_arr:
            method_arr.append(token[index-1])
    return method_arr

#remove stopwords
def stopwords_rm(text):
    tokens = nltk.word_tokenize(text)
    clean_tokens = []
    sr = stopwords.words('english')
    for token in tokens:
        if token not in sr and len(token) != 1 and token not in NameAndLocation and token not in others and token.isdigit() == False:
            clean_tokens.append(token)
    return clean_tokens

#use TF-IDF algorithm
def word_importance(text,list_words):
    sents = nltk.sent_tokenize(text)
    words = [nltk.word_tokenize(sent) for sent in sents]  # 对每个句子进行分词
    corpus = nltk.TextCollection(words)  # 构件语料库
    # print('--------------计算TF-IDF值-------------')
    words_tfidf = []
    for item in list_words:
        tf_idf = corpus.tf_idf(item[0], corpus)
        if tf_idf != 0:
            words_tfidf.append((item[0], tf_idf))
    return words_tfidf

#Processing TFIDF arrays with bubble sort
def tfidf_bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

#Select ten nons with highest TFIDF value
def tfidf_topn(arr,candidate_noun,candidate_verb):
    n = len(arr)-1
    data = []
    i = 0
    while i<10:
        if arr[n][0] not in attribute and arr[n][0] in candidate_noun and arr[n][0] not in candidate_verb:
            data.append(arr[n][0])
            i += 1
        n -= 1
    return data

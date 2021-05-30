import nltk
from bin.class_identify import word_importance, dependency_parsing, tfidf_bubblesort, \
    stopwords_rm, tfidf_topn

class ClassDiagramMaker:
    def __init__(self,requirement_filename):
        self.req_fname = requirement_filename

    def get_classes(self):
        with open(self.req_fname,'r',encoding='UTF-8') as file:
            text = file.read().lower()
            clean_tokens = stopwords_rm(text)
            # print('clean tokens:'+str(clean_tokens))
            # print('-' * 150)
            #find frequency most
            freq_dist = nltk.FreqDist(clean_tokens)
            print('frequency of clean words:'+str(freq_dist))
            freq_dist_most_common = freq_dist.most_common()
            print('Word frequency is sorted in ascending order:'+str(freq_dist_most_common))
            print('-' * 150)
            #part of speech tagging
            pos_words = nltk.pos_tag(clean_tokens)
            # print('Part of speech:'+str(pos_words))
            print('-' * 150)
            candidate_noun = [a for (a,b) in pos_words if 'NN' in b]
            print('candidate_noun is:'+str(candidate_noun))
            print('-' * 150)
            candidate_verb = [a for (a,b) in pos_words if 'VB' in b]
            # print('candidate_verb is:'+str(candidate_verb))
            # print('-' * 150)
            tfidf = word_importance(text,freq_dist_most_common)
            # print('TF-IDF value:'+str(tfidf))
            # print('-' * 150)
            tfidf_inc = tfidf_bubblesort(tfidf)
            print('Increment TF-IDF value:'+str(tfidf_inc))
            print('-' * 150)
            tfidf_top10_noun = tfidf_topn(tfidf_inc,candidate_noun,candidate_verb)
            print('Ten nouns with highest TF-IDF values:'+str(tfidf_top10_noun))
            print('-' * 150)
            dict = dependency_parsing(text,tfidf_top10_noun)
            print(dict)

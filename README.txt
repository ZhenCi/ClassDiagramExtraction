    bin存放启动文件
    core存放逻辑文件
    tests存放测试文件

一、关键词提取

    关键词是能够表达文档中心内容的词语，常用于计算机系统标引论文内容特征、信息检索、系统汇集以供读者检阅。关键词提取是文本挖掘领域
的一个分支，是文本检索、文档比较、摘要生成、文档分类和聚类等文本挖掘研究的基础性工作。
    从算法的角度来看，关键词提取算法主要有两类：无监督关键词提取方法和有监督关键词提取方法。

1.无监督关键词提取方法

    不需要人工标注的语料，利用某些方法发现文本中比较重要的词作为关键词，进行关键词提取。该方法是先抽取出候选词， 然后对各个候选词进
行打分，然后输出topK个分支最高的候选词作为关键词。根据打分的策略不同，有不同的算法，例如TF-IDF,TextRank,LDA等算法。

    无监督关键词提取方法主要有三类：基于统计特征的关键词提取(TF,TF-IDF);基于词图模型的关键词提取(PageRank,TextRank);基于主题模型
的关键词提取(LDA)
    1)基于统计特征的关键词提取算法的思想是利用文档中词语的统计信息抽取文档的关键词；
    2)基于词图模型的关键词提取首先要构件文档的语言网络图，然后对语言进行网络图分析，在这个图上寻找具有重要作用的词语或者短语，这些
短语就是文档的关键词；
    3)基于主题关键词提取算法主要利用的是主体模型中关于主题分布的性值进行关键词提取；

2.有监督关键词提取方法

    将关键词抽取过程视为二分类问题，先提取出候选词，然后对于每个候选词划定标签，要么是关键词，要么不是关键词，然后训练关键词抽取分
类器.当信赖一篇文档时，抽取出所有的候选词，然后利用训练好的关键词提取分类器，对各个候选词进行分类，最终将标签为关键词的候选词作为关
键词。

3.无监督方法和有监督方法的优缺点

    无监督方法不需要人工标注训练集合的过程，因此更加快捷，但由于无法有效综合利用多种信息对候选关键词排序，所以效果无法与有监督方法
媲美；而有监督方法可以通过训练学习调节多种信息对于判断关键词的影响成都，因此效果更有，有监督的文本关键词提取算法需要高昂的人工成本，
因此现有的文本关键词提取主要采用适用性较强的无监督关键词提取。


    TF-IDF（term frequency-inverse document frequency,词频-逆向文件词频）是一种用于信息检索(information retrival)与文本挖掘
(text mining)的常用加权技术。
    TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。字词的重要性随着它在文件中出现的次数
成正比增加，但同时会随着它在语料库中出现的频率成反比下降。
    TF-IDF的主要思想是：如果某个单词在一篇文章中出现的频率TF高

    命名实体识别（Named Entity Recognition,简称NRE）,又称作“专名识别”，是指识别文本中具有特定意义的实体，主要包括认名、地名、机
构名、专有名词等。简单地将，就是识别自然文本中的实体指称的边界和类别

类名和属性名、方法名之间的关系
1.arr[0] == 'nsubj' ,


ROOT：要处理文本的语句
IP：简单从句
NP：名词短语
VP：动词短语
PU：断句符，通常是句号、问号、感叹号等标点符号
LCP：方位词短语
PP：介词短语
CP：由‘的’构成的表示修饰性关系的短语
DNP：由‘的’构成的表示所属关系的短语
ADVP：副词短语
ADJP：形容词短语
DP：限定词短语
QP：量词短语
NN：常用名词
NR：固有名词
NT：时间名词
PN：代词
VV：动词
VC：是
CC：表示连词
VE：有
VA：表语形容词
AS：内容标记（如：了）
VRD：动补复合词
CD: 表示基数词
DT: determiner 表示限定词
EX: existential there 存在句
FW: foreign word 外来词
IN: preposition or conjunction, subordinating 介词或从属连词
JJ: adjective or numeral, ordinal 形容词或序数词
JJR: adjective, comparative 形容词比较级
JJS: adjective, superlative 形容词最高级
LS: list item marker 列表标识
MD: modal auxiliary 情态助动词
PDT: pre-determiner 前位限定词
POS: genitive marker 所有格标记
PRP: pronoun, personal 人称代词
RB: adverb 副词
RBR: adverb, comparative 副词比较级
RBS: adverb, superlative 副词最高级
RP: particle 小品词
SYM: symbol 符号
TO:”to” as preposition or infinitive marker 作为介词或不定式标记
WDT: WH-determiner WH限定词
WP: WH-pronoun WH代词
WP$: WH-pronoun, possessive WH所有格代词
WRB:Wh-adverb WH副词

关系表示
abbrev: abbreviation modifier，缩写
acomp: adjectival complement，形容词的补充；
advcl : adverbial clause modifier，状语从句修饰词
advmod: adverbial modifier状语
agent: agent，代理，一般有by的时候会出现这个
amod: adjectival modifier形容词
appos: appositional modifier,同位词
attr: attributive，属性
aux: auxiliary，非主要动词和助词，如BE,HAVE SHOULD/COULD等到
auxpass: passive auxiliary 被动词
cc: coordination，并列关系，一般取第一个词
ccomp: clausal complement从句补充
complm: complementizer，引导从句的词好重聚中的主要动词
conj : conjunct，连接两个并列的词。
cop: copula。系动词（如be,seem,appear等），（命题主词与谓词间的）连系
csubj : clausal subject，从主关系
csubjpass: clausal passive subject 主从被动关系
dep: dependent依赖关系
det: determiner决定词，如冠词等
dobj : direct object直接宾语
expl: expletive，主要是抓取there
infmod: infinitival modifier，动词不定式
iobj : indirect object，非直接宾语，也就是所以的间接宾语；
mark: marker，主要出现在有“that” or “whether”“because”, “when”,
mwe: multi-word expression，多个词的表示
neg: negation modifier否定词
nn: noun compound modifier名词组合形式
npadvmod: noun phrase as adverbial modifier名词作状语
nsubj : nominal subject，名词主语
nsubjpass: passive nominal subject，被动的名词主语
num: numeric modifier，数值修饰
number: element of compound number，组合数字
parataxis: parataxis: parataxis，并列关系
partmod: participial modifier动词形式的修饰
pcomp: prepositional complement，介词补充
pobj : object of a preposition，介词的宾语
poss: possession modifier，所有形式，所有格，所属
possessive: possessive modifier，这个表示所有者和那个’S的关系
preconj : preconjunct，常常是出现在 “either”, “both”, “neither”的情况下
predet: predeterminer，前缀决定，常常是表示所有
prep: prepositional modifier
prepc: prepositional clausal modifier
prt: phrasal verb particle，动词短语
punct: punctuation，这个很少见，但是保留下来了，结果当中不会出现这个
purpcl : purpose clause modifier，目的从句
quantmod: quantifier phrase modifier，数量短语
rcmod: relative clause modifier相关关系
ref : referent，指示物，指代
rel : relative
root: root，最重要的词，从它开始，根节点
tmod: temporal modifier
xcomp: open clausal complement
xsubj : controlling subject 掌控者
中心语为谓词
  subj — 主语
 nsubj — 名词性主语（nominal subject） （同步，建设）
   top — 主题（topic） （是，建筑）
npsubj — 被动型主语（nominal passive subject），专指由“被”引导的被动句中的主语，一般是谓词语义上的受事 （称作，镍）
 csubj — 从句主语（clausal subject），中文不存在
 xsubj — x主语，一般是一个主语下面含多个从句 （完善，有些）
中心语为谓词或介词
   obj — 宾语
  dobj — 直接宾语 （颁布，文件）
  iobj — 间接宾语（indirect object），基本不存在
 range — 间接宾语为数量词，又称为与格 （成交，元）
  pobj — 介词宾语 （根据，要求）
  lobj — 时间介词 （来，近年）
中心语为谓词
  comp — 补语
 ccomp — 从句补语，一般由两个动词构成，中心语引导后一个动词所在的从句(IP) （出现，纳入）
 xcomp — x从句补语（xclausal complement），不存在
 acomp — 形容词补语（adjectival complement）
 tcomp — 时间补语（temporal complement） （遇到，以前）
lccomp — 位置补语（localizer complement） （占，以上）
       — 结果补语（resultative complement）
中心语为名词
   mod — 修饰语（modifier）
  pass — 被动修饰（passive）
  tmod — 时间修饰（temporal modifier）
 rcmod — 关系从句修饰（relative clause modifier） （问题，遇到）
 numod — 数量修饰（numeric modifier） （规定，若干）
ornmod — 序数修饰（numeric modifier）
   clf — 类别修饰（classifier modifier） （文件，件）
  nmod — 复合名词修饰（noun compound modifier） （浦东，上海）
  amod — 形容词修饰（adjetive modifier） （情况，新）
advmod — 副词修饰（adverbial modifier） （做到，基本）
  vmod — 动词修饰（verb modifier，participle modifier）
prnmod — 插入词修饰（parenthetical modifier）
   neg — 不定修饰（negative modifier） (遇到，不)
   det — 限定词修饰（determiner modifier） （活动，这些）
 possm — 所属标记（possessive marker），NP
  poss — 所属修饰（possessive modifier），NP
  dvpm — DVP标记（dvp marker），DVP （简单，的）
dvpmod — DVP修饰（dvp modifier），DVP （采取，简单）
  assm — 关联标记（associative marker），DNP （开发，的）
assmod — 关联修饰（associative modifier），NP|QP （教训，特区）
  prep — 介词修饰（prepositional modifier） NP|VP|IP（采取，对）
 clmod — 从句修饰（clause modifier） （因为，开始）
 plmod — 介词性地点修饰（prepositional localizer modifier） （在，上）
   asp — 时态标词（aspect marker） （做到，了）
partmod– 分词修饰（participial modifier） 不存在
   etc — 等关系（etc） （办法，等）
中心语为实词
  conj — 联合(conjunct)
   cop — 系动(copula) 双指助动词？？？？
    cc — 连接(coordination)，指中心词与连词 （开发，与）
其它
  attr — 属性关系 （是，工程）
cordmod– 并列联合动词（coordinated verb compound） （颁布，实行）
  mmod — 情态动词（modal verb） （得到，能）
    ba — 把字关系
tclaus — 时间从句 （以后，积累）
       — semantic dependent
   cpm — 补语化成分（complementizer），一般指“的”引导的CP （振兴，的）


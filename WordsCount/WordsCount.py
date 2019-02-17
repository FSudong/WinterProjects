import sys,re,collections,nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
'''
    统计字符串中的单词数目——统计字符串中单词的数目，更复杂的话从一个文本中读出字符串并生成单词数目统计结果。
'''
pat_letter = re.compile(r'[^a-zA-Z \']+')


# 找到代词后面的代词。 re.I是指忽略大小写
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
# 找到单词后面的's  如： he's
pat_s = re.compile("(?<=[a-zA-Z])\'s")
# 找到以s结尾的单词后面的'  如: apples'
pat_s2 = re.compile("(?<=s)\'s?")
# 找到not的缩写 't
pat_not = re.compile("(?<=[a-zA-Z])n\'t")
# 找到would的缩写 'd
pat_would = re.compile("(?<=[a-zA-Z])\'d")
# 找到will的缩写 'll
pat_will = re.compile("(?<=[a-zA-Z])\'ll")
# 找到am的缩写 'm
pat_am = re.compile("(?<=[I|i])\'m")
# 找到are的缩写 're
pat_are = re.compile("(?<=[a-zA-Z])\'re")
# 找到have的缩写 've
pat_ve = re.compile("(?<=[a-zA-Z])\'ve")



stopwords = open('english.txt',encoding='utf-8')


lmtzr = WordNetLemmatizer()


def get_words(file):
    with open(file, encoding='gb18030') as f:
        words_box = []
        pat = re.compile(r'[^a-zA-Z \']+')

        for line in f:
            words_box.extend(pat.sub(' ', line).strip().lower().split())
            words_box.extend(merge(replace_abbreviations(line).split()))

    return collections.Counter(words_box)


def merge(words):
    new_words = []
    for word in words:
        if word:
            tag = nltk.pos_tag(word_tokenize(word))
            pos = get_wordnet_pos(tag[0][1])
            if pos:
                lemmatized_word = lmtzr.lemmatize(word, pos)
                new_words.append(lemmatized_word)
            else:
                new_words.append(word)
    return new_words


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''


def replace_abbreviations(text):
    new_text = text
    new_text = pat_letter.sub(' ', text).strip().lower()
    new_text = pat_is.sub(r"\1 is", new_text)
    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')
    return new_text


def append_ext(words):
    new_words = []
    for item in words:
        word, count = item
        tag = nltk.pos_tag(word_tokenize(word))[0][1]
        new_words.append((word, count, tag))
    return new_words


def write_to_file(words, file='results.txt'):
    f = open(file, 'w', encoding='gb18030')
    for item in words:
        for field in item:
            f.write(str(field) + ',')
        f.write('\n')


if __name__ == '__main__':
    book = sys.argv[1]
    if not book:
        "MicroMP3.txt"
    print("counting...")
    words = get_words(book)
    print("writing file...")
    write_to_file(append_ext(words.most_common()))
    print("results have been writted in file result.txt ")


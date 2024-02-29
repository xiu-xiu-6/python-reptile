import jieba
import pandas as pd

import wordcloud

stopwords_filepath = r"scu_stopwords.txt" #引用停用词
# 读取CSV文件
df = pd.read_csv('Book250.csv', encoding='utf_8_sig')

# 提取一句话评价列数据
comments = df['一句话评价'].dropna().tolist()  # 转换为列表
# 创建停用词list
def stopwordslist(stopwords_filepath):
    stopwords = [line.strip() for line in open(stopwords_filepath, 'r',
                                               encoding='utf-8-sig', errors='ignore').readlines()]
    return stopwords

# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(stopwords_filepath)  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# inputs = open(r'commentsAll.txt', 'r', encoding='utf-8', errors='ignore')
outputs = open(r'result2.txt', 'w',encoding='utf-8')
for comment in comments:
    line_seg = seg_sentence(comment)
    outputs.write(line_seg + '\n')
outputs.close()
# inputs.close()

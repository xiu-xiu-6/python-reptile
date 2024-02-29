import pandas as pd
import jieba
from collections import Counter
import nltk

nltk.download('punkt')  # 下载必要的语料库文件

# 读取CSV文件
df = pd.read_csv('Book250.csv', encoding='utf_8_sig')

# 提取一句话评价列数据
comments = df['一句话评价'].dropna().tolist()  # 转换为列表

# 分词和统计词频
words = []
for comment in comments:
    seg_list = jieba.cut(comment)  # 使用jieba进行分词
    words.extend(seg_list)

# 去除停用词（可根据实际情况自定义停用词表）
stop_words = ['这', '那', '更']
words = [word for word in words if word not in stop_words]

# 统计词频
word_count = Counter(words)

# 输出词频统计结果
for word, count in word_count.most_common(10):  # 输出出现频率最高的前10个词
    print(word, count)

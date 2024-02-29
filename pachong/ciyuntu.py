import jieba.analyse
import wordcloud

path = 'result2.txt'
file_in = open(path, encoding='utf-8')
s = file_in.read()
y = ''

for x, w in jieba.analyse.extract_tags(s, topK=100, withWeight=True):  # 基于 TF-IDF 算法，抽取10个关键词
    print('%s %s' % (x, w))
    y += x + ' '
print(y)
wc = wordcloud.WordCloud(
    width=1000,
    height=700,  # 词云比例
    background_color='white',  # 图片背景颜色
    font_path='D:/下载/SimHei.ttf',  # 词云字体
    max_words=100,
)
# 给词云输入文字
wc.generate(y)
# 词云图保存图片地址
wc.to_file('yun.png')
# 开发日期：{DATA}

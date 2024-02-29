# python 爬取豆瓣图书的书籍信息

#### 介绍
实现python爬取豆瓣图书的信息，并将信息保存到csv文件当中，提取高频关键词生成词云

#### 软件架构
软件架构说明

IDE：PyCharm

python version:3.8



#### 使用说明

##### 1. 导入依赖库
- requests库：用于发送HTTP请求，获取网页内容。
- BeautifulSoup库：用于解析HTML网页，提取所需数据。
- pandas库：用于将数据保存为CSV文件。
- Jieba库：用于中文分词。
- wordcloud库：用于生成词云频率图。


##### 2. 设置全局变量

根据所要提取的信息设置全局变量，通过列表来将爬取到的数据进行临时存储
``` book_name = []  # 书名
book_url = []  # 书籍链接
book_star = []  # 书籍评分
book_star_people = []  # 评分人数
book_author = []  # 书籍作者
book_translater = []  # 书籍译者
book_publisher = []  # 出版社
book_pub_year = []  # 出版日期
book_price = []  # 书籍价格
book_comment = []  # 一句话评价
```
##### 3.  函数定义
定义一个get_book_info（后面简写为get）函数和一个save_to_csv（后面简写为save）函数，通过get函数爬取数据，其中在爬取数据的过程中有些特殊情况需要处理（如某本书没有一句话评价之类的），之后通过save函数将列表中的数据存储到csv文件当中。在main函数中定义一个请求头header和网站url,传到get函数当中进行数据爬取。



#### 进阶
##### 统计词频
获取书中的高频词，其中要对一些无效高频词进行去除。保存到csv文件当中。
##### 构造词云
读取csv文件，通过其出现频率来生成一定比例的词云图。




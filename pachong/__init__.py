# 程序功能：爬取豆瓣读数TOP250的数据
import re
import requests  # 发送请求
from bs4 import BeautifulSoup  # 解析网页
import pandas as pd  # 存取csv
from time import sleep  # 等待时间

book_name = []  # 书名
book_url = []  # 书籍链接
book_star = []  # 书籍评分
book_star_people = []  # 评分人数
book_author = []  # 书籍作者
book_translater = []  # 书籍译者
book_publisher = []  # 出版社
book_pub_year = []  # 出版日期
book_price = []  # 书籍价格
book_comment = []  # 一句话评价


def get_book_info(url, headers):
    """
    获取豆瓣书籍详情数据
    :param url: 爬取地址
    :param headers: 爬取请求头
    :return: None
    """
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    for book in soup.select('.item'):
        name = book.select('.pl2 a')[0]['title']  # 书名
        book_name.append(name)
        bkurl = book.select('.pl2 a')[0]['href']  # 书籍链接
        book_url.append(bkurl)
        star = book.select('.rating_nums')[0].text  # 书籍评分
        book_star.append(star)

        # 使用正则表达式提取评分人数
        star_people_match = re.search(r'(\d+)人评价', book.select('.pl')[1].text)
        star_people = star_people_match.group(1) if star_people_match else '未知'
        book_star_people.append(star_people)

        # 没有一句话评价的情况处理
        comment = book.select('.quote span')
        book_comment.append(comment[0].text if comment else None)

        # 使用正则表达式提取书籍信息
        info_text = book.select('.pl')[0].text
        info = re.split(r'\s*/\s*', info_text)

        # 提取作者、译者、出版社、出版日期、价格等信息
        if len(info) >= 4:
            # 假设最后两项总是出版日期和价格
            book_pub_year.append(info[-2])
            book_price.append(info[-1])
            book_publisher.append(info[-3])
            # 如果有译者，则假设第一项是作者，第二项是译者
            if "译" in info[-4] or len(info) == 5:
                book_translater.append(info[-4])
                book_author.append(info[0] if len(info) > 4 else None)
            # 否则假设没有译者
            else:
                book_translater.append(None)
                book_author.append(info[-4])
        else:
            book_author.append(None)
            book_translater.append(None)
            book_publisher.append(None)
            book_pub_year.append(None)
            book_price.append(None)


def save_to_csv(csv_name):
    """
	数据保存到csv
	:return: None
	"""
    df = pd.DataFrame()  # 初始化一个DataFrame对象
    df['书名'] = book_name
    df['豆瓣链接'] = book_url
    df['作者'] = book_author
    df['译者'] = book_translater
    df['出版社'] = book_publisher
    df['出版日期'] = book_pub_year
    df['价格'] = book_price
    df['评分'] = book_star
    df['评分人数'] = book_star_people
    df['一句话评价'] = book_comment
    df.to_csv(csv_name, encoding='utf_8_sig')  # 将数据保存到csv文件


if __name__ == "__main__":
    # 定义一个请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    # 开始爬取豆瓣数据
    for i in range(10):  # 爬取共10页，每页25条数据
        page_url = 'https://book.douban.com/top250?start={}'.format(str(i * 25))
        print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
        get_book_info(page_url, headers)
        sleep(1)  # 等待1秒
    # 保存到csv文件
    save_to_csv(csv_name="Book250.csv")

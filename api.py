# -*- coding: utf-8 -*-

import json
# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys # 文字を入力する時に使う

#ここからflaskの必要分
import os
from flask import Flask

#ここからflaskでcorsの設定 ajaxを使う時のクロスドメイン制約用
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "使い方 : /api/検索する単語/取得ページ数"

@app.route('/api/<string:word>/<int:page>') # 検索ワード/ページ数をパスから変数に受け取る
def slide(word,page):
 
    driver = webdriver.PhantomJS() # PhantomJSを使う 
    driver.set_window_size(1124, 850) # PhantomJSのサイズを指定する
    driver.implicitly_wait(20) # 指定した要素などがなかった場合出てくるまでdriverが最大20秒まで自動待機してくれる

    URL = "http://www.slideshare.net/search/"
    driver.get(URL) # slideshareのURLにアクセスする
    data_list = [] # 全ページのデータを集める配列

    search = driver.find_element_by_id("nav-search-query") # 検索欄要素を取得
    search.send_keys(word) # 検索ワードを入力
    search.submit() # 検索をsubmitする

    lang = driver.find_element_by_xpath("//select[@id='slideshows_lang']/option[@value='ja']") # 言語選択リストの日本語の部分を抽出
    lang.click() # 言語選択の日本語を選択

    for i in range(0,page): 
        print(str(i+1) + u"ページ目")
        data = driver.page_source.encode('utf-8') # ページ内の情報をutf-8で用意する
        soup = BeautifulSoup(data,"lxml") # 加工しやすいようにlxml形式にする
        slide_list = soup.find_all("div",class_="thumbnail-content") # スライド単位で抽出
        for slide in slide_list:
            slide_in = {} # スライドの情報を辞書形式でまとめる
            
            # スライドの投稿者の名前を入手
            name = slide.find("div",class_="author").text
            slide_in["name"] = name.strip() # strip()は両端の空白と改行をなくしてくれる
            
            # スライドのタイトルを入手
            title = slide.find("a",class_="title title-link antialiased j-slideshow-title").get("title") # 指定したタグ&クラス内のtitleを出す
            slide_in["title"] = title

            # スライドのリンクを入手
            link = slide.find("a",class_="title title-link antialiased j-slideshow-title").get("href") # 指定したタグ&クラス内のhrefを出す
            slide_in["link"] = "http://www.slideshare.net" + link
            
            # スライドのサムネのリンクを入手
            imagetag = slide.find("a",class_="link-bg-img").get("style") # 指定したタグ&クラス内のstyleを出す
            image = imagetag[imagetag.find("url(")+4:imagetag.find(");")] # いらない部分を取り除く
            slide_in["image"] = image
            
            # スライドのページ数であるslidesとlikesを入手
            info = slide.find("div",class_="small-info").string # slidesとlikesの文字列を入手
            slides = info[7:info.find("slides")] # slides部分を抽出
            slide_in["slides"] = slides.strip() # strip()は両端の空白と改行をなくしてくれる
            if "likes" in info:
                likes = info[info.find(", ")+2:info.find("likes")] # likes部分を抽出
            else:
                likes = "0"
            slide_in["likes"] = likes.strip() # strip()は両端の空白と改行をなくしてくれる

            data_list.append(slide_in) # data_listに1ページ分の内容をまとめる

        driver.execute_script('window.scrollTo(0, 3000)') # ページャーのある下に移動
        next = driver.find_element_by_xpath("//li[@class='arrow']/a[@rel='next']") # ページャーのNEXT要素を抽出
        next.click() # Nextボタンをクリック

    driver.close() # ブラウザ操作を終わらせる
    jsonstring = json.dumps(data_list,ensure_ascii=False,indent=2) # 作った配列をjson形式にして出力する
    return jsonstring
 
# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
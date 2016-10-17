# SlideShareをスクレイピングし、jsonにして投げてくれるAPI
URLに/api/slideshareの検索ワード/データ化するページ数
を指定してアクセスすると自動で単語で日本語のスライドを検索し、json形式で返してくれます。
## 返ってくる内容
+ title : スライドのタイトル
+ image : スライドのサムネイル
+ link : スライドへのリンク
+ name : スライドの作成者
+ slides : スライドの枚数
+ likes : スライドについたlikes数
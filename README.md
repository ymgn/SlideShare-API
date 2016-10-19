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

## Qiitaの記事
+ 前編 : [Re:ゼロからFlaskで始めるHeroku生活 〜環境構築とこんにちは世界〜](http://qiita.com/ymgn_ll/items/96cac1dcf388bc7a8e4e)
+ 中編 : [Re:ゼロからFlaskで始めるHeroku生活 〜Selenium & PhantomJS & Beautifulsoup〜](http://qiita.com/ymgn_ll/items/4c2964a14ff80ca2fa28)
+ 後編 : [Re:ゼロからFlaskで始めるHeroku生活 〜PhantomJSをHerokuへ〜](http://qiita.com/ymgn_ll/items/585e94a3d2d23ca1fec3)
# 🌋 Docker + Django + MySQL
<br></br>
### 🗽 一番最初に実行するコマンド
```
docker-compose up -d
```
OR
```
docker-compose up
```
- 上記のコマンドのどちらかを実行し、http://localhost:8001/ を見ると懐かしのあのロケットが見れる
<br></br>
### 🏰 **Docker**やterminalでdatabaseを見たい時に実行するコマンド
- 下のコマンドを打った後に
```
docker exec -it dejavu-db-1 /bin/bash
```
- こんなんなったら→sh-4.2# こちらを打つ☟
```
mysql -u root -proot
```


#### databaseの中身どうやって見るの？
- databaseを見る☟
```
show databases;
```
- dejavu-dbを使う☟

```
use dejavu-db
```
- dejavu-dbに入っているtableを見せる☟

```
show tables;
```
<br></br>
### 🍔 makemigrationsやmigrateコマンド
- makemigrations
```
docker-compose run web python3 manage.py makemigrations dejavu_app
```
- migrate
```
docker-compose run web python3 manage.py migrate
```
<br></br>
### なんかめちゃくちゃ不安定です。
- できない時とできる時がある

#### なんとか対処法
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")
```
- 上みたいなエラーが出た時、settings.pyの'HOST'の'db'を消してもう一回'db'にする
<br></br>
### 🥨 サーバーが混み合っていますみたいな画面出た
- Dockerのアプリのdejavu-web-1のLogs見てみて！エラーが出てる
- それかdocker-compose up をしてエラーを出してみて
<br></br>
### 🎠 references
- [How to build an environment](https://qiita.com/bakupen/items/f23ce3d2325b4491a2dd)
- [other environment](https://docker.hatenablog.jp/entry/2023/05/12/212955)
- [Error no matching manifest for linux/arm64/v8 in the manifest list entries](https://zenn.dev/marumarumeruru/articles/55173a98863d4e)
- [Error services.db.volumes must be a list](https://github.com/docker/compose/issues/5065)
- [Error django.db.utils.OperationalError](https://stackoverflow.com/questions/57407940/cant-connect-to-mysql-while-building-docker-compose-image)

<br></br>
<details><summary>Click here</summary><div>

#### I'm so hungry!!!
- Banana
- Apple
- Orange
- Kebab

#### I want to eat them!

</div></details>
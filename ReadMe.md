## コマンドチートシート

- source cooking/bin/activate

### 初期設定

- django-admin startproject api_cooking .
- django-admin startapp api

### migration

- python manage.py makemigrations
- python manage.py migrate

### admin 作る

- admin.site.register
- ここまでできたら python manage.py createsuperuser して RUN
  - http://127.0.0.1:8000/admin

### テスト

- user create
  - url はhttp://127.0.0.1:8000/api/register
  - email, passwordを入力
  - post
- 作ったらトークン取得できるかを POSTMAN から確認
  - http://127.0.0.1:8000/authen/jwt/createに対して、「Body」のformdataに
  - email にメアド
  - password にパスワード
  - post で
- modheader（拡張機能）でトークンを入れて、名前を Autholization にして、
  - http://127.0.0.1:8000/api/videosにブラウザで
  - トークンは「JWT （トークン）」が値になる

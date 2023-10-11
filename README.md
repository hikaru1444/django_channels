###公開先
https://github.com/hikaru1444/djangochannels

###概要

同時編集可能なスプレッドシートにPython,Djangoの強力な機能を持ち合わせたアプリとなっています。
urls.pyに1行追加するだけでDjango django.contrib.adminのような使用感でモデルを編集することができます｡


###サンプル
ここれでは、編集をするともう片方のウィンドウにも反映されること、ページの更新をしてもモデルが保存されていることを確認しています。

https://github.com/hikaru1444/djangochannels/assets/82006837/7c1e835a-c3dd-457b-ba00-013b0ba59928


###インストール

Python3,PostgreSQLをインストール


Git
git clone https://github.com/hikaru1444/djangochannels

Docker
DjangoChannelsのチュートリアルを元にDockerでredisを起動
Dockerのダウンロード先
https://www.docker.com/products/docker-desktop/
起動方法
https://channels.readthedocs.io/en/latest/tutorial/part_2.html#enable-a-channel-layer


Django
cd djangochannels
.\.venv\Scripts\activate
pip install -V requirements.txt
.envにPostgreSQL
python manage.py migrations
python manage.py runserver

http://127.0.0.1:8000にアクセスして編集が出来れば成功


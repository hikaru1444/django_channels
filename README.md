DjangoChannelsとhandsontable(MITライセンス版)を使用したスプレットシートの同時編集アプリ


チュートリアル
DjangoChannelsのチュートリアルを理解し､asyncサーバーをすでに構築しているものとする
https://channels.readthedocs.io/en/stable/


pip install -r requirements.txt(?)
git clone github.com...(?)
python manage.py runserver
http://127.0.0.1:8000/



別プロジェクトでの使用方法
注:現在は､IntegerField,CharField,DateField,TimeField,ForeignKey,BooleanField のみ対応している(DBはPostgreSQL)
IntegerField,DateField,TimeField,ForeignKeyはnull=Trueにすること

models.py
modelの作成(Fieldは上記のみ使用可)
ForeignKeyはForeignKeyWithStrToFieldを使用し､dropdownで表示したいフィールドをto_fieldで指定する
指定しない場合はIDが表示される


views.py
hotsettingsの追加可能
class クラス名(RoomView)
    model = モデル名


urls.py
path("<str:room_name>/", views.RoomView.as_view(), name="room")  # サンプル


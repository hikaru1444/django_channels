import json

from django.http import QueryDict
from django.shortcuts import render

from chat.models import Shop


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    params = {"check": "チェック:", "room_name": room_name}
    if request.method == 'POST':  # POSTの処理
        # JSON文字列の取得
        dic = QueryDict(request.body, encoding='utf-8')
        c = Shop.objects.get(pk=dic['id'])
        print("変更後", str(c), dic.get('field'), dic.get('value'))
        setattr(c, dic.get('field'), dic.get('value'))
        try:
            c.save()
        except ValueError:
            print("roomvalueerror")
            params['check'] = "チェック:エラーです｡"
    params['fields'] = [field.name for field in Shop._meta.fields]
    params['columns'] =[field.verbose_name for field in Shop._meta.fields]
    params['data'] = json.dumps(list(Shop.objects.all().values_list()))
    print("columns", params['columns'])
    return render(request, "chat/room.html", params)
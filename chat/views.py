import json

from django.http import QueryDict
from django.shortcuts import render

from chat.models import Shop
from django.http import JsonResponse


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
            params['check'] = "チェック:" + str(dic.get('value')) + "に変更しました!"
        except ValueError:
            print("roomvalueerror")
            params['check'] = "チェック:" + str(dic.get('value')) \
                              + "はエラーです｡戻すには｢ctrl+Zキー｣を押してください"
        return JsonResponse({'status': 'success', 'message': params['check']})  # JSONを返す
    params['fields'] = [field.name for field in Shop._meta.fields]
    params['columns'] = [field.verbose_name for field in Shop._meta.fields]
    params['data'] = json.dumps(list(Shop.objects.all().values_list()))
    return render(request, "chat/room.html", params)

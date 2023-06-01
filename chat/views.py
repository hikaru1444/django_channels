import json

from django.http import QueryDict
from django.shortcuts import render

from chat.models import Shop, User
from django.http import JsonResponse
from django.db import models


def index(request):
    return render(request, "chat/index.html")


# commit test
def room(request, room_name):
    params = {"check": "チェック:", "room_name": room_name}
    if request.method == 'POST':  # POSTの処理
        # JSON文字列の取得
        dic = QueryDict(request.body, encoding='utf-8')
        c = Shop.objects.get(pk=dic['id'])
        print("変更後", str(c), dic.get('field'), dic.get('value'), dic.get('type'),
              type(dic.get('type')))
        dic_value = dic.get('value')
        if dic.get('type') == 'checkbox':
            dic_value = True if dic_value == 'true' else False
        if dic.get('type') == 'dropdown':
            dic_value = User.objects.get(pk=int(dic_value))
        if dic.get('type') == 'numeric':
            dic_value = int(dic_value)
        setattr(c, dic.get('field'), dic_value)
        try:
            c.save()
            params['check'] = "チェック:" + str(dic.get('value')) + "に変更しました!"
        except ValueError:
            print("roomvalueerror")
            params['check'] = "チェック:" + str(dic.get('value')) \
                              + "は保存できません｡戻すには｢ctrl+Zキー｣を押してください"
        return JsonResponse({'status': 'success', 'message': params['check']})  # JSONを返す
    params['fields'] = [field.name for field in Shop._meta.fields]
    params['colHeaders'] = [field.verbose_name for field in Shop._meta.fields]
    params['columns'] = []

    for count, field in enumerate(Shop._meta.fields):
        column = {
            'data': count,
            'type': 'text'  # Default type is 'text'
        }
        if isinstance(field, models.BooleanField):
            column['type'] = 'checkbox'
        elif isinstance(field, models.ForeignKey):
            # Assuming you have a related model named 'RelatedModel'
            column['type'] = 'dropdown'
            print("related_model", field.related_model)
            column['source'] = [obj.id for obj in field.related_model.objects.all()]
        elif isinstance(field, models.IntegerField):
            # Assuming you have a related model named 'RelatedModel'
            column['type'] = 'numeric'

        params['columns'].append(column)

    # print(params['columns'])
    params['data'] = json.dumps(list(Shop.objects.all().values_list()))
    return render(request, "chat/room.html", params)

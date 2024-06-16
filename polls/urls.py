from django.urls import path

from . import views

urlpatterns = [
    #path関数　の4つの引数　route:必須 view:必須 kwargs(任意のキーワード引数を辞書として対象のビューに渡せます) name(URL に名前付け 特にtemplateで役立つ) 
    path("", views.index, name="index"),
]
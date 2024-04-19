from django.shortcuts import render,redirect
from .models import User,Aikotoba

#ログイン処理
def Login(request):

    #GET時/初期画面を返す
    if request.method == 'GET':
        return render(request,'login.html') 

    #POST時/ログイン処理を行う
    elif request.method == 'POST':
        
        #画面項目を変数へ格納
        user_name = request.POST['username']
        password = request.POST['password']
        aikotoba = request.POST['aikotoba']

        # DB検索
        UserInf = User.objects.filter(username=user_name).first()
        AikotobaInf = Aikotoba.objects.first()

        # DB検索結果チェック
        if not UserInf:
            error_message = "登録されていないユーザ名です。"
            return render(request, 'login.html', {'error_message': error_message})
        
        if UserInf.password != password:
            error_message = "パスワードが違います。"
            return render(request, 'login.html', {'error_message': error_message})

        if AikotobaInf.aikotoba != aikotoba:
            error_message = "合言葉が違います。"
            return render(request, 'login.html', {'error_message': error_message})
        

        # エラーがない場合：テトリス画面へ
        return render(request,'multi_post.html', {'userInf': UserInf, 'checked': True, 'select_human': "common"})

from django.shortcuts import render
from .models import HumansImage,MemberWorks
from django.http import HttpResponse
from django.utils.timezone import make_aware
import datetime

#みんなの作品-初期処理
def works_init(request):

    if request.method == 'GET':
        return render(request,'multi_post.html', {'checked': False, 'select_human': "common"})

    elif request.method == 'POST':
        
        #画面項目を変数へ格納
        username = request.POST['username']
        checked = request.POST['checked']
        select_human = request.POST['select_human']

        context = context_maker(username, checked, select_human, "")

        return render(request,'team_works.html', context)



#みんなの作品-登録
def works_insert(request):

    # GET時/初期画面を返す
    if request.method == 'GET':
        return render(request,'login.html') 

    #POST時/DB登録を行う
    elif request.method == 'POST':

        #画面へ返す項目
        username = request.POST['username']
        select_human = request.POST['select_human']
        checked = request.POST['checked']

        #タイトル重複排除処理
        request_title = request.POST['title-name']
        ExistTitle = MemberWorks.objects.filter(title=request_title).first()

        if ExistTitle:
            error_message = "すでに登録済みのタイトルです。別のタイトル名で登録してください。"
            context = context_maker(username, checked, select_human, error_message)
            return render(request,'team_works.html', context)

        work_obj = MemberWorks()
        
        #画面項目をDBへ登録
        work_obj.member = request.POST['select_human']
        work_obj.date = make_aware(datetime.datetime.now())
        work_obj.title = request.POST['title-name']
        work_obj.picture = request.FILES['img-name']
        work_obj.link = request.POST['link-name']
        if  request.POST.get('file-name', None) == None:
            work_obj.file = request.FILES['file-name']
        
        work_obj.explanation = request.POST['message-text']

        work_obj.save()

        context = context_maker(username, checked, select_human, "")
        return render(request,'team_works.html', context)



#みんなの作品-削除
def works_delete(request):

    # GET時/初期画面を返す
    if request.method == 'GET':
        return render(request,'login.html') 

    #POST時/DB削除を行う
    elif request.method == 'POST':
        
        #画面項目をDBへ登録
        username = request.POST['username']
        checked = request.POST['checked']
        select_human = request.POST['select_human']
        delete_title = request.POST['delete_title']

        #削除
        result = MemberWorks.objects.get(title=delete_title)
        result.delete()

        context = context_maker(username, checked, select_human, "")
        return render(request,'team_works.html', context)



#共通の画面返却処理
def context_maker(username, checked, select_human, message):

        #DB検索-メンバー画像
        masaya_img = HumansImage.objects.filter(title="masaya").first()
        konitan_img = HumansImage.objects.filter(title="konitan").first()
        paisen_img = HumansImage.objects.filter(title="paisen").first()
        leo_img = HumansImage.objects.filter(title="leo").first()
        ryotaro_img = HumansImage.objects.filter(title="ryotaro").first()

        member_imgs = {
            'masaya': masaya_img,
            'konitan': konitan_img,
            'paisen': paisen_img,
            'leo': leo_img,
            'ryotaro': ryotaro_img,
        }

        #DB検索-作品一覧
        all_works = MemberWorks.objects.filter(member=select_human, is_delete=False).order_by('date')

        #コンテキストを作成
        context = {'username':username,
                    'checked':checked,
                    'select_human':select_human,
                    'member_imgs':member_imgs,
                    'all_works':all_works,
                    'message':message,}

        # エラーがない場合：テトリス画面へ
        return context

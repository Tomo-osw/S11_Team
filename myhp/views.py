from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView #テンプレートタグ
from .forms import AccountForm #ユーザーアカウントフォーム
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)

                # ホームページ遷移
                return HttpResponseRedirect(reverse('myhp:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'Login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('myhp:Login'))

@login_required
def home(request):
    template = loader.get_template('home.html')
    context = {"UserID":request.user,}
    return HttpResponse(template.render(context, request))


@login_required
def makelist(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のタイトル・詳細・閲覧の有無の取得
        user = request.user
        listtitle = request.POST.get('listtitle')
        listdiscription = request.POST.get('listdiscription')
        onpublic = request.POST.get('on')

        if onpublic == True:
            list = Lists.objects.create(user_id_id=user.id, list_title=listtitle, list_discription=listdiscription, or_list_public=True)
        else:
            list = Lists.objects.create(user_id_id=user.id, list_title=listtitle, list_discription=listdiscription, or_list_public=True)
        
        return HttpResponseRedirect(reverse('myhp:home'))
    else:
        return render(request, 'makelist.html')

@login_required
def makepost(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のタイトル・詳細・閲覧の有無の取得
        user = request.user
        posttitle = request.POST.get('posttitle')
        postdiscription = request.POST.get('postdiscription')
        address = request.POST.get('address')
        placename = request.POST.get('placename')
        postimage = request.POST.get('postimage')
        postlink = request.POST.get('postlink')
        postdate = request.POST.get('postdate')
        posthashtag = request.POST.get('posthashtage')
        onpublic = request.POST.get('on')
        listvalue = request.POST.get('listvalue')
        listid = Lists.objects.get(list_title=listvalue)
        if onpublic == 'on':
            list = Posts.objects.create(list_id=listid, user_id_id=user.id, address=address, place_name=placename, post_title=posttitle, post_discription=postdiscription, post_image=postimage, post_link=postlink, post_date=postdate, post_hashtag=posthashtag, or_datail=onpublic)
        else:
            list = Posts.objects.create(list_id=listid, user_id_id=user.id, address=address, place_name=placename, post_title=posttitle, post_discription=postdiscription, post_image=postimage, post_link=postlink, post_date=postdate, post_hashtag=posthashtag, or_datail=onpublic)
        
        return HttpResponseRedirect(reverse('myhp:home'))
    else:
        return render(request, 'makepost.html')

class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

            return HttpResponseRedirect(reverse('myhp:home'))

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)



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

from django.shortcuts import render
from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム

from django.utils import timezone
from .models import TestPost, OldWaterTemperature,OldWaterHigh,MapDanger,WRCSAll
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# slack機能
from .slack_post import slack_post_test, slack_post_water_temp,slack_post_water_high

class TestViews(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    datas = TestPost.objects.all()
    print("GET-OK")
    return render(request, 'wrcsystem/test_post_list.html', {'datas': datas})

  def post(self, request, *args, **kwargs):
    context = TestPost(title=request.POST["title"],text=request.POST["text"])
    context.save()
    print(context.text) 
    slack_post_test(context.title,context.text)
    datas = TestPost.objects.all()
    print("POST-OK")
    return render(request, 'wrcsystem/test_post_list.html', {'datas': datas})

class WaterTemperatureViews(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    latest_data = OldWaterTemperature.objects.all().last()
    datas = OldWaterTemperature.objects.all()
    print("GET-OK")
    return render(request, 'wrcsystem/water_temperature_list.html', {'datas': datas, 'latest_data': latest_data})

  def post(self, request, *args, **kwargs):
    fahrenheit = (float(request.POST["celsius"])*9/5)+32
    context = OldWaterTemperature(RaspberryPi_Name=request.POST["RaspberryPi_Name"],celsius=request.POST["celsius"],fahrenheit=fahrenheit) 
    context.save()
    print(context)
    slack_post_water_temp(context.RaspberryPi_Name,context.celsius,context.fahrenheit)
    print("Slack-OK")
    latest_data = OldWaterTemperature.objects.all().last()
    datas = OldWaterTemperature.objects.all()
    print("POST-OK")
    return render(request, 'wrcsystem/water_temperature_list.html', {'datas': datas, 'latest_data': latest_data})

class WaterHighViews(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    latest_data = OldWaterHigh.objects.all().last()
    datas = OldWaterHigh.objects.all()
    print("GET-OK")
    return render(request, 'wrcsystem/water_high_list.html', {'datas': datas, 'latest_data': latest_data})
  def post(self, request, *args, **kwargs):
    context = OldWaterHigh(RaspberryPi_Name=request.POST["RaspberryPi_Name"],high=int(float(request.POST["high"])*100))
    context.save()
    print(context.high) 
    slack_post_water_high(context.RaspberryPi_Name,context.high)
    latest_data = OldWaterHigh.objects.all().last()
    datas = OldWaterHigh.objects.all()
    print("POST-OK")
    return render(request, 'wrcsystem/water_high_list.html', {'datas': datas, 'latest_data': latest_data})

class RiskMapViews(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    datas = MapDanger.objects.filter(risk=1)
    print("GET-OK")
    return render(request, 'wrcsystem/riskmap.html', {'datas': datas})

@login_required
def delete_test(request, *args, **kwargs):
    print("DELETE-OK")
    id_list = request.POST.getlist("delete")
    print(id_list)
    for id in id_list:
        content = TestPost.objects.filter(id=id).first()
        TestPost.delete(content)
    datas = TestPost.objects.all()
    return render(request, 'wrcsystem/test_post_list.html', {'datas': datas})


@login_required
def delete_water_temperature(request, *args, **kwargs):
    print("DELETE-OK")
    id_list = request.POST.getlist("delete")
    print(id_list)
    for id in id_list:
        content = OldWaterTemperature.objects.filter(id=id).first()
        OldWaterTemperature.delete(content)
    datas = OldWaterTemperature.objects.all()
    latest_data = OldWaterTemperature.objects.all().last()
    return render(request, 'wrcsystem/water_temperature_list.html', {'datas': datas, 'latest_data': latest_data})

@login_required
def delete_water_high(request, *args, **kwargs):
    print("DELETE-OK")
    id_list = request.POST.getlist("delete")
    print(id_list)
    for id in id_list:
        content = OldWaterHigh.objects.filter(id=id).first()
        OldWaterHigh.delete(content)
    datas = OldWaterHigh.objects.all()
    latest_data = OldWaterHigh.objects.all().last()
    return render(request, 'wrcsystem/water_high_list.html', {'datas': datas, 'latest_data': latest_data})


@csrf_exempt
def raspost_test(request):
    context = TestPost(title=request.POST["title"],text=request.POST["text"])
    context.save()
    print(context)
    print("RAS-POST-OK")
    return render(request, 'wrcsystem/ras_post.html')

@csrf_exempt
def raspost_water_temp(request):
    context = OldWaterTemperature(RaspberryPi_Name=request.POST["RaspberryPi_Name"],celsius=request.POST["celsius"],fahrenheit=request.POST["fahrenheit"])
    context.save()
    print(context)
    print("RAS-POST-OK")
    return render(request, 'wrcsystem/ras_post.html')

@csrf_exempt
def raspost_water_high(request):
    context = OldWaterHigh(RaspberryPi_Name=request.POST["RaspberryPi_Name"],high=int(float(request.POST["high"])*100))
    context.save()
    print(context)
    print("RAS-POST-OK")
    return render(request, 'wrcsystem/ras_post.html')

@csrf_exempt
def raspost_risk_map(request):
    context = MapDanger()
    context.save()
    print(context)
    print("RAS-POST-OK")
    return render(request, 'wrcsystem/ras_post.html')


test_list = TestViews.as_view()
water_temperature_list = WaterTemperatureViews.as_view()
water_high_list = WaterHighViews.as_view()
riskmap_list = RiskMapViews.as_view()


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
                return HttpResponseRedirect(reverse('index'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'account/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('index'))

#ホーム
def index(request):
    params = {"UserID":request.user,}
    return render(request, "wrcsystem/index.html",context=params)

#全データ一覧
def data_all(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "water_level_asc" in request.GET:
        datas = WRCSAll.objects.order_by('water_level').all()
    elif "water_level_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-water_level').all()
    elif "water_temp_asc" in request.GET:
        datas = WRCSAll.objects.order_by('water_temperature').all()
    elif "water_temp_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-water_temperature').all()
    elif "ground_level_asc" in request.GET:
        datas = WRCSAll.objects.order_by('ground_altitude').all()
    elif "ground_level_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-ground_altitude').all()
    elif "out_on" in request.GET:
        datas = WRCSAll.objects.all().filter(OutWater_flg=True)
    elif "out_off" in request.GET:
        datas = WRCSAll.objects.all().filter(OutWater_flg=False)
    elif "in_on" in request.GET:
        datas = WRCSAll.objects.all().filter(InWater_flg=True)
    elif "in_off" in request.GET:
        datas = WRCSAll.objects.all().filter(InWater_flg=False)
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_all.html', {'datas': datas})

#水位データの一覧
def data_water_level(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "water_level_asc" in request.GET:
        datas = WRCSAll.objects.order_by('water_level').all()
    elif "water_level_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-water_level').all()
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_water_level.html', {'datas': datas})

#散水状況の一覧
def data_out(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "out_on" in request.GET:
        datas = WRCSAll.objects.all().filter(OutWater_flg=True)
    elif "out_off" in request.GET:
        datas = WRCSAll.objects.all().filter(OutWater_flg=False)
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_out.html', {'datas': datas})

#吸水状況の一覧
def data_in(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "in_on" in request.GET:
        datas = WRCSAll.objects.all().filter(InWater_flg=True)
    elif "in_off" in request.GET:
        datas = WRCSAll.objects.all().filter(InWater_flg=False)
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_in.html', {'datas': datas})

#水温データの一覧
def data_water_temp(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "water_temp_asc" in request.GET:
        datas = WRCSAll.objects.order_by('water_temperature').all()
    elif "water_temp_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-water_temperature').all()
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_water_temp.html', {'datas': datas})

#地盤データの一覧
def data_ground(request):
    if "date_asc" in request.GET:
        datas = WRCSAll.objects.order_by('date').all()
    elif "date_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-date').all()
    elif "ground_level_asc" in request.GET:
        datas = WRCSAll.objects.order_by('ground_altitude').all()
    elif "ground_level_desc" in request.GET:
        datas = WRCSAll.objects.order_by('-ground_altitude').all()
    elif request.POST:
        ras = request.POST["ras"]
        ras_num = -1; ras_pos = "all"
        try:
            ras_num = int(ras)
        except ValueError:
            ras_pos = ras
        if ras_num != -1 and ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_id=ras_num, ras_point=ras_pos)
        elif ras_num != -1:
            datas = WRCSAll.objects.all().filter(ras_id=ras_num)
        elif ras_pos != "all":
            datas = WRCSAll.objects.all().filter(ras_point=ras_pos)
        else:
            datas = WRCSAll.objects.all()
    else:
        datas = WRCSAll.objects.all()
    return render(request, 'wrcsystem/data_ground.html', {'datas': datas})

#ラズパイからデータ受信
@csrf_exempt
def raspost_all(request):
    if request.method == "GET":
        print("RAS-GET-OK")
        return render(request, 'wrcsystem/ras_post.html')
    elif request.method == "POST":
        datas = WRCSAll(ras_name=request.POST.get("ras_name"),
                        ras_id=request.POST.get("ras_id"),
                        ras_point=request.POST.get("ras_point"),
                        OutWater_flg=request.POST.get("OutWater_flg"),
                        InWater_flg=request.POST.get("InWater_flg"),
                        water_level=request.POST.get("water_level"),
                        water_level_flg=request.POST.get("water_level_flg"),
                        water_temperature=request.POST.get("water_temperature"),
                        ground_altitude=request.POST.get("ground_altitude"))
        datas.save()
        print(datas)
        print("RAS-POST-OK")
        return render(request, 'wrcsystem/ras_post.html')

@csrf_exempt
def raspost_access_check(request):
    print("RAS-POST-OK")
    return render(request, 'wrcsystem/ras_post.html')

#アンケートホーム
def survey(request):
    return render(request, "layout/home.html")


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"account/register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"account/register.html",context=self.params)
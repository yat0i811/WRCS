from django.shortcuts import render, get_list_or_404
from .models import WRCS_samples,WebLayoutQuestions
from django.http import HttpResponse

def home(request):
    return render(request, 'layout/home.html', {})

def sample1(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample1.html', {'datas': datas})

def sample2(request):
    return render(request, 'layout/sample2.html', {})

def sample2a(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2a.html', {'datas': datas})

def sample2b(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2b.html', {'datas': datas})

def sample2c(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2c.html', {'datas': datas})

def sample2d(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2d.html', {'datas': datas})

def sample2e(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2e.html', {'datas': datas})

def sample2f(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2f.html', {'datas': datas})

def sample2g(request):
    datas = WRCS_samples.objects.all()
    return render(request, 'layout/sample2g.html', {'datas': datas})

def sample3(request):
    before_datas = WRCS_samples.objects.all()
    datas = []
    datas_id = []
    for i in before_datas:
        if i.RaspberryPi_ID not in datas_id:
            datas.append(i)
            datas_id.append(i.RaspberryPi_ID)
    print(datas)
    return render(request, 'layout/sample3.html', {'datas': datas})

def sample3_detail(request,id):
    datas = get_list_or_404(WRCS_samples, RaspberryPi_ID=id)
    return render(request, 'layout/sample3_detail.html', {'datas': datas})

def post_survey(request):
    student_number = request.POST.get('student_number')
    datas = WebLayoutQuestions.objects.filter(student_number=student_number)
    survey1 = request.POST.getlist("survey1")
    survey2 = request.POST.get("survey2")
    survey3 = request.POST.getlist("survey3")
    survey4 = request.POST.get("survey4")
    survey5 = request.POST.getlist("survey5")
    survey6 = request.POST.getlist("survey6")
    survey7 = request.POST.getlist("survey7")
    survey8 = request.POST.getlist("survey8")
    survey9 = request.POST.get("survey9")
    survey = [False]*27
    #surveies = [survey1, survey2, survey3, survey4, survey5, survey6,survey7,survey8,survey9]
    if '1' in survey1:
        survey[0] = True
    if '2' in survey1:
        survey[1] = True
    if '3' in survey1:
        survey[2] = True
    if '1' in survey3:
        survey[3] = True
    if '2' in survey3:
        survey[4] = True
    if '3' in survey3:
        survey[5] = True
    if 'Yes' == survey5[0]:
        survey[6] = True
        if '1' in survey6:
            survey[8] = True
        if '2' in survey6:
            survey[9] = True
        if '3' in survey6:
            survey[10] = True
        if '4' in survey6:
            survey[11] = True
        if '5' in survey6:
            survey[12] = True
        if '6' in survey6:
            survey[13] = True
        if '7' in survey6:
            survey[14] = True
        if '8' in survey6:
            survey[15] = True
        if '9' in survey6:
            survey[16] = True
        if '10' in survey6:
            survey[17] = True
        if '11' in survey6:
            survey[18] = True
        if '12' in survey6:
            survey[19] = True
    else:
        survey[6] = False
    if 'Yes' == survey7[0]:
        survey[7] = True
        if '1' in survey8:
            survey[20] = True
        if '2' in survey8:
            survey[21] = True
        if '3' in survey8:
            survey[22] = True
        if '4' in survey8:
            survey[23] = True
        if '5' in survey8:
            survey[24] = True
        if '6' in survey8:
            survey[25] = True
        if '7' in survey8:
            survey[26] = True
    else:
        survey[7] = False
    if len(datas) == 0:
        context = WebLayoutQuestions(student_number=int(student_number),
                                    question_first_sumple1=survey[0],
                                    question_first_sumple2=survey[1],
                                    question_first_sumple3=survey[2],
                                    question_second=int(survey2),
                                    question_third_sumple1=survey[3],
                                    question_third_sumple2=survey[4],
                                    question_third_sumple3=survey[5],
                                    question_fourth=survey4,
                                    question_fifth=survey[6],
                                    question_sixth_date=survey[8],
                                    question_sixth_RaspberryPi_ID=survey[9],
                                    question_sixth_RaspberryPi_point=survey[10],
                                    question_sixth_is_water_out=survey[11],
                                    question_sixth_is_water_in=survey[12],
                                    question_sixth_water_high=survey[13],
                                    question_sixth_water_temperature=survey[14],
                                    question_sixth_altitude=survey[15],
                                    question_sixth_now_weather=survey[16],
                                    question_sixth_future_weather=survey[17],
                                    question_sixth_now_temperature=survey[18],
                                    question_sixth_future_temperature=survey[19],
                                    question_seventh=survey[7],
                                    question_eighth_date=survey[20],
                                    question_eighth_RaspberryPi_ID=survey[21],
                                    question_eighth_water_high=survey[22],
                                    question_eighth_water_temperature=survey[23],
                                    question_eighth_altitude=survey[24],
                                    question_eighth_now_temperature=survey[25],
                                    question_eighth_future_temperature=survey[26],
                                    question_ninth=survey9,
                                    )
        context.save()
    else:
        WebLayoutQuestions.objects.update_or_create(student_number=student_number,
        defaults = {'question_first_sumple1':survey[0],
        'question_first_sumple2':survey[1],
        'question_first_sumple3':survey[2],
        'question_second':int(survey2),
        'question_third_sumple1':survey[3],
        'question_third_sumple2':survey[4],
        'question_third_sumple3':survey[5],
        'question_fourth':survey4,
        'question_fifth':survey[6],
        'question_sixth_date':survey[8],
        'question_sixth_RaspberryPi_ID':survey[9],
        'question_sixth_RaspberryPi_point':survey[10],
        'question_sixth_is_water_out':survey[11],
        'question_sixth_is_water_in':survey[12],
        'question_sixth_water_high':survey[13],
        'question_sixth_water_temperature':survey[14],
        'question_sixth_altitude':survey[15],
        'question_sixth_now_weather':survey[16],
        'question_sixth_future_weather':survey[17],
        'question_sixth_now_temperature':survey[18],
        'question_sixth_future_temperature':survey[19],
        'question_seventh':survey[7],
        'question_eighth_date':survey[20],
        'question_eighth_RaspberryPi_ID':survey[21],
        'question_eighth_water_high':survey[22],
        'question_eighth_water_temperature':survey[23],
        'question_eighth_altitude':survey[24],
        'question_eighth_now_temperature':survey[25],
        'question_eighth_future_temperature':survey[26],
        'question_ninth':survey9})
    return render(request, 'layout/thanks.html', {})

def thanks(request):
    return render(request, 'layout/thanks.html', {})

import csv
def download_survey(request):
    datas = WebLayoutQuestions.objects.all()
    list_datas = []
    for data in datas:
        list_data = [data.student_number,
                    data.question_first_sumple1,
                    data.question_first_sumple2,
                    data.question_first_sumple2,
                    data.question_second,
                    data.question_third_sumple1,
                    data.question_third_sumple2,
                    data.question_third_sumple3,
                    data.question_fourth,
                    data.question_fifth,
                    data.question_sixth_date,
                    data.question_sixth_RaspberryPi_ID,
                    data.question_sixth_RaspberryPi_point,
                    data.question_sixth_is_water_out,
                    data.question_sixth_is_water_in,
                    data.question_sixth_water_high,
                    data.question_sixth_water_temperature,
                    data.question_sixth_altitude,
                    data.question_sixth_now_weather,
                    data.question_sixth_future_weather,
                    data.question_sixth_now_temperature,
                    data.question_sixth_future_temperature,
                    data.question_seventh,
                    data.question_eighth_date,
                    data.question_eighth_RaspberryPi_ID,
                    data.question_eighth_water_high,
                    data.question_eighth_water_temperature,
                    data.question_eighth_altitude,
                    data.question_eighth_now_temperature,
                    data.question_eighth_future_temperature,
                    data.question_ninth
                    ]
        list_datas.append(list_data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="survey.csv"'
    writer = csv.writer(response)
    header = ['学籍番号',
                'サンプルページ1が見やすかった',
                'サンプルページ2が見やすかった',
                'サンプルページ3が見やすかった',
                '1番見やすかったサンプル',
                'サンプルページ1が貯水槽の稼働状況を見比べやすかった',
                'サンプルページ2が貯水槽の稼働状況を見比べやすかった',
                'サンプルページ3が貯水槽の稼働状況を見比べやすかった',
                '一番貯水槽の稼働状況を見比べやすかったサンプル',
                'フィルターは必要か',
                'フィルター取得日時',
                'フィルターラズパイID',
                'フィルターラズパイ場所',
                'フィルター吸水状況',
                'フィルター散水状況',
                'フィルター水位',
                'フィルター水温',
                'フィルター高度',
                'フィルター現在天気',
                'フィルター今後天気',
                'フィルター現在気温',
                'フィルター今後気温',
                'ソートは必要か',
                'ソート取得日時',
                'ソートラズパイID',
                'ソート水位',
                'ソート水温',
                'ソート高度',
                'ソート現在気温',
                'ソート今後気温',
                '意見']
    writer.writerow(header)
    for list_data in list_datas:
        writer.writerow(list_data)
    return response
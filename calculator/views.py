from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CalcForm

def calc(request):
    if request.method == 'POST':
        try:
            frstn = float(request.POST.get('first_num',0))
            scndn = float(request.POST.get('second_num',0))
        except ValueError:
            frstn = 0
            scndn = 0
        op = request.POST.get('operation')

        res = 0
        if op == '+':
            res = frstn + scndn
        elif op == '-':
            res = frstn - scndn
        elif op == 'x':
            res = frstn * scndn
        elif op == '÷':
            if scndn != 0:
                res = frstn / scndn
            else:
                res = 'Ошибка: деление на ноль'
        request.session['calc_data'] = {
            'frstn' : frstn,
            'scndn' : scndn,
            'oper' : op,
            'res' : res
        }
        return redirect('calcresult')
    else:
        calcform = CalcForm()
        return render(request, 'calculator.html', {'form': calcform})

def calcresult(request):
    data = request.session.get('calc_data',{})
    if not data:
        return HttpResponse('Данные не найдены. Заполните форму заново')
    frn = data.get('frstn')
    scnd = data.get('scndn')
    op = data.get('oper')
    res = data.get('res')
    return HttpResponse(f"""
        <h1>RESULT</h1>
        <h2>{frn} {op} {scnd} = {res}</h2>
    """)

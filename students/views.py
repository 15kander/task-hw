from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentForm
def inp(request):
    if request.method == 'POST':
        request.session['st_data'] = {
            'name' : request.POST.get('name'),
            "surename": request.POST.get('surename'),
            'age' : request.POST.get('age'),
            'email' : request.POST.get('email'),
        }
        return redirect('result')
    else:
        studentform = StudentForm()
        return render(request, "student.html", {"form": studentform})

def result(request):
    student = request.session.get('st_data',{})
    if not student:
        return HttpResponse('Данные не найдены. Заполните форму заново')
    return HttpResponse(f"""
        <h1>Данные студента</h1>
        <h2>Имя: {student.get('name')}</h2>
        <h2>Фамилия: {student.get('surename')}</h2>
        <h2>Возраст: {student.get('age')}</h2>
        <h2>Email: {student.get('email')}</h2>
    """)
from django.shortcuts import render
from .models import Student, Grant

def home(request):
    return render(request, 'home.html')


def recommend(request):
    student = Student.objects.first()
    grants = Grant.objects.all()

    mos_grantlar = []   # 👈 shu yerda list ochiladi

    # 👇 SHU KODNI BU YERGA YOZASAN
    for g in grants:
        if student.gpa >= g.min_gpa:
            mos_grantlar.append(g)

    return render(request, 'recommend.html', {
        'student': student,
        'grants': mos_grantlar
    })

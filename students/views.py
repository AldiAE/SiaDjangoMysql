from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Student


# Create your views here.
def index(request):
    context = {
        'title': 'Halaman Siswa',
        'students': Student.objects.all()
    }
    return render(request, 'students/index.html', context)


def detail(request, student_id):
    context = {
        'title': 'Halaman Siswa',
        'student': get_object_or_404(Student, id=student_id)
    }
    return render(request, 'students/detail.html', context)


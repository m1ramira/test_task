from django.shortcuts import render
from .models import User


# Create your views here.
def post_list(request):
    """
    вывод данных о пользователе и его постах на страницу
    """
    users = User.objects.all()
    content = {'users': users}
    return render(request, 'table.html', content)

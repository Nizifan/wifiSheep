from django.shortcuts import render
from .models import UserInfo

def index(request):
	userinfo_list = UserInfo.objects.all()
	context = {'userinfo_list':userinfo_list,}
	return render(request, 'wifisheep/index.html', context)

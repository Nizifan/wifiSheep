from django.shortcuts import render
from .models import UserInfo
import random

def index(request):
	userInfoList = UserInfo.objects.all()
	for userInfo in userInfoList:
		userInfo.userName = __mosaic(userInfo.userName)
		userInfo.password = __mosaic(userInfo.password)
	context = {'userinfo_list':userInfoList,}
	return render(request, 'wifisheep/index.html', context)

def __mosaic(string):
	print string
	if len(string) < 4:
		return string[0] + '*' * (len(string) - 1)
	else:
		maskLen = random.randint(2,3)
		startPos = random.randint(0,len(string) - maskLen -1)
		return string[0:startPos] + '*' * maskLen \
			+ string[startPos+maskLen+1:]

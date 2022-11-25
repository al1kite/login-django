from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
import json

# def login(request : HttpRequest):
#         data = json.dumps(request.GET) #dictionary를 문자열로 바꿔줌
#         return HttpResponse(data)

# def login_detail(request,id):
#         return HttpResponse('user id는'+str(id)+'입니다.')

def login(request):
        user_data = {
                'username': 'python',
                'password': 'django'
        }

        if(request.method == 'GET'):
                username, password = None, None
                try:
                        username = request.GET['username']
                        password = request.GET['password']
                except MultiValueDictKeyError:
                        if username is None:
                                return HttpResponse('유저 아이디를 입력해주세요')
                        if password is None:
                                return HttpResponse('유저 비밀번호를 입력해주세요')        

                if(username != user_data['username']):
                        return HttpResponse('유저 아이디가 올바르지 않습니다.')

                if(password != user_data['password']):
                        return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
                
                return HttpResponse('로그인 성공!!')

        return HttpResponse()
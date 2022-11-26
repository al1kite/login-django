from django.shortcuts import render, request 
from django.http import HttpResponse,HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
import json

# def login(request : HttpRequest):
#         data = json.dumps(request.GET) #dictionary를 문자열로 바꿔줌
#         return HttpResponse(data)

# def login_detail(request,id):
#         return HttpResponse('user id는'+str(id)+'입니다.')
context = {
        'method': request.method, 
        'is_valid': True

}
def login(request):
        user_data = {
                'username': 'python',
                'password': 'django'
        }
        # if(request.method == 'GET'):
                 # username = request.GET['username']
                # password = request.GET['password']
        if(request.method == 'GET'):
                return render(request, 'user/login.html', context) 

        if(request.method == 'POST'):
                username = request.POST.get('username')
                password = request.POST.get('password')

                if username is '':
                               context['is_valid'] = False
                if password is 'None':
                                context['is_valid'] = True
                if(username != user_data['username']):
                                context['is_valid'] = False
                if(password != user_data['password']):
                                context['is_valid'] = False
                
                return HttpResponse(request, 'users/login.html',context) #request, 'users/login.html'

        return HttpResponse('로그인 성공!')
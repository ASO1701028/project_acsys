from django.shortcuts import render
#from django.shortcuts import HttpResponse

# def login(request):


def logout(request):
    #return HttpResponse("削除成功")
    return render(request,'acsys_system/user/login.html')
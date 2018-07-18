from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from .models import UserMessage
from django.views.decorators.csrf import csrf_exempt
from SH1801Django.utils import check_user_login

'''
/message/chat?user='刘德华'
'''
def say_hello(request):
	username = request.GET.get('user', '张三')
	res = f"你好，{username}"
	return HttpResponse(res)



@check_user_login
@csrf_exempt
def MessageSubmitHandler(request):
	method = request.method
	if method == "POST":
		#（1）get post sections value
		name  = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address', '')
		message = request.POST.get('message', '')
		#(2) 保存数据到db
		usermsg = UserMessage(name=name, email=email, address=address,message=message)
		usermsg.save()

		# (3) 渲染一个新的列表页面
		usermsg_queryset = UserMessage.objects.all()
		total = usermsg_queryset.count()
		data = usermsg_queryset
		context = dict(
			pagenum=1,
			total=total,
			prev=1,
			next=1,
			pagerange=range(1, 2),
			data=data,
			url=request.path,
			page=1,
		)
		return render(request, 'msg_list.html', context=context)

	return render(request, "msg_form.html")


@check_user_login
@csrf_exempt
def MessageSubmitHandlerV2(request):
	from message import forms
	umsg_form = forms.UserMessageForm()
	if request.method == "POST":
		umform = forms.UserMessageForm(data=request.POST)
		if not umform.is_valid():
			context = dict(
				form = umform
			)
			return render(request, "msg_form_v2.html", context=context)
		form_data = umform.cleaned_data
		UserMessage.objects.create(**form_data)

		# (3) 渲染一个新的列表页面
		usermsg_queryset = UserMessage.objects.all()
		total = usermsg_queryset.count()
		data = usermsg_queryset
		context = dict(
			pagenum=1,
			total=total,
			prev=1,
			next=1,
			pagerange=range(1, 2),
			data=data,
			url=request.path,
			page=1,
		)
		return render(request, 'msg_list.html', context=context)

	context = dict(
		form = umsg_form
	)
	return render(request, "msg_form_v2.html", context=context)

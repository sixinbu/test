from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import Student

def hello_world(request):
	return HttpResponse("hello, worldsdfs sd sdfsfssdfs.")

'''
/app/index?username=zhangsan
'''
def index(request):
	import datetime
	print(dir(request))
	print('url:' + request.path)
	import json
	print('GET METHOD: ' + request.method)
	print('GET content: ' + json.dumps(request.GET))
	print(request.session.model)
	username = request.GET.get('username', 'laoda')
	address = "北京"
	t = datetime.datetime.now()
	context = dict(
		username = username
	)
	#return render(request, "home/index.html", context=context)
	return render(request, "home/index.html", locals())


def test(request):
	return render(request, "home/test.html")



def stu_forms(request):
	from .forms import StudentForm
	form = StudentForm()
	if request.method == "POST":
		form = StudentForm(data=request.POST)
		if not form.is_valid(): #验证提交的表单是否合法, 若不合法，返回错误信息
			return HttpResponse("提交数据失败！")
		form_data = form.cleaned_data
		Student.objects.create(**form_data)
		'''
		name = form_data['name']
		sex = form_data['sex']

		student = Student(name=name, sex=sex, address=form_data['address'],
		                  flag=form_data['flag'])
		student.save()
		'''
		return HttpResponse("提交数据成功！")
	context = {
		'form':form
	}
	return render(request, "home/stu_forms.html", context=context)


def query_stu(request):
	stu_list = Student.objects.all()
	context = dict(
		stu_list = stu_list
	)
	return render(request, "home/query_stu.html", context=context)


'''
采用django中实现接口：

url:   /add?x=2&y=3

输入参数：  x, y

输出结果：

{ 'status':200, 'msg':'ok', 'data':[5] }
'''

def add(request):
	x = int(request.GET.get('x', 0))
	y = int(request.GET.get('y', 0))
	sum = x + y
	import json
	result = dict(
		status = 200,
		message = 'ok',
		data = [sum]
	)
	return HttpResponse(json.dumps(result))

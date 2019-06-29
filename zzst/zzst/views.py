from django.http import JsonResponse

from model.models import Test

def hello(request):
    return JsonResponse({"good":"Hello world ! "})

def testdb(request):
	# 增
    # test1 = Test(name='runoob')
    # test1.save()
    # 删
    # 改
    # 查
    response = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list1 = Test.objects.all()
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    list2 = Test.objects.filter(id=1)
    # 获取单个对象
    list3 = Test.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    list4 = Test.objects.order_by('name')[0:2]
    #数据排序
    list5 = Test.objects.order_by("id")
    # 上面的方法可以连锁使用
    list6 = Test.objects.filter(name="runoob").order_by("id")
    # 输出所有数据
    for var in list5:
        response += str(var.id) + ' '
    return JsonResponse({"good":response})

def testform(request):
	q = request.GET['q']
	return JsonResponse({"good":q})
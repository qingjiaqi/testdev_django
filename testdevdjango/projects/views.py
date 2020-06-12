import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import  View
from projects.models import Projects
from projects.serializer import ProjectSerializer
# Create your views here.
def index(request):
    return HttpResponse('<h1>欢迎来到首页视图</h1>')

# 类视图
class ProjectsListold(View):
    """
    不使用序列化器
    """
    def get(self,request):
        project_qs=Projects.objects.all()
        project_list=[]
        for project in project_qs:
            project_list.append(
                {"name":project.name,
                 "leader":project.leader,
                 "tester":project.tester,
                 "programer":project.programer,
                 "create_date":project.create_date
                 }
            )
        #  JsonResponse默认只能返回字典对象，如果需要返回其他对象需要将safe=False
        return JsonResponse(project_list,safe=False)



class ProjectsList(View):
    """
    项目操作
    """
    def get(self,request):
        """查询项目列表"""
        project_list=Projects.objects.all()
        print(project_list)
        # 将数据模型对象传到序列化器中将数据进行序列化，如果是多个对象需要加many=True
        serializer=ProjectSerializer(instance=project_list,many=True)
        #  JsonResponse默认只能返回字典对象，如果需要返回其他对象需要将safe=False
        # serializer.data通过序列器中的这个data属性就可以获取到转换后的字典类型
        return JsonResponse(serializer.data,safe=False)



    def post(self,request):
        # 将传入的json格式拿到并解码为utf-8
        json_data=request.body.decode('utf-8')
        # 将数据转为字典类型
        python_data=json.loads(json_data,encoding='utf-8')
        # 对数据进行校验
        serializer=ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        # 1.将数据拆包传入创project对象存入数据库,使用校验器后校验后的数存放在serializer.validated_data中
        # project=Projects.objects.create(**serializer.validated_data)
        # 2.通过序列器来保存数据到数据库中
        #如果在创建序列器时传的参数是data那么调用save()方法，就是调用序列化器对象的create()方法
        # serializer.save(name='qj_01') # 可以进行传参，传入的参数如果key存在更新值，不存在就添加
        serializer.save()

        # 返回新增的数据
        # serializer=ProjectSerializer(instance=project)
        return  JsonResponse(serializer.data,status=200)

class ProjectDetails(View):

    def get_object(self,pk):
        """ 判断id是否存在"""
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        """查询项目详情"""
        project=self.get_object(pk)
        serializer=ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    """更新方法写在视图函数内2020-06-04"""
    # def put(self, request,pk):
    #     """更新项目"""
    #     # 判断id是否存在,并返回操作对象
    #     project=self.get_object(pk)
    #     #将请求数据转为字典
    #     json_data=request.body.decode('utf-8')
    #     python_Data=json.loads(json_data,encoding='utf-8')
    #     # 请求参数反序列化
    #     serializer=ProjectSerializer(data=python_Data)
    #     # 对请求数据进行校验
    #     try:
    #         # is_valid必须调用这个方法才会进行校验
    #         serializer.is_valid(raise_exception=True)
    #     except Exception as e:
    #         # 只有进行数据校验且报错后errors才会有
    #         return  JsonResponse(serializer.errors)
    #     # 对数据进行更新
    #     project.name=serializer.validated_data['name']
    #     project.leader=serializer.validated_data['leader']
    #     project.tester=serializer.validated_data['tester']
    #     project.programer=serializer.validated_data['programer']
    #     project.publish_app=serializer.validated_data['publish_app']
    #     project.status=serializer.validated_data['status']
    #     project.desc=serializer.validated_data['desc']
    #     # 保存
    #     project.save()
    #     # 序列化数据
    #     serializer_project=ProjectSerializer(instance=project)
    #     return JsonResponse(serializer_project.data)

    # 更新方法写在视图函数内2020-06-04

    """更新方法从视图函数内抽到序列化器中 2020-06-06"""
    def put(self, request,pk):
        """更新项目"""
        # 判断id是否存在,并返回操作对象
        project=self.get_object(pk)
        #将请求数据转为字典
        json_data=request.body.decode('utf-8')
        python_Data=json.loads(json_data,encoding='utf-8')
        # 请求参数反序列化，和序列化
        serializer=ProjectSerializer(instance=project,data=python_Data)
        # 对请求数据进行校验
        try:
            # is_valid必须调用这个方法才会进行校验
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # 只有进行数据校验且报错后errors才会有
            return  JsonResponse(serializer.errors)
        # 对数据进行更新
        # 当创建序列化器时传了instance参数和data参数时，调用save()实际会调用实例化里面的update方法
        serializer.save()

        return JsonResponse(serializer.data)

    def delete(self,requset,pk):
        # 校验要删除的数据是否存在
        project=self.get_object(pk)
        # 执行删除操作
        project.delete()
        msg='删除成功:{}'.format(project.name)
        return JsonResponse(msg,safe=False,status=204)
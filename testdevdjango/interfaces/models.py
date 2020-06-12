from django.db import models
from projects.models import Projects

# Create your models here.

class Interfaces(models.Model):
    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    desc = models.TextField(verbose_name='简要描述', max_length=50, blank=True, default='', null=True, help_text='简要描述')
    # 第一种(不导入)第一个参数为关联的模块路径(应用名，模型类)或者模型类
    # 第二个参数为当父表删除后，该字段的处理方式
    # CASCADE-->表示字表也会被删除
    #SET_NULL-->当前外键会被设置为None,null=True也要打开
    #PROJECT-->会报错
    #SET_DEFAULT --> 设置默认值，同时需要设置指定的默认值
    # project=models.ForeignKey('projects.Projects',on_delete=models.CASCADE,verbose_name='所属项目',help_text='所属项目')
    # 第二种(导入)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    # 定义子类Meta(好像只能写这个名字)用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interface'
        # 会在admin站点中，显示一个更人性化的表名
        verbose_name = '接口'
        # 复数形式，中文没有复数形式所以写一样的值
        verbose_name_plural = '接口'
    # 重写str方法，打印对象时会返回对象的属性name
    def __str__(self):
        return self.name
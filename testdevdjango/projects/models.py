from django.db import models

# Create your models here.
class Projects(models.Model):
    """
    创建项目表
    max_length:设置存储的最大字节数
    unique：参数用于设置当前字段是否唯一，默认为unique=False
    verbose_name：用于设置更人性化的字段名
    help_text 用于api文档中的一个中文名称
    blank：用于设置前端可以不传递
    null:用于设置数据库可以为空
    auto_now_add：自动添加
    default：默认值
    """
    name = models.CharField(verbose_name='项目名称',max_length=200,unique=True,help_text='请输入项目名称')
    leader = models.CharField(verbose_name='负责人',max_length=50,help_text='请输入负责人')
    tester = models.CharField(verbose_name='测试人员',max_length=50,help_text='请输入测试人员')
    programer = models.CharField(verbose_name='开发人员',max_length=50,help_text='请输入开发人员')
    publish_app = models.CharField(verbose_name='发布应用',max_length=100,help_text='请选择')
    status = models.BooleanField(verbose_name='应用状态',default=1,help_text='请输入应用状态')
    create_date = models.DateTimeField(verbose_name='创建时间',auto_now_add=True,help_text='创建时间')
    desc = models.TextField(verbose_name='简要描述',max_length=50,blank=True,default='',null=True,help_text='简要描述')

    #定义子类Meta(好像只能写这个名字)用于设置当前数据模型的元数据信息
    class Meta:
        db_table='tb_projects'
        # 会在admin站点中，显示一个更人性化的表名
        verbose_name='项目'
        # 复数形式，中文没有复数形式所以写一样的值
        verbose_name_plural='项目'
    # 重写str方法，打印对象时会返回对象的属性name
    def __str__(self):
        return self.name
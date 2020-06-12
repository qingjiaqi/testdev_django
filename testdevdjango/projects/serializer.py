# -*- coding: utf-8 -*-
# @Time     :2020/06/11  13:28
# @Author   :qingjia
# @Email   :834789582@qq.com
# @File     serializer.py 序列化器模块
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects

def is_unique_project_name(name):
    """自动定义校验器,使用时会自动化传name"""
    # 校验项目名称中一定要包含"项目"两个字
    if '项目' not in name:
        # 使用序列化器中的ValidationError输出错误信息
        raise serializers.ValidationError('项目名称中必须包含"项目"关键字')

class ProjectSerializer(serializers.Serializer):
    """
    1.创建项目序列化器，字段名往往与被序列化的模型类中定义的一致
    2.定义的序列器字段，既可以进行序列化输出，也可以进行反序列化输入
    2.label：用于设置更人性化的字段名
    3.allow_blank：设置前端可以不传
    4.read_only=True表示表示该字段只能序列化输出，不能反序列化输入
    5.write_only=True 表示该字段只能反序列化输入，不能序列化输出
    6.需要那些字段就在序列化器中定义那些字段
    7.校验器validators
    8.is_unique_project_name 自定义校验器，只需要写名字，必须放在序列化类的前面
    """
    id=serializers.IntegerField(label='ID',read_only=True)
    name=serializers.CharField(label='项目名称',max_length=200,help_text='请输入项目名称',
                               validators=[
                                           UniqueValidator(queryset=Projects.objects.all(), message='项目名称不能重复'),
                                           is_unique_project_name
                                           ])
    leader=serializers.CharField(label='负责人',max_length=200,help_text='请输入负责人',write_only=True)
    tester=serializers.CharField(label='测试人员',max_length=200,help_text='请输入测试人员')
    programer=serializers.CharField(label='开发人员',max_length=200,help_text='请输入开发人员')
    publish_app=serializers.CharField(label='发布应用',max_length=200,help_text='请选择')
    status=serializers.BooleanField(label='应用状态',allow_null=True,help_text='请输入应用状态')
    desc=serializers.CharField(label='简要描述',allow_null=True,allow_blank=True,help_text='简要描述')

    # 单字段校验
    #字段校验器顺序：定义字段时validators列表中从左到右依次校验--->单字段校验--->多字段校验
    #  方法名必须是validate_字段名
    def validate_name(self, value):
        """判断项目名称是以项目结尾的"""
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        # 校验后一定要返回
        return value

    # 多字段校验
    def  validate(self, attrs):
        """
        项目名称或者leader里面必须有一个包括qj"
        :param attrs: 请求的数据，字典
        :return: 返回校验后的数据
        """""
        if 'qj' not in attrs['name'] and 'qj' not in attrs['leader']:
            raise serializers.ValidationError('qj必须存在项目名称或leader字段中')
        # 校验后一定要返回
        return attrs

    #创建数据对象到数据库中
    def create(self, validated_data):
        # 保存校验通过的数据到数据库中
        project=Projects.objects.create(**validated_data)
        return project

    # 更新数据到数据对象中
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.status = validated_data['status']
        instance.desc = validated_data['desc']
        # 保存
        instance.save()
        return instance

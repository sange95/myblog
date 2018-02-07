from django.shortcuts import render
from django.http import HttpResponse
import base64  
import json 
import subprocess  
import datetime  
import sys  
import os  
import time  
from pydub import AudioSegment  
from aip import  AipSpeech
import subprocess


# Create your views here.
#主页
def home(request):
    return render(request , "home.html");

def error(request):
    return HttpResponse("404,页面不存在哦。。。。")

#管理员页面
def manage(request):
    return render(request , "manage.html");

#添加文章路由实现
def addBlog(request):
    return render(request , "addBlog.html");

#相册
def pictures(request):
    return HttpResponse("pictures");

#博客详情
def blogDetail(request):
    return HttpResponse("blogDetail")

def login(request):
    return HttpResponse("login")

def qqLogin(request):

    return HttpResponse("qqLogin")

def base(request):
    return render(request , "base.html")









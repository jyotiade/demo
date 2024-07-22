from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):

    data=Student.objects.all()
    # print(data)
    data=Student.objects.last()
    
#=============================two types of query------------>single query and multiple query


    # data=Student.objects.filter(stu_name='viti')   #to filter the particular object
    # data=Student.objects.filter(stu_city='bhopal')

    # data=Student.objects.order_by('stu_name')           #to arrange in alphabetical order
    # data=Student.objects.order_by('stu_city')

    # data=Student.objects.exclude(stu_name='Jyoti')   #to delecte single object

    # data=Student.objects.order_by('stu_name').reverse()    #to reverse the order

    # data=Student.objects.values()
    # data=Student.objects.values('stu_name','stu_city')     #single column name
    # print(data)
     
    data=Student.objects.values('stu_name','stu_city')[0:2]   #slicing
    print(data)  
    data=Student.objects.values('stu_name','stu_city')[::-1] 
    print(data) 
    data=Student.objects.values('stu_name','stu_city')[::-1][:2] 
    print(data)  
      


    # print(data.values())

    return HttpResponse("hello everyone.................")
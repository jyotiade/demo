from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
# def home(request):

    # data=Student.objects.all()
    # # print(data)
    # data=Student.objects.last()
    
#=============================two types of query------------>single query and multiple query

#=======================multiple object query==========================================
#     '''data=Student.objects.filter(stu_name='viti')   #to filter the particular object
#     data=Student.objects.filter(stu_city='bhopal')

#     data=Student.objects.order_by('stu_name')           #to arrange in alphabetical order
#     data=Student.objects.order_by('stu_city')

#     data=Student.objects.order_by('?')    #for random order
#     print(data)
#     data=Student.objects.exclude(stu_name='Jyoti')   #to delecte single object

#     data=Student.objects.order_by('stu_name').reverse()    #to reverse the order

#     data=Student.objects.values()
#     data=Student.objects.values('stu_name','stu_city')     #single column name
#     print(data)
     
#     data=Student.objects.values('stu_name','stu_city')[0:2]   #slicing
#     print(data)  
#     data=Student.objects.values('stu_name','stu_city')[::-1] 
#     print(data) 
#     data=Student.objects.values('stu_name','stu_city')[::-1][:2] 
#     print(data)  
      
# '''
#======================================single object query=======================================================

# def home(request):
   
   
# ''' 
# data=Student.objects.get(id=3) #get arguments always used primary-key column

# print(data)
# print(data.id,data.stu_name,data.stu_city)

# '''
# '''data=Student.objects.first() 
# data=Student.objects.order_by('stu_name').first()
# data=Student.objects.order_by('stu_name').last()
# data=Student.objects.order_by('-stu_name').first()

# print(data.id,data.stu_name,data.stu_city)
# return HttpResponse(data)
# '''
#==========to create==============
# '''
# #    data=Student.objects.create(stu_name='ved',stu_city="mumbai",stu_email='ved@gmail.com',)
# #    print(data.id,data.stu_name,data.stu_city)
# #    return HttpResponse(data)
# # print(data.values())'''

#============get or create======combine====================
   
def home(request):
#    data,created=Student.objects.get_or_create(stu_name="raj",stu_city='jabalpur',stu_email="raj@gmail.com")
#    print(data.id,data.stu_name,data.stu_city)
#    return HttpResponse(data)

#    data=Student.objects.get(id=5).delete()

#    print(data)
#    data = Student.objects.filter(stu_name = "ved").delete()
#    print(data)
#    print(data.id,data.stu_name,data.stu_city)

   data=Student.objects.create(stu_name='ved',stu_city="mumbai",stu_email='ved@gmail.com',)
   print(data.id,data.stu_name,data.stu_city)
   data=Student.objects.create(stu_name='ansh',stu_city="noida",stu_email='ansh@gmail.com',)
   print(data.id,data.stu_name,data.stu_city)

   return HttpResponse(data)  
    # return HttpResponse("hello everyone.................")
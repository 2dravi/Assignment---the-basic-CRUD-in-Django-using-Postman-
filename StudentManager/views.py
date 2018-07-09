from django.shortcuts import render
from django.views.generic import View
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Student



#  class to get two parameter p1 and p2 and do the addition
class calculator(View):

    def get(self, request):
        try:
            p1 = request.GET['p1']
            p2 = request.GET['p2']
            result = int(p1) + int(p2)
            return HttpResponse('sum is : ' + str(result), status=200)
        except Exception as exception:
            return HttpResponse("Internal Server Error", status=500)


# class to get ,update ,put and delete from student Model
class student_manager(View):
    # Method to get the all student data
    def get(self, request):
        try:
            student_list = Student.objects.all()
            result = []
            for student in student_list:
                res = {}
                res['first_name'] = student.first_name
                res['last_name'] = student.last_name
                res['college_name'] = student.college_name
                res['roll_no'] = student.roll_no
                res['email'] = student.email
                result.append(res)
            return HttpResponse(result, status=200)


        except Exception as exception:
            return HttpResponse('Internal Server Error', status=500)

    # Method for new entry in Student model
    def post(self, request):
        try:
            post_req = request.POST

            f_name_ = post_req['first_name']
            l_name_ = post_req['last_name']
            college_ = post_req['college_name']
            email_ = post_req['email']
            rno_ = post_req['roll_no']

            obj = Student(first_name=f_name_, last_name=l_name_, college_name=college_, email=email_, roll_no=rno_)
            obj.save()
            return HttpResponse(str(f_name_) + ' '+ str(rno_) + " record  successfully created ", status=200)
        except IntegrityError:
            return HttpResponse("Roll No already exists!")
        except MultiValueDictKeyError:
            return HttpResponse("Multi Valued DictKey error", status=500)

    # Method to delete record

    def delete(self, request, id):
        try:
            Student.objects.get(id=id).delete()
            return HttpResponse("successfully deleted", status=200)

        except ObjectDoesNotExist:
            return HttpResponse(' Object does not exist', status=500)

        except MultiValueDictKeyError:
            return HttpResponse(' Multi Value Dict Key error', status=500)

    # method to update record
    def put(self, request, roll):
        try:
            put_req = QueryDict(request.body)
            obj = Student.objects.get(roll_no=roll)

            if 'first_name' in put_req.keys():
                obj.first_name = put_req['first_name']
            if 'last_name' in put_req.keys():
                obj.last_name = put_req['last_name']
            if 'email' in put_req.keys():
                obj.email = put_req['email']
            if 'college_name' in put_req.keys():
                obj.college_name = put_req['college_name']

            obj.save()
            return HttpResponse("successfully Updated ", status=200)
        except ObjectDoesNotExist:
            return HttpResponse(' Object does not exist', status=500)

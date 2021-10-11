from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

from api.models import student
from api.serializers import studentSerializer

# Create your views here.
class studentList(APIView):
    def get(self, request):
        students = student.objects.all()
        s_serlializer = studentSerializer(students, many=True)

        return Response(s_serlializer.data)

    def post(self):
        pass
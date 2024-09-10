from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from api.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teacher_model import TeacherModel

@csrf_exempt
def teacher_view(request):
    if request.method == 'GET':
        teachers = TeacherModel.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(datda=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Course
from .serializer import CourseSerializer



class CourseList(ListModelMixin, CreateModelMixin, GenericAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



class CourseDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
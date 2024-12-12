from rest_framework import generics
from .models import (
    Todo,
)
from .serializers import (TodoSerializer,)


# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
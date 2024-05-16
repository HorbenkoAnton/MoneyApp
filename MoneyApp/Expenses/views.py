from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExpenseSerializer,CategorySerializer
from .models import Category, Expense

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'expenses': reverse('expenses-list', request=request, format=format),
#         'categories': reverse('categories-list', request=request,format=format)
#     })


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
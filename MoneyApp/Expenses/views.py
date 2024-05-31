from django.shortcuts import render
from rest_framework import viewsets, permissions
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
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
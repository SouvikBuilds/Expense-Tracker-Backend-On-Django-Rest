from django.shortcuts import render
from .models import ExpenseModel
from .serializers import ExpenseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def home(request):
    return Response({"message": "Django API is Running 🚀"})


@api_view(['GET'])
def get_all_expenses(request):
    expenses = ExpenseModel.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_expense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_expense(request, pk):
    try:
        expense = ExpenseModel.objects.get(pk=pk)
    except ExpenseModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExpenseSerializer(expense, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_expense(request, pk):
    try:
        expense = ExpenseModel.objects.get(pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ExpenseModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


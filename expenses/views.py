from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Expense
from .serializers.common import ExpenseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ExpenseListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get(self, _request):
        expense = Expense.objects.all()
        serialized_expense = ExpenseSerializer(expense, many=True)
        return Response(serialized_expense.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['owner'] = request.user.id
        expense_to_add = ExpenseSerializer(data=request.data)
        try: 
            expense_to_add.is_valid()
            expense_to_add.save()
            return Response(expense_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error")
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ExpenseDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_expense(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise NotFound(detail="Can't find that expense")

    def get(self, _request, pk):
        expense = self.get_expense(pk=pk)
        serialized_expense = ExpenseSerializer(expense)
        return Response(serialized_expense.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        expense_to_edit = self.get_expense(pk=pk)
        if expense_to_edit.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        original_owner = expense_to_edit.owner.id  
        request.data['owner'] = original_owner
        
        updated_expense = ExpenseSerializer(expense_to_edit, data=request.data)
        try:
            updated_expense.is_valid()
            updated_expense.save()
            return Response(updated_expense.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({ 'detail': str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        expense_to_delete = self.get_budget(pk=pk)
        if expense_to_delete.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        expense_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
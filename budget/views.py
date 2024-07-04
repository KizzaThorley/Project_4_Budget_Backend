from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Budget
from .serializers.common import BudgetSerializer 

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BudgetListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get(self, _request):
        budget = Budget.objects.all()
        serialized_budget = BudgetSerializer(budget, many=True)
        return Response(serialized_budget.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['owner'] = request.user.id
        print(request.data)
        budget_to_add = BudgetSerializer(data=request.data)
        try: 
            budget_to_add.is_valid()
            budget_to_add.save()
            return Response(budget_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error")
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BudgetDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_budget(self, pk):
        try:
            return Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise NotFound(detail="Can't find that Budget")

    def get(self, _request, pk):
        budget = self.get_budget(pk=pk)
        serialized_budget = BudgetSerializer(budget)
        return Response(serialized_budget.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        budget_to_edit = self.get_budget(pk=pk)
        if budget_to_edit.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        original_owner = budget_to_edit.owner.id  
        request.data['owner'] = original_owner
        
        updated_budget = BudgetSerializer(budget_to_edit, data=request.data)
        try:
            updated_budget.is_valid()
            updated_budget.save()
            return Response(updated_budget.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({ 'detail': str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        budget_to_delete = self.get_budget(pk=pk)
        if budget_to_delete.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        budget_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
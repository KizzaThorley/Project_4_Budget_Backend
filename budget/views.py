from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from datetime import datetime
current_month = datetime.now().month
current_year = datetime.now().year

from .models import Budget
from .serializers.common import BudgetSerializer 
from .serializers.populated import PopulatedBudgetSerializer

from rest_framework.permissions import IsAuthenticated

class BudgetListView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        budget = Budget.objects.filter(owner=request.user.id)
        serialized_budget = PopulatedBudgetSerializer(budget, many=True)
        return Response(serialized_budget.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['owner'] = request.user.id
        request.data['month'] = current_month
        request.data['year'] = current_year
        print(request.data)
        budget_to_add = BudgetSerializer(data=request.data)
        try: 
            budget_to_add.is_valid()
            budget_to_add.save()
            return Response(budget_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error")
            return Response(budget_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BudgetDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    def get_budget(self, pk):
        try:
            return Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise NotFound(detail="Can't find that Budget")

    def get(self, request, pk):
        budget = self.get_budget(pk=pk)
        if budget.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serialized_budget = PopulatedBudgetSerializer(budget)
        
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

from .common import BudgetSerializer
from jwt_auth.serializers import UserSerializer
from expenses.serializers.common import ExpenseSerializer


class PopulatedBudgetSerializer(BudgetSerializer):
    expenses = ExpenseSerializer(many=True)
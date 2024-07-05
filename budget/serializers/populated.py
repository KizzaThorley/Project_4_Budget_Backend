
from .common import BudgetSerializer
from jwt_auth.serializers import UserSerializer
from expenses.serializers.common import ExpenseSerializer


# does everthing theat the standard movie serializer does plus uses 
# the studio serializer to populate the author key on a studio
class PopulatedBudgetSerializer(BudgetSerializer):
    expenses = ExpenseSerializer(many=True)
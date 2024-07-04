from django.urls import path
from .views import BudgetListView, BudgetDetailView

urlpatterns = [
    path('', BudgetListView.as_view()),
    path('<int:pk>/', BudgetDetailView.as_view()),
]
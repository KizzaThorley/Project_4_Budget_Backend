from django.urls import path
from .views import ExpenseListView
from .views import ExpenseDetailView

urlpatterns = [
    path('', ExpenseListView.as_view()),
    path('<int:pk>/', ExpenseDetailView.as_view()),
]
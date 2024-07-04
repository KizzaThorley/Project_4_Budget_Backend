from django.db import models

# Create your models here.
class Expense(models.Model):
	def __str__(self):
		return f'{self.cost} - {self.category}'
	cost = models.FloatField()
	owner = models.ForeignKey(
        "jwt_auth.User",
        related_name = 'expenses',
        on_delete = models.CASCADE,
    )
	budget = models.ForeignKey(
        "budget.Budget",
        related_name = 'budget',
        on_delete = models.CASCADE,
    )
	category = models.CharField(max_length=50)
	description = models.TextField(max_length=300)
	
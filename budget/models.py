from django.db import models


# Create your models here.

class Budget(models.Model):
    def __str__(self):
        return f'{self.owner} - {self.amount}'
    amount = models.FloatField()
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name = 'budget',
        on_delete = models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=3)
    year = models.FloatField()

    class Meta:
        unique_together = ('month', 'year', 'owner')

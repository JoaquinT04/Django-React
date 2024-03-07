from django.db import models
from book.models import Book
# Create your models here.
class Loan(models.Model):
	"""# User who borrowed the books
	user = models.ForeignKey(User, on_delete=models.CASCADE) """
	# Books borrowed by the user
	books = models.ManyToManyField(Book)
	# Date when the books were borrowed
	loan_date = models.DateField(auto_now_add=True)
	# Estimated return date of the books
	estimated_return_date = models.DateField()
	def __str__(self):
		return f"Loan by {self.user.username} - {self.loan_date}"
from django.db import models
from datetime import datetime


class site_users(models.Model):
    username = models.CharField(max_length=200, default='')
    join_date = models.DateTimeField('date joined', default=datetime.now())
    # author_name = models.CharField(max_length=200)
    credits = models.IntegerField(default=0) 
    num_transactions = models.IntegerField(default=0)
    # num_votes = models.IntegerField(default=0)
    # book_image = models.CharField(max_length=250) 
    
    def __str__(self):
        return self.username       
 
# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     user = models.CharField(max_length=200)
#     review_text = models.CharField(max_length=300)

#     def __str__(self):
#         return self.review_text
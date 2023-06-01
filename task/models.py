from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering=['-name']
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name 


class Task(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Select Category")
    title=models.CharField(max_length=200,help_text="", default="")
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False, )
    created_by=models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE,null=True, blank=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='notifications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Payment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Reminder(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='reminders')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField()

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)    

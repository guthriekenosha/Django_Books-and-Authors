from django.db import models

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long!"
        if len(postData['notes']) < 5:
            errors['notes'] = "Notes must be at least 5 characters long!"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="authors") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
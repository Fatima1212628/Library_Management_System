from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    isbn=models.CharField(max_length=13 , unique=True)
    genre=models.CharField(max_length=100 , blank=True)
    total_copies=models.PositiveIntegerField(default=1)
    available_copies=models.PositiveIntegerField(default=1)
    added_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering=['title'] # Sorts alphabetically by title
        
        
    
class Member(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, blank=True)
    joined_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class IssueRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE, related_name='issue_records')
    member=models.ForeignKey(Member, on_delete=models.CASCADE, related_name='issue_records')
    issued_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    return_date=models.DateTimeField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
    
    def __str__(self):
        status="Returned" if self.is_returned else "Issued"
        return f"{self.book.title} -> {self.member.name} ({status})"
    
    class Meta: #Defines the rules, configurations, and settings for the table itself.
        ordering= ['-issued_date'] 
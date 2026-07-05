from django import forms
from .models import Book, Member, IssueRecord

class IssueBookForm(forms.Form):
    book=forms.ModelChoiceField(queryset=Book.objects.filter(available_copies__gt=0)) #__gt means "greater than"
    member=forms.ModelChoiceField(queryset=Member.objects.all())
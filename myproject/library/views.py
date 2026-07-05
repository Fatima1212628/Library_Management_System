from django.shortcuts import render, redirect, get_object_or_404
from .models import Book,Member,IssueRecord
from .forms import IssueBookForm 
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

def issue_book(request):
    if request.method=="POST":
        form=IssueBookForm(request.POST)
        if form.is_valid():
            book=form.cleaned_data['book']
            member=form.cleaned_data['member']
            
            if book.available_copies<1:
                messages.error(request,f"No available copies for {book.title}")
                return redirect('issue_book')
            
            IssueRecord.objects.create(
                book=book,
                member=member,
                due_date=timezone .now().date() + timedelta(days=14)
            )
            
            book.available_copies -=1
            book.save()
            messages.success(request,f"{book.title} issued to {member.name}.")
            return redirect("issue_book")
            
    else:
        form=IssueBookForm()
        
    active_issues=IssueRecord.objects.filter(is_returned=False)
        
    return render(
        request,
        "issue_book.html",
        {
            'form':form,
            'active_issues':active_issues
     })
        
            
    
    
def return_book(request, record_id):
    record=get_object_or_404(IssueRecord,id=record_id, is_returned=False)
            
    record.is_returned=True
    record.return_date=timezone.now()
    record.save()
    
    record.book.available_copies+=1
    record.book.save()
    
    messages.success(request, f"{record.book.title} returned by { record.member.name}.")
    return redirect('issue_book')

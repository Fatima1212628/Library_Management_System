from django.contrib import admin
from .models import Book, Member, IssueRecord

# Register your models here.

class IssueRecordInlineForBook(admin.TabularInline):
    model=IssueRecord
    fk_name='book'
    extra=0
    readonly_fields=('issued_date',)
    
class IssueRecordInlineForMember(admin.TabularInline):
    model=IssueRecord
    fk_name='member'
    extra=0
    readonly_fields=('issued_date',)
    
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display=('title','author','isbn','total_copies','available_copies')
    search_fields=('title','author','isbn')
    list_filter=('genre',)
    inlines=[IssueRecordInlineForBook]
    
    
@admin.register(Member)
class AdminMember(admin.ModelAdmin):
    list_display=('name','email','joined_on')
    search_fields=('name','email')
    inlines=[IssueRecordInlineForMember]
    
    
@admin.register(IssueRecord)
class AdminBook(admin.ModelAdmin):
    list_display=('book','member','issued_date','due_date','is_returned')
    search_fields=('book__title','member__name')
    list_filter=('is_returned',)
    


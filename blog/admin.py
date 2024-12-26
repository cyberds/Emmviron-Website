from django.contrib import admin
from .models import Blog
from ckeditor.widgets import CKEditorWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),  # Use CKEditorWidget for content
        }

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)

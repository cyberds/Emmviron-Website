from django.contrib import admin
from .models import Blog, Tags
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': CKEditorUploadingWidget(
                config_name='full',
                external_plugin_resources=[(
                    'youtube',
                    '/static/ckeditor/ckeditor/plugins/youtube/',
                    'plugin.js',
                ), (
                    'image2',
                    '/static/ckeditor/ckeditor/plugins/image2/',
                    'plugin.js',
                ), (
                    'codesnippet',
                    '/static/ckeditor/ckeditor/plugins/codesnippet/',
                    'plugin.js',
                )],
            ),
        }

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

class TagsAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tags, TagsAdmin)

from cloudinary_storage.storage import MediaCloudinaryStorage
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.core.files.base import ContentFile
import cloudinary.uploader
from urllib.parse import urlparse
import os

class CKEditorCloudinaryStorage(MediaCloudinaryStorage):
    def get_available_name(self, name, max_length=None):
        # Remove any existing Cloudinary URL structure
        if name.startswith('http'):
            parsed = urlparse(name)
            name = parsed.path.split('/')[-1]
        return name
    
    def _save(self, name, content):
        try:
            # Handle file-like objects
            if hasattr(content, 'read'):
                content.seek(0)
                content_data = content.read()
                if isinstance(content_data, str):
                    content_data = content_data.encode()
                content = ContentFile(content_data)
            
            # Clean the filename
            name = self.clean_name(name)
            
            # Upload to Cloudinary
            response = cloudinary.uploader.upload(
                content,
                public_id=name,
                folder='ckeditor_uploads',
                resource_type="auto",
                invalidate=True,
                unique_filename=True,
                overwrite=True
            )
            
            return response.get('secure_url')
            
        except Exception as e:
            print(f"Upload error: {str(e)}")
            raise

    def clean_name(self, name):
        """Clean the file name to make it Cloudinary friendly"""
        # Replace backslashes with forward slashes
        name = name.replace('\\', '/')
        
        # Remove any leading paths like 'uploads/2025/04/02/'
        name = os.path.basename(name)
        
        # Remove any special characters and spaces
        name = "".join(c for c in name if c.isalnum() or c in ('-', '_', '.'))
        
        return name

    def url(self, name):
        # Prevent double-processing of URLs
        if name.startswith('http'):
            return name
        return super().url(name)
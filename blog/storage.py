from cloudinary_storage.storage import MediaCloudinaryStorage

class CKEditorCloudinaryStorage(MediaCloudinaryStorage):
    def get_available_name(self, name, max_length=None):
        return name
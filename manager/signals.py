from django.db.models.signals import pre_save
from django.dispatch import receiver
from manager.models import Author

@receiver(pre_save,sender=Author)
def before_saving_author(sender,instance,**kwargs):
    if not instance.image:
        instance.image="author/default_author_image.jpg"


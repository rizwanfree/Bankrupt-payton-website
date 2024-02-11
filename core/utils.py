from django.utils.text import slugify
import uuid

def generate_slug(title:str) -> str:
    from .models import Case
    title = slugify(title)
    while(Case.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[0:4]}'
    return title
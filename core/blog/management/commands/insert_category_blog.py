from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import ProductCategoryModel
from django.utils.text import slugify
from blog.models import PostCategory,PostModel,PostStatusType

class Command(BaseCommand):
    help = 'Generate fake blog categories'
    
    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")
        for _ in range(10):
            name = fake.word()
            slug = slugify(name,allow_unicode=True)
            PostCategory.objects.get_or_create(name=name, slug=slug)
        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake product categories'))

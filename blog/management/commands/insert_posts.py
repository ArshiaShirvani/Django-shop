import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from shop.models import ProductModel, ProductCategoryModel,ProductStatusType
from accounts.models import User,UserType
from blog.models import PostModel,PostStatusType,CommentModel,CommentStatusType,PostCategory
from pathlib import Path
from django.core.files import File

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = 'Generate fake post of the blog'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")
        author = User.objects.get(type=UserType.superuser.value)
        # List of images
        image_list = [
            "./images/img1.jpg",
            "./images/img2.jpg",
            "./images/img3.jpg",
            "./images/img4.jpg",
            "./images/img5.jpg",
            "./images/img6.jpg",
            # Add more image filenames as needed
        ]

        categories = PostCategory.objects.all()

        for _ in range(10):  # Generate 10 fake products
            author = author  
            num_categories = random.randint(1, 4)
            selected_categories = random.sample(list(categories), num_categories)
            title = ' '.join([fake.word() for _ in range(1,3)])
            slug = slugify(title,allow_unicode=True)
            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image,"rb"),name=Path(selected_image).name)
            content = fake.paragraph(nb_sentences=10)
            counted_view = fake.random_int(min=0, max=100)
            status = random.choice(PostStatusType.choices)[0]

            post = PostModel.objects.create(
                author=author,
                title=title,
                slug=slug,
                image=image_obj,
                content=content,
                status=status,
                counted_view=counted_view,
            )
            post.category.set(selected_categories)

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake post in blog'))
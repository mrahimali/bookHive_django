from django.db import models

# Create your models here.
class UserDetail(models.Model):
    userType=(
        ('BUYER', 'Buyer'),
        ('SELLER', 'Seller')
    )
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    user_type=models.CharField(max_length=6,choices= userType, default='SELLER')
    password=models.CharField(max_length=100)


    def registerUser(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return UserDetail.objects.get(email=email)
        except:
            return False





class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    


class BookInfo(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    book_image=models.ImageField(upload_to='upload/books/')
    writer=models.CharField(max_length=100, default='')

    @staticmethod
    def get_all_books():
        return BookInfo.objects.all()
    
    @staticmethod
    def get_books_by_category(category_id):
        return BookInfo.objects.filter(category=category_id)

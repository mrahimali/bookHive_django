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
    # user_type=models.CharField(max_length=6,choices= userType, default='SELLER')
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    uploaded_by=models.ForeignKey(UserDetail, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title


    def add_book(self):
        self.save()

    @staticmethod
    def get_all_books():
        return BookInfo.objects.all()
    
    @staticmethod
    def get_books_by_ids(ids):
        return BookInfo.objects.filter(id__in=ids)
    


    @staticmethod
    def get_books_by_owner_id(id):
        return BookInfo.objects.filter(uploaded_by=id)
    


    @staticmethod
    def get_books_by_category(category_id):
        return BookInfo.objects.filter(category=category_id)


class ShippingAddresses(models.Model):
    name=models.CharField(max_length=100, default="")
    address = models.CharField(max_length=200)
    city=models.CharField(max_length=50, default='')
    phone=models.IntegerField(default=0000)
    details_of=models.ForeignKey(UserDetail, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.address
    
    def addAddress(self):
        self.save()

    def get_address_by_id(id):
        return ShippingAddresses.objects.filter(details_of=id)


class Order(models.Model):
    ordered_by = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.ForeignKey(ShippingAddresses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order by {self.ordered_by.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    product_owner = models.ForeignKey(UserDetail, related_name='owned_books', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    

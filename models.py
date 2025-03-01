from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_categories'


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='dishes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_dishes'


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='events/')
    is_visible = models.BooleanField(default=True)

    class Meta:
            db_table = 'main_events'
            ordering = ['date']

            def __str__(self):
                return self.title


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='staff/')
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_staff'
        ordering = ['name']

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_gallery'
        ordering = ['title']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'main_contacts'
        ordering = ['created_at']

    def __str__(self):
        return f"Contact from {self.name} - {self.email}"
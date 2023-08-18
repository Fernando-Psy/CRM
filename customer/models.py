import kwargs as kwargs
from django.db import models
from django.urls import reverse


class Customer(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    birthDate = models.DateField()
    areaCode = models.CharField(max_length=3)
    phoneNumber = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    def get_full_phoneNumber(self):
        return f'({self.areaCode}) {self.phoneNumber}'

    def get_full_name(self):
        return f'{self.firstName} {self.lastName}'

    def get_full_city(self):
        return f'{self.city} - {self.state}'

    def get_absolute_url(self):
        return reverse('customer:customer-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('customer:customer-delete', kwargs={'id': self.id})

    class Meta:
        db_table = 'customer'

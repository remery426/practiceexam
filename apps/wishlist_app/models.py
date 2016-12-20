from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

class productManager(models.Manager):
    def create_product(self,postData,get_name):
        response = {}
        errors = []
        get_name = get_name
        if len(postData["name"])<3:
            errors.append("Make America great again")
        if errors:
            response['status'] = False
            response['error'] = errors
            print get_name
            return response
        response['status'] = True
        product1=Product.objects.filter(name = postData["name"])
        if product1:
            print "test"
            test1 = product1[0].user.username
            user2 = User.objects.get(username = test1)
            item = self.create(name = postData['name'], user = user2)
            user3 = User.objects.get(username = get_name)
            item.wishlist.add(user3)
            response['status'] = True
            response['item'] = item
            return response
        user3 = User.objects.get(username = get_name)
        item = self.create(name = postData['name'], user = user3)
        item.wishlist.add(user3)
        response['status'] = True
        response['item'] = item
        return response
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    wishlist = models.ManyToManyField(User, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = productManager()

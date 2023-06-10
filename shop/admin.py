from django.contrib import admin
from .models import Slide , Product , Category , Brand , Contact

# Register your models here.
admin.site.register(Slide)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Contact)
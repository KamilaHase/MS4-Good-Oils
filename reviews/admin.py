from django.contrib import admin
from .models import ProductReview

""" Renders Models to the Admin View"""


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'nickname',
        'description',
        'rating',
        'review_date'
    )


admin.site.register(ProductReview, ReviewAdmin)

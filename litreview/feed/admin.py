from django.contrib import admin

from feed.models import Ticket, Review
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'ticket')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)

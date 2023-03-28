from django.contrib import admin

from feed.models import Ticket, Review
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','user')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'ticket','user')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)

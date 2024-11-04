from django.contrib import admin
from .models import Movie, Guest, Post, Reservation


admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Post)
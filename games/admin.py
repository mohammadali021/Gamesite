from django.contrib import admin

from games.models import Game, GameDetails


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug')
    prepopulated_fields = {'slug': ('title',)}



# Register your models here.

from django.contrib import admin
from .models import User, Competition, Resource, Topic, Difficulty, Milestone, Event
# Register your models here.

class  UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("name", "rounds")
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "topic", "difficulty", "url")
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ("name", "real_name")
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ("user", "competition","round", "placement", "score", "status") 
class EventAdmin(admin.ModelAdmin):
    list_display = ("competition","date", "written") 
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Difficulty, DifficultyAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Event, EventAdmin)
from django.contrib import admin

from .models import ProjectsModel, LanguagesModel, UserAccountModel, HardSkillsModel


@admin.register(UserAccountModel)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'occupation', 'description', 'telegram', 'discord', 'github',
                    'portfolio', 'avatar')
    list_filter = ('user', 'phone', 'address', 'occupation', 'description', 'telegram', 'discord', 'github',
                   'portfolio', 'avatar')
    search_fields = ('user', 'phone', 'address', 'occupation', 'description', 'telegram', 'discord', 'github',
                     'portfolio', 'avatar')

    class Meta:
        model = UserAccountModel

    def __str__(self):
        return self.user


@admin.register(ProjectsModel)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'description', 'time_create')
    list_filter = ('name_project', 'description', 'time_create')
    search_fields = ('name_project', 'description', 'time_create')

    class Meta:
        model = ProjectsModel

    def __str__(self):
        return self.name_project


@admin.register(LanguagesModel)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language', 'language_level')
    list_filter = ('language', 'language_level')
    search_fields = ('language', 'language_level')

    class Meta:
        model = LanguagesModel

    def __str__(self):
        return self.language


@admin.register(HardSkillsModel)
class HardSkillsAdmin(admin.ModelAdmin):
    list_display = ('programming_language', 'description')
    list_filter = ('programming_language', 'description')
    search_fields = ('programming_language', 'description')

    class Meta:
        model = HardSkillsModel

    def __str__(self):
        return self.programming_language

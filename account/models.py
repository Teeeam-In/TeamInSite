from django.db import models


class UserAccountModel(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    discord = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    portfolio = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/ava3.webp',
        null=True,
        blank=True
    )
    languages = models.ManyToManyField('LanguagesModel', blank=True)
    hard_skills = models.ManyToManyField('HardSkillsModel', blank=True)
    projects = models.ManyToManyField('ProjectsModel', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_account'
        verbose_name = 'Обліковий запис користувача'
        verbose_name_plural = 'Облікові записи користувачів'


class LanguagesModel(models.Model):
    language = models.CharField(max_length=255)
    language_level = models.CharField(max_length=255)

    def __str__(self):
        return self.language

    class Meta:
        db_table = 'languages'
        verbose_name = 'Мова програмування'
        verbose_name_plural = 'Мови програмування'


class HardSkillsModel(models.Model):
    programming_language = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.programming_language

    class Meta:
        db_table = 'hard_skills'
        verbose_name = 'Навичка'
        verbose_name_plural = 'Навички'


class ProjectsModel(models.Model):
    name_project = models.CharField(max_length=255)
    type_project = models.CharField(max_length=255)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField('UserAccountModel', blank=True)

    def __str__(self):
        return self.name_project

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'

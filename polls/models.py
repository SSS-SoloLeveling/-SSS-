from django.db import models


class Task(models.Model):
    title = models.CharField('ФИО', max_length=50)
    task = models.CharField('Группа', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'





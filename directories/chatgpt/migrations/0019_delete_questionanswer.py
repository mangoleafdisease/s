# Generated by Django 3.1.3 on 2024-01-08 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0018_questionanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]

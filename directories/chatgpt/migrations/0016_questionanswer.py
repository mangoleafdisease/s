# Generated by Django 3.1.3 on 2023-12-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0015_delete_questionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('code', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.TextField()),
                ('user', models.CharField(max_length=1000)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 3.1.3 on 2023-12-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0011_chatgptrecord_profiles_resetlink_talktopdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('user', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='user',
        ),
        migrations.RemoveField(
            model_name='resetlink',
            name='user',
        ),
        migrations.RemoveField(
            model_name='talktopdf',
            name='profiles',
        ),
        migrations.DeleteModel(
            name='ChatGPTRecord',
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
        migrations.DeleteModel(
            name='ResetLink',
        ),
        migrations.DeleteModel(
            name='TalkToPdf',
        ),
    ]

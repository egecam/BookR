# Generated by Django 4.1.7 on 2023-03-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', help_text='Title of the book', max_length=70)),
                ('contributors', models.TextField(max_length=200)),
            ],
        ),
    ]
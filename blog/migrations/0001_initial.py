# Generated by Django 4.2.17 on 2024-12-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-published_on'],
            },
        ),
    ]

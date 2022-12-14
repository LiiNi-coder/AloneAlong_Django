# Generated by Django 4.0.6 on 2022-08-16 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(help_text='Post ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('1', '혼밥'), ('2', '혼술'), ('3', '혼카페'), ('4', '혼놀')], default='1', max_length=3)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog_photo')),
                ('body', models.TextField()),
                ('location', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communityapp.blog')),
            ],
        ),
    ]

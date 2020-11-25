# Generated by Django 3.1.3 on 2020-11-24 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('username', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=254)),
                ('suite', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('zipcode', models.CharField(max_length=254)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('phone', models.CharField(max_length=254)),
                ('website', models.URLField()),
                ('company_name', models.CharField(max_length=254)),
                ('catch_phrase', models.TextField()),
                ('bs', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('body', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
    ]
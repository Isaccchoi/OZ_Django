# Generated by Django 5.0.4 on 2024-04-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d', verbose_name='이미지'),
        ),
    ]

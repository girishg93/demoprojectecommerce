# Generated by Django 4.1.3 on 2022-12-12 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_alter_category_name_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name', 'image', 'description', 'slug'), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
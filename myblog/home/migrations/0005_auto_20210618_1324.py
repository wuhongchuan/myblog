# Generated by Django 3.2.4 on 2021-06-18 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210618_1319'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='tb_article1',
        ),
        migrations.AlterModelTable(
            name='articlecategory',
            table='tb_category1',
        ),
    ]

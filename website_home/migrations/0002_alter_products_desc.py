# Generated by Django 3.2.3 on 2021-06-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.TextField(),
        ),
    ]

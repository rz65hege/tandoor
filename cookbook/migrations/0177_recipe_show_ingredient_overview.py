# Generated by Django 4.0.4 on 2022-06-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0176_alter_searchpreference_icontains_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='show_ingredient_overview',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-04-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0004_blog_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

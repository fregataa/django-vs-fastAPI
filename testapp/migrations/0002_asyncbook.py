# Generated by Django 3.2.4 on 2021-06-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AsyncBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, unique=True)),
                ("author", models.CharField(max_length=50, null=True)),
                ("volume", models.IntegerField(null=True)),
            ],
        ),
    ]

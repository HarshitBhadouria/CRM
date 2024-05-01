# Generated by Django 5.0.4 on 2024-04-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("created_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=20)),
            ],
        ),
    ]

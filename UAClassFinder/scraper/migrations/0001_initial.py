# Generated by Django 4.1.3 on 2023-10-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_id", models.CharField(max_length=10)),
                ("department", models.CharField(max_length=10)),
                ("class_code", models.CharField(max_length=10)),
                ("course_name", models.CharField(max_length=100)),
                ("instructor", models.CharField(max_length=100)),
            ],
        ),
    ]
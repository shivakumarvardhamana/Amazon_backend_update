# Generated by Django 4.1.5 on 2023-02-01 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("amazon_backend_api", "0007_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=200, verbose_name="Product Name")),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Brand_Name",
                        to="amazon_backend_api.brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Category",
                        to="amazon_backend_api.category",
                    ),
                ),
                (
                    "subcategory1",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="SubCategory1",
                        to="amazon_backend_api.subcategory",
                    ),
                ),
                (
                    "subcategory2",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="SubCategory2",
                        to="amazon_backend_api.subcategory",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
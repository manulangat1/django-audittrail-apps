# Generated by Django 4.1.2 on 2023-04-16 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=199)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=199)),
                ("content", models.TextField()),
                ("isPublished", models.BooleanField(default=False)),
                ("image", models.CharField(max_length=255, null=True)),
                ("slug", models.CharField(max_length=255, null=True)),
                ("tags", models.ManyToManyField(to="blogs.tag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AuditTrail",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("login_IP", models.GenericIPAddressField(blank=True, null=True)),
                ("action_datetime", models.DateTimeField(auto_now=True)),
                ("changed_object", models.CharField(max_length=40)),
                ("event_category", models.CharField(max_length=40)),
                ("user_agent_info", models.CharField(max_length=255)),
                ("is_deleted", models.BooleanField(default=False)),
                ("action", models.CharField(max_length=40)),
                ("change_summary", models.CharField(max_length=199)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

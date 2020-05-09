# Generated by Django 3.0.5 on 2020-05-09 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_bookshelf_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bookshelf', to=settings.AUTH_USER_MODEL, verbose_name='本棚の所持者'),
        ),
    ]

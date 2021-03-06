# Generated by Django 3.0.5 on 2020-04-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200422_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_no', models.IntegerField(verbose_name='本の列')),
                ('row_no', models.IntegerField(verbose_name='本の行')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookPosition',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='api.BookPosition', verbose_name='本の位置'),
        ),
    ]

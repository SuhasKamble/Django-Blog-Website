# Generated by Django 3.0.7 on 2021-02-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]

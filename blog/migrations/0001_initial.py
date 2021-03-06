# Generated by Django 3.0.7 on 2021-02-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.CharField(max_length=3000)),
                ('author', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=340)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

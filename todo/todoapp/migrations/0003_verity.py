# Generated by Django 4.2.1 on 2023-05-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='verity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.CharField(max_length=50)),
                ('mobiles', models.CharField(max_length=50)),
                ('otp', models.IntegerField()),
            ],
        ),
    ]
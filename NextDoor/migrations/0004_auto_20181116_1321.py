# Generated by Django 2.1.2 on 2018-11-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NextDoor', '0003_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='subject',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(max_length=350),
        ),
    ]
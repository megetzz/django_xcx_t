# Generated by Django 3.0.3 on 2020-03-30 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juheapp', '0003_auto_20200328_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickName',
            field=models.CharField(db_index=True, max_length=64),
        ),
    ]

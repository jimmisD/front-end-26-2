# Generated by Django 3.0.2 on 2020-02-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200225_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='api_key',
            field=models.CharField(blank=True, db_column='api_key', max_length=256, null=True),
        ),
    ]

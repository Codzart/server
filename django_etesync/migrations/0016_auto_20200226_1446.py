# Generated by Django 3.0.3 on 2020-02-26 14:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_etesync', '0015_auto_20200226_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='uid',
            field=models.CharField(db_index=True, max_length=44, validators=[django.core.validators.RegexValidator(message='Not a valid UID. Expected a 256bit base64url.', regex='[a-zA-Z0-9\\-_=]{43}')]),
        ),
        migrations.AlterField(
            model_name='collectionitem',
            name='uid',
            field=models.CharField(db_index=True, max_length=44, validators=[django.core.validators.RegexValidator(message='Not a valid UID. Expected a 256bit base64url.', regex='[a-zA-Z0-9\\-_=]{43}')]),
        ),
        migrations.AlterField(
            model_name='collectionitemchunk',
            name='uid',
            field=models.CharField(db_index=True, max_length=44, validators=[django.core.validators.RegexValidator(message='Not a valid UID. Expected a 256bit base64url.', regex='[a-zA-Z0-9\\-_=]{43}')]),
        ),
    ]

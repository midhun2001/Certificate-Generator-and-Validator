# Generated by Django 4.2.6 on 2023-10-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_remove_certificate_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='token',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]

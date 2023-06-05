# Generated by Django 4.2 on 2023-05-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_s', '0002_alter_api_s_contact_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_s',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='api_s',
            name='Location',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='api_s',
            name='Number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='api_s',
            name='Contact_details',
            field=models.CharField(max_length=120),
        ),
    ]

# Generated by Django 4.2 on 2023-05-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Address', models.CharField(max_length=120)),
                ('Contact_details', models.CharField(choices=[('Number', 'Number'), ('Email', 'Email')], max_length=120)),
                ('Tech_skill', models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('ruby', 'Ruby'), ('docker', 'Docker'), ('node', 'Node'), ('javascript', 'JavaScript')], max_length=120)),
            ],
        ),
    ]

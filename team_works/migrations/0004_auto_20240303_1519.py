# Generated by Django 3.0.2 on 2024-03-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_works', '0003_auto_20240302_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberworks',
            name='file',
            field=models.FileField(default='', upload_to='members_work/files'),
        ),
        migrations.AlterField(
            model_name='memberworks',
            name='link',
            field=models.CharField(default='', max_length=2100),
        ),
    ]

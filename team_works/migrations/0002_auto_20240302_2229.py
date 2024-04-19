# Generated by Django 3.0.2 on 2024-03-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=200)),
                ('sortno', models.IntegerField()),
                ('title', models.CharField(max_length=200, unique=True)),
                ('picture', models.ImageField(upload_to='members_work/images')),
                ('link', models.CharField(max_length=2100)),
                ('file', models.FileField(upload_to='members_work/files')),
                ('explanation', models.TextField()),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='humansimage',
            name='picture',
            field=models.ImageField(upload_to='team_member_img/'),
        ),
        migrations.AlterField(
            model_name='humansimage',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
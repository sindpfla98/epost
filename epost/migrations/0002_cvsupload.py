# Generated by Django 2.2.4 on 2020-02-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVSUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='파일')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='업로드 날짜')),
            ],
        ),
    ]

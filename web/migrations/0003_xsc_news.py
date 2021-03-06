# Generated by Django 2.1.1 on 2018-09-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_jwc_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='xsc_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('source', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=255)),
                ('release_time', models.DateTimeField()),
                ('read_status', models.IntegerField()),
                ('get_time', models.DateTimeField()),
                ('imgs', models.CharField(max_length=255)),
            ],
        ),
    ]

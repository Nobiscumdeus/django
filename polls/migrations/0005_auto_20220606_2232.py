# Generated by Django 3.1.2 on 2022-06-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_jss1_jss2_jss3_sss1_sss2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sss1',
            name='grades',
            field=models.CharField(default='A', max_length=1),
        ),
    ]

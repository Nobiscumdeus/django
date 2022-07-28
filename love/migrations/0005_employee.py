# Generated by Django 3.1.2 on 2022-05-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0004_author_blog_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employe',
            },
        ),
    ]
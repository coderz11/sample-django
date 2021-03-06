# Generated by Django 3.2.5 on 2021-08-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=100)),
                ('postdate', models.DateField(auto_now_add=True, null=True)),
                ('category', models.CharField(choices=[{'Business', 'ビジネス'}, {'生活', 'Life'}, {'Others', 'その他'}], default='ビジネス', max_length=50, null=True)),
            ],
        ),
    ]

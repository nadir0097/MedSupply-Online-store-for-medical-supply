# Generated by Django 3.1.7 on 2021-03-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('img', models.ImageField(default='Product Image', upload_to='media')),
            ],
        ),
    ]
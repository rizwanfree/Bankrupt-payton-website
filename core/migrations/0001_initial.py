# Generated by Django 4.2.8 on 2024-02-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_no', models.CharField(max_length=100, unique=True)),
                ('district', models.CharField(max_length=50)),
                ('chapter', models.IntegerField()),
                ('assets', models.IntegerField()),
                ('date_filed', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('ssn', models.CharField(max_length=50)),
                ('street1', models.CharField(max_length=255)),
                ('street2', models.CharField(blank=True, max_length=255, null=True)),
                ('street3', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('zip', models.CharField(max_length=10)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]

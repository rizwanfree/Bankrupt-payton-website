# Generated by Django 4.2.8 on 2024-02-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_case_case_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('date_send', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('date_send',),
            },
        ),
    ]

# Generated by Django 4.2.8 on 2024-02-12 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_contact_options_remove_contact_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactUs',
        ),
    ]

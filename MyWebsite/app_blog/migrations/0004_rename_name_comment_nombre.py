# Generated by Django 3.2 on 2021-05-06 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_post_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='nombre',
        ),
    ]
# Generated by Django 3.2.14 on 2022-08-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_alter_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(related_name='projects', to='portfolios.Tag'),
        ),
    ]
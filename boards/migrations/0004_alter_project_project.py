# Generated by Django 3.2.6 on 2021-08-25 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20210825_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='boards.projects'),
        ),
    ]

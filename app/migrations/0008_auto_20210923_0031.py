# Generated by Django 3.1 on 2021-09-22 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210922_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='app.project'),
        ),
    ]
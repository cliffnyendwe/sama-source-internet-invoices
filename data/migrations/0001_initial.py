# Generated by Django 3.1 on 2021-09-27 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='agent name', max_length=150)),
                ('ssdc_number', models.CharField(default='agent ssdc number', max_length=100)),
                ('installation', models.IntegerField(default=0)),
                ('payment_method', models.CharField(choices=[('m-pesa', 'm-pesa'), ('bank', 'bank'), ('airtel money', 'airtel money'), ('t-kash', 't-kash'), ('paypal', 'paypal')], default='m-pesa', max_length=200)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='tl name', max_length=150)),
                ('ssdc_number', models.CharField(default='tl ssdc number', max_length=100)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('team_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.teamleader')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isp_name', models.CharField(default='isp name', max_length=100)),
                ('monthly_subscription', models.IntegerField(default='monthly subscription')),
                ('invoice_file', models.FileField(blank=True, null=True, upload_to='invoices/')),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Payment Pending', 'Payment Pending'), ('Not Paid', 'Not Paid')], default='Payment Pending', max_length=100)),
                ('date_submitted', models.DateField(default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.agent')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.project')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.job'),
        ),
        migrations.AddField(
            model_name='agent',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='data.project'),
        ),
        migrations.AddField(
            model_name='agent',
            name='team_leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.teamleader'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
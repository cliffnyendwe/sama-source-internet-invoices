# Generated by Django 3.1 on 2021-09-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_invoice_invoice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Payment Pending', 'Payment Pending')], default='Payment Pending', max_length=100),
        ),
    ]

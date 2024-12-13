# Generated by Django 4.1.5 on 2023-07-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='card_type',
            field=models.CharField(choices=[('Master', 'Master'), ('Visa', 'Visa'), ('Verve', 'Verve')], default='Master', max_length=20),
        ),
    ]
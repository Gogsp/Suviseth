# Generated by Django 3.2.4 on 2021-08-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuvisethApp', '0003_customer_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='district',
            field=models.CharField(choices=[('Jaffna', 'Jaffna'), ('Galle', 'Galle')], max_length=150, null=True),
        ),
    ]
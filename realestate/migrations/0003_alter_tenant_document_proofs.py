# Generated by Django 4.2.7 on 2024-01-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_alter_tenant_document_proofs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='document_proofs',
            field=models.ImageField(upload_to='images'),
        ),
    ]

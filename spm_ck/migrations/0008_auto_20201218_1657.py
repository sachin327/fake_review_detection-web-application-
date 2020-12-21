# Generated by Django 3.1.4 on 2020-12-18 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spm_ck', '0007_auto_20201218_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='rated_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spm_ck.product'),
        ),
    ]
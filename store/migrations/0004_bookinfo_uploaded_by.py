# Generated by Django 4.2.16 on 2024-10-04 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_bookinfo_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.userdetail'),
        ),
    ]

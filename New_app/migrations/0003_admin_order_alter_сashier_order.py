# Generated by Django 4.1.1 on 2022-09-17 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('New_app', '0002_сashier'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='New_app.order'),
        ),
        migrations.AlterField(
            model_name='сashier',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='New_app.order'),
        ),
    ]

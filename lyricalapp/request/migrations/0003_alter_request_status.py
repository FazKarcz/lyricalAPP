# Generated by Django 4.2.7 on 2024-04-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('PG', 'Nie rozpatrzony'), ('AC', 'Przyjęty'), ('DC', 'Odrzucony')], default='PG', max_length=2),
        ),
    ]

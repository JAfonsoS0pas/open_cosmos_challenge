# Generated by Django 4.2.10 on 2024-02-20 10:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscardedValue',
            fields=[
                ('value_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business.value')),
                ('reasons', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
            ],
            options={
                'verbose_name_plural': 'Discarded Data',
            },
            bases=('business.value',),
        ),
    ]

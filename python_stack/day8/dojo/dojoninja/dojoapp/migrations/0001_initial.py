# Generated by Django 4.2.5 on 2023-09-21 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dojo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2)),
                ('name', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ninja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('dojo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dojon', to='dojoapp.dojo')),
            ],
        ),
    ]

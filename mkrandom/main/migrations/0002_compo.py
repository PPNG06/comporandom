# Generated by Django 3.1.7 on 2021-09-20 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
                ('glider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.glider')),
                ('tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tire')),
                ('veh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehicle')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-11 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_and_reservation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='item',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='quantity',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_note',
            field=models.TextField(blank=True, max_length=500, verbose_name='Poznámka k rezervaci'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='Vytvořena dne'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='organisation_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Organizace'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_number',
            field=models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Rezervační číslo'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Upravena dne'),
        ),
        migrations.CreateModel(
            name='ReservedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Počet kusů')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_and_reservation.itemvariation', verbose_name='Rezervovaná položka')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_and_reservation.reservation', verbose_name='Rezervace')),
            ],
        ),
    ]

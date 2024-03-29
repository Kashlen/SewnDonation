# Generated by Django 4.0.3 on 2022-05-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_and_reservation', '0003_rename_reservation_reserveditem_reservation_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemvariation',
            options={'verbose_name': 'Varianta položky', 'verbose_name_plural': 'Varianty položek'},
        ),
        migrations.AlterModelOptions(
            name='reserveditem',
            options={'verbose_name': 'Rezervovaná položka', 'verbose_name_plural': 'Rezervované položky'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Vytvořena dne'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('new', 'nová'), ('in progress', 'rozpracovaná'), ('completed', 'připravená k odeslání'), ('sent', 'odeslaná'), ('cancelled', 'zrušená')], default='new', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Upravena dne'),
        ),
    ]

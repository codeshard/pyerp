# Generated by Django 2.2.4 on 2019-08-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20190821_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pyaccountmove',
            name='lines',
        ),
        migrations.AddField(
            model_name='pyaccountmoveline',
            name='move',
            field=models.ForeignKey(blank=True, null=True, on_delete='cascade', related_name='lines', to='account.PyAccountMove'),
        ),
    ]

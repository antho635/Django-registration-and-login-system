# Generated by Django 4.1.3 on 2022-11-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_mdpgenere'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MdpGenere',
        ),
    ]
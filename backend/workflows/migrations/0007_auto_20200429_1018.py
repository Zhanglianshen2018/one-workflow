# Generated by Django 3.0.2 on 2020-04-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0006_state_state_field_str'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state_field_str',
        ),
        migrations.AddField(
            model_name='state',
            name='fields',
            field=models.ManyToManyField(blank=True, to='workflows.CustomField', verbose_name='可编辑字段'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='field_attribute',
            field=models.BooleanField(default=False, verbose_name='字段是否内置'),
        ),
    ]
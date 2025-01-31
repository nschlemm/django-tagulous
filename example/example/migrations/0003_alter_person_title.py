# Generated by Django 3.2.6 on 2021-08-24 07:28

from django.db import migrations
import django.db.models.deletion
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_auto_20190224_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='title',
            field=tagulous.models.fields.SingleTagField(_set_tag_meta=True, blank=True, help_text='This is a SingleTagField - effectively a CharField with dynamic choices', initial='Mr, Mrs', null=True, on_delete=django.db.models.deletion.CASCADE, to='example.tagulous_person_title'),
        ),
    ]

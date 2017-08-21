# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 14:43
from __future__ import unicode_literals

from django.db import migrations
import falmer.content.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20170714_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='full_time_officers',
            field=wagtail.wagtailcore.fields.StreamField((('figure', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', falmer.content.blocks.ImageBlock()), ('link', wagtail.wagtailcore.blocks.CharBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='part_time_officers',
            field=wagtail.wagtailcore.fields.StreamField((('figure', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', falmer.content.blocks.ImageBlock()), ('link', wagtail.wagtailcore.blocks.CharBlock(required=False))))),)),
        ),
    ]
# Generated by Django 2.0.8 on 2018-08-18 14:05

from django.db import migrations
import falmer.content.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0004_auto_20180704_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='main',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h2', 'bold', 'italic', 'ol', 'ul', 'hr', 'link']))])), ('image', wagtail.core.blocks.StructBlock([('image', falmer.content.blocks.FalmerImageChooserBlock(required=True)), ('alternative_title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('callout', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.TextBlock()), ('variant', wagtail.core.blocks.ChoiceBlock(choices=[('info', 'Info'), ('alert', 'Alert')], label='Variant'))]))], blank=True, help_text='Any additional information about this deal'),
        ),
    ]
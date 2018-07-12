# Generated by Django 2.0.5 on 2018-07-04 10:03

from django.db import migrations
import falmer.content.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0007_auto_20180703_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kbreferencepage',
            name='main',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h2', 'bold', 'italic', 'ol', 'ul', 'hr']))])), ('callout', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.TextBlock()), ('variant', wagtail.core.blocks.ChoiceBlock(choices=[('info', 'Info'), ('alert', 'Alert')], label='Variant'))])), ('image', wagtail.core.blocks.StructBlock([('image', falmer.content.blocks.FalmerImageChooserBlock(required=True)), ('alternative_title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('button_group_links', wagtail.core.blocks.StreamBlock([('internal_link', wagtail.core.blocks.StructBlock([('link', falmer.content.blocks.FalmerPageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(required=False))], label='Internal page')), ('external_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('target', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Open link in'), ('_self', 'Same window'), ('_blank', 'New window')], help_text='Open link in'))], label='External Page'))]))], blank=True, null=True, verbose_name='Main Content'),
        ),
    ]

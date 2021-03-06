# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Identify this component for other editors', max_length=100)),
                ('header', models.CharField(blank=True, help_text='Heading that will display on page for this component', max_length=500)),
                ('description', wagtail.core.fields.RichTextField(blank=True, help_text='Body (richtext) of component')),
                ('newsletter', models.CharField(default='mozilla-foundation', help_text='The (pre-existing) SalesForce newsletter to sign up for', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'CTA',
            },
        ),
        migrations.CreateModel(
            name='ModularPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', models.CharField(blank=True, max_length=250)),
                ('body', wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'image'])), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button'), ('btn-success', 'Success button'), ('btn-info', 'Info button'), ('btn-warning', 'Warning button'), ('btn-error', 'Error button'), ('btn-ghost', 'Ghost button')])), ('outline', wagtail.core.blocks.BooleanBlock(default=False, required=False))))), ('spacer', wagtail.core.blocks.StructBlock((('rem', wagtail.core.blocks.IntegerBlock()),)))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MiniSiteNameSpace',
            fields=[
                ('modularpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.ModularPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailpages.modularpage',),
        ),
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('cta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.CTA')),
                ('google_forms_url', models.URLField(help_text='Google form to post petition data to', max_length=2048, null=True)),
                ('checkbox_1', models.CharField(blank=True, help_text='label for the first checkbox option (may contain HTML)', max_length=1024)),
                ('checkbox_1_form_field', models.CharField(blank=True, help_text='Google form field name for Checkbox 1', max_length=1024, verbose_name='First checkbox Google Form field')),
                ('checkbox_2', models.CharField(blank=True, help_text='label for the second checkbox option (may contain HTML)', max_length=1024)),
                ('checkbox_2_form_field', models.CharField(blank=True, help_text='Google form field name for Checkbox 1', max_length=1024, verbose_name='Second checkbox Google Form field')),
                ('given_name_form_field', models.CharField(blank=True, help_text='Google form field name for Given Name(s)', max_length=1024, verbose_name='Given Name(s) Google Form field')),
                ('surname_form_field', models.CharField(blank=True, help_text='Google form field name for Surname', max_length=1024, verbose_name='Surname Google Form field')),
                ('email_form_field', models.CharField(blank=True, help_text='Google form field name for Email', max_length=1024, verbose_name='Email Google Form field')),
                ('newsletter_signup_form_field', models.CharField(blank=True, help_text='Google form field name for Mozilla Newsletter checkbox', max_length=1024, verbose_name='Mozilla Newsletter signup checkbox Google Form field')),
                ('share_link', models.URLField(blank=True, help_text='Link that will be put in share button', max_length=1024)),
                ('share_link_text', models.CharField(blank=True, default='Share this', help_text='Text content of the share button', max_length=20)),
                ('thank_you', models.CharField(default='Thank you for signing too!', help_text='Message to show after thanking people for signing', max_length=140)),
            ],
            options={
                'verbose_name': 'petition snippet',
            },
            bases=('wagtailpages.cta',),
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('cta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.CTA')),
            ],
            options={
                'verbose_name': 'signup snippet',
            },
            bases=('wagtailpages.cta',),
        ),
        migrations.CreateModel(
            name='CampaignPage',
            fields=[
                ('minisitenamespace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.MiniSiteNameSpace')),
                ('cta', models.ForeignKey(blank=True, help_text='Choose existing or create new sign-up form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page', to='wagtailpages.Petition')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailpages.minisitenamespace',),
        ),
        migrations.CreateModel(
            name='OpportunityPage',
            fields=[
                ('minisitenamespace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.MiniSiteNameSpace')),
                ('cta', models.ForeignKey(blank=True, help_text='Choose existing or create new petition form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page', to='wagtailpages.Signup')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailpages.minisitenamespace',),
        ),
    ]

# Generated by Django 5.2.4 on 2025-07-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(choices=[('database_management', 'Database Management'), ('system_analysis', 'System Analysis and Design'), ('artificial_intelligence', 'Artificial Intelligence'), ('technopreneurship', 'Technopreneurship'), ('compiler_design', 'Compiler Design and Construction')], default='database_management', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]

# Generated by Django 2.2.12 on 2020-04-10 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('watson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watsonaccess',
            name='fk_assistants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Assistants', verbose_name='Assistente Virtual'),
        ),
        migrations.AlterField(
            model_name='watsonaccess',
            name='fk_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Proprietário'),
        ),
        migrations.AlterField(
            model_name='watsoncomponents',
            name='pk_watson_components',
            field=models.CharField(choices=[('Assistant Skills', 'Workspace Assistant Skills'), ('Watson Assistant', 'Assistente Virtual Watson'), ('Watson Studio', 'Aprendizado de Máquina Embarcado'), ('Watson Machine Learning', 'Aprendizado de Máquina'), ('Compare and Comply', 'Processamento de Documentos'), ('Discovery', 'Busca Analítica de Conteúdo'), ('Knowledge Catalog', 'Busca, Cataloga e Compartilha Documentos'), ('Knowledge Studio', 'Aprendizado de Linguagem de Domínio'), ('Language Translator', 'Tradutor de Linguagens'), ('Natural Language Understanding', 'Analisador de Textos'), ('Personality Insights', 'Gerar Perfil Psicológico'), ('SpeechToText', 'Reconheciento de Fala'), ('TextToSpeech', 'Transforma Texto em Fala'), ('Visual Recognition', 'Reconhecimento de Imagens')], max_length=50, primary_key=True, serialize=False, verbose_name='Tipo Componente'),
        ),
        migrations.AlterField(
            model_name='watsonlogs',
            name='flag_invalid_response',
            field=models.SmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=0, verbose_name='Resposta Inválida'),
        ),
        migrations.AlterField(
            model_name='watsonlogs',
            name='flag_resolve',
            field=models.SmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=0, verbose_name='Resolvida'),
        ),
    ]

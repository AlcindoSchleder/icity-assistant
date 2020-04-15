INSERT INTO "icity_assistants" 
    ("pk_assistants", "dsc_assistant", "flag_logon", "insert_date", "update_date", "workspace_Key", "workspace_URL", "workspace_id", "workspace_name")
VALUES
    (1, 'Informações sobre o Corona Vírus', 0, '2020-04-10T21:45:25.017', '2020-04-13T23:08:43.018', 'gQ6ZgBpiL1c9svR7qiGjLjz7M6Aw87zd7LYJRqjCrq-u', 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/84d98d44-37ec-4257-a0e4-1148961f3648/v2/assistants/84d98d44-37ec-4257-a0e4-1148961f3648/sessions', '84d98d44-37ec-4257-a0e4-1148961f3648', 'corona_info');
INSERT INTO "icity_assistants" 
    ("pk_assistants", "dsc_assistant", "flag_logon", "insert_date", "update_date", "workspace_Key", "workspace_URL", "workspace_id", "workspace_name")
VALUES
    (2, 'Atendimento Suspeitos Corona Vírus', 1, '2020-04-10T21:46:07.880', '2020-04-14T20:18:00.634', 'gQ6ZgBpiL1c9svR7qiGjLjz7M6Aw87zd7LYJRqjCrq-u', 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/84d98d44-37ec-4257-a0e4-1148961f3648/v2/assistants/84d98d44-37ec-4257-a0e4-1148961f3648/sessions', '84d98d44-37ec-4257-a0e4-1148961f3648', 'covid_forwarder');
INSERT INTO "icity_assistants" 
    ("pk_assistants", "dsc_assistant", "flag_logon", "insert_date", "update_date", "workspace_Key", "workspace_URL", "workspace_id", "workspace_name")
VALUES
    (3, 'Concierge Gramado - RS', 0, '2020-04-10T21:46:28.256', '2020-04-11T21:07:02.172', 'J8fqtO9lF2CK3YQt_b1UpyY8UZ4curQkrTDEwFL1U4pc', 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/94c08f80-908a-40e4-8ca6-ba21803f3658/v2/assistants/01a988aa-dc97-4e72-847f-a59228c56d63/sessions', '01a988aa-dc97-4e72-847f-a59228c56d63', 'icity_gramado');


INSERT INTO "icity_publicity" 
    ("pk_publicity", "title_media", "dsc_media", "file_path", "insert_date", "update_date")
VALUES
    (1, 'Magazine Regalli', 'A melhor loja da internet. Preços atrativos e entrega garantida com a qualidade que você já conhece. Uma associada Magazine Luiza.', 'publicity/magazine_regalli_6w2zMdb.jpeg', '2020-04-13T15:55:16.578', '2020-04-13T21:36:37.486');
INSERT INTO "icity_publicity" 
    ("pk_publicity", "title_media", "dsc_media", "file_path", "insert_date", "update_date")
VALUES
    (2, 'Le Petit Clos Restaurant', 'Venha desfrutar os melhores momentos de sua vida conosco. Em Gramado, a única casa tradicional de fondues e pratos a la carte deliciosos acompanhados dos melhores vinhos do mercado', 'publicity/lepetit.jpeg', '2020-04-13T21:10:41.727', '2020-04-13T21:35:28.272');
INSERT INTO "icity_publicity" 
    ("pk_publicity", "title_media", "dsc_media", "file_path", "insert_date", "update_date")
VALUES
    (3, 'Ensa Tecnologia', 'Hardware Especialista, Software Especiais, IoT, Inteligência Artificial, Data Science, tudo isso e muito mais  encontre aqui. Entre em contato conosco hoje mesmo', 'publicity/ensa01.jpeg', '2020-04-13T21:33:25.641', '2020-04-13T21:33:25.641');
INSERT INTO "icity_publicity" 
    ("pk_publicity", "title_media", "dsc_media", "file_path", "insert_date", "update_date")
VALUES
    (4, 'Ensa Tecnologia', 'Hardware Especialista, Software Especiais, IoT, Inteligência Artificial, Data Science, tudo isso e muito mais  encontre aqui. Entre em contato conosco hoje mesmo', 'publicity/ensa02.jpeg', '2020-04-13T22:22:59.693', '2020-04-13T22:22:59.693');


INSERT INTO "icity-pub-assistants" 
    ("id", "publicity_id", "assistants_id")
VALUES
    (1, 1, 3);
INSERT INTO "icity-pub-assistants" 
    ("id", "publicity_id", "assistants_id")
VALUES
    (2, 2, 3);


INSERT INTO "watson_components" 
    ("pk_watson_components", "dsc_comp", "insert_date", "update_date")
VALUES
    ('Language Translator', 'wlt_iCity', '2020-04-04T06:11:57.808', '2020-04-10T22:27:08.273');
INSERT INTO "watson_components" 
    ("pk_watson_components", "dsc_comp", "insert_date", "update_date")
VALUES
    ('Personality Insights', 'wpi_iCity', '2020-04-04T06:13:06.220', '2020-04-10T22:27:48.334');
INSERT INTO "watson_components" 
    ("pk_watson_components", "dsc_comp", "insert_date", "update_date")
VALUES
    ('Natural Language Understanding', 'wnlu-icity', '2020-04-10T22:25:17.161', '2020-04-10T22:28:26.722');
INSERT INTO "watson_components" 
    ("pk_watson_components", "dsc_comp", "insert_date", "update_date")
VALUES
    ('SpeechToText', 'wstt_iCity', '2020-04-10T22:26:37.784', '2020-04-10T22:26:37.784');
INSERT INTO "watson_components" 
    ("pk_watson_components", "dsc_comp", "insert_date", "update_date")
VALUES
    ('TextToSpeech', 'wtts_iCity', '2020-04-10T22:29:06.862', '2020-04-10T22:29:06.862');


INSERT INTO "watson_access" 
    ("pk_watson_access", "fk_watson_components_id", "component_name", "component_key", "component_url", "insert_date", "update_date")
VALUES
    (1, 'SpeechToText', 'Speech To Text', '1DYKCjKEywSBx8OSrwllWmPbwyXhUDENDNDPpr33CN0q', 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ad9d0721-4718-494e-8351-a1e04d42176f', '2020-04-10T22:40:22.291', '2020-04-11T00:16:17.740');
INSERT INTO "watson_access" 
   ("pk_watson_access", "fk_watson_components_id", "component_name", "component_key", "component_url", "insert_date", "update_date")
VALUES
    (2, 'Language Translator', 'Language Translator', 'YzCtPx54CevyJYNDMJ5gdzdu0B2QbjW6gFffNovrjGEy', 'https://gateway.watsonplatform.net/language-translator/api', '2020-04-10T22:42:00.277', '2020-04-11T00:16:09.773');
INSERT INTO "watson_access" 
    ("pk_watson_access", "fk_watson_components_id", "component_name", "component_key", "component_url", "insert_date", "update_date")
VALUES
    (3, 'TextToSpeech', 'Text to Speech', 'rwm9apTmqH96nGQre0OtO55bBEoI6EPmIastgJv-uEF7', 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/bdcbabd3-098b-4430-803c-fea18199fbbd', '2020-04-10T22:43:41.001', '2020-04-11T00:16:00.669');
INSERT INTO "watson_access" 
    ("pk_watson_access", "fk_watson_components_id", "component_name", "component_key", "component_url", "insert_date", "update_date")
VALUES
    (4, 'Personality Insights', 'Personality Insights', 'sWrKUfkI0DgZR58fb3dQALv-nUTDwyq9EFQ9Rdzlyprb', 'https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/66d1e7f1-16a9-4ec1-996d-99ef0dcafa3d', '2020-04-10T22:44:44.304', '2020-04-11T00:15:43.154');


INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (1, 4, 1);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (2, 4, 2);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (3, 4, 3);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (4, 3, 1);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (5, 3, 2);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (6, 3, 3);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (7, 2, 1);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (8, 2, 2);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (9, 2, 3);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (10, 1, 1);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (11, 1, 2);
INSERT INTO "watson_access_fk_assistants" 
    ("id", "watsonaccess_id", "assistants_id")
VALUES
    (12, 1, 3);

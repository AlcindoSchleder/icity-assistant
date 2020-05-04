--
-- PostgreSQL database dump
--

-- Dumped from database version 11.6
-- Dumped by pg_dump version 12.2

-- Started on 2020-05-04 00:13:45

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3021 (class 0 OID 16428)
-- Dependencies: 203
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.icity_assistants (pk_assistants, dsc_assistant, flag_logon, workspace_name, workspace_id, "workspace_URL", "workspace_Key", insert_date, update_date, assistant_class) FROM stdin;
1	Informações sobre o Corona Vírus	0	corona_info	84d98d44-37ec-4257-a0e4-1148961f3648	https://api.us-south.assistant.watson.cloud.ibm.com/instances/84d98d44-37ec-4257-a0e4-1148961f3648/v2/assistants/84d98d44-37ec-4257-a0e4-1148961f3648/sessions	gQ6ZgBpiL1c9svR7qiGjLjz7M6Aw87zd7LYJRqjCrq-u	2020-04-10 21:45:25.017-03	2020-04-13 23:08:43.018-03	 
2	Atendimento Suspeitos Corona Vírus	1	covid_forwarder	84d98d44-37ec-4257-a0e4-1148961f3648	https://api.us-south.assistant.watson.cloud.ibm.com/instances/84d98d44-37ec-4257-a0e4-1148961f3648/v2/assistants/84d98d44-37ec-4257-a0e4-1148961f3648/sessions	gQ6ZgBpiL1c9svR7qiGjLjz7M6Aw87zd7LYJRqjCrq-u	2020-04-10 21:46:07.88-03	2020-04-14 20:18:00.634-03	 
3	Concierge Gramado - RS	0	icity_gramado	01a988aa-dc97-4e72-847f-a59228c56d63	https://api.us-south.assistant.watson.cloud.ibm.com/instances/94c08f80-908a-40e4-8ca6-ba21803f3658/v2/assistants/01a988aa-dc97-4e72-847f-a59228c56d63/sessions	J8fqtO9lF2CK3YQt_b1UpyY8UZ4curQkrTDEwFL1U4pc	2020-04-10 21:46:28.256-03	2020-04-11 21:07:02.172-03	 
\.


--
-- TOC entry 3036 (class 0 OID 16578)
-- Dependencies: 218
-- Data for Name: icity_publicity; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.icity_publicity (pk_publicity, title_media, dsc_media, file_path, insert_date, update_date) FROM stdin;
3	Ensa Tecnologia	Hardware Especialista, Software Especiais, IoT, Inteligência Artificial, Data Science, tudo isso e muito mais  encontre aqui. Entre em contato conosco hoje mesmo	publicity/ensa01.jpeg	2020-04-13 21:33:25.641-03	2020-04-13 21:33:25.641-03
4	Ensa Tecnologia	Hardware Especialista, Software Especiais, IoT, Inteligência Artificial, Data Science, tudo isso e muito mais  encontre aqui. Entre em contato conosco hoje mesmo	publicity/ensa02.jpeg	2020-04-13 22:22:59.693-03	2020-04-13 22:22:59.693-03
2	Le Petit Clos Restaurant	Venha desfrutar os melhores momentos de sua vida conosco. Em Gramado, a única casa tradicional de fondues e pratos a la carte deliciosos acompanhados dos melhores vinhos do mercado	publicity/lepetit.jpeg	2020-04-13 21:10:41.727-03	2020-04-16 10:49:45.791384-03
1	Magazine Regalli	A melhor loja da internet. Preços atrativos e entrega garantida com a qualidade que você já conhece. Uma associada Magazine Luiza.	publicity/magazine_regalli_6w2zMdb.jpeg	2020-04-13 15:55:16.578-03	2020-04-16 10:50:00.376713-03
\.


--
-- TOC entry 3038 (class 0 OID 16589)
-- Dependencies: 220
-- Data for Name: icity_pub_assistants; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.icity_pub_assistants (id, publicity_id, assistants_id) FROM stdin;
1	2	3
2	1	3
\.


--
-- TOC entry 3039 (class 0 OID 16609)
-- Dependencies: 221
-- Data for Name: watson_components; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.watson_components (pk_watson_components, dsc_comp, insert_date, update_date) FROM stdin;
Language Translator	wlt_iCity	2020-04-04 06:11:57.808-03	2020-04-10 22:27:08.273-03
Personality Insights	wpi_iCity	2020-04-04 06:13:06.22-03	2020-04-10 22:27:48.334-03
Natural Language Understanding	wnlu-icity	2020-04-10 22:25:17.161-03	2020-04-10 22:28:26.722-03
SpeechToText	wstt_iCity	2020-04-10 22:26:37.784-03	2020-04-10 22:26:37.784-03
TextToSpeech	wtts_iCity	2020-04-10 22:29:06.862-03	2020-04-10 22:29:06.862-03
\.


--
-- TOC entry 3043 (class 0 OID 16627)
-- Dependencies: 225
-- Data for Name: watson_access; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.watson_access (pk_watson_access, component_name, component_key, component_url, insert_date, update_date, fk_watson_components_id) FROM stdin;
1	Speech To Text	1DYKCjKEywSBx8OSrwllWmPbwyXhUDENDNDPpr33CN0q	https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ad9d0721-4718-494e-8351-a1e04d42176f	2020-04-10 22:40:22.291-03	2020-04-11 00:16:17.74-03	SpeechToText
2	Language Translator	YzCtPx54CevyJYNDMJ5gdzdu0B2QbjW6gFffNovrjGEy	https://gateway.watsonplatform.net/language-translator/api	2020-04-10 22:42:00.277-03	2020-04-11 00:16:09.773-03	Language Translator
3	Text to Speech	rwm9apTmqH96nGQre0OtO55bBEoI6EPmIastgJv-uEF7	https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/bdcbabd3-098b-4430-803c-fea18199fbbd	2020-04-10 22:43:41.001-03	2020-04-11 00:16:00.669-03	TextToSpeech
4	Personality Insights	sWrKUfkI0DgZR58fb3dQALv-nUTDwyq9EFQ9Rdzlyprb	https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/66d1e7f1-16a9-4ec1-996d-99ef0dcafa3d	2020-04-10 22:44:44.304-03	2020-04-11 00:15:43.154-03	Personality Insights
\.


--
-- TOC entry 3045 (class 0 OID 16638)
-- Dependencies: 227
-- Data for Name: watson_access_fk_assistants; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.watson_access_fk_assistants (id, watsonaccess_id, assistants_id) FROM stdin;
1	4	1
2	4	2
3	4	3
4	3	1
5	3	2
6	3	3
7	2	1
8	2	2
9	2	3
10	1	1
11	1	2
12	1	3
\.


--
-- TOC entry 3041 (class 0 OID 16616)
-- Dependencies: 223
-- Data for Name: watson_logs; Type: TABLE DATA; Schema: public; Owner: sysdba
--

COPY public.watson_logs (pk_watson_logs, sender_name, sender_message, response_message, flag_invalid_response, flag_resolve, insert_date, update_date, fk_user_id, fk_watson_components_id) FROM stdin;
\.


--
-- TOC entry 3051 (class 0 OID 0)
-- Dependencies: 202
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- TOC entry 3052 (class 0 OID 0)
-- Dependencies: 204
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3053 (class 0 OID 0)
-- Dependencies: 200
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- TOC entry 3054 (class 0 OID 0)
-- Dependencies: 208
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3055 (class 0 OID 0)
-- Dependencies: 206
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- TOC entry 3056 (class 0 OID 0)
-- Dependencies: 210
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3057 (class 0 OID 0)
-- Dependencies: 212
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 3, true);


--
-- TOC entry 3058 (class 0 OID 0)
-- Dependencies: 198
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- TOC entry 3059 (class 0 OID 0)
-- Dependencies: 196
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 21, true);


--
-- TOC entry 3060 (class 0 OID 0)
-- Dependencies: 219
-- Name: icity-pub-assistants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public."icity-pub-assistants_id_seq"', 2, true);


--
-- TOC entry 3061 (class 0 OID 0)
-- Dependencies: 215
-- Name: icity_assistants_pk_assistants_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.icity_assistants_pk_assistants_seq', 1, false);


--
-- TOC entry 3062 (class 0 OID 0)
-- Dependencies: 217
-- Name: icity_publicity_pk_publicity_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.icity_publicity_pk_publicity_seq', 1, false);


--
-- TOC entry 3063 (class 0 OID 0)
-- Dependencies: 226
-- Name: watson_access_fk_assistants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.watson_access_fk_assistants_id_seq', 1, false);


--
-- TOC entry 3064 (class 0 OID 0)
-- Dependencies: 224
-- Name: watson_access_pk_watson_access_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.watson_access_pk_watson_access_seq', 1, false);


--
-- TOC entry 3065 (class 0 OID 0)
-- Dependencies: 222
-- Name: watson_logs_pk_watson_logs_seq; Type: SEQUENCE SET; Schema: public; Owner: sysdba
--

SELECT pg_catalog.setval('public.watson_logs_pk_watson_logs_seq', 1, false);


-- Completed on 2020-05-04 00:13:45

--
-- PostgreSQL database dump complete
--


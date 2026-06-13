# Projets Incontournables pour Construire Votre Portfolio de Data Engineer

---

## Introduction

Créer des projets est une excellente manière pour les débutant·es en ingénierie des données d'acquérir une expérience pratique, développer leurs compétences, et construire un portfolio qui met en valeur leurs aptitudes auprès des employeurs.

---

## Qu'est-ce qu'un·e Data Engineer ?

Un·e Data Engineer est un·e professionnel·le spécialisé·e dans la gestion, la transformation et l'orchestration des données au sein d'une organisation. Son rôle principal est de construire des pipelines de données robustes et évolutifs, permettant de collecter, transformer, et stocker les données de manière efficace pour répondre aux besoins analytiques et opérationnels.

### Compétences clés pour devenir Data Engineer

| Domaine | Technologies |
|---------|-------------|
| **Langages de programmation** | Python, Java, Scala |
| **Bases de données** | SQL, NoSQL (MongoDB, Cassandra) |
| **Big Data** | Apache Spark, Hadoop |
| **Cloud computing** | AWS, GCP, Azure |
| **ETL** | Création et gestion de pipelines de données |
| **Orchestration de workflows** | Apache Airflow, Luigi |
| **Visualisation de données** | Tableau, Power BI |
| **Ingénierie temps réel** | Kafka, Apache Flink |

---

## Partie 0 : L'aventure en programmation

Avant de plonger dans des projets complexes, il est essentiel de maîtriser les bases de la programmation et de la manipulation des bases de données. Voici deux projets pour vous familiariser avec ces concepts fondamentaux.

---

### Projet 1 : Premiers pas avec Python

Apprenez les bases de la programmation avec Python en créant une application simple pour gérer une bibliothèque personnelle.

#### Étapes

1. Créez un programme qui permet d'ajouter, de modifier et de supprimer des livres d'une bibliothèque personnelle.
2. Implémentez des fonctions pour :
   - Afficher tous les livres disponibles.
   - Rechercher un livre par titre ou auteur.
   - Trier les livres par date d'ajout ou par catégorie.
3. Structurez votre projet avec des classes pour représenter les livres et la bibliothèque.
4. Sauvegardez les données localement dans un fichier JSON pour la persistance des données.

#### Objectifs

- Comprendre les bases de la programmation orientée objet.
- Structurer un projet avec des modules et des classes.
- Utiliser des bibliothèques comme `json` pour la gestion de fichiers.

#### Technologies utilisées

- Python (modules intégrés, JSON)

#### Liens utiles

- [Python Beginner Projects](https://github.com/topics/python-beginner-projects)
- [Simple Python Projects](https://github.com/topics/simple-python-projects)

---

### Projet 2 : L'aventure SQL

Apprenez à interagir avec des bases de données relationnelles en créant et en interrogeant une base SQL.

#### Étapes

1. Définissez une structure de base de données pour un système de gestion d'une bibliothèque (livres, auteur·es, emprunteur·euses).
2. Insérez des données fictives pour représenter des emprunts, des retours, et des informations de lecteur·rice·s.
3. Écrivez des requêtes pour répondre à des questions comme :
   - "Quels sont les livres empruntés cette semaine ?"
   - "Quel·le auteur·e a publié le plus de livres ?"
   - "Quels emprunteur·euses ont emprunté le plus de livres sur une période donnée ?"
4. Ajoutez des vues SQL pour simplifier les requêtes fréquentes.

#### Objectifs

- Comprendre les concepts de bases de données relationnelles.
- Maîtriser l'écriture de requêtes SQL avancées (jointures, agrégations).
- Optimiser les requêtes avec des index.

#### Technologies utilisées

- SQLite ou MySQL

#### Liens utiles

- [SQL Practice](https://www.sql-practice.com/)
- [Kaggle SQL Datasets](https://www.kaggle.com/datasets)
- [LeetCode - SQL](https://leetcode.com/problemset/database/)

---

## Partie 1 : Système de collecte et de stockage des données

La collecte et le stockage des données sont au cœur des responsabilités d'un·e data engineer. Grâce à des projets concrets comme ceux présentés ici, vous pourrez apprendre à extraire des données depuis diverses sources, les transformer et les organiser dans des bases adaptées pour une exploitation optimale.

---

### Projet 3 : Système de collecte de données API et stockage SQL

#### Contexte métier

Une entreprise dans le secteur du tourisme souhaite automatiser la collecte de données météo pour ses différentes destinations afin d'optimiser ses recommandations aux clients. Ces données doivent être structurées et accessibles aux équipes pour intégrer des prévisions dans leurs applications mobiles.

#### Contexte technique

Collecter des données via une API publique, comme OpenWeather API pour les données météo. Les données collectées sont nettoyées, normalisées, et stockées dans une base SQL.

#### Étapes clés

1. Se connecter à l'API avec une clé d'accès.
2. Récupérer les données au format JSON.
3. Nettoyer et transformer les données (normalisation, gestion des valeurs manquantes).
4. Créer une base de données relationnelle et concevoir les tables nécessaires.
5. Insérer les données dans la base SQL.

#### Technologies possibles

- **Langages** : Python
- **Bibliothèques pour API** : `requests`
- **Bases de données relationnelles** : PostgreSQL, MySQL, SQL Server, SQLite
- **Autres outils** : Docker pour la conteneurisation, Airflow pour l'automatisation

#### Lien vers la base de données

- [OpenWeather API](https://openweathermap.org/api)

---

### Projet 4 : Scraping et stockage de données web

#### Contexte métier

Une plateforme d'e-commerce souhaite analyser les avis de ses concurrents pour mieux comprendre les retours clients sur des produits similaires. Les données doivent être extraites de sites comme Trustpilot, nettoyées et organisées pour des analyses comparatives.

#### Contexte technique

Récupérer des données à partir d'un site web, comme des avis de consommateurs sur Trustpilot. Les données sont ensuite nettoyées, transformées et stockées dans une base SQLite.

#### Étapes clés

1. Identifier et extraire les éléments d'intérêt sur une page web.
2. Gérer les structures HTML avec des sélecteurs CSS.
3. Nettoyer les données (suppression des balises HTML, gestion des doublons).
4. Créer une base SQLite et concevoir une structure adaptée.
5. Insérer les données collectées.

#### Technologies possibles

- **Langages** : Python
- **Bibliothèques pour le scraping** : BeautifulSoup, Scrapy, Selenium
- **Bases de données** : SQLite, MongoDB, DynamoDB
- **Automatisation** : Apache Airflow

#### Lien vers la base de données

- [Trustpilot Reviews Dataset](https://www.kaggle.com/datasets)

---

## Partie 2 : Pipeline ETL (Extract, Transform, Load)

Les pipelines ETL permettent de collecter, transformer et charger des données de manière automatisée et scalable. Ils sont indispensables pour alimenter les entrepôts de données, effectuer des analyses en profondeur et garantir une prise de décision éclairée.

---

### Projet 5 : Pipeline ETL pour analyse des ventes

#### Contexte métier

Une entreprise de e-commerce souhaite analyser ses données de vente pour identifier les produits les plus performants, les périodes de forte activité et les tendances émergentes. Pour cela, elle doit centraliser ses données provenant de plusieurs plateformes (site web, points de vente physiques, réseaux sociaux) dans un entrepôt de données.

#### Contexte technique

Ce projet consiste à extraire des données brutes de plusieurs sources, à appliquer des transformations (nettoyage, enrichissement, agrégation) pour les rendre exploitables, et à les charger dans un entrepôt de données pour des analyses ultérieures.

#### Étapes clés

1. Extraire des données de vente provenant de plusieurs sources (API de plateforme e-commerce, fichiers CSV, bases relationnelles).
2. Nettoyer et transformer les données pour corriger les incohérences (formatage, gestion des doublons, enrichissement).
3. Charger les données transformées dans un entrepôt de données (par exemple, AWS Redshift).
4. Configurer un outil d'orchestration pour automatiser et planifier les tâches ETL.
5. Mettre en place des mécanismes de monitoring pour surveiller les erreurs et optimiser les performances.

#### Technologies possibles

- **Extraction** : Python (`pandas`, `requests`, `SQLAlchemy`), API REST, fichiers CSV
- **Transformation** : Pandas, PySpark, dbt (Data Build Tool)
- **Chargement** : AWS Redshift, Snowflake, BigQuery
- **Orchestration** : Apache Airflow, Prefect, Luigi
- **Monitoring** : Grafana, Prometheus, ELK Stack

#### Lien vers la base de données

- [Sales Dataset](https://www.kaggle.com/datasets)

---

### Projet 6 : Pipeline ETL sur données financières

#### Contexte métier

Une institution financière souhaite consolider ses données issues de plusieurs sources (Yahoo Finance, Bloomberg, fichiers Excel internes) pour analyser des indicateurs clés de performance (KPI) tels que les revenus, la rentabilité, ou les risques liés aux fluctuations du marché.

#### Contexte technique

Le projet implique l'intégration de données financières hétérogènes, la réalisation de calculs avancés (comme les moyennes mobiles ou les taux de variation), et la génération de rapports analytiques prêts à l'emploi.

#### Étapes clés

1. Extraire les données financières à partir de plusieurs sources (API comme Yahoo Finance, fichiers Excel, bases SQL).
2. Effectuer des transformations avancées, comme des calculs statistiques (écarts types, indicateurs techniques), et enrichir les données avec des métadonnées (secteurs d'activité, régions).
3. Charger les données transformées dans une base relationnelle ou un entrepôt pour un accès rapide et fiable.
4. Automatiser le pipeline pour des mises à jour périodiques (quotidiennes ou hebdomadaires).
5. Générer des rapports dynamiques ou des tableaux de bord pour faciliter l'analyse.

#### Technologies possibles

- **Extraction** : Yahoo Finance API, Alpha Vantage, fichiers CSV, bases SQL
- **Transformation** : PySpark, Apache Nifi, dbt
- **Chargement** : PostgreSQL, Snowflake, BigQuery
- **Orchestration** : Apache Nifi, Airbyte, Apache Airflow
- **Visualisation** : Tableau, Power BI, Metabase

#### Lien vers la base de données

- [Yahoo Finance API](https://finance.yahoo.com/)

---

### Projet 7 : Analyse des performances en cricket (Pipeline ETL)

#### Contexte métier

Une organisation sportive souhaite analyser les performances des joueurs de cricket à partir des données de match pour identifier des tendances, évaluer les performances individuelles et d'équipe, et optimiser les stratégies pour les compétitions futures.

#### Contexte technique

Ce projet consiste à collecter des données de match issues de diverses sources (fichiers CSV, API, bases de données sportives), à transformer ces données pour calculer des statistiques clés, et à les charger dans un entrepôt pour des analyses détaillées et des visualisations.

#### Étapes clés

1. Extraire les données des matchs (scores, performances des joueurs, etc.) depuis des API sportives ou des fichiers de données historiques.
2. Transformer les données pour calculer des indicateurs comme les moyennes de score, les taux de victoire, ou les comparaisons entre joueurs.
3. Charger les données traitées dans un entrepôt analytique (par exemple, Snowflake ou BigQuery).
4. Concevoir des tableaux de bord interactifs pour visualiser les performances des joueurs et des équipes.
5. Automatiser le pipeline ETL pour mettre à jour les données après chaque match.

#### Technologies possibles

- **Extraction** : Python (`pandas`, `requests`), R
- **Transformation** : dbt, PySpark
- **Chargement** : Snowflake, BigQuery, Redshift
- **Visualisation** : Tableau, Power BI, Looker
- **Orchestration** : Apache Airflow, Prefect

#### Lien vers la base de données

- [ESPNcricinfo Ball-by-Ball Dataset](https://www.kaggle.com/datasets)

---

### Projet 8 : Dashboard d'analyse des données Uber

#### Contexte métier

Uber souhaite analyser les données de trajets pour identifier les tendances en termes de temps de trajet, de localisation, et de comportements des utilisateur·ices. Ces informations permettent d'optimiser les stratégies tarifaires, de prévoir les pics d'activité, et d'améliorer l'expérience client.

#### Contexte technique

Ce projet vise à construire un pipeline ETL complet qui extrait, transforme et charge les données des trajets Uber dans une base analytique. Les données nettoyées et agrégées sont ensuite utilisées pour créer des visualisations interactives.

#### Étapes clés

1. **Extraction des données** : Collecter les données des trajets à partir du dataset "TLC Trip Record Dataset". Charger les fichiers CSV bruts dans Google Cloud Storage ou un système équivalent.
2. **Transformation des données** : Utiliser PySpark pour nettoyer les données (gestion des valeurs manquantes, doublons, et incohérences), enrichir les données avec des calculs supplémentaires (par exemple, durée moyenne des trajets par heure) et les agréger selon différents axes (localisation, temps, comportement des utilisateur·ices).
3. **Chargement dans un entrepôt** : Charger les données nettoyées dans BigQuery pour permettre des analyses rapides et scalables.
4. **Visualisation interactive** : Créer un tableau de bord avec Looker pour explorer les données. Inclure des graphiques sur les temps de trajet moyens, les zones les plus fréquentées, les pics horaires, et les habitudes de réservation.
5. **Orchestration** : Automatiser l'ensemble du pipeline ETL à l'aide de Mage, un outil moderne pour la création et la gestion de workflows.

#### Analyses disponibles dans le tableau de bord

- Temps moyen de trajet par heure et par jour de la semaine
- Zones les plus fréquentées (pick-up/drop-off)
- Analyse des pics horaires et des comportements saisonniers
- Identification des trajets les plus courts et les plus longs

#### Technologies possibles

- **Extraction et stockage** : Google Cloud Storage, AWS S3
- **Transformation des données** : PySpark, dbt, Pandas
- **Entrepôt de données** : Google BigQuery, Snowflake, Amazon Redshift
- **Visualisation** : Looker, Tableau, Power BI
- **Orchestration** : Mage, Apache Airflow, Prefect

#### Lien vers la base de données

- [TLC Trip Record Dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

### Projet 9 : Analyse des recommandations produit Amazon

#### Contexte métier

Amazon souhaite analyser les avis des clients pour comprendre les sentiments exprimés, identifier les produits les plus populaires et affiner ses systèmes de recommandation. Ces insights permettent d'améliorer l'expérience utilisateur·ice, d'optimiser les ventes croisées, et de renforcer la fidélité des client·es.

#### Contexte technique

Ce projet consiste à concevoir un pipeline ETL qui traite les avis clients disponibles dans le dataset public d'Amazon. Les données sont analysées pour extraire des informations utiles comme les sentiments, les tendances des avis, et les performances des produits.

#### Étapes clés

1. **Extraction des données** : Collecter les données brutes des avis clients disponibles dans le dataset Amazon Customer Reviews. Les fichiers sont stockés dans AWS S3 pour une gestion centralisée.
2. **Transformation des données** : Utiliser Apache Spark pour effectuer les transformations suivantes :
   - Nettoyage des données (suppression des doublons, gestion des valeurs manquantes).
   - Analyse des sentiments des avis clients avec des outils NLP.
   - Agrégation des données pour identifier les produits les plus populaires, les catégories avec le plus d'avis positifs/négatifs, et les tendances générales.
3. **Chargement dans un entrepôt** : Charger les données transformées dans AWS Redshift pour permettre des analyses rapides et scalables.
4. **Visualisation et reporting** : Intégrer les résultats dans un tableau de bord interactif, permettant aux équipes marketing ou produit d'explorer les performances des produits, les retours clients, et les catégories populaires.
5. **Orchestration** : Automatiser l'exécution du pipeline ETL avec des outils comme AWS Glue ou Apache Airflow.

#### Analyses disponibles dans le tableau de bord

- Produits les plus recommandés en fonction des avis clients
- Sentiments globaux des clients par catégorie de produit
- Tendances dans les avis positifs et négatifs sur une période donnée
- Analyse des mots-clés les plus fréquents dans les avis

#### Technologies possibles

- **Stockage des données** : AWS S3, Google Cloud Storage
- **Transformation des données** : Apache Spark, PySpark, dbt
- **Entrepôt de données** : AWS Redshift, Snowflake, Google BigQuery
- **NLP pour analyse des sentiments** : spaCy, Hugging Face, TextBlob
- **Visualisation** : Tableau, Power BI, AWS QuickSight
- **Orchestration** : AWS Glue, Apache Airflow, Prefect

#### Lien vers la base de données

- [Amazon Customer Reviews Dataset](https://registry.opendata.aws/amazon-reviews/)

---

## Partie 3 : Traitement de données en temps réel

Le traitement des données en temps réel est essentiel dans les contextes où des décisions rapides doivent être prises à partir de flux de données en continu. Ces projets vous permettront de comprendre comment concevoir des architectures scalables et réactives pour analyser des données en temps réel.

---

### Projet 10 : Analyse des tweets en temps réel

#### Contexte métier

Une entreprise de marketing digital souhaite surveiller les tendances et les sentiments exprimés sur Twitter concernant ses produits ou sa marque en temps réel. Ces informations sont utilisées pour adapter les campagnes publicitaires et répondre rapidement aux retours des clients.

#### Contexte technique

Ce projet consiste à collecter des tweets via l'API de Twitter, à analyser les sentiments exprimés à l'aide d'un modèle de NLP, et à stocker les résultats dans une base de données pour des visualisations en direct.

#### Étapes clés

1. Configurer une connexion à l'API Twitter pour collecter des tweets en temps réel en fonction de mots-clés ou hashtags.
2. Traiter les flux de données avec Apache Kafka pour assurer une ingestion fluide et fiable.
3. Analyser les sentiments des tweets en temps réel avec Spark Streaming et un modèle de traitement du langage naturel.
4. Stocker les résultats de l'analyse dans une base NoSQL comme MongoDB pour permettre des requêtes rapides.
5. Créer un tableau de bord en direct pour visualiser les tendances et les sentiments.

#### Technologies possibles

- **Streaming** : Apache Kafka, Spark Streaming, AWS Kinesis
- **NLP** : spaCy, Hugging Face Transformers, TextBlob
- **Bases de données** : MongoDB, Cassandra, Elasticsearch
- **Visualisation** : Grafana, Kibana, Tableau

#### Lien vers la base de données

- [Twitter API Documentation](https://developer.twitter.com/en/docs)

---

### Projet 11 : Pipeline de données Reddit

#### Contexte métier

Une entreprise spécialisée dans les études de marché souhaite surveiller les discussions sur Reddit pour détecter les tendances émergentes et analyser l'opinion publique sur des produits ou sujets spécifiques.

#### Contexte technique

Ce projet consiste à concevoir un pipeline de données capable de collecter des messages Reddit en temps réel, de les transformer (par exemple, analyse de sentiment ou extraction de mots-clés), et de fournir des rapports en quasi temps réel.

#### Étapes clés

1. Collecter les données en streaming à partir de Reddit via l'API Reddit ou d'outils comme Pushshift.
2. Traiter les données en utilisant des technologies de streaming pour analyser les sentiments, détecter les sujets les plus discutés, ou suivre des mots-clés spécifiques.
3. Charger les résultats dans une base de données ou un tableau de bord pour une consultation en direct.
4. Mettre en place des mécanismes d'alerte pour signaler des changements soudains ou des discussions à fort engagement.
5. Automatiser et superviser le pipeline pour garantir sa stabilité.

#### Technologies possibles

- **Streaming** : Apache Kafka, Spark Streaming, AWS Kinesis
- **Analyse** : spaCy, Hugging Face Transformers, NLTK pour l'analyse de texte
- **Stockage** : Elasticsearch, MongoDB, PostgreSQL
- **Visualisation** : Kibana, Grafana, Tableau

#### Lien vers la base de données

- [Reddit API Documentation](https://www.reddit.com/dev/api/)

---

### Projet 12 : Surveillance IoT en temps réel

#### Contexte métier

Une entreprise spécialisée dans les solutions IoT souhaite surveiller en temps réel les données provenant de capteurs installés dans des usines pour détecter des anomalies, prévenir des pannes, ou optimiser la maintenance.

#### Contexte technique

Ce projet vise à collecter des flux de données provenant de capteurs IoT, à analyser ces données pour détecter des anomalies, et à fournir des alertes ou rapports en temps réel.

#### Étapes clés

1. Configurer les capteurs IoT pour envoyer des données en streaming vers un système centralisé via AWS IoT Core ou MQTT.
2. Utiliser Apache Flink pour traiter les flux de données en temps réel et détecter des anomalies (par exemple, des valeurs hors des plages acceptables).
3. Mettre en place un système d'alerte qui notifie les opérateurs en cas de problème identifié.
4. Stocker les données traitées dans une base relationnelle ou NoSQL pour une analyse historique.
5. Intégrer un tableau de bord pour visualiser les données des capteurs et surveiller les alertes en direct.

#### Technologies possibles

- **Streaming** : Apache Flink, Apache Kafka Streams, AWS IoT Core, MQTT
- **Analyse** : PySpark, SQL sur Flink, Machine Learning pour la détection d'anomalies (scikit-learn, TensorFlow)
- **Bases de données** : InfluxDB, TimescaleDB, DynamoDB
- **Visualisation** : Grafana, Kibana, Power BI

#### Lien vers la base de données

- [Simulated IoT Sensor Data](https://www.kaggle.com/datasets)

---

### Projet 13 : Création d'un tableau de bord des prix des cryptomonnaies

#### Contexte métier

Une entreprise de fintech ou un·e investisseur·e souhaite surveiller en temps réel les prix des cryptomonnaies pour détecter des anomalies, identifier des opportunités d'investissement, ou anticiper des mouvements brusques du marché.

#### Contexte technique

Ce projet vise à concevoir un pipeline Big Data capable de collecter les prix des cryptomonnaies en temps réel à partir de l'API CoinMarketCap. Les données sont transformées pour détecter des anomalies et chargées dans un tableau de bord dynamique pour une visualisation en direct.

#### Étapes clés

1. **Extraction des données** : Utiliser l'API CoinMarketCap pour collecter les prix des cryptomonnaies en temps réel. Configurer un flux continu pour récupérer les mises à jour fréquentes (par exemple, chaque minute).
2. **Ingestion en streaming** : Intégrer les données collectées dans Apache Kafka pour gérer les flux en temps réel.
3. **Traitement des données** : Utiliser Apache Spark Streaming pour transformer les données, calculer des indicateurs clés (moyennes mobiles, variations en pourcentage), et détecter des anomalies.
4. **Stockage des données** : Charger les données transformées dans une base analytique comme Snowflake pour permettre des requêtes rapides et des analyses historiques.
5. **Visualisation** : Créer un tableau de bord interactif pour visualiser les prix en temps réel, les tendances, et les alertes en cas d'anomalies.

#### Exemples d'analyses disponibles

- Suivi des variations de prix minute par minute
- Identification des cryptomonnaies les plus volatiles sur une période donnée
- Détection d'anomalies sur des variations de prix inhabituelles
- Alertes sur les mouvements brusques de prix

#### Technologies possibles

- **Extraction des données** : API CoinMarketCap, Python (`requests`, `websockets`)
- **Streaming** : Apache Kafka, AWS Kinesis, RabbitMQ
- **Traitement des données** : Apache Spark Streaming, Flink, PySpark
- **Stockage** : Snowflake, Google BigQuery, Amazon Redshift
- **Visualisation** : Tableau, Grafana, Kibana, Power BI
- **Surveillance et alertes** : Prometheus, Grafana

#### Lien vers la base de données

- [CoinMarketCap API](https://coinmarketcap.com/api/)

---

## Partie 4 : Solutions d'entrepôts de données

Les entrepôts de données jouent un rôle central dans les environnements data modernes. Ils permettent de centraliser des données provenant de différentes sources, de les structurer et de les analyser efficacement.

---

### Projet 14 : Conception d'un entrepôt de données pour l'e-commerce

#### Contexte métier

Une entreprise de e-commerce souhaite centraliser ses données de commandes, client·es et produits provenant de différents systèmes (CRM, ERP, site web) afin de produire des rapports consolidés.

#### Contexte technique

Ce projet consiste à construire un entrepôt de données sur Snowflake pour centraliser et structurer des données issues de multiples sources. Une fois les données intégrées, des visualisations analytiques sont produites à l'aide d'un outil de BI tel que Tableau.

#### Étapes clés

1. Collecter les données brutes depuis plusieurs sources (fichiers CSV, bases SQL, API de CRM/ERP).
2. Créer une zone de staging pour stocker les données dans leur format brut.
3. Transformer les données (nettoyage, enrichissement, agrégation) et les charger dans une zone d'entrepôt structurée (schéma en étoile ou en flocon).
4. Concevoir des tableaux de bord et des rapports dynamiques pour suivre les KPI tels que le revenu, les retours client·es, ou les performances produit.
5. Automatiser le pipeline d'intégration et les actualisations des visualisations.

#### Technologies possibles

- **Entrepôt de données** : Snowflake, Amazon Redshift, Google BigQuery
- **Transformation des données** : dbt, Talend, Apache Nifi
- **Outils BI** : Tableau, Power BI, Metabase
- **Automatisation** : Apache Airflow, Prefect, Fivetran

#### Lien vers la base de données

- [E-Commerce Dataset](https://www.kaggle.com/datasets)

---

### Projet 15 : Entrepôt pour données climatiques

#### Contexte métier

Une organisation environnementale souhaite analyser les données climatiques collectées à travers le monde afin d'identifier des tendances à long terme, comme les variations de température, les précipitations ou les catastrophes naturelles.

#### Contexte technique

Le projet consiste à modéliser un entrepôt de données pour centraliser des données climatiques issues de plusieurs sources, telles que des stations météorologiques, des satellites, ou des rapports gouvernementaux.

#### Étapes clés

1. Extraire des données climatiques depuis des sources variées (API NOAA, fichiers CSV, bases de données).
2. Stocker les données brutes dans une zone de stockage intermédiaire (data lake ou zone de staging).
3. Transformer et structurer les données dans un entrepôt (modèle en étoile ou en flocon) pour permettre des analyses rapides.
4. Créer des tableaux de bord dynamiques pour visualiser les tendances climatiques et les anomalies.
5. Optimiser les coûts et les performances des requêtes dans l'entrepôt via des partitions et des index.

#### Technologies possibles

- **Entrepôt de données** : Google BigQuery, Snowflake, Azure Synapse Analytics
- **Transformation des données** : dbt, Apache Beam, Spark SQL
- **Outils BI** : Looker, Tableau, Power BI
- **Automatisation** : Dataflow, Cloud Composer, Fivetran

#### Lien vers la base de données

- [NOAA Climate Data](https://www.ncei.noaa.gov/)

---

## Partie 5 : Système de contrôle qualité des données

La qualité des données est un enjeu crucial dans tout projet data. Des données erronées ou incohérentes peuvent conduire à des analyses inexactes et des décisions erronées.

---

### Projet 16 : Contrôle qualité sur données d'inventaire

#### Contexte métier

Une entreprise de logistique souhaite garantir la fiabilité des données d'inventaire pour éviter des ruptures de stock, des commandes inexactes ou des pertes financières.

#### Contexte technique

Ce projet consiste à concevoir un système de contrôle qualité des données pour analyser les anomalies dans un jeu de données d'inventaire. Les contrôles sont automatisés pour fournir des rapports réguliers aux équipes opérationnelles.

#### Étapes clés

1. Charger les données d'inventaire à partir de fichiers CSV ou d'une base relationnelle.
2. Identifier les problèmes courants tels que les doublons, les valeurs manquantes ou des incohérences (par exemple, quantité négative en stock).
3. Créer des règles de validation spécifiques, comme les plages de valeurs autorisées pour chaque champ.
4. Automatiser les contrôles à l'aide d'Apache Airflow ou d'un outil équivalent pour une vérification régulière.
5. Générer des rapports d'anomalies exploitables par les équipes.

#### Technologies possibles

- **Langages** : Python (`pandas`, `great_expectations`), R
- **Orchestration** : Apache Airflow, Prefect
- **Bases de données** : PostgreSQL, MySQL, Snowflake
- **Visualisation** : Tableau, Power BI, Metabase

#### Lien vers la base de données

- [Inventory Data](https://www.kaggle.com/datasets)

---

### Projet 17 : Analyse qualité des données de santé

#### Contexte métier

Un hôpital ou un organisme de santé souhaite garantir l'intégrité et la précision des données patient·es pour éviter les erreurs médicales et améliorer les soins.

#### Contexte technique

Ce projet vise à développer un système de contrôle qualité des données pour valider l'intégrité des informations critiques liées aux patient·es.

#### Étapes clés

1. Charger les données de santé à partir d'un entrepôt ou d'une base relationnelle.
2. Définir des règles de validation qualité (par exemple, plage acceptable de valeurs médicales, absence de doublons dans les identifiants des patient·es).
3. Effectuer des vérifications qualité automatisées en utilisant des scripts Python ou des requêtes SQL.
4. Construire des tableaux de bord pour visualiser les anomalies et les tendances dans les problèmes de qualité des données.
5. Automatiser le pipeline de vérification pour une surveillance continue.

#### Technologies possibles

- **Langages** : Python (`pandas`, `great_expectations`), SQL
- **Bases de données** : PostgreSQL, BigQuery, Snowflake
- **Outils BI** : Metabase, Tableau, Power BI
- **Orchestration** : Apache Airflow, Prefect

#### Lien vers la base de données

- [Healthcare Dataset](https://data.world/datasets/healthcare)

---

## Partie 6 : Cloud Computing et orchestration de workflows

Le cloud computing offre des solutions flexibles et évolutives pour traiter de grandes quantités de données, exécuter des modèles prédictifs et créer des visualisations analytiques.

---

### Projet 18 : Analyse des tendances musicales Spotify

#### Contexte métier

Spotify souhaite analyser les habitudes d'écoute des utilisateur·rices pour améliorer ses recommandations musicales et adapter ses stratégies de marketing.

#### Contexte technique

Ce projet consiste à extraire et analyser les données des playlists Spotify issues du dataset "Spotify Million Playlist". Les résultats sont transformés en visualisations exploitables.

#### Étapes clés

1. **Extraction des données** : Charger le dataset depuis une source cloud (par exemple, Google Cloud Storage).
2. **Transformation des données** : Nettoyer et enrichir les données avec PySpark, effectuer des agrégations pour analyser les artistes les plus écoutés, les genres populaires, et les variations au fil du temps.
3. **Stockage des données** : Charger les données nettoyées et agrégées dans BigQuery pour un accès rapide et des requêtes analytiques.
4. **Visualisation** : Créer des tableaux de bord interactifs avec Looker pour suivre les tendances musicales par région, période, ou type de playlist.
5. **Orchestration des workflows** : Automatiser les étapes du pipeline de traitement avec des outils cloud (par exemple, Cloud Composer).

#### Technologies possibles

- **Cloud et stockage** : Google Cloud Storage, AWS S3
- **Transformation** : PySpark, Dataflow, dbt
- **Stockage et analyse** : BigQuery, Snowflake, Redshift
- **Visualisation** : Looker, Tableau, Power BI
- **Orchestration** : Google Cloud Composer, Apache Airflow

#### Lien vers la base de données

- [Spotify Million Playlist Dataset](https://research.atspotify.com/datasets/)

---

### Projet 19 : Prévisions météorologiques

#### Contexte métier

Les prévisions météorologiques sont essentielles pour de nombreux secteurs, comme l'agriculture, les transports ou la gestion des catastrophes naturelles.

#### Contexte technique

Ce projet exploite les capacités d'Azure ML Studio pour entraîner des modèles prédictifs sur des données climatiques historiques, puis visualiser les résultats via des tableaux de bord interactifs.

#### Étapes clés

1. **Extraction des données** : Collecter des données historiques sur les précipitations, températures, ou autres paramètres via le dataset NOAA Climate Data.
2. **Préparation des données** : Nettoyer les données dans Databricks, appliquer des transformations (par exemple, création de nouvelles variables) et effectuer des agrégations.
3. **Modélisation prédictive** : Utiliser Azure ML Studio pour entraîner un modèle de régression ou de machine learning supervisé pour prédire des paramètres climatiques.
4. **Stockage et visualisation** : Charger les résultats dans Power BI pour créer des tableaux de bord.
5. **Orchestration** : Planifier les workflows pour réentraîner le modèle et mettre à jour les visualisations de manière régulière.

#### Technologies possibles

- **Cloud et orchestration** : Azure ML Studio, Databricks, AWS SageMaker
- **Transformation des données** : PySpark, Pandas, SQL
- **Visualisation** : Power BI, Tableau, Metabase
- **Stockage** : Azure Data Lake, AWS S3, Snowflake

#### Lien vers la base de données

- [NOAA Climate Data](https://www.ncei.noaa.gov/)

---

## Ressources et projets pour Data Engineer

### 1. Awesome Open Source Data Engineering
Une collection d'outils, de frameworks et de projets open source orientés Data Engineering.

### 2. Kaggle
Plateforme populaire offrant des datasets et des idées de projets dans divers domaines.

- **Superstore Dataset** : Analyse des ventes
- **TMDb Movie Dataset** : Pipeline ETL pour les données de films

### 3. Seattle Data Guy - Data Engineering Projects
Une série d'idées de projets Data Engineering pour enrichir votre portfolio.

### 4. Analytics Vidhya - Top Data Engineering Project Ideas (Part 1)
Une première liste d'idées de projets Data Engineering avec des exemples concrets et du code source.

### 5. Analytics Vidhya - Top Data Engineering Project Ideas (Part 2)
Suite d'idées de projets innovants pour approfondir vos compétences.

### 6. AWS Open Data Registry
Datasets hébergés sur AWS pour des projets Big Data et cloud.

- **NOAA Climate Data** : Analyse climatique
- **Medicare Dataset** : Surveillance de données médicales

### 7. Google Cloud Public Datasets
Datasets publics hébergés sur Google Cloud.

- **World Bank Population Data** : Étude démographique
- **NYC Taxi Dataset** : Analyse des trajets de taxis

### 8. NYC Open Data
Datasets ouverts de la ville de New York.

- **TLC Trip Record Data** : Analyse des trajets en taxi
- **Housing Dataset NYC** : Étude des tendances de logement

### 9. StatsBomb Open Data
Données sportives pour l'analyse des matchs de football.

- Analyse des performances des joueurs
- Création de tableaux de bord interactifs

### 10. Spotify Million Playlist Dataset
Dataset pour explorer les tendances musicales et les recommandations.

- Analyse des genres musicaux populaires
- Construction d'un système de recommandation basé sur les playlists

### 11. CoinMarketCap API
Données en temps réel sur les cryptomonnaies.

- Détection des anomalies de prix
- Tableau de bord en temps réel pour surveiller les tendances

### 12. Amazon Open Data
Dataset pour l'analyse des avis clients.

- Analyse des sentiments des avis produits
- Rapports sur les produits les mieux notés

### 13. Healthcare Datasets
Datasets pour explorer les données médicales et les tendances en santé publique.

- Analyse des tendances de santé
- Surveillance des anomalies dans les données médicales

### 14. OpenStreetMap Data
Données géographiques pour des projets de cartographie.

- Analyse des transports publics
- Visualisation des zones urbaines et rurales

### 15. TLC Trip Record Dataset
Données pour analyser les trajets de taxis à New York.

- Étude des tendances horaires et géographiques
- Optimisation des trajets

### 16. DataPortals.org
Une collection mondiale de portails de données ouvertes.

### 17. Azure Open Datasets
Datasets publics pour des projets cloud avec Azure.

---

> **Pour ne pas manquer mes prochains posts, suivez-moi sur [YouTube](https://www.youtube.com/@LeCoinStat), [LinkedIn](https://www.linkedin.com/), [Instagram](https://www.instagram.com/) et [TikTok](https://www.tiktok.com/) !**

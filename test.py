import pandas as pd
from sentence_transformers import SentenceTransformer, util


class Article:
    def __init__(self, title, keywords, abstact, citation, tokens, tf, tfidf):
        self.title = title
        self.keywords = keywords
        self.abstact = abstact
        self.citation = citation
        self.tokens = tokens
        self.tf = tf
        self.tfidf = tfidf

    def __str__(self):
        return f"Title: {self.title}\nKeywords: {self.keywords}\nCitation: {self.citation}\nAbstract: {self.abstact}"



def similarity(articles, keywords_researcher):
    model = SentenceTransformer('stsb-roberta-large')

    test = []
    for article in articles:
        test.append([])
        # test[-1].append(article.title)

        for keyword in keywords_researcher:
            keyword = model.encode(keyword, convert_to_tensor=True)
            text = article.title + ' ' + article.keywords + ' ' + article.abstact
            text = model.encode(text, convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(keyword, text)
            test[-1].append(cosine_scores.item())
            # test[-1].append('0')

    titles = [article.title for article in articles]
    df = pd.DataFrame(test, columns=keywords_researcher, index=titles)
    print(df)
    df.to_excel('keywords_researcher.xlsx')

articles = [
    Article('An intelligent linguistic error detection approach to automated diagnosis of Dyslexia disorder in Persian speaking children','', "Dyslexia is a learning disability in which a child with a normal IQ has difficulties with reading. Each of these difficulties is linked to a certain type of weakness, such as visual memory impairment, auditory sensitivity impairment, attention, and so on. If left undiagnosed, the disorder grows with the child's development and, due to insufficient awareness of the parents, teachers and other people who interact with him / her, causes problems such as frustration and feelings of weakness in comparison to other children. Therefore, the need for early detection of this disorder at a young age is very significant. Educational scientists working in the field of diagnosis and treatment of learning disabilities use various standardized tests for screening. However, the use of intelligent systems for automatic diagnosis of dyslexia can be performed for initial screening, on a large scale and with less time costs and specialized manpower. In", 0, '', '', ''),
    Article('An interactive user groups recommender system based on reinforcement learning','', 'Nowadays, we have access to countless and diverse user data in various fields. Thus, it requires analysis to find a set of users. Several steps are taken to understand and identify users interactively to achieve such a goal. This article introduces a reinforcement learning model of interactive recommendations based on user groups. An agent learns the appropriate policy to discover users among groups based on feedback during a sequential decision-making process and recommends the best action for the next step. There are three datasets available for courses, jobs, and LinkedIn, but these three datasets are not related to each other, which causes errors in learning politics. Furthermore, taking different actions will significantly affect learning from these datasets. To improve learning, semantic similarity and text processing are used to extract relationships between datasets. As a result, a set of groups is constructed', 0, '', '', ''),
    Article('Big data fuzzy C-means algorithm based on bee colony optimization using an Apache Hbase','', 'Clustering algorithm analysis, including time and space complexity analysis, has always been discussed in the literature. The emergence of big data has also created a lot of challenges for this issue. Because of high complexity and execution time, traditional clustering techniques cannot be used for such an amount of data. This problem has been addressed in this research. To present the clustering algorithm using a bee colony algorithm and high-speed read/write performance, Map-Reduce architecture is used. Using this architecture allows the proposed method to cluster any volume of data, and there is no limit to the amount of data. The presented algorithm has good performance and high precision. The simulation results on 3 datasets show that the presented algorithm is more efficient than other big data clustering methods. Also, the results of our algorithm execution time on huge datasets are much', 0, '', '', ''),
    Article('Bipolar disorder detection over social media','', 'Bipolar disorder is a mental illness characterized by manic and depressive episodes. The inability to track the patient at different stages of the disease, the patient�s concealment of information, and the difficulty in obtaining and paying for a psychologist are all weaknesses in traditional diagnosis procedures. In this regard, computer researchers have developed automated prediction algorithms in response to issues involved in using traditional ways of diagnosing bipolar disorder. Although these automated approaches have eliminated many problems that plagued previous systems, there are still many challenges to tackle. Discovering a mechanism to track changes in user behavior and aggregating various features into a cohesive model are the most critical issues in this context. To address these concerns, this research proposes a novel approach for detecting bipolar disorder among Twitter users.', 0, '', '', ''),
    Article('Configurational entropy as a simple input data for glass science and engineering','', 'The current study seeks to propose new input data for glass science and engineering based on the simple calculations of the configurational entropy. Initially, the configurational entropy of the 15,000 silicate-based glasses with different amounts of alkali or alkaline earth oxide additives (10, 15, and 25 mol%), which were extracted from the SciGlass database, was calculated using S Conf=− R∑ i= 1 x x i ln x i formula. In the mentioned formula, S Conf is the configurational entropy, R is the gas constant, and x i is the molar fraction of i element. Then, the relation between entropy and glass properties was theoretically investigated in three conditions. The results indicated that the entropy of the studied glasses is in the range of 0.03 R to 2.15 R. The results showed positive or negative slopes in the entropy-T g curves for different glass compositions. The found reasons behind the various trends between the entropy and T...', 0, '', '', ''),
    Article('DxGenerator: An Improved Differential Diagnosis Generator for Primary Care Based on MetaMap and Semantic Reasoning','', "Background In recent years, researchers have used many computerized interventions to reduce medical errors, the third cause of death in developed countries. One of such interventions is using differential diagnosis generators in primary care, where physicians may encounter initial symptoms without any diagnostic presuppositions. These systems generate multiple diagnoses, ranked by their likelihood. As such, these reports' accuracy can be determined by the location of the correct diagnosis in the list. Objective This study aimed to design and evaluate a novel practical web-based differential diagnosis generator solution in primary care. Methods In this research, a new online clinical decision support system, called DxGenerator, was designed to improve diagnostic accuracy; to this end, an attempt was made to converge a semantic database with the unified medical language system (UMLS) knowledge...", 0, '', '', ''),
    Article('Early multi-class ensemble-based fake news detection using content features','', 'Nowadays, social media plays an essential role in spreading the news with low cost and high speed in publishing, and easy availability. Given that, anyone can publish any news on social networks, with some of them to be fake. These fake stories should be detected as soon as possible since they might have negative impacts on the society. To address this issue, most researches consider fake news detection as a binary classification problem. However, as some news are half-true, recently, multi-class detection has gained more attention. This paper investigates an early detection of fake news using multi-class classification. This is achieved by extracting the content features, such as sentiment and semantic features, from the news. The proposed model employs five classifiers (Random Forest, Support Vector Machine, Decision Tree, LightGBM, and XGBoost) as primary classifiers. Furthermore, AdaBoost is used for', 0, '', '', ''),
    Article('Elaboration of entropy with glass composition: A molecular dynamics study','', 'Recently, entropy was proposed as a simple input into glass science and engineering, which has an interesting relationship with the glass properties containing glass transition temperature (Tg), melting point, and concentration of non-bridging oxygens (NBOs). In the current study, molecular dynamics (MD) simulation as the powerful method was used to approve the recently observed relations. In this regard, various silicate-based compositions containing 25, 30, and 35 mol% of alkaline earth oxides were simulated. The Tg, bond length, and the concentration of NBOs were evaluated using MD simulation results, including volume-temperature curves and radial distribution functions (RDF) results. According to the results, Tg values of the simulated glass were reduced up to 400 K by increasing the amounts of additives up to 35 mol%. The distance between Si and O species as the glass former basis increased from 1', 0, '', '', ''),
    Article('Geo-Enabled Business Process Modeling','', 'Recent advancements in location-aware analytics have created novel opportunities in different domains. In the area of process mining, enriching process models with geolocation helps to gain a better understanding of how the process activities are executed in practice. In this paper, we introduce our idea of geo-enabled process modeling and report on our industrial experience. To this end, we present a real-world case study to describe the importance of considering the location in process mining. Then we discuss the shortcomings of currently available process mining tools and propose our novel approach for modeling geo-enabled processes focusing on 1) increasing process interpretability through geo-visualization, 2) incorporating location-related metadata into process analysis, and 3) using location-based measures for the assessment of process performance. Finally, we conclude the paper by future research directions.', 0, '', '', ''),
    Article('HAM-Net: Predictive business process monitoring with a hierarchical attention mechanism','', 'One of the essential tasks in Business Process Management (BPM) is Predictive Business Process Monitoring. This task aims to predict the behavior of an ongoing process based on the historical data stored in event logs. Since feed-forward neural networks do not consider the order of events for the prediction, they may not be helpful in predictive process monitoring. Recent research shows that using Recurrent Neural Networks such as LSTM and GRU may not be also helpful in predictive process monitoring. Because these networks use only the last hidden state as the context vector, and may lose some of past information, especially in long sequences. In addition, many existing approaches just use the activity name of each event as the representative of that event. In this context, they may ignore other events� attributes in generating the feature vector. Some works have utilized these attributes simply by', 0, '', '', ''),
    Article('Identification of Bibliographic Relationships in the National Library and Archives of Iran (NLAI) According to the Functional Requirements for Bibliographic Records (FRBR �','', 'The aim of this study is to find out the bibliographic relationships between the metadata records in the National Library and Archives of Iran (NLAI) according to FRBR model, in order to represent the Knowledge network of Iranian-Islamic publications. To achieve this objective, the content analysis method was used. The study population includes metadata records for books in NLAI for four bibliographic families including Quran, Nahj al-Balagha,Shahnameh, and Masnavi (a total of 28213 records), that were accessible through the NLAI OPAC. In this study, the data gathering methods were structured (systematic) observation and documentary method. A checklist is used for data gathering, and a matrix is used to display the analyzed data. The results of the study showed that all relationship types of the Functional Requirements for Bibliographic Records (FRBR) model, except the �arrangement (music)� relationship from the section �Expression-to-Expression Relationships: between expressions of the same work�, were found in metadata records. Since the �arrangement (music)� relationship is used only for musical objects, so it can be concluded that NLAI encompasses the entire range of the FRBR relationship types that provided for books. The results of this study can be useful to implement FRBR model in persian libraries, and also to design NLAI metadata ontology model and create and publish the NLAI dataset based on linked data method.', 0, '', '', ''),
    Article('InfOnto: An ontology for fashion influencer marketing based on Instagram','', 'The present applied research attempts to design an ontology of fashion influencer marketing domain based on fashion marketing resources in Iran that were available during the years 2014-2021. To extract concepts, relationships, and properties with inspiration from the knowledge engineering method proposed by Na and Neoh�s study, Delphi and Domain Analysis approach was used in 3815 influencers� selection reason documents. To construct the ontology, a combination of The NeOn Methodology and Ontology Development 101, and Prot�g� (5.5.0 edition), were used. Ultimately, InfOnto was created with 1 conceptual core, 3 main concepts, 81 concepts, 8 categories, 2373 axioms, 1196 logical axioms, 61 object properties, 72 data properties, and 9 annotative properties. Concepts were evaluated using the Delphi method through interviews and questionnaires with 12 experts. In addition to the full supervision', 0, '', '', ''),
    Article('Interpreting sarcasm on social media using attention-based neural networks','', 'Posting sarcastic comments is a common trend on social media in which the intended meaning of the expression by the user is opposite to the literal meaning. Most existing approaches have mainly focused on sarcasm detection and left sarcasm interpretation rather underexplored, whereas what can really improve the efficiency of social text analysis techniques are generating the correct interpretation of sarcastic posts. In this paper, we present a deep learning neural network architecture for sarcasm interpretation in which the effect of adapting the idea of different attention mechanisms with the proposed architecture is explored to generate a non-sarcastic post conveying the same meaning as the original sarcastic one. This is based on the idea that, in interpreting a sarcastic post, the incongruity between a positive word and a negative situation plays a key role and consequently making it necessary to pay more', 0, '', '', ''),
    Article('Ontirandoc: Integrated Collaborative System for Developing Persian Ontology','', 'While ontology development is beneficial, it is very costly and time consuming. In order to reduce this cost as well as to increase the accuracy and quality of ontology development, researchers have proposed different methodologies. The goal of these methodologies is to present a systematic manual or semi-automated development of ontologies, while each differs and has its strengths and weaknesses. In this paper, after reviewing current methodologies, we present a new integrated collaborative methodology for ontology development, and compare it with the existing ones. This new system, called Ontirandoc, has been used in two ontology development projects and its accuracy has been evaluated.', 0, '', '', ''),
    Article('Post-hoc Explanation for Twitter List Recommendation','', 'Twitter List recommender systems have the ability to generate accurate recommendations, but since they utilize heterogeneous user and List information on Twitter and usually apply complex hybrid prediction models, they cannot provide user-friendly intrinsic explanations. In this paper, we propose an explanation model to provide post-hoc explanations for recommended Twitter Lists based on the user�s own actions; and consequently benefits to improve recommendation acceptance by end users. The proposed model includes two main components:(1) candidate explanation generation in which the most semantically related actions of a user on Twitter to the recommended List are retrieved as candidate explanations; and (2) explanation ranking to re-rank candidates based on relatedness to the List and their informativeness. Through experiments on a real-world Twitter dataset, we demonstrate that the proposed explanation model can effectively generate related, informative and useful post-hoc explanations for the recommended Lists to users, while maintaining parity in recommendation performance.', 0, '', '', ''),
    Article('Schema and content aware classification for predicting the sources containing an answer over corpus and knowledge graphs','', 'Today, several attempts to manage question answering (QA) have been made in three separate areas:(1) knowledge-based (KB),(2) text-based and (3) hybrid, which takes advantage of both prior areas in extracting the response. On the other hand, in question answering on a large number of sources, source prediction to ensure scalability is very important. In this paper, a method for source prediction is presented in hybrid QA, involving several KB sources and a text source. In a few hybrid methods for source selection, including only one KB source in addition to the textual source, prioritization or heuristics have been used that have not been evaluated so far. Most methods available in source selection services are based on general metadata or triple instances. These methods are not suitable due to the unstructured source in hybrid QA. In this research, we need data details to predict the source. In addition, unlike KB federated methods that are based on triple instances, we use the behind idea of mediated schema to ensure data integration and scalability. Results from evaluations that consider word, triple, and question level information, show that the proposed approach performs well against a few benchmarks. In addition, the comparison of the proposed method with the existing approaches in hybrid and KB source prediction and also QA tasks has shown a significant reduction in response time and increased accuracy.', 0, '', '', ''),
    Article('The process of multi-class fake news dataset generation','', 'Nowadays, news plays a significant role in everyday life. Due to the increasing usage of social media and the dissemination of news by people who have access to social media, there is a problem that the validation of the news may be questioned, and people may publish fake news for their benefit. Automatic fake news detection is a complex issue. It is necessary to have up-to-date and reliable data to build an efficient model for detection. However, there are very few such datasets available for researchers. In this paper, we proposed a new fake news dataset extracted from three famous and reliable fact-checking websites. Because of the different labels used in each site, an algorithm was developed to integrated these 37 labels into five unified labels. Some experiments were conducted to show the usability and validity of the dataset.', 0, '', '', ''),
    Article('The Role of Corpus Linguistics in Sentiment Analysis of Persian Texts, Case Study: A Farsi News Agency Website','sentiment analysis, text mining, corpus linguistics, persian language, computational linguistics', 'The aim of the current article is improving a linguistic model in the sentiment analysis of a Persian News Agency Website. After investigating many computational problems and shortages in the field of computational linguistics, we could see that the main problem of computational linguists could be found in linguistics, not in computational sciences. Presenting a model can lead to the management of uncertainty of semantic and sentiment analysis of Persian documents. The Integration of systems that operate in the field can result in considerable developmental growth in smart systems of sentiment analysis of Persian language in a way that could reduce complexities in the Persian language. Moreover, the presence of a comprehensive model can facilitate the generation of smart systems of sentiment analysis in text mining. First, we collected existing models for text mining of sentiment analysis and tried to suggest a model as a general principle. The obtained model will help for information management and planning of text mining systems in computational linguistics and shows the shortages of Persian language natural processing in line with the automation of sentiment analysis.', 0, '', '', ''),
    Article('Use of Existing Ontology Elements in Ontology Construction: Presenting and Testing a Systematic Merge-based Method','', 'Integration of existing ontologies is an approach for reusing ontology elements in construction of a new ontology. Researchers have proposed various tools and methods for ontology merging, but very few of them work in an integrated manner with a comprehensive ontology construction methodology and also none of them support Persian language. In this paper we proposed a systematic merge-based method for reusing ontology elements with Persian support in ontology construction. Proposed method built based on the design science research method. The process and algorithms of proposed method implemented and improved based on general cycle of design science method. Proposed method used to create a reference ontology for educational and research organizations in the subset of Iranian ministry of science, research and technology. Final product was evaluated and verified by a gold standard.', 0, '', '', '')
]

similarity(articles ,['semantic technologies', 'computational linguistic', 'process mining', 'social media mining', 'computational psychology'])

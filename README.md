# Universal-KG-sampling
Samping from the DBPedia-EN and DBPedia-FR 

## Universal-KG-sampling Method and Datasets
As the DBpedia dataset has many similarities to real-world KGs, experiments can better simulate the problems present in real-world KGs if we are conducted using the relatively large DBpedia dataset. We therefore chose one SameAS based sampling algorithm to generate dataset based on the alignment of the embedded entities.

### SameAS based Sampling
The proposed algorithm is based on the relation:sameAS finding the set of EN-FR entity linkings from the original DBpedia-EN and DBpedia-FR, for each entity there is at least one set of relationship triples, the following diagram depicts the sampling process.
<p>
  <img width="50%" src="https://github.com/dice-group/Universal-KG-sampling/blob/main/sampling.png" />
</p>

### Dataset Overview
We choose one well-known KG as our sources: DBpedia (2016-10) Also, We consider a cross-lingual version of DBpedia. the first is English--French. We use the SameAs algorithm to sample the original English--French entity set.

### The specific process of sampling and the data obtained
* Get the original EN-FR data set from DBpedia, including entities and relation triples.
* Find the SameAS relation between EN_FR entities and FR_EN entities, ensure the entities are present in both KGs. EN_FR entities can be computed from http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_en.ttl.bz2 ,FR_EN entities can be computed from http://downloads.dbpedia.org/2016-10/core-i18n/fr/interlanguage_links_fr.ttl.bz2

*#* Raw Entities | Dataset names
:---: | :---: 
1,359,645| EN-FR
1,359,645| FR-EN

* Merge EN-FR and FR-EN,the number of the merged entities is 1,359,645 .
* Using the relationship triplet as a filter apply on merged EN-FR entities which we obtained from last step.we can find the reltion triples from http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_en.ttl.bz2(for EN) and  http://downloads.dbpedia.org/2016-10/core-i18n/fr/mappingbased_objects_fr.ttl.bz2(for FR) 

*#* Filtered Entities  | Dataset names
:---: | :---: 
526907| DBP(EN-FR)





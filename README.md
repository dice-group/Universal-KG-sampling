# Universal-KG-sampling
Samping from the DBPedia-EN and DBPedia-FR 

## Universal-KG-sampling Method and Datasets
As the DBpedia dataset has many similarities to real-world KGs, experiments can better simulate the problems present in real-world KGs if we are conducted using the relatively large DBpedia dataset. We therefore chose a base dataset sampling algorithm to generate dataset based on the alignment of the embedded entities.

### sameAS relation based Sampling
The proposed algorithm is based on the relation:sameAS finding the set of EN-FR entity linkings from the original DBpedia-EN and DBpedia-FR, for each entity there is at least one set of relationship triples, the following diagram depicts the sampling process.
<p>
  <img width="50%" src="https://github.com/dice-group/Universal-KG-sampling/blob/main/sampling.png" />
</p>


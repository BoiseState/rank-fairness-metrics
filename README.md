This repository contains code that can be used to run experiments of the paper Measuring Fairness in Ranked Results: An Analytical and Empirical, published at SIGIR’22.[(https://dl.acm.org/doi/10.1145/3477495.3532018)]

**Abstract**

Information access systems, such as search and recommender systems, often use ranked lists to present results believed to be relevant to the user's information need. Evaluating these lists for their fairness along with other traditional metrics provides a more complete understanding of an information access system's behavior beyond accuracy or utility constructs. To measure the (un)fairness of rankings, particularly with respect to the protected group(s) of producers or providers, several metrics have been proposed in the last several years. However, an empirical and comparative analyses of these metrics showing the applicability to specific scenario or real data, conceptual similarities, and differences is still lacking.
We aim to bridge the gap between theoretical and practical ap-plication of these metrics. In this paper we describe several fair ranking metrics from the existing literature in a common notation, enabling direct comparison of their approaches and assumptions, and empirically compare them on the same experimental setup and data sets in the context of three information access tasks. We also provide a sensitivity analysis to assess the impact of the design choices and parameter settings that go in to these metrics and point to additional work needed to improve fairness measurement.

**Metrics**

The paper implemented several fair ranking metrics from following papers:

FA\*IR: This metric is proposed by Zehlike et al. in  [FA\*IR: A Fair Top-k Ranking Algorithm](https://doi.org/10.1145/3132847.3132938).

AWRF (attention-weighted rank fairness): This metric is proposed by Sapiezynski et al. in [Quantifying the Impact of User Attention on Fair Group Representation in Ranked Lists](https://doi.org/10.1145/3308560.3317595).

IAA (inequity in amortized attention):  This metric is proposed by Biega et al. in [Equity of Attention: Amortizing Individual Fairness in Rankings](https://doi.org/10.1145/3209978.3210063).

DP (demographic parity), EUR (exposed utility ratio), RUR (realized utility ratio): This metric family is derived from [Fairness of Exposure in Rankings](https://doi.org/10.1145/3219819.3220088) written by Singh and Joachims. 

EE (expected-exposure): This metric family is proposed by Diaz e.at. in [Evaluating Stochastic Rankings with Expected Exposure](https://doi.org/10.1145/3340531.3411962)

**Dataset Description**

The project used two dataset: GoodReads book data and Fair Ranking Track 2021 data.

*GoodReads book data:* GoodReads book dataset can be obtained from https://bookdata.piret.info/. We used implicit feedback for generating recommendations. 

*FairTREC dataset:* Fair ranking track dataset can be obtained from https://fair-trec.github.io/2020/index.html. 

**Requirements:**
- python
- pandas
- numpy
- scikit-learn
- tqdm

**Directory Layout**

*bookgender* is a Python package that contains our support and configuration code. 

*bookgender/fair_ranking/metrics* contains the scripts of metrics implementations.

*bookgender/fair_metrics/Run_metrics_IR.py* or *bookgender/fair_metrics/Run_metrics_Rec.py* can be used to run the experiments depending on the dataset used.

*bookgender/fair_metrics/metric_utils* contains all the utility functions that are needed to implements the metrics

*eval5* will contain goodreads book recommendations.

*data* will contain the datasets.

*results* will contain metric scores for the ranked lists.

**Citation**

@inproceedings{raj2022measuring,

  title={Measuring fairness in ranked results: An analytical and empirical comparison},

  author={Raj, Amifa and Ekstrand, Michael D},

  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},

  pages={726--736},
  
  year={2022}
}









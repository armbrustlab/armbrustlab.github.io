---
title: SeaFlow project
---
![Seaflow]({% link /assets/images/SeaFlowAnalysis-logo.png %})

## Computational Flow Cytometry Analysis of Marine Phytoplankton

(funded by the [Simons Foundation](https://www.simonsfoundation.org/life-sciences/microbial-oceanography/))

![Seaflow]({% link /assets/images/SeaFlow-cruisetracks.png %})
SeaFlow is an shipboard underway flow cytometer that provides continuous optical measurements of light scatter and fluorescence associated with the pigments chlorophyll a and phycoerythrin at the single cell level ([Swalwell et al. 2011](https://doi.org/10.4319/lom.2011.9.466)). Over the last decade, we have operated SeaFlow for 14,000 hours across 140,000 km of ocean, collecting over 300,000 samples.  We have created Popcycle, an R package that use new reproducible analytical methods to uniformly process, calibrate and curate SeaFlow data. We have developed new reproducible analytical methods to uniformly process, calibrate and curate SeaFlow data. The data sets were expanded to include diameter and carbon quotas derived from light scatter measurements.

* An example dataset representing the compilation of over 69,000 SeaFlow-based estimates of cell abundance, cell diameter and carbon quotas for the cyanobacteria <i>Prochlorococcus</i>, <i>Synechococcus</i> and small-sized <i>Crocosphaera</i> (< 5 µm), and picophytoplankton and nanophytoplankton (2-5 µm) collected during 27 oceanographic cruises is available [here](http://doi.org/10.5281/zenodo.2678021) without restriction.

* Description of the data can be found in [Ribalet et al. 2019](https://doi.org/10.1038/s41597-019-0292-2).

* List of available data can be found [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vT76VR2_VAulc6caxklUqOTOj_7EEnNJiFlHqaD1fC7Pc_zqw5i7wwcQUcDa8dtALZXoVHt2t0mdPS5/pubhtml).

We are currently implementing a [size-structured matrix population model](https://github.com/fribalet/Bayesian-matrixmodel) for <i>Prochlorococcus</i> and <i>Synechococcus</i> to estimate cell growth and cell mortality rates, two key traits that govern how these organisms interact with their environment.



### Team
- [Francois Ribalet](https://armbrustlab.ocean.washington.edu/people/ribalet/) (Principal Investigator)
- [Annette Hynes](https://armbrustlab.ocean.washington.edu/people/hynes/) (Research Scientist)
- [Chris Berthiaume](https://armbrustlab.ocean.washington.edu/people/beethiaume/) (Software Engineer)
- [Mattias Cape](https://armbrustlab.ocean.washington.edu/people/cape/) (Postdoctoral Research Associate)
- [Kristof Glauninger](https://www.stat.washington.edu/person/kristof-glauninger)(Graduate Student)

### Software
* [popcycle](https://github.com/uwescience/popcycle) - an R package that analyzing continuous flow cytometry data from SeaFlow repository. The software is built to perform both coarse real-time data analysis and fine-tuned population clustering analysis.

* [seaflowpy](https://github.com/armbrustlab/seaflowpy) - Python libraries and scripts to complement ```popcycle```

* [Bayesian-matrixmodel](https://github.com/fribalet/Bayesian-matrixmodel) - A size-structured matrix population model to estimate hourly division rates of microbial populations from size distribution provided by SeaFlow data. These estimates are independent of variations in cell abundance and can be used to study physiologically-driven changes in population dynamics.

---
title: SeaFlow project
---
![Seaflow]({% link /assets/images/seaflow.jpeg %})

## Computational Flow Cytometry Analysis of Marine Phytoplankton

(funded by the [Simons Foundation](https://www.simonsfoundation.org/life-sciences/microbial-oceanography/))

<img src="https://github.com/armbrustlab/seaflow-sfl/blob/master/cruise-track.png" alt="SeaFlow cruisetracks"	title="SeaFlow cruisetracks" align="left" style="float" width="400">

SeaFlow is an shipboard underway flow cytometer that provides continuous optical measurements of light scatter and fluorescence associated with the pigments chlorophyll a and phycoerythrin at the single cell level ([Swalwell et al. 2011](https://doi.org/10.4319/lom.2011.9.466)). Over the last decade, the instrument has measured the optical properties of over 300 billions small individual phytoplankton cells (< 5 µm in diameter) across the North Pacific Ocean at a spatial resolution of ~ 1 km along the cruise track. We have developed new reproducible analytical methods to uniformely process, calibrate and curate SeaFlow data. The data sets were expanded to include diameter and carbon quotas derived from light scatter measurements. An example dataset representing the compilation of over 69,000 SeaFlow-based estimates of cell abundance, cell diameter and carbon quotas for the cyanobacteria <i>Prochlorococcus</i>, <i>Synechococcus</i> and small-sized <i>Crocosphaera</i> (< 5 µm), and picophytoplankton and nanophytoplankton (2-5 µm) collected during 27 oceanographic cruises is available [here](http://doi.org/10.5281/zenodo.2678021) without restriction. Description of the data can be found in [Ribalet et al. 2019](http://doi.org/10.5281/zenodo.2678021). List of available data can be found [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vT76VR2_VAulc6caxklUqOTOj_7EEnNJiFlHqaD1fC7Pc_zqw5i7wwcQUcDa8dtALZXoVHt2t0mdPS5/pubhtml). 

We are currently implementing a [size-structured matrix population model](https://github.com/armbrustlab/ssPopModel) for <i>Prochlorococcus</i> and <i>Synechococcus</i> to estimate cell growth and cell mortality rates, two key traits that govern how these organisms interact with their environment.



### Team
- [Francois Ribalet](https://armbrustlab.ocean.washington.edu/people/ribalet/) (Principal Investigator)
- [Annette Hynes](https://armbrustlab.ocean.washington.edu/people/hynes/) (Research Scientist)
- [Chris Berthiaume](https://armbrustlab.ocean.washington.edu/people/beethiaume/) (Software Engineer)
- [Mattias Cape](https://armbrustlab.ocean.washington.edu/people/cape/) (Postdoctoral Research Associate)
- [Kristof Glauninger](https://www.stat.washington.edu/person/kristof-glauninger)(Graduate Student)

### Software
* [popcycle](https://github.com/uwescience/popcycle) - an R package that analyzing continuous flow cytometry data from SeaFlow repository. The software is built to perform both coarse real-time data analysis and fine-tuned population clustering analysis.

* [seaflowpy](https://github.com/armbrustlab/seaflowpy) - Python libraries and scripts to complement ```popcycle```

* [ssPopModel](https://github.com/armbrustlab/ssPopModel) - an R package that uses size-structured matrix population model to estimate hourly division rates of microbial populations from SeaFlow data. These estimates are independent of variations in cell abundance and can be used to study physiologically-driven changes in population dynamics.


### Instrument 
#### Technology
SeaFlow is a custom-built shipboard flow cytometer developed for high-resolution observations of small phytoplankton (< 5 $\mu$m) in surface waters [(Swalwell et al. 2011)](https://doi.org/10.4319/lom.2011.9.466). The instrument utilizes light scattering and autofluorescence properties to discriminate and quantify different cell populations that span 0.5-5 micrometer in size. Unlike a conventional flow cytometer, SeaFlow directly analyzes a raw stream of seawater using two detectors that determine the position of the particle within the focal region of the instrument optical system. With this technology, measurements from particles that pass through the ideal focal position of the collection optics can be differentiated from improperly positioned particles, producing a measurement equivalent to that obtained with a conventional cytometer (see [OPP filtration](https://github.com/armbrustlab/seaflow-filter)). The ratio of these optimally positioned particles (OPP) to the total detectable particles is used to retrieve the volumetric flow rate, allowing accurate estimation of cell abundances (see [Virtual Core calibration](https://github.com/armbrustlab/seaflow-virtualcore)). The instrument is semi-autonomous and can be controlled remotely via satellite connection. 

#### Photos

**Prototype** SeaFlow (June 2008)  
![Seaflow Gen 1]({% link /assets/images/SeaFlow-gen1.jpg %})

**First-generation** SeaFlow (August 2009)  
![Seaflow Gen 2]({% link /assets/images/seaflow-gen2.jpg %})

SeaFlow on the UW **research vessel** (April 2010)  
![Seaflow Research Vessel]({% link /assets/images/seaflow-research-vessel.png %})

SeaFlow on a **container ship** (Oocl Tokyo) (January 2011)  
![Seaflow Container Ship]({% link /assets/images/seaflow-container-ship.jpg %})

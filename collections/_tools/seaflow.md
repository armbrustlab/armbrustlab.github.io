---
title: SeaFlow project
---

![Seaflow]({% link /assets/images/seaflow.jpeg %})

**SeaFlow** is a novel underway flow cytometer created at UW by the Armbrust lab that is designed to measure continuously the abundance and composition of microbial populations, making it possible to analyze the equivalent of one sample every three minutes. The instrument collects information about the size and pigment content of an individual cell and counts several thousands cells every second in real-time. The instrument utilizes light scattering and autofluorescence properties of individual cells to discriminate and quantify different cell populations that span 0.5-15 micrometer in size (see [Swalwell et al. 2009](https://doi.org/10.4319/lom.2011.9.466) for more details). The instrument is semi-autonomous and can be controlled remotely via satellite connection. Real-time data can be visualized using [our web interface](http://armbrustlab.github.io/seaflowviz3/).

### SeaFlow project team members
- [Ginger Armbrust](https://armbrustlab.ocean.washington.edu/people/armbrust/) (Principal investigator)
- [Francois Ribalet](https://armbrustlab.ocean.washington.edu/people/ribalet/) (Co-Investigator)
- [Jarred Swalwell](https://armbrustlab.ocean.washington.edu/people/swalwell/) (Instrument engineer)
- [Chris Berthiaume](https://armbrustlab.ocean.washington.edu/people/beethiaume/) (Software engineer)
- [Annette Hynes] (Data analyst)


### Software
* [popcycle](https://github.com/uwescience/popcycle) - an R package that analyzing continuous flow cytometry data from SeaFlow repository. The software is built to perform both coarse real-time data analysis and fine-tuned population clustering analysis.

* [ssPopModel](https://github.com/armbrustlab/ssPopModel) - an R package that uses size-structured matrix population model to estimate hourly division rates of microbial populations from SeaFlow data. These estimates are independent of variations in cell abundance and can be used to study physiologically-driven changes in population dynamics.

* [seaflowpy](https://github.com/armbrustlab/seaflowpy) - Python libraries and scripts to complement [popcycle](https://github.com/uwescience/popcycle)

### Instrument Photos

**First-generation** SeaFlow (June 2008)  
![Seaflow Gen 1]({% link /assets/images/SeaFlow-gen1.jpg %})

**Second-generation** SeaFlow (August 2009)  
![Seaflow Gen 2]({% link /assets/images/seaflow-gen2.jpg %})

SeaFlow on the UW **research vessel** (April 2010)  
![Seaflow Research Vessel]({% link /assets/images/seaflow-research-vessel.png %})

SeaFlow on a **container ship** (Oocl Tokyo) (January 2011)  
![Seaflow Container Ship]({% link /assets/images/seaflow-container-ship.jpg %})

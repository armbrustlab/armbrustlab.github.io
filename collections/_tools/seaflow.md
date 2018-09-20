---
title: SeaFlow cytometer
---

![Seaflow]({% link /assets/images/seaflow.jpeg %})

**SeaFlow** is a novel underway flow cytometer created at UW by [Jarred Swalwell]({% link _people/swalwell.md %}) that is designed to measure continuously the abundance and composition of microbial populations, making it possible to analyze the equivalent of one sample every three minutes. The instrument collects information about the size and pigment content of an individual cell and counts several thousands cells every second in real-time. The instrument utilizes light scattering and autofluorescence properties of individual cells to discriminate and quantify different cell populations that span 0.5-15 micrometer in size. The instrument is semi-autonomous and can be controlled remotely via Satellite connection.  
Description of the instrument can be found in the following publication: Swalwell, J.E., Ribalet, F., and Armbrust, E.V. 2011. SeaFlow: A novel underway flow-cytometer for continuous observations of phytoplankton in the ocean. [Limnology & Oceanography Methods 9: 466-477.](https://doi.org/10.4319/lom.2011.9.466)

The analysis and distribution of SeaFlow data is led by [Francois Ribalet]({% link _people/ribalet.md %}). Abundance and optical properties of the different microbial populations can be visualized using [our web interface](http://armbrustlab.github.io/seaflowviz3/) created by [Chris Berthiaume]({% link _people/berthiaume.md %}). Rates of cell growth for cyanobacteria populations (namely <i>Prochlorococcus</i> and <i>Synechococcus</i>) are available upon request.



### Software
* [popcycle](https://github.com/uwescience/popcycle) - an R package that analyzing continuous flow cytometry data from SeaFlow repository. The software is built to perform both coarse real-time data analysis and fine-tuned population clustering analysis.

* [ssPopModel](https://github.com/armbrustlab/ssPopModel) - an R package that uses size-structured matrix population model to estimate hourly division rates of microbial populations from SeaFlow data. These estimates are independent of variations in cell abundance and can be used to study physiologically-driven changes in population dynamics.

* [seaflowpy](https://github.com/armbrustlab/seaflowpy) - Python libraries and scripts for analyzing SeaFlow data

### Instrument Photos

**First-generation** SeaFlow (June 2008)  
![Seaflow Gen 1]({% link /assets/images/SeaFlow-gen1.jpg %})

**Second-generation** SeaFlow (August 2009)  
![Seaflow Gen 2]({% link /assets/images/seaflow-gen2.jpg %})

SeaFlow on the UW **research vessel** (April 2010)  
![Seaflow Research Vessel]({% link /assets/images/seaflow-research-vessel.png %})

SeaFlow on a **container ship** (Oocl Tokyo) (January 2011)  
![Seaflow Container Ship]({% link /assets/images/seaflow-container-ship.jpg %})

---
title: SEAStAR Quick Start
nested: true
---
If you would like to easily try out SEAStAR, we recommend working through our "Quick Start" tutorial. We have packaged everything you'll need to get started in a handy pre-built "Virtual Machine Appliance" file that can be run on most up-to-date computers with very little fuss. In the tutorial, all the software you'll need is pre-installed, and we walk you though all the steps to turn raw metagenomic sequence reads into de novo assembled scaffolds. We provide a working, reduced-size example dataset that can be quickly processed even on a laptop, so the whole tutorial should take you less than an hour to complete.

### Requirements:
The SEAStAR Quick Start Virtual Appliance should "just work" on most computers with a 64-bit dual-core processor, 4GB RAM, and ~7 Gb of free disk space, running Windows, Mac OS X or Linux.

### Steps to get it running:

1. Download the [SEAStAR Quick Start Appliance file](https://drive.google.com/file/d/1fBWelGezHK2hbI27jQs5P0-O6lmlX47X/view?usp=sharing){:target="_blank"}. Warning: Large file! ~2 GBytes. Allow plenty of time to download! While it is downloading, you can work on the next two steps. When the download completes, you may want to check that the file's [MD5 sum](https://www.google.com/search?q=how+to+check+an+MD5+sum) = d860840913b7b99c2f2beb809820acd9
1. Download and install the most recent version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (free) for your operating system.
1. Download and install the most recent version of the [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads) (same file for all operating systems).
1. Once the "Appliance file" from step 1 has been successfully downloaded: Run VirtualBox on your computer. Open the File>Import Appliance...> menu and load the .ova file you downloaded above.
1. Once the import is complete, select the "SEAStAR" VM from the left-hand panel, and then press the big green "Start" button. The virtual machine will boot into Linux. Wait for the start-up process to finish. If you've never run a Virtual Machine before and you receive a cryptic error message from VirtualBox at this point, you may need to enable the "Virtualization Technology" for your processor. This is done in the BIOS settings of your computer. You can find help online by Googling: "[enabling virtualization in bios](https://www.google.com/search?q=enabling+virtualization+in+bios)"
1. When you see these two windows in the VM, you are ready to go: (on a small laptop screen one may be on top of the other...)

![seastar quick start]({% link /assets/images/seastar-quick-start.png %})

---
first_name: Chris
last_name: Berthiaume
---

I support reproducible computational research in the Armbrust Lab.
My primary focus is working with the [SeaFlow]({% link _tools/seaflow.md %}) instrument,
our in-house continuous flow cytometer. I write software to analyze SeaFlow data ([seaflowpy](https://github.com/seaflow-uw/seaflowpy), [popcycle](https://github.com/seaflow-uw/popcycle)), manage the data itself, and create systems for realtime collection, processing, and monitoring of SeaFlow data while at sea.
I've also worked on a number of genomics projects in the Armbrust Lab involving RNA microarrays, Sanger and 454 EST library creation, SOLiD and Illumina short-read transcriptomes and genomes, and de novo SOLiD short-read metagenomic assemblies.

github: [https://github.com/ctberthiaume](https://github.com/ctberthiaume)

#### Publications

<div class="publications">
{%- assign years = (site.min_pub_year..site.max_pub_year) | reverse %}
{%- for y in years %}
  {%- capture bib_count %}
    {%- bibliography_count -f berthiaume -q @*[year={{y}}]* %}
  {%- endcapture %}
  {%- assign bib_count = bib_count | to_integer %}
  {%- if bib_count > 0 %}
    <h3 class="year">{{y}}</h3>
    {% bibliography -f berthiaume -q @*[year={{y}}]* %}
  {%- endif %}
{% endfor %}
</div>

# armbrustlab.github.io

This repository holds [Jekyll](https://jekyllrb.com) site source for the [Armbrust Lab](https://armbrustlab.ocean.washington.edu) at the [University of Washington](https://www.washington.edu/). It uses a modified version of the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Local development installation
These instructions assume MacOS or Linux.


Clone the repository

```sh
git clone https://github.com/armbrustlab/armbrustlab.github.io.git
```


To bring up a Docker container to host a development version of the website run

```sh
cd armbrustlab.github.io
docker compose up
```

Now access the site at http://localhost:8080.

## Notes on source organization
Top-level pages, those listed in the primary menu, are located in `_pages`. Other pages are organized as Jekyll collections and can be found in folders `_people`, `_research`, and `_tools`. Images are located in `assets/img`.

All pages should be written in Markdown text format. [See here for a quick summary of major syntax](https://www.markdownguide.org/basic-syntax).

### Theme customizations

This site has modified the base `al-folio` theme, forked around March 2023 and again in August 2025, in the following places:

#### `_includes/footer.liquid`

Removed Jekyll / theme, modified copyright to reference `_config.yml` `copyright_holder` site variable.

#### `_includes/bio_row.liquid`

Created a new include definition for the profile entry for each lab member to be included in `_pages/people.md`.

#### `_layouts/bib_bio.liquid`

Modified default bibliography layout originally found in `_layouts/bib.liquid`.
The `jekyll-scholar` section of `_config.yml` has been modified to make this the default bibliography template.

## Common tasks

### Create internal links

Links to places within the site should be created using the the [Liquid template](https://jekyllrb.com/docs/templates/) tag `{% link %}`. See [https://jekyllrb.com/docs/templates/#link](https://jekyllrb.com/docs/templates/#link). Using a link tag ensures that internal links on the site will be valid for each build. If a link is invalid and can't be generated the build will fail. As an example, to create a link to `https://armbrustlab.ocean.washington.edu/tools/seaflow`, you would use `{% link _tools/seaflow.md %}`. This could be wrapped into a Markdown link as `[SeaFlow]({% link _tools/seaflow.md %})`.

### Add a new lab member page

To add a new lab member simply create a new Markdown file at `_people` and name it `lastname.md`. It's easiest to copy an existing lab members profile file, then edit the [YAML Front Matter](https://jekyllrb.com/docs/frontmatter/) header at the top of the file and the actual Markdown content below. To add a profile picture add the image file to `/assets/img`, sized appropriately, then update the bio page frontmatter section. Here's an example of the front matter section for a lab member profile page.

```yaml
---
first_name: FirstName
last_name: LastName
profile:
  align: right
  image: LastName_profile.jpg  # this image should exist in /assets/img
  image_circular: false # crops the image to make it circular
---
```

### Add a new research or tools section page

Create a new markdown file, or copy an existing one, at `_research` or `_tools`.
The Front Matter should follow this pattern

```yaml
title: ecology
description: Phytoplankton ecology and physiology along environmental gradients
order: 1
img: assets/img/CTD_at_sunrise_preview.jpg
```

where the `title`, `description`, and `img` are used to create an entry in the `/research/` or `/tools` page tiself.
And the `order` controls the sort order of research sections listed on the `/research/` or `/tools` page.

### Add an image to a page

See above for adding profile images to lab member pages.

The general method to add an image in the contents of a page would follow this template using a Liquid Template include snippet

```liquid
{% include figure.html path="assets/img/SeaFlowAnalysis-logo.png" alt="SeaFlow Logo" class="img-fluid rounded z-depth-1" %}
```

where the optional class parameters `rounded` rounds out the image box corners,
and `z-depth-1` adds depth and creates a subtle drop shadow.
`figure.liquid` is the include to use, defined at `_includes/figure.liquid`.

For more control over image presentation and alignment you could embed HTMl in your Markdown file.

```html
<figure class="figure w-100 text-center">
  <img src="{% link assets/img/metagenome-small.gif %}" title="metagenome" class="figure-img img-fluid"/>
  <figcaption class="figure-caption text-center">Within each liter of seawater, how do a billion individual microbial cells compete for available resources, interact with one another, shape and respond to environmental change, and ultimately reproduce or perish?</figcaption>
</figure>
```

You could even have the image function as a link

```html
<figure class="figure w-100 text-center">
  <a href="{% link assets/img/metagenome-large.gif %}">
    <img src="{% link assets/img/metagenome-small.gif %}" title="metagenome" class="figure-img img-fluid"/>
  </a>
  <figcaption class="figure-caption text-center">Within each liter of seawater, how do a billion individual microbial cells compete for available resources, interact with one another, shape and respond to environmental change, and ultimately reproduce or perish?</figcaption>
</figure>
```

You can control image and caption alignment by altering the CSS class `text-center` to one of `text-left`, `text-center`, or `text-right`.

### Add a publications section to your profile page

As an alternative to maintaining a list of your publications as Markdown text,
you can upload a bibtex file with your publications to `_bibliography`
and have a publications automatically generated based on the contents of that file.

To do this you should add a section like this to your profile page,
assuming you've already uploaded a bibtext file named `_bibliography/bibtex_file_name.bib`.

```
#### Publications

<div class="publications">
{%- assign years = (site.min_pub_year..site.max_pub_year) | reverse %}
{%- for y in years %}
  {%- capture bib_count %}
    {%- bibliography_count -f bibtex_file_name -q @*[year={{y}}]* %}
  {%- endcapture %}
  {%- assign bib_count = bib_count | to_integer %}
  {%- if bib_count > 0 %}
    <h3 class="year">{{y}}</h3>
    {% bibliography -f bibtex_file_name -q @*[year={{y}}]* %}
  {%- endif %}
{% endfor %}
</div>
```

This will group your publications by year, most recent first.

To produce an reverse chronological list of publications with no grouping by year you could simply use this

```
#### Publications

<div class="publications">
  {% bibliography -f bibtex_file_name %}
</div>
```

Remember to change `bibtext_file_name` to match the bibtex file placed in `_bibliography`, without the `.bib` extension.

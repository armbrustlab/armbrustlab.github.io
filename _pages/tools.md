---
layout: page
permalink: /tools/
title: tools
nav: true
nav_order: 3
horizontal: true
---
<!-- _pages/tools.md -->
<div class="projects">
{%- assign sorted_projects = site.tools | sort: "order" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
</div>

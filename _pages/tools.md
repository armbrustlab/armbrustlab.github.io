---
layout: page
permalink: /tools/
title: tools
nav: true
nav_order: 3
horizontal: false
---
<!-- _pages/tools.md -->
<div class="projects">
{%- assign sorted_projects = site.tools | sort: "order" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
</div>

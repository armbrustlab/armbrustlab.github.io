---
title: Lab Members
permalink: /people/
---
![Lab Retreat 2018]({% link /assets/images/LabPhoto2018_crop.png %})

<ul>
{% for item in site.people %}
  <li>
    <a href="{{ item.url }}">{{ item.title }}</a>
  </li>
{% endfor %}
</ul>

---
title: Lab Members
permalink: /people/
---
![Lab Retreat 2015]({% link /assets/images/LabRetreat_2015.JPG %})

<ul>
{% for item in site.people %}
  <li>
    <a href="{{ item.url }}">{{ item.title }}</a>
  </li>
{% endfor %}
</ul>

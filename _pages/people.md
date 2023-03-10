---
title: Lab Members
permalink: /people/
---


<ul>
{% for item in site.people %}
  <li>
    <a href="{{ item.url }}">{{ item.title }}</a>
  </li>
{% endfor %}
</ul>

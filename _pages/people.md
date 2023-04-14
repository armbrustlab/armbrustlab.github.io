---
layout: page
permalink: /people/
title: people
description:
nav: true
nav_order: 2
---
<!-- _pages/people.md -->

{% assign by_last_name = site.people | group_by: "last_name" %}
{% assign sorted_by_last_name = by_last_name | sort: "name" %}
{% for ln in sorted_by_last_name %}
  {% assign sorted_by_first_name = ln.items | sort: "first_name" %}
  {% for bio in sorted_by_first_name %}
    {% include bio_row.html profile_image=bio.profile.image url=bio.url first_name=bio.first_name last_name=bio.last_name %}
  {% endfor %}
{% endfor %}

---
layout: home
---

<h2 class="post-list-heading">Learning Vector Art</h2>

{% if site.categories.lva.size > 0 %}
  <table>
    <tr>
      {% assign i = 0 %}
      {% for post in site.categories.lva %}

        {% comment %} Determine image filename 01, 02, .. 99 etc. {% endcomment %}
        {% assign count = site.categories.lva.size | minus: i %}
        {% capture number %}{% if count > 9 %}{{count}}{% else %}0{{count}}{% endif %}{% endcapture %}

        <td><a href="{{ site.baseurl }}{{ post.url }}"><img src="{{ site.baseurl }}/assets/images/posts/2018/LearningVectorArt/{{ number }}.svg"></a></td>
        {% assign i = i | plus: 1 %}

        {% comment %} Add a new row after each 4 images {% endcomment %}
        {% if i > 0 %}
          {% assign value = i | modulo:3 %}
          {% if value == 0 %}
            </tr><tr>
          {% endif %}
        {% endif %}

      {% endfor %}
    </tr>
  </table>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
{% endif %}

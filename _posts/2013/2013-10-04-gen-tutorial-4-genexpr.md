---
layout: post
title: Gen Tutorial 4 - GenExpr
date: 2013-10-04 22:00:00 +02:00
tags:
- Max MSP
- Gen
- C
- dsp
- tutorial
---
In the sidebar on the right of *Gen* you may have noticed a section called ‘code’.

![]({{site.url}}/assets/images/posts/2013/13-10-04/01.png)

This is a textual representation of the *Gen* patch, in this case, the defining of an add variable, which is assigned to the addition of inputs 1 and 2, and then assigned as the output. This code panel is a representation only, and if you try to change it, nothing will happen. Luckily *Gen* sports the **codebox** operator which is undoubtedly the most unique and extendible operator in *Gen*.

Create a new **[gen~]** object, and in the *Gen* replace the **+** operator with the operator **codebox**. This should turn into a text box with the default code

{% highlight c %}
out1 = in1 + in2;
{% endhighlight c %}

Test out the patch, sounds familiar?

![]({{site.url}}/assets/images/posts/2013/13-10-04/02.png)

Yes you’re right, this is the same patch as GenTutorial1.1, albeit this time using written code instead of the visual operator **+**.

*GenExpr* is the internal language (similar to *C* and *Javascript*) used by *Gen* patchers, compiled directly into machine code, thus making it so fast and efficient. When we use operators like **+**, **history**, **buffer** etc., *Gen* automatically does this compilation for us, however we can directly write *GenExpr* code ourselves using **expr** and **codebox**. Note that there is no performance difference in writing the *GenExpr* code ourselves, however sometimes one approach is more convenient than the other. For instance, take a look at the following video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/OwHfkoAj2-U" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<p></p>

Here the presented wished to create a waveshaper, and easily found some code online which he was able to convert into *GenExpr* code, and thus created a waveshaper in the matter of minutes.

The **expr** operator has the same functionality as **codebox**, but lacks the text editor features such as syntax highlighting, multi-line text display, and navigation. Thus **expr** is most useful for short, one-line expressions, saving time patching multiple operators together.

![]({{site.url}}/assets/images/posts/2013/13-10-04/03.png)

All patches can be downloaded [here](https://drive.google.com/open?id=1eQuAESTleCjDFjV-H-fqKs-8Tg3E7oU5){:target="_blank"}.
---
layout: post
title: Waiting Until all jQuery AJAX Request are Successfully Completed
date:  2013-12-17 23:32:00 +01:00
category: tech
tags:
- javascript
- jQuery
- AJAX
---
One of the issue with the current version of the DNPT (Deutsch Nomen Plural Test) is that it loads the singular words, plural words, and their English equivalent from file, but if there is a delay, then the page is rendered regardlessly, and **init** function called. Luckily, it is really easily to wait until a method (or request) is successfully completed.

```javascript
//only when all three functions have returned true
$.when( fn1(), fn2() ).done( function()
{
	//is this print out done
	console.log("when");
});
//function one
function fn1()
{
	console.log("fn1");
	return $.get("list1.txt", function(data)
	{
		console.log(data);
	});
}
//function two
function fn2()
{
	console.log("fn2");
	return $.get("list2.txt", function(data)
	{
		console.log(data);
	});
}
```

This is achieved as follows. Firstly we put the AJAX request inside a function, and give the function the result of the AJAX request. Now the AJAX **when** request will wait and only trigger when until both **fn1** and **fn2** functions return true, thus executing it’s function body. And so the console output is as follows:

```
fn1
fn2
a
b
c
1
2
3
when
```

For more information, see the [official API](http://api.jquery.com/jQuery.when/).

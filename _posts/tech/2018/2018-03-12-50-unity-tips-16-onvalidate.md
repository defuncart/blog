---
layout: post
title: '50 Unity Tips #16: OnValidate'
date: 2018-03-12 10:00:00 +01:00
category: tech
tags:
- Unity
- UnityTipsTricks
---

Yesterday we talked about the **[Range]** attribute which ensures that float/int values entered in the inspector are constrained to a certain range, thus ensuring valid input. However wouldn't it be great to validate data for all properties, not just those of type float and int?

**OnValidate** is a callback when a script extending *MonoBehaviour* or *ScriptableObject* (not mentioned in the API) is loaded or the value of a property is changed in the inspector. Here we can use if statements or assertions to check that the inputted data is valid.

```C#
public class MyComponent : MonoBehaviour
{
  [SerializeField] private Button myButton;

  private void OnValidate()
  {
    Assert.IsNotNull(myButton, "Expected myButton to be not null");
  }
}
```

![](https://raw.githubusercontent.com/defuncart/50-unity-tips/master/%2316-OnValidate/images/onValidate1.png)
![](https://raw.githubusercontent.com/defuncart/50-unity-tips/master/%2316-OnValidate/images/onValidate2.png)

## Further Reading

[Scripting API - MonoBehaviour.OnValidate()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnValidate.html)

[Scripting API - Assertions.Assert](https://docs.unity3d.com/ScriptReference/Assertions.Assert.html)


<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/50-unity-tips/tree/master/%2316-OnValidate">GitHub repository</a>.</font></p>

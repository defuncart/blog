---
layout: post
title: '50 Unity Tips #5: Custom Invoke'
date: 2017-06-01 10:00:00 +02:00
tags:
- Unity3D
- unity2d
- UnityTipsTricks
---

[github_link]: https://github.com/defuncart/50-unity-tips/tree/master/%2305-CustomInvoke
[![]({{site.url}}/assets/images/viewOnGitHub.png)][github_link]

```public void Invoke(string methodName, float time)``` allows one to trigger a given method (via string methodName) after a delay of time seconds. However there are two notable issues:

1. Invoke uses reflection which can have a large overhead and should be avoided when possible.
2. Invoke methods are difficult to debug as methods called by name are hard to track in code.

A better Invoke can be accomplished by using Coroutines and Actions:

```csharp
public static Coroutine Invoke(this MonoBehaviour monoBehaviour, Action action, float time)
{
  return monoBehaviour.StartCoroutine(InvokeImplementation(action, time));
}

private static IEnumerator InvokeImplementation(Action action, float time)
{
  yield return new WaitForSeconds(time);
  action();
}
```

which can be easily called within any class that extends MonoBehaviour

```csharp
private void Test()
{
  Debug.Log("Test using custom invoke");
}

this.Invoke(Test, 3f);

this.Invoke(() => {
  Debug.Log("Test using closure");
}, 4f);
```

This custom Invoke can easily be cancelled by holding a reference to its returned coroutine.

```csharp
public static void CancelInvoke(this MonoBehaviour monoBehaviour, Coroutine coroutine)
{
  monoBehaviour.StopCoroutine(coroutine);
}

Coroutine coroutine = this.Invoke(Test, 10f);
this.CancelInvoke(coroutine);
```

Custom Invoke could be further extended with the ability to include parameters too, although this isn't something I've found a use for yet.

```csharp
public static Coroutine Invoke<T>(this MonoBehaviour monoBehaviour, Action<T> action, T parameter, float time) where T : class
{
  return monoBehaviour.StartCoroutine(InvokeImplementation(action, parameter, time));
}

private static IEnumerator InvokeImplementation<T>(Action<T> action, T parameter, float time) where T : class
{
  yield return new WaitForSeconds(time);
  action(parameter);
}

private void TestWithParameter(string param)
{
  Debug.Log(param);
}

this.Invoke(TestWithParameter, "Test using custom invoke and param", 5f);
```

As discussed in [the previous tip](https://github.com/defuncart/50-unity-tips/tree/master/%2304-MoreEfficientYieldStatements), we should limit the number of created *WaitForSeconds* when possible. This can be achieved utilizing **WaitFor** and caching *WaitForSeconds* variables.

```csharp
public static Coroutine Invoke(this MonoBehaviour monoBehaviour, Action action, float time, bool useCachedWaits = true)
{
  return monoBehaviour.StartCoroutine(InvokeImplementation(action, time, useCachedWaits));
}

private static IEnumerator InvokeImplementation(Action action, float time, bool useCachedWaits)
{
  //wait for time seconds then invoke the action. if useCachedWaits is true, uses a cached WaitForSeconds, otherwise creates a new one
  yield return (useCachedWaits ? WaitFor.Seconds(time) : new WaitForSeconds(time));
  action();
}
```

The *useCachedWaits* variable can be set to false if it would be more desirable in creating a new *WaitForSeconds*, that would be subsequently removed by the garbage collector.

```csharp
this.Invoke(action: () => {
  Debug.Log("Some action with a unique wait time that will only be triggered once.");
}, time: 4f, useCachedWaits: false);
```

Finally, ```public void InvokeRepeating(string methodName, float time, float repeatRate)``` can be similarly implemented using Coroutines.

```csharp
public static Coroutine InvokeRepeating(this MonoBehaviour monoBehaviour, Action action, float time, float repeatRate, bool useCachedWaits = true)
{
  return monoBehaviour.StartCoroutine(InvokeRepeatingImplementation(action, time, repeatRate, useCachedWaits));
  }

/// <summary>The coroutine implementation of InvokeRepeating.
private static IEnumerator InvokeRepeatingImplementation(Action action, float time, float repeatRate, bool useCachedWaits)
{
  //wait for a given time then indefiently loop - if useCachedWaits is true, uses a cached WaitForSeconds, otherwise creates a new one
  yield return (useCachedWaits ? WaitFor.Seconds(time) : new WaitForSeconds(time));
  while(true)
  {
    //invokes the action then waits repeatRate seconds - if useCachedYields is true, uses a cached WaitForSeconds, otherwise creates a new one
    action();
    yield return (useCachedYields ? WaitFor.Seconds(repeatRate) : new WaitForSeconds(repeatRate));
  }
}
```

These custom invoke methods could also be added to a custom class inherited from MonoBehaviour which one would then always use as their base class.

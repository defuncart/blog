---
layout: post
title: 'Learning Xamarin: #07 Autosize Label'
date: 2019-02-16 16:00:00 +01:00
category: tech
tags:
- Xamarin
---

An application which explores autosizing a label in Xamarin.Forms.

## Overview

The ability for the system to autosize a label depending on text length is pretty fundamental, especially when considering localization. Coming from iOS Development and Unity, this is something I expected to be build into Xamarin.Forms, and was a little perplexed that I needed to invest so much time in reading docs, forms and inventually needing to roll my own solution.

### Case #1

Consider that a label spans a single line. As the German string may be longer than the English string, the fontsize should automatically resize (scale-down) to fit all text on a single line.

### Case #2

Consider that a label should maximize the font size (scale-up) so that the text takes up the full rectangular space.

## Solution

For #1, we could use *XamarinCommunityToolkit* NuGet package with the *LabelSizeFontToFit* effect:

```xaml
<Label.Effects>
  <effects:LabelSizeFontToFit />
</Label.Effects>
```

This method, however, will not scale up a font size, only down. Thus, to solve #2, I decided to adopt Charles Petzold's generally approach of *Empirically fitting text* in Chapter 5 *Dealing with Sizes* of his book *Creating Mobile Apps with Xamarin.Forms* into my own custom label.

*DALabel* extends *Xamarin.Forms.Label* and adds the following two methods:

```Csharp
/// <summary>
/// Autosizes the label's font size with regards to it's container size.
/// </summary>
private void AutoFontSize()
{
    //determine the text height for the min font size
    double lowerFontSize = 10;
    double lowerTextHeight = TextHeightForFontSize(lowerFontSize);

    //determine the text height for the max font size
    double upperFontSize = 100;
    double upperTextHeight = TextHeightForFontSize(upperFontSize);

    //start a loop which'll find the optimal font size
    while(upperFontSize - lowerFontSize > 1)
    {
        //determine current average font size and calculate corresponding text height
        double fontSize = (lowerFontSize + upperFontSize) / 2;
        double textHeight = TextHeightForFontSize(upperFontSize);

        //if the calculated height is out of bounds, update max values, else update min values
        if(textHeight > Height)
        {
            upperFontSize = fontSize; upperTextHeight = textHeight;
        }
        else
        {
            lowerFontSize = fontSize; lowerTextHeight = textHeight;
        }
    }

    //finally set the correct font size
    FontSize = lowerFontSize;
}

/// <summary>
/// Determines the text height for the label with a given font size.
/// </summary>
private double TextHeightForFontSize(double fontSize)
{
    FontSize = fontSize;
    return OnMeasure(Width, Double.PositiveInfinity).Request.Height;
}

```

Now, whenever the label's size is updated, the fontsize will be adjusted.

```csharp
/// <summary>
/// Callback when the size of the element is set during a layout cycle.
/// </summary>
protected override void OnSizeAllocated(double width, double height)
{
    //call base implementation
    base.OnSizeAllocated(width, height);

    //update font size
    AutoFontSize();
}
```

Likewise, whenever the text itself is actually set, we can update the font size

```csharp
/// <summary>
/// The label's text.
/// </summary>
new public string Text
{
    get { return (string)GetValue(TextProperty); }
    set { SetValue(TextProperty, value); AutoFontSize(); }
}
```

As an added bonus, MinFontSize and MaxFontSize properties can be added so that the min/max font size values can be specified in XAML.

## Resources

[Charles Petzold Creating Mobile Apps with Xamarin.Forms](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/creating-mobile-apps-xamarin-forms/)

[Charles Petzold Chapter 5. Dealing with Sizes](https://download.xamarin.com/developer/xamarin-forms-book/XamarinFormsBook-Ch05-Apr2016.pdf)

[Xamarin Community Toolkit](https://github.com/xamarin/XamarinCommunityToolkit)

[Xamarin.Forms.Label Source](https://github.com/xamarin/Xamarin.Forms/blob/master/Xamarin.Forms.Core/Label.cs)

<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/Xamarin/tree/master/07-AutosizeLabel">GitHub repository</a>.</font></p>

---
layout: post
title: 'Learning Xamarin: #02 Layouts'
date: 2019-01-12 16:00:00 +01:00
category: tech
tags:
- Xamarin
---

An application which explores the different type of layouts in Xamarin.Forms.

## Overview

Xamarin.Forms Layouts are used to compose user-interface controls into visual structures. These layouts can be divided into two categories: those containing a single child and those with multiple children.

![](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/layouts-images/layouts-sml.png)

### Layouts with Single Content

| Layout  | Description  |
|:--|---|
| Content View | A view which contains a single child. |
| Frame | A class derived from *ContentView* which displays a rectangular frame around its child. |
| Scroll View | A view capable of scrolling its contents. Scrolling can be either horizontal, vertical or both. |

### Layouts with Multiple Children

| Layout  | Description  |
|:--|---|
| StackLayout | StackLayout positions its children in horizontally or vertically stacks based on a *Orientation* property. Simple linear interfaces can be created by just adding views to a StackLayout, while more complex ones can be created by nesting them. |
| Grid | Grid positions its children in a grid of rows and columns. A child's position is indicated using the properties *Row*, *Column*, *RowSpan* and *ColumnSpan*. |
| AbsoluteLayout | AbsoluteLayout positions and sizes child elements at specific locations relative to its parent. Child views may be positioned and sized using proportional values or static values, and proportional and static values can be mixed. A child's position is indicated using the properties *LayoutBounds* and *LayoutFlags*. |
| RelativeLayout | RelativeLayout is used to position and size views relative to properties of the layout or sibling views. Unlike *AbsoluteLayout*, RelativeLayout does not have the concept of the moving anchor and does not have facilities for positioning elements relative to the bottom or right edges of the layout. |
| FlexLayout | FlexLayout is similar to the *StackLayout* in that it can arrange its children horizontally and vertically in a stack. However, FlexLayout can, for example, wrapp its children if there are too many to fit in a single row or column etc. FlexLayout is based on the CSS Flexible Box Layout Module. |

## Resources

[Xamarin.Forms Layouts](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/layouts)

<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/Xamarin/tree/master/02-Layouts">GitHub repository</a>.</font></p>

---
layout: post
title: 'Learning Xamarin #05: ListView'
date: 2019-02-02 16:00:00 +01:00
category: tech
tags:
- Xamarin
---

An application which explores the ListView in Xamarin.Forms.

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/defuncart/Xamarin/master/05-ListView/Images/1.png" width="300"/></td>
    <td><img src="https://raw.githubusercontent.com/defuncart/Xamarin/master/05-ListView/Images/2.png" width="300"/></td>
  </tr>
</table>

## Overview

*ListView* is a view for presenting lists of data, especially long lists that require scrolling. It support context actions and data binding. Unlike *TableView*, ListView is best suited for data of the same type as only one type of cell can be used for each row in the list.

ListView has a number of components available to exercise the native functionality of each platform:

- Headers and Footers
- Groups
- Cells
  - Built in: 
    - TextCell
    - ImageCell
  - CustomCells

ListView supports a number of interaction styles, including:

- Pull-to-refresh
- Context Actions
- Selection

## Images

Images can be shared across platforms with Xamarin.Forms, they can be loaded specifically for each platform, or they can be downloaded for display.

*Embedded Images* are shipped with the application with image file is embedded in the assembly as a resource. **NOTE**: build target needs to be set to **EmbeddedResource**.

An image can be easily loaded using 

```csharp
ImageSource.FromResource("PROJECT_NAME.IMAGE_NAME.EXTENSION");
```

where the *Resource ID* is the default namespace dot filename. Note that images can be organized into folders, for instance ListView.Images.de.png is the resource id for the german flag located inside the Images folder.

### ImageCell

ListView compiles down to native Android and iOS views, however as seen in the screenshots above, their behavior isn't always the same. For instance, ImageCell uses 60px width (with height matching aspect ratio) on Android, while the images on iOS have constant height (with width matching aspect ratio).

### ImageResourceExtension

By default embedded images cannot be assigned in XAML. This helper extension, although not used in this project, helps fix that.

## Json

Json can be easily deserialized using NuGet Newtonsoft.Json. First get a reference to the JSON resource (EmbeddedResource)

```csharp
var assembly = IntrospectionExtensions.GetTypeInfo(typeof(MY_PAGE)).Assembly;
Stream stream = assembly.GetManifestResourceStream(RESOURCE_ID);
```

then read all text from this filestream

```csharp
string text = "";
using(var reader = new StreamReader(stream))
{
    text = reader.ReadToEnd();
}
```

and then deserialize

```csharp
object myObject = JsonConvert.DeserializeObject<object>(text);
```

## Resources

[Xamarin Docs - ListView](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/listview/)

[Xamarin Docs - Images](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/images)

## Assets Utilized

[countries.json](https://gist.github.com/erdem/8c7d26765831d0f9a8c62f02782ae00d)

[Flags](https://github.com/hjnilsson/country-flags)

<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/Xamarin/tree/master/05-ListView">GitHub repository</a>.</font></p>

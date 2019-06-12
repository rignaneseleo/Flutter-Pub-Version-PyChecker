# Tool to find the last version of Flutter plugins
### This is a free open source tool to quikly get the list of the last versions of your Flutter plugins.

## How TO
First you have to edit your pubspec.yaml adding ```#vcontrol-start``` before the first plugin and ```#vcontrol-end``` after the last plugin you want to analyze.

Then run ``` py flutter_pychecker.py```  or ``` python flutter_pychecker.py```  to execute the tool.

## Example
My pubspec.yaml contains:
```
[...]
dependencies:
  flutter:
    sdk: flutter

  #vcontrol-start
  sqflite: ^1.1.5
  path_provider: ^1.1.0
  curved_navigation_bar: ^0.1.26
  fluttertoast: ^3.0.3
  #esys_flutter_share: ^1.0.2
  intl: ^0.15.8
  flutter_speed_dial: ^1.1.2

  photo: ^0.3.4
  #image_picker: ^0.6.0+3
  photo_view: ^0.4.0
  image_downloader: ^0.15.2
  image: ^2.0.7
  cached_network_image: ^0.8.0
  #vcontrol-end
[...]
``` 

So let's start the tool and insert the absolute path of pubspec.yaml as required:
``` 
Insert the absolute path of your pubspec.yaml: 
/Users/leonardorignanese/Progetti/Flutter/MyGrandKids/my_grand_kids/pubspec.yaml
``` 

Then you'll get the list of active plugins with their last version:
``` 
Found 11 plugins:
        The last version of sqflite: ^1.1.5 is 1.1.5
        The last version of path_provider: ^1.1.0 is 1.1.0
        The last version of curved_navigation_bar: ^0.1.26 is 0.2.20
        The last version of fluttertoast: ^3.0.3 is 3.1.0
        The last version of intl: ^0.15.8 is 0.15.8
        The last version of flutter_speed_dial: ^1.1.2 is 1.2.1
        The last version of photo: ^0.3.4 is 0.3.4+1
        The last version of photo_view: ^0.4.0 is 0.4.0
        The last version of image_downloader: ^0.15.2 is 0.15.4
        The last version of image: ^2.0.7 is 2.1.4
        The last version of cached_network_image: ^0.8.0 is 0.8.0
```

The tool can return also the updated list to copy and replace in your file:
```
Do you want to see the list updated to copy and paste in your pubspec.yaml?[Y/n]
Y

#vcontrol-start
  sqflite: ^1.1.5
  path_provider: ^1.1.0
  curved_navigation_bar: ^0.2.20
  fluttertoast: ^3.1.0
  intl: ^0.15.8
  flutter_speed_dial: ^1.2.1
  photo: ^0.3.4+1
  photo_view: ^0.4.0
  image_downloader: ^0.15.4
  image: ^2.1.4
  cached_network_image: ^0.8.0
  #esys_flutter_share: ^1.0.2
  #image_picker: ^0.6.0+3
#vcontrol-end
```

Peace

### Tool to find the last version of Flutter plugins
# Credits Leonardo Rignanese <dev.rignaneseleo@gmail.com>
# Github: https://github.com/rignaneseleo

This is a free open source tool to quikly get the list of the last versions of your Flutter plugins.
Run "py flutter_pychecker.py" or "python flutter_pychecker.py" to execute the tool.

You will insert the path of your pubspec.yaml that MUST contain #vcontrol-start before the first plugin and #vcontrol-end after the last plugin you want to analyze.

Example:
'
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
'
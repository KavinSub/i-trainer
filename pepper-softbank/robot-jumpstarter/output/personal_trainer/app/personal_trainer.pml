<?xml version="1.0" encoding="UTF-8" ?>
<Package name="personal_trainer" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="dialogue" src="dialogue/dialogue.dlg" />
        <Dialog name="ExampleDialog" src="ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="style" src="html/css/style.css" />
        <File name="index" src="html/index.html" />
        <File name="icon" src="icon.png" />
        <File name="jquery-1.11.0.min" src="html/js/jquery-1.11.0.min.js" />
        <File name="main" src="html/js/main.js" />
        <File name="robotutils" src="html/js/robotutils.js" />
        <File name="" src="html/music/.DS_Store" />
        <File name="gymmusic" src="html/music/gymmusic.mp3" />
        <File name="movearound" src="movearound.pmt" />
    </Resources>
    <Topics>
        <Topic name="dialogue_enu" src="dialogue/dialogue_enu.top" topicName="dialogue" language="en_US" />
        <Topic name="ExampleDialog_enu" src="ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>

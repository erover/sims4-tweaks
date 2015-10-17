#Sms 4 Age Mod Generation Script
Don't like EAxis' settings for Sim lifespans? Don't like any of the pre-existing mods? XML fill you with the overwhelming urge to pry your own eyes from your skull like it does with me?
This is a simple python script that allows users to generate a new .tuning file that overrides the game's age length XML.

I'm currently still testing this and the XML that it generates. If you want to help that would be neat but if you don't like packaging up untested XML and adding it to your game, maybe give this a pass for the moment.

##Instructions


Mods that this tool creates override the XML resource 03B33DDF 00000000 5D0152209188C58B, so any other packages that override the same resource will conflict and your games wont work when trying to use both of them.
Basically, don't try to install multiple packages that modify age length because that will prevent your game from loading and also is just really stupid.

##How it Works
1. User (you) does their bit, enters values in response to prompts.
2. Copy is made of template.tuning file.
3. Script takes use-entered age length value and overwrites placeholders in template copy.
4. Template is renamed to "S4_03B33DDF_00000000_5D0152209188C58B%%+ITUN.tuning".
5. Whitespace is purged from the newly created .tuning file because EA recommends doing so for performance.

##Changelog
| Date     | Change            |
|----------|-------------------|
| 17/10/15 | Initial 'Release' |

##TOU
Whatever.

##Credits
[Sims4Group](http://sims4group.github.io/) for s4pe.
velocitygrass and scumbumbo for their respecive Sims 4 XML extractors.
Mark Hamill. Just in general.
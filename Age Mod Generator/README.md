#Sms 4 Age Mod Generation Script
Don't like EAxis' settings for Sim lifespans? Don't like any of the pre-existing mods? XML fill you with the overwhelming urge to pry your own eyes from your skull like it does with me?
This is a (really) simple python script that allows users to generate a new .tuning file that overrides the game's age length XML without ever having to actually read any XML because XML is bloody hateful.

I'm currently still testing this and the XML that it generates. If you want to help that would be neat but if you don't like packaging up untested XML and adding it to your game, maybe give this a pass for the moment.

##Instructions
0. MAKE SAVE BACKUPS BEFORE YOU DO ANYTHING TO YOUR SIMS GAME.
1. Run the script in the Python Interpreter.
2. Follow instructions on screen.
3. When you're sure you've got all of the correct values you'd like in your mod, select menu option 4, "Finish and Export".
4. Open [s4pe](https://github.com/Kuree/Sims4Tools/releases).
5. File -> New in s4pe.
6. Resource -> Import -> From File
7. Navigate to the directory this script is saved to and select S4_03B33DDF_00000000_5D0152209188C58B%%+ITUN.tuning.
8. File -> Save. Name it anything you want, anywhere you want. Make sure to append .package to the end of your file name.
9. Congratulations you now have a .package file that overrides the default age lengths in The Sims 4.
10. Write back and tell me if your game blew up or not. Seriously anything this thing can spit out has barely been tested.

Mods that this tool creates override the XML resource 03B33DDF 00000000 5D0152209188C58B, so any other packages that override the same resource will conflict and your games wont work when trying to use both of them.
Basically, don't try to install multiple packages that modify age length because that will prevent your game from loading and also is just really stupid.

##How it Works
1. User (you) does their bit, enters values in response to prompts.
2. Copy is made of template.tuning file.
3. Script takes use-entered age length value and overwrites placeholders in template copy.
4. Template is renamed to "S4_03B33DDF_00000000_5D0152209188C58B%%+ITUN.tuning".

##Changelog
| Date     | Change            |
|----------|-------------------|
| 17/10/15 | Initial 'Release' |
| 17/10/15 | Hotfixed problem where whitespace purging was corrupting saves somehow. By removing all the purge code. Purging to be returned to at later date. Also fixed issue with new.tuning not getting deleted when it should have been.|

##Known Issues
* The neat little tables that the script is meant to show don't look very neat anymore because formatting got broked somewhere down the line. I have decided that this issue loses to precedent to confirming that the script actually spits out valid XML.

##TOU
Whatever. It's a find-and-replace script. ¯\_(⊙_ʖ⊙)_/¯

##Credits
* [Sims4Group](http://sims4group.github.io/) for s4pe.
* velocitygrass and scumbumbo for their respecive Sims 4 XML extractors.
* Mark Hamill. Just in general.

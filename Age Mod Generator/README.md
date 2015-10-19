#Sms 4 Age Mod Generation Script
This is a really simple script that generates XML files that override the default life stange lengths in The Sims 4. The files that are generated are named correctly so that all one has to do to turn the XML that this spits out is import it into s4pe and hit Save.
I basically wrote this up because I wanted to experiment with a number of different tunings for life states but also hate reading/editing XML.

Mods that this tool creates override the XML resource 03B33DDF 00000000 5D0152209188C58B, so any other packages that override the same resource will conflict and your games wont work when trying to use both of them.
Basically, don't try to install multiple packages that modify age length because that will prevent your game from loading and also is just really stupid.

##How it Works
Sims 4 aging tuning works kind of weird. Each life stage has only one value (named age_transition_threshold) that represents the number of days that the life stage lasts, despite there being three different settings for sim aging accessible from the Game Options menu. For example, by default the age_transiton_threshold for children is 13. This is the length of the child life stage on the Normal setting. The other two settings (Long and Short) aren't actually definied in the XML but are calculated by the game based on the age_transition_threshold and another value called the age_speed_setting_multiplier, which has three versions; one for each setting.
So in order to find the length of the Child stage on the Long lifespan setting, the game divides the length of the Normal setting by the multiplier for the Long setting (referred to as 'SLOW' in the XML).
This script allows the changing of both the age_transition_threshold for every stage as well as the age_speed_setting multiplier for the long and short lifespan settings (changing the multiplier for the Normal setting would be weird and pointless).
The output file is named S4_03B33DDF_00000000_5D0152209188C58B%%+ITUN.tuning, which shouldn't be changed if you're planning at all on importing this tuning into s4pe to create a usable mod out of it.

##Changelog
| Date     | Change            |
|----------|-------------------|
| 17/10/15 | Initial 'Release' |
| 17/10/15 | Hotfixed problem where whitespace purging was corrupting saves somehow. By removing all the purge code. Purging to be returned to at later date. Also fixed issue with new.tuning not getting deleted when it should have been.|

##Known Issues
* The neat little tables that the script is meant to show don't look very neat anymore because formatting got broked somewhere down the line. I have decided that this issue loses to precedent to confirming that the script actually spits out valid XML.

##TOU
Whatever. It's just a find-and-replace script that might actually take longer to run than it would to actually change the XML yourself if you're familiar with how The Sims 4 handles life stage tuning and XML doesn't make your eyes bleed.

##Credits
* [Sims4Group](http://sims4group.github.io/) for s4pe.
* velocitygrass and scumbumbo for their respecive Sims 4 XML extractors.
* Mark Hamill. Just in general.

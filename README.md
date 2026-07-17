# ZZAR-SteamFix
A quick fix for audio replacement mods on Steam.

# Original fix from Anime Game Audio Replacers discord by Rex The Orange
**NOTE: YOU DO NOT NEED TO THE FOLLOWING STEPS AS THIS SCRIPT DOES THIS FOR YOU**

While I am grateful to our resident orange for this post, it stumped me for days despite being so simple. The script in this repo performs these steps for you while also coaching you into what you have to do at each step. No guesswork needed.

**Note 2: THIS BEEN EDITED FOR CLARITY**

---

Here's the potential manual solution **FOR STEAM VERSION:**

## Step zero:
Back up two folders listed below, in case something goes wrong, and they need to be restored to default state.
- `ZenlessZoneZero_Data/Persistent/Audio`
- `ZenlessZoneZero_Data/StreamingAssets/Audio`

*Clarification*
1. Create a folder named `Persistent-bak` in `ZenlessZoneZero_Data`
2. Create a folder named `StreamingAssets-bak` in `ZenlessZoneZero_Data`
3. Copy the **folder** `ZenlessZoneZero_Data/Persistent/Audio` into `ZenlessZoneZero_Data/Persistent-bak`
4. Copy the **folder** `ZenlessZoneZero_Data/StreamingAssets/Audio` into `ZenlessZoneZero_Data/StreamingAssets-bak`
5. Copy the **file** `ZenlessZoneZero_Data/StreamingAssets/audio_version` to `ZenlessZoneZero_Data/StreamingAssets-bak`

## Step one:
Temporary disable all audio mods.

## Step two:
Replace `ZenlessZoneZero_Data/StreamingAssets/audio_version` with a renamed copy of `ZenlessZoneZero_Data/Persistent/audio_version_persist`.

Don't forget to change file name accordingly, to avoid confusing game with unexpected filenames.
You want the file **name** to remain `audio_version`, while contents of the file to be replaced

*Clarification:* `audio_version` and `audio_version_persist` **are extensionless files**. **THEY ARE NOT FOLDERS**. You are simply replacing the persist version with the streamed version.

## Step three:
Move `ZenlessZoneZero_Data/Persistent/Audio` into `ZenlessZoneZero_Data/StreamingAssets` replacing files when there's a conflict.

(Use cut and paste instead of copy-paste , because you don't want any duplicates to remain in Persistent folder)

*Clarification:* You are free to copy and paste. ZZZ will delete all the files in `ZenlessZoneZero_Data/Persistent/Audio` for you as it will no longer need them.

## Step four:
Boot the game and let it auto-complete file verification. It might download or shuffle some files.
Download size would be fairly small if you have not made any mistakes during previous two steps, Less then one gigabyte as of zenless patch 3.0

*Clarification:* This will likely be < 300 Mb in size.

## Step five:
Close the game and make sure that folder `ZenlessZoneZero_Data/Persistent/Audio` did not got automatically filled back in during **step four**.

If something somehow appeared there, then you want to re-do steps #3, #4 and #5

Mods can be installed on steam build after that. They should stop leading to redownloads on each reboot.

(**WARNING** - when you boot up audio manager - it can detect actions you took while following five steps above as an issue, and offer to automatically fix audio folders by shuffling files around. **DO NOT ACCEPT** this offer. If you accept - it can cause some audio to get nuked and will require you to then retrieve it

*Clarification:* This warning only applies to XXAR currently. It will give a warning about how your languages are not in the StreamingAssets folder but will also delete files you need. If you do not see it, you may have already accepted it, breaking your Steam install. Delete both `ZenlessZoneZero_Data/Persistent/Audio` and `ZenlessZoneZero_Data/StreamingAssets/Audio` then verify your game's files via Steam to start from scratch.) 


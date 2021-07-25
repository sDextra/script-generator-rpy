init python:
###############################################################################################
    gs_folder = "generated/" # Folder for extracting .txt files and generating .rpy files
    gs_tag_label = 'LABEL: ' # search and insert label
    gs_need_enter_after_quoute = False # if you need enter after the speaker's dialogue, set True
    gs_dissolve = ' with dissolve'
    gs_dissolve_with_enter = '\n    with dissolve'
###############################################################################################

###############################################################################################
    # CHARACTERS LIST
    characters = { 
        "PLAYER" : 'p',
        "AMY" : 'a',
        "LIEN" : 'l',
    }
    think = '' # for a dialogue without a name tag, or ex: 't '
###############################################################################################

###############################################################################################
    # СЛОВАРЬ СПРАЙТОВ
    tag_sp_show = 'SPRITE: ' # show sprite
    tag_sp_hide = 'HIDE SPRITE: ' # hide sprite
    list_sprites = { 
            tag_sp_show+"AMY FEAR": 'amy fear'+gs_dissolve,
            tag_sp_show+"AMY HORROR FAST": 'amy horror',
            tag_sp_show+"AMY HORROR DISS": 'amy horror'+gs_dissolve,
            tag_sp_show+"AMY HORROR ENTERDISS": 'amy horror'+gs_dissolve_with_enter,
            tag_sp_hide+"AMY": 'amy with dissolve',
    }
###############################################################################################

###############################################################################################
    # BG's LIST
    tag_bg = 'BG: ' 
    list_backgrounds = { 
            tag_bg+"HALLWAY DISS": 'bg hallway'+gs_dissolve,
            tag_bg+"HALLWAY FAST": 'bg hallway',
            tag_bg+"STREET DISS": 'bg street'+gs_dissolve,
            tag_bg+"STREET FAST": 'bg street',
    }
###############################################################################################

###############################################################################################
    # CG's LIST
    tag_cg = 'CG: '
    list_cg = { 
        tag_cg+"AMY CRY": 'cg amy_cry'+gs_dissolve,
    }
###############################################################################################

###############################################################################################
    # ADDING MUSIC TRACKS
    music_fadeout = 1.0 # default music fadeout
    music_fadein = 1.0 # default music fadein
    music_fadeactive = True # set False, if fadein and fadeout don't need 
    music_pref = 'play music '
    music_suff = ' fadein %s fadeout %s'%(music_fadein, music_fadeout)
#############################################################################
    # LIST OF MUSIC TRACKS
    tag_ms = 'MUSIC: '
    list_music = { 
            tag_ms+"SAD": 'sad',
            tag_ms+"USUAL": 'usual',
    }
###############################################################################################
    
###############################################################################################
    # ADDING EFFECT SOUNDS
#############################################################################
    sound_fadeout = 0.3 # default sound fadeout
    sound_fadein = 0.3 # default sound fadein
    sound_fadeactive = True # set False, if fadein and fadeout don't need 
    sound_pref = 'play sound '
    sound_suff = ' fadein %s fadeout %s'%(sound_fadein, sound_fadeout)
#############################################################################
    # LIST OF EFFECT SOUNDS
    tag_sn = 'SOUND: '
    list_sounds = { 
        tag_sn+"CRY": 'cry',
        tag_sn+"KNOCK": 'knock',
        tag_sn+"HEARTBET": 'heartbeat',
    }
###############################################################################################

###############################################################################################
# by sDextra
###############################################################################################

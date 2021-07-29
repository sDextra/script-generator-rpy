init -1 python hide:
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '/']
    config.automatic_images_strip = ['images']

init python:
#############################################################################
    utf8 = "utf-8"
    def file_check(file, folder, ex='.rpy'):
        try:
            check = renpy.file(folder+file+ex)
            if check:
                return True
        except Exception:
            pass
        return False

    def full_list_files(query, folder):
        f = []
        bg = len(folder)
        en = len(query)*-1
        for lf in renpy.list_files():
            if lf[:bg] == folder and lf[en:] == query:
                lf = lf[bg:en]
                f.append(lf)
        return f

    def script_generator(file, folder, ending='return'):
        tab = '\t'
        enter = '\n'
        suffix = "\""
        spaced = '    '
        prefix = ''

        full_path = renpy.loader.transfn(folder+file+".txt")
        path = full_path.strip(".txt")
        txt = open(full_path, 'r')
        rpy = open(path+'.rpy', 'w')
        rpy.write('label '+file+':'+enter)

        for line in txt:
            with_quotes = True

            if enter in line:
                line = line.replace(enter, '')
            if suffix in line:
                line = line.replace(suffix, '')

            if gs_tag_label.encode(utf8) in line:
                label = line.strip().split(': ')[1]
                line = 'label '+label+':'+enter
                with_quotes = False

            elif tag_sp_hide.upper().encode(utf8) in line.upper():
                for k,v in store.list_sprites.items():
                    if k.upper().encode(utf8) in line.upper():
                        line = spaced + 'hide '+ v.encode(utf8) + enter
                        with_quotes = False
                        break
            elif tag_sp_show.upper().encode(utf8) in line.upper():
                for k,v in store.list_sprites.items():
                    if k.upper().encode(utf8) in line.upper():
                        line = spaced + 'show '+ v.encode(utf8) + enter
                        with_quotes = False
                        break
            elif tag_bg.upper().encode(utf8) in line.upper():
                for k,v in store.list_backgrounds.items():
                    if k.upper().encode(utf8) in line.upper():
                        line = spaced + 'scene '+ v.encode(utf8) + enter
                        with_quotes = False
                        break
            elif tag_cg.upper().encode(utf8) in line.upper():
                for k,v in store.list_cg.items():
                    if k.upper().encode(utf8) in line.upper():
                        line = spaced + 'scene '+v.encode(utf8) + enter
                        with_quotes = False
                        break
            elif tag_ms.upper().encode(utf8) in line.upper():
                for k,v in store.list_music.items():
                    if k.upper().encode(utf8) in line.upper():
                        if store.music_fadeactive:
                            line = spaced + store.music_pref.encode(utf8)+ v.encode(utf8) +store.music_suff.encode(utf8) + enter
                        else:
                            line = spaced + store.music_pref.encode(utf8)+ v.encode(utf8) + enter
                        with_quotes = False
                        break
            elif tag_sn.upper().encode(utf8) in line.upper():
                for k,v in store.list_sounds.items():
                    if k.upper().encode(utf8) in line.upper():
                        if store.sound_fadeactive: 
                            line = spaced + store.sound_pref.encode(utf8)+ v.encode(utf8) +store.sound_suff.encode(utf8) + enter 
                        else:
                            line = spaced + store.sound_pref.encode(utf8)+ v.encode(utf8) + enter 
                        with_quotes = False
                        break
            if with_quotes:
                if line and line[0] != tab:
                    prefix = spaced+store.think.encode(utf8)+suffix
                else:
                    for k,v in store.characters.items(): 
                        if k.upper().encode(utf8) in line.upper():
                            line = ''
                            prefix = spaced+v.encode(utf8)+' "' 

                while tab in line:
                    line = line.replace(tab, '')

                line = prefix+line+suffix+enter

                if gs_need_enter_after_quoute:
                    if prefix != spaced+suffix:
                        line += enter

            if "\"\"" in line:
                continue

            line = line.encode('UTF-8').decode(utf8)
            rpy.write(line)
        else:
            rpy.write(enter+spaced+ending)
        
        rpy.close()
        txt.close()

        renpy.reload_script()
        renpy.set_autoreload(False)
#############################################################################
#############################################################################

#############################################################################
screen script_generator_screen():
    modal True 
    default file = False
    default x = int(config.screen_width*0.5)
    default y = int(config.screen_height*0.7)
    default txt_list = full_list_files('.txt', gs_folder)
    frame xysize x,y align (.5,.5):
        text _('SCRIPT GENERATOR') align .5,.01
        frame xysize x, int(y*.85) align .5,.5:
            viewport id "gs" draggable True mousewheel True:
                vbox xsize x:
                    for lf in txt_list:
                        textbutton "[lf].txt" action SetScreenVariable('file', lf) alternate SetScreenVariable('file', False) xalign .5
            if len(txt_list) > 12:
                vbar value YScrollValue("gs") align (1.0,.5)

        textbutton _("Ok") action If(file, [If(file_check(file, gs_folder), [Show('gs_sure', file=file)], [Function(script_generator, file, gs_folder)])] ) align (.2, 1.0)
        textbutton _("Reload") action Function(renpy.reload_script) align (.5,1.0)
        textbutton _("Quit") action MainMenu(confirm=False) align (.8,1.0)
    key 'K_ESCAPE' action MainMenu(confirm=False) 
    text _("Made by {a=https://github.com/sDextra}sDextra{/a} ") align 1.0,1.0
#############################################################################

#############################################################################
screen gs_sure(file=None):
    modal True
    add '#00000090'
    default x = int(config.screen_width*0.6)
    default y = int(config.screen_height*0.3)

    frame xysize x,y align (.5,.5):
        text _("File '[file].rpy' will be regenerated.") align (.5,.25)
        text _("Are you sure?") align (.5,.5)
        textbutton _("Ok") action Hide('gs_sure'), Function(script_generator, file, gs_folder) align (.3, .9)
        textbutton _("Cancel") action Hide('gs_sure') align (.7,.9)
    key 'K_ESCAPE' action Hide('gs_sure')
#############################################################################
# by sDextra
#############################################################################

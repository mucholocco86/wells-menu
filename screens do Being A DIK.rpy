init offset = -1









style slot_text_custom:
    font "fonts/candara.ttf"
    size 40
    color "#ffffff"
    xmaximum 320
    yoffset 5
    outlines [(4, "#330000", 0, 0)]
    hover_outlines [(4, "#330000", 0, 0)]
    text_align 0.5

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















define persistent.say_window_alpha = 0.3
screen say(who, what):
    style_prefix "say"

    window:
        background Transform(style.window.background, alpha=persistent.say_window_alpha)
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos











screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:

    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    properties gui.text_properties("input_prompt")

style input:
    xalign 0.5
    xmaximum gui.dialogue_width










init -1:


    style menu_sex_style is default



    style menu_sex_style is button_text:
        font "fonts/Audrey-Bold.otf"
        size 30
        color "#ffcc66"
        hover_color "#ffffff"

        yoffset 5
        xoffset 55
        outlines [(1, "#330000", 0, 0)]
        hover_outlines [(1, "#660066", 0, 0)]

        drop_shadow [(2, 2)]
        drop_shadow_color "#663300"

    style menu_sex_style_disabled is button_text:
        font "fonts/Audrey-Bold.otf"
        size 30
        color "#ffffff"
        hover_color "#ffffff"

        yoffset 5
        xoffset 55



        drop_shadow [(2, 2)]
        drop_shadow_color "#663300"


    style menu_sex_style_button is button:
        background Frame("images/gui/buttons/sex_buttons/sex_choices_idle.png",0,0)
        hover_background Frame("images/gui/buttons/sex_buttons/sex_choices_hover.png",0,0)

        xminimum int(config.screen_width * 0.3)
        xmaximum int(config.screen_width * 0.3)


        yminimum 90
        ymaximum 180
        ypadding 10
        xpadding 15
    style menu_sex_style_button_disabled is button:
        background Frame("images/gui/buttons/sex_buttons/sex_choices_disabled.png",0,0)
        hover_background Frame("images/gui/buttons/sex_buttons/sex_choices_disabled.png",0,0)


        xminimum int(config.screen_width * 0.3)
        xmaximum int(config.screen_width * 0.3)


        yminimum 90
        ymaximum 180
        ypadding 10
        xpadding 15

screen choice:
    style_prefix "choice"


    vbox:
        xalign 1.0
        yalign 0.8
        style "menu"
        spacing 2

        for caption, action, chosen in items:
            if action:
                if " (disabled)" in caption:
                    button:
                        style "menu_sex_style_button_disabled"
                        text caption.replace(" (disabled)", "") style "menu_sex_style_disabled"
                else:
                    button:
                        action action
                        style "menu_sex_style_button"
                        text caption style "menu_sex_style"
            else:
                text caption style "menu_sex_style"



define config.autosave_slots = 12
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 900
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")






style quick_btn_style:

    hover_color "#fe9416"
    size 20
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    color "#FFFFFF"

screen quick_menu():


    zorder 100
    if not phone_opened:
        mousearea:
            area (0, 980, 720, 100)
            hovered SetVariable("quick_menu_hovered", True)
            unhovered SetVariable("quick_menu_hovered", False)
        if persistent.quick_menu > 0 and quick_menu > 0:
            if (quick_menu_hovered and persistent.quick_menu == 1) or (persistent.quick_menu == 2):

                hbox:
                    style_prefix "quick"
                    xalign 0.0
                    yalign 1.0

                    if persistent.qm_back:
                        textbutton _("Back") action Rollback() text_style "quick_btn_style"
                    if persistent.qm_history:
                        textbutton _("History") action ShowMenu('history') text_style "quick_btn_style"
                    if persistent.qm_skip:
                        textbutton _("Skip") action Skip() text_style "quick_btn_style"
                    if persistent.qm_auto:
                        textbutton _("Auto") action Preference("auto-forward", "toggle") text_style "quick_btn_style"
                    if persistent.qm_save:
                        textbutton _("Save") action ShowMenu('save') text_style "quick_btn_style"
                    if persistent.qm_qsave:
                        textbutton _("Q.Save") action QuickSave() text_style "quick_btn_style"
                    if persistent.qm_qload:
                        textbutton _("Q.Load") action (SetVariable("persistent.current_save_name",FileSaveName(1, page="quick")),QuickLoad()) text_style "quick_btn_style"

                    if persistent.qm_prefs:
                        textbutton _("Prefs") action ShowMenu('preferences') text_style "quick_btn_style"
                    if persistent.qm_guide and (steamConfig or nonPatreonConfig) and renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
                        textbutton _("Guide") action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0),Function(show_guide_func)) text_style "quick_btn_style"




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu_hovered = False
default quick_menu = 2
default tmpMenu = 2
default tmpMenu2 = 2
default persistent.qm_back = True
default persistent.qm_history = True
default persistent.qm_skip = True
default persistent.qm_auto = True
default persistent.qm_save = True
default persistent.qm_qsave = True
default persistent.qm_qload = True
default persistent.qm_prefs = True
default persistent.qm_guide = True
default persistent.quick_menu = 2

style quick_button is default
style quick_button_text is button_text
define quick_button.choice_text_hover_color = '#0066cc'
style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation:




























    vbox:

        xalign 0.01
        yalign 0.01
        spacing 5
        textbutton _("MAIN MENU") action (MainMenu()) text_style "custom_menu_style_header_btn"
        textbutton _("QUIT") action Quit(confirm=not main_menu) text_style "custom_menu_style_header_btn"

    hbox:

        xalign 0.5
        yalign 0.08
        spacing 30
        textbutton _("SAVE") action ShowMenu("save") text_style "custom_menu_style_header_btn"
        imagebutton:
            idle "gui/preferences/custom_menu_separator.png"
            hover "gui/preferences/custom_menu_separator.png"
            action NullAction()
            yoffset -2
        textbutton _("LOAD") action ShowMenu("load") text_style "custom_menu_style_header_btn"
        imagebutton:
            idle "gui/preferences/custom_menu_separator.png"
            hover "gui/preferences/custom_menu_separator.png"
            action NullAction()
            yoffset -2
        textbutton _("AUDIO") action ShowMenu("audio") text_style "custom_menu_style_header_btn"
        imagebutton:
            idle "gui/preferences/custom_menu_separator.png"
            hover "gui/preferences/custom_menu_separator.png"
            action NullAction()
            yoffset -2
        textbutton _("DIALOGUE") action ShowMenu("dialogue") text_style "custom_menu_style_header_btn"
        imagebutton:
            idle "gui/preferences/custom_menu_separator.png"
            hover "gui/preferences/custom_menu_separator.png"
            action NullAction()
            yoffset -2
        textbutton _("SETTINGS") action ShowMenu("preferences") text_style "custom_menu_style_header_btn"

style custom_menu_style_header_btn:
    font "fonts/candara.ttf"
    size 35
    hover_color "#fe9416"
    selected_color "#fe9416"
    color "#ffffff"
    insensitive_color "#808080"

style custom_menu_style_footer_btn:
    size 35
    hover_color "#fe9416"
    selected_color "#fe9416"
    color "#ffffff"

style custom_menu_style_text:
    font "fonts/candara.ttf"
    size 32
    color "#ffffff"

style custom_menu_style_text3:
    font "fonts/candara.ttf"
    size 32
    color "#00a0e6"

style custom_menu_style_text2:
    font "fonts/candara.ttf"
    size 32
    color "#636363"
    hover_color "#fe9416"

style custom_menu_style_text2_enabled:
    font "fonts/candara.ttf"
    size 32
    color "#fe9416"
    hover_color "#fe9416"

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








image spr_bg:
    spr_mm_arr[0][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[0][1]

    spr_mm_arr[1][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[1][1]

    spr_mm_arr[2][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[2][1]

    spr_mm_arr[3][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[3][1]

    spr_mm_arr[4][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[4][1]
    repeat

image spr_mid:
    spr_mm_arr[0][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[0][3]

    spr_mm_arr[1][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[1][3]

    spr_mm_arr[2][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[2][3]

    spr_mm_arr[3][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[3][3]

    spr_mm_arr[4][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr[4][3]
    repeat

image spr_top:
    spr_mm_arr[0][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s2[0][5]

    spr_mm_arr[1][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s2[1][5]

    spr_mm_arr[2][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s2[2][5]

    spr_mm_arr[3][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s2[3][5]

    spr_mm_arr[4][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s2[4][5]
    repeat

image spr_bg_s3:
    spr_mm_arr_s3[0][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[0][1]

    spr_mm_arr_s3[1][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[1][1]

    spr_mm_arr_s3[2][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[2][1]

    spr_mm_arr_s3[3][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[3][1]

    spr_mm_arr_s3[4][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[4][1]

    spr_mm_arr_s3[5][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[5][1]

    spr_mm_arr_s3[6][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[6][1]

    spr_mm_arr_s3[7][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[7][1]

    spr_mm_arr_s3[8][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[8][1]

    spr_mm_arr_s3[9][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[9][1]

    spr_mm_arr_s3[10][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[10][1]

    spr_mm_arr_s3[11][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[11][1]

    spr_mm_arr_s3[12][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[12][1]

    spr_mm_arr_s3[13][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[13][1]

    spr_mm_arr_s3[14][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[14][1]

    spr_mm_arr_s3[15][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[15][1]

    spr_mm_arr_s3[16][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[16][1]

    spr_mm_arr_s3[17][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[17][1]

    spr_mm_arr_s3[18][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[18][1]

    spr_mm_arr_s3[19][0] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[19][1]
    repeat

image spr_mid_s3:
    spr_mm_arr_s3[0][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[0][3]

    spr_mm_arr_s3[1][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[1][3]

    spr_mm_arr_s3[2][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[2][3]

    spr_mm_arr_s3[3][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[3][3]

    spr_mm_arr_s3[4][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[4][3]

    spr_mm_arr_s3[5][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[5][3]

    spr_mm_arr_s3[6][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[6][3]

    spr_mm_arr_s3[7][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[7][3]

    spr_mm_arr_s3[8][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[8][3]

    spr_mm_arr_s3[9][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[9][3]

    spr_mm_arr_s3[10][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[10][3]

    spr_mm_arr_s3[11][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[11][3]

    spr_mm_arr_s3[12][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[12][3]

    spr_mm_arr_s3[13][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[13][3]

    spr_mm_arr_s3[14][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[14][3]

    spr_mm_arr_s3[15][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[15][3]

    spr_mm_arr_s3[16][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[16][3]

    spr_mm_arr_s3[17][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[17][3]

    spr_mm_arr_s3[18][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[18][3]

    spr_mm_arr_s3[19][2] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[19][3]
    repeat

image spr_top_s3:
    spr_mm_arr_s3[0][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[0][5]

    spr_mm_arr_s3[1][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[1][5]

    spr_mm_arr_s3[2][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[2][5]

    spr_mm_arr_s3[3][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[3][5]

    spr_mm_arr_s3[4][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[4][5]

    spr_mm_arr_s3[5][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[5][5]

    spr_mm_arr_s3[6][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[6][5]

    spr_mm_arr_s3[7][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[7][5]

    spr_mm_arr_s3[8][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[8][5]

    spr_mm_arr_s3[9][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[9][5]

    spr_mm_arr_s3[10][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[10][5]

    spr_mm_arr_s3[11][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[11][5]

    spr_mm_arr_s3[12][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[12][5]

    spr_mm_arr_s3[13][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[13][5]

    spr_mm_arr_s3[14][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[14][5]

    spr_mm_arr_s3[15][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[15][5]

    spr_mm_arr_s3[16][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[16][5]

    spr_mm_arr_s3[17][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[17][5]

    spr_mm_arr_s3[18][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[18][5]

    spr_mm_arr_s3[19][4] with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 10.0 zoom spr_mm_arr_s3[19][5]
    repeat

image spr_title:
    "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
    pause 1.5
    "gui/main_menu_sprites/spr_badik.png" with Dissolve(1, alpha=True)
    pause 7
    "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)

image spr_title2:
    "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
    pause 3.5
    "gui/main_menu_sprites/spr_badik2.png" with Dissolve(1, alpha=True)
    pause 5
    "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)

style main_menu_btn_style:
    color "ffffff"
    hover_color "ffaa46"

screen main_menu():


    style_prefix "main_menu" tag menu

    if renpy.loadable("scripts/episode9/update9.rpyc") and persistent.episode_interlude:
        add "spr_bg_s3"
        add "spr_mid_s3"
        add "spr_top_s3"
    else:
        add "spr_bg"
        add "spr_mid"
    if not musicCreditsOpen:
        add "gui/main_menu_sprites/spr_bottom_border.png"
        add "spr_title"
        add "spr_title2"
        
    add "gui/main_menu_sprites/spr_bottom_border.png" xpos -0.6 ypos -0.12
    if renpy.loadable("1NewCheatMode.rpy"):
                text "scrappy's Mod Installed":
                     color "#F1B300"
                     hover_color "E68231"
                     font "Museo500.otf"
                     size 45
                     bold True                
                     xalign 0.01
                     yalign 0.83
    else:
                text "Mod not installed correctly":
                     color "#F0F0F0"
                     hover_color "E68231"
                     font "Museo500.otf"
                     size 45
                     bold True                
                     xalign 0.01
                     yalign 0.83


    if not musicCreditsOpen:
        if not steamConfig and not nonPatreonConfig:
            imagebutton:
                xpos 50
                ypos 975
                idle Transform ("images/gui/buttons/new_game_btn.png")
                hover Transform ("images/gui/buttons/new_game_btn_hover.png")
                action (Start(), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 340
                ypos 975
                idle Transform ("images/gui/buttons/continue_btn.png")
                hover Transform ("images/gui/buttons/continue_btn_hover.png")
                action (ShowMenu("load"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 700
                ypos 975
                idle Transform ("images/gui/buttons/options_btn.png")
                hover Transform ("images/gui/buttons/options_btn_hover.png")
                action (ShowMenu("preferences"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            if menuGalleryOpen:
                imagebutton:
                    xpos 1010
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Hide("menu_gallery"), Hide("music_credits"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1010
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Show("menu_gallery"), Hide("music_credits"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
            if musicCreditsOpen:
                imagebutton:
                    xpos 1350
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1350
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Show("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
        elif nonPatreonConfig:
            imagebutton:
                xpos 50
                ypos 975
                idle Transform ("images/gui/buttons/new_game_btn.png")
                hover Transform ("images/gui/buttons/new_game_btn_hover.png")
                action (Start(), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 340
                ypos 975
                idle Transform ("images/gui/buttons/continue_btn.png")
                hover Transform ("images/gui/buttons/continue_btn_hover.png")
                action (ShowMenu("load"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 700
                ypos 975
                idle Transform ("images/gui/buttons/options_btn.png")
                hover Transform ("images/gui/buttons/options_btn_hover.png")
                action (ShowMenu("preferences"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            if menuGalleryOpen:
                imagebutton:
                    xpos 1010
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Hide("menu_gallery"), Hide("music_credits"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1010
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Show("menu_gallery"), Hide("music_credits"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
            if musicCreditsOpen:
                imagebutton:
                    xpos 1350
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1350
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Show("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 1620
                ypos 975
                idle Transform ("images/gui/buttons/quit_btn.png")
                hover Transform ("images/gui/buttons/quit_btn_hover.png")
                action Quit()
        else:
            imagebutton:
                xpos 30
                ypos 975
                idle Transform ("images/gui/buttons/new_game_btn.png")
                hover Transform ("images/gui/buttons/new_game_btn_hover.png")
                action (Start(), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 310
                ypos 975
                idle Transform ("images/gui/buttons/continue_btn.png")
                hover Transform ("images/gui/buttons/continue_btn_hover.png")
                action (ShowMenu("load"), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 670
                ypos 975
                idle Transform ("images/gui/buttons/dlc_btn.png")
                hover Transform ("images/gui/buttons/dlc_btn_hover.png")
                action (ShowMenu("dlc"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 840
                ypos 975
                idle Transform ("images/gui/buttons/options_btn.png")
                hover Transform ("images/gui/buttons/options_btn_hover.png")
                action (ShowMenu("preferences"), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
            if menuGalleryOpen:
                imagebutton:
                    xpos 1150
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Hide("menu_gallery"), Hide("music_credits"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1150
                    ypos 975
                    idle Transform ("images/gui/buttons/menu_gallery_btn.png")
                    hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png")
                    action (Show("menu_gallery"), Hide("music_credits"), Hide("dlc"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
            if musicCreditsOpen:
                imagebutton:
                    xpos 1480
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Hide("music_credits"), Hide("menu_gallery"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
            else:
                imagebutton:
                    xpos 1480
                    ypos 975
                    idle Transform ("images/gui/buttons/music_credits_btn.png")
                    hover Transform ("images/gui/buttons/music_credits_btn_hover.png")
                    action (Show("music_credits"), Hide("menu_gallery"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
            imagebutton:
                xpos 1740
                ypos 975
                idle Transform ("images/gui/buttons/quit_btn.png")
                hover Transform ("images/gui/buttons/quit_btn_hover.png")
                action Quit()

    if not musicCreditsOpen:
        if steamConfig or nonPatreonConfig:
            vbox:
                xalign 0.03
                yalign 0.05
                spacing 10
                imagebutton:
                    idle Transform ("images/gui/buttons/discord_btn_new.png")
                    hover Transform ("images/gui/buttons/discord_btn_new_hover.png")
                    action OpenURL("https://discord.gg/kESb9Dh")
                if nonPatreonConfig:
                    imagebutton:
                        idle Transform ("images/gui/buttons/gog_btn.png")
                        hover Transform ("images/gui/buttons/gog_btn_hover.png")
                        action OpenURL("https://www.gog.com/game/being_a_dik")
        else:
            vbox:
                xalign 0.03
                yalign 0.08
                spacing 10
                imagebutton at mm_zoom:
                    idle Transform ("images/gui/buttons/patreon_btn_new.png")
                    hover Transform ("images/gui/buttons/patreon_btn_new_hover.png")
                    action OpenURL("https://www.patreon.com/DrPinkCake")
                imagebutton at mm_zoom:
                    idle Transform ("images/gui/buttons/discord_btn_new.png")
                    hover Transform ("images/gui/buttons/discord_btn_new_hover.png")
                    action OpenURL("https://discord.gg/KyCc5E4")
                imagebutton at mm_zoom:
                    idle Transform ("images/gui/buttons/steam_new_btn.png")
                    hover Transform ("images/gui/buttons/steam_new_btn_hover.png")
                    action OpenURL("https://store.steampowered.com/app/1126320/Being_a_DIK__Season_1/")
                imagebutton at mm_zoom:
                    xalign 0.5
                    idle Transform ("images/ep11/gui/bluesky_idle.png")
                    hover Transform ("images/ep11/gui/bluesky_hover.png")
                    action OpenURL("https://bsky.app/profile/drpinkcake.bsky.social")

        if not steamConfig and not nonPatreonConfig:
            vbox:
                style_prefix "help"
                yalign 0.992
                yoffset 10
                xalign 0.98
                spacing -20
                text _("{size=+10}{font=fonts/collegiate.ttf}{color=#ffffff}Version [config.version!t]{/color}{/font}{/size}\n")


    frame




transform mm_zoom:
    zoom 0.8
transform twitter_zoom:
    zoom 0.1

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if _in_replay:
        vbox:
            xalign 0.01
            yalign 0.94
            textbutton _("END REPLAY") action EndReplay(confirm=True) text_style "custom_menu_style_header_btn"
    vbox:
        xalign 0.01
        yalign 0.99
        textbutton _("RETURN"):
            text_style "custom_menu_style_header_btn"
            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -65



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu

    use file_slots(_("Save"))

    if FilePageName() == u'a' or FilePageName() == u'q':
        timer 0.001 action FilePage(1)

screen load():
    tag menu


    use file_slots(_("Load"))

style badik_input_style:
    background "#ffffff"

style badik_input_style2:
    color "#00a0e6"
    font "fonts/candara.ttf"
    size 20

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(""):
        if title == "Save":
            textbutton _("Save Collectibles") action (Function(savePersistentData), Show("saveMsg")) text_style "custom_menu_style_header_btn":
                xalign 0.0
                yalign 1.0
                xoffset -170
                yoffset -20


        fixed:



            order_reverse True
            ypos -30


            button:
                style "custom_menu_style_header_btn"

                key_events True
                xalign 0.99
                yalign 0.99
                yoffset 65
                xoffset 20
                action page_name_value.Toggle()

                input:
                    style "custom_menu_style_header_btn"
                    length 30
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xpos -250
                yalign 0.1

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    $ bad_minigames = FileJson(slot, "minigames", empty=False, missing=False)
                    $ bad_chapter = FileJson(slot, "badik_chapter", empty="0", missing="-1")
                    $ startedChapter = FileJson(slot, "badik_started_chapter", empty="1", missing="1")
                    $ compatibleSave = FileJson(slot, "steamConfig", empty=False, missing=False)
                    button:
                        if bad_chapter == "0" or bad_chapter == "-1" or bad_chapter == "1":
                            if title == "Load" and compatibleSave==steamConfig:
                                action (SetVariable("persistent.current_save_name",FileSaveName(slot)),FileAction(slot))
                            elif title == "Save":
                                action (FileAction(slot))
                            else:
                                action NullAction()
                        elif startedChapter == "1" and bad_chapter == "2":
                            if title == "Load" and compatibleSave==steamConfig:
                                action FileAction(slot)
                            elif title == "Save":
                                action (FileAction(slot))
                            else:
                                action NullAction()
                        else:
                            if title == "Save":
                                action (FileAction(slot))
                            else:
                                action NullAction()

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            if bad_chapter == "0" or bad_chapter == "1" or bad_chapter == "-1":
                                if compatibleSave==steamConfig or FileTime(slot, format=_("{font=fonts/candara.ttf}{#file_time}%B %d %Y, %H:%M{/font}"), empty=_("Empty slot")) == "Empty slot":
                                    if bad_minigames:
                                        text FileTime(slot, format=_("{font=fonts/candara.ttf}{size=-6}{#file_time}%B %d %Y, %H:%M, Mini-games: {color=fe9416}On{/color}{/size}{/font}"), empty=_("Empty slot")):
                                            style "slot_time_text"
                                            font "fonts/candara.ttf"
                                    else:
                                        text FileTime(slot, format=_("{font=fonts/candara.ttf}{size=-6}{#file_time}%B %d %Y, %H:%M{/size}{/font}"), empty=_("Empty slot")):
                                            style "slot_time_text"
                                            font "fonts/candara.ttf"

                                    $ sname_ok = True
                                    for c in FileSaveName(slot):
                                        if not c.isalnum() and c != " " and c != "_":
                                            $ sname_ok = False
                                    if sname_ok:
                                        text FileSaveName(slot):

                                            font "fonts/candara.ttf"
                                            size 21
                                            xalign 0.5
                                            yoffset 2
                                            color "#00a0e6"
                                else:
                                    text "{color=#ff0000}Incompatible save{/color}":
                                        style "slot_time_text"
                                        yoffset -70
                            elif startedChapter == "1" and bad_chapter == "2":
                                if compatibleSave==steamConfig or FileTime(slot, format=_("{font=fonts/candara.ttf}{#file_time}%B %d %Y, %H:%M{/font}"), empty=_("Empty slot")) == "Empty slot":
                                    text FileTime(slot, format=_("{font=fonts/candara.ttf}{size=-3}{#file_time}%B %d %Y, %H:%M{/size}{/font}"), empty=_("Empty slot")):
                                        style "slot_time_text"
                                        font "fonts/candara.ttf"
                                else:
                                    text "{color=#ff0000}Incompatible save{/color}":
                                        style "slot_time_text"
                                        font "fonts/candara.ttf"
                                        yoffset -70
                            else:
                                text "{color=#ff0000}Incompatible save{/color}":
                                    style "slot_time_text"
                                    font "fonts/candara.ttf"
                                    yoffset -70

                            $ bad_chapter = FileJson(slot, "badik_chapter", empty="1", missing="1")
                            if bad_chapter == "0" or bad_chapter == "2" or bad_chapter == "-1":
                                $ sname_ok = True
                                for c in FileSaveName(slot):
                                    if not c.isalnum() and c != " " and c != "_":
                                        $ sname_ok = False
                                if sname_ok:
                                    text FileSaveName(slot):
                                        style "slot_name_text"

                            key "save_delete" action FileDelete(slot)


            if title == "Save":
                hbox:
                    style_prefix "page"
                    yoffset 10
                    xoffset 20
                    xalign 0.99
                    yalign 0.99
                    spacing 10

                    text "{font=fonts/candara.ttf}{size=-5}Save name {/size}{/font}"
                    frame:
                        add "gui/preferences/custom_input_ol.png"
                        style "badik_input_style"
                        ymaximum 26
                        xmaximum 385
                        if mphone_current_input == "save_name":
                            input:
                                size 20
                                default "[save_name]"
                                font "fonts/candara.ttf"
                                color "#00a0e6"
                                value VariableInputValue('save_name')
                                length 23
                                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _1234567890"
                                yoffset 4
                        else:
                            if persistent.current_save_name.strip() == "":
                                textbutton "Click to name your save":
                                    text_style "badik_input_style2"
                                    action SetVariable("mphone_current_input","save_name")
                                    text_align 0.5
                                    xalign 0.5
                                    yoffset -1
                            else:
                                textbutton "[persistent.current_save_name]":
                                    text_style "badik_input_style2"
                                    action SetVariable("mphone_current_input","save_name")
                                    text_align 0.5
                                    xalign 0.5
                                    yoffset -1


            vbox:
                xalign 0.5
                yalign 1.05
                yoffset 30
                xoffset -200
                hbox:
                    xalign 0.5
                    style_prefix "page"
                    spacing gui.page_spacing

                    if config.has_autosave and title == "Load":
                        textbutton _("{font=fonts/Museo500.otf}{#auto_page}A{/font}") action FilePage("auto") text_style "custom_menu_style_footer_btn"

                    if config.has_quicksave and title == "Load":
                        textbutton _("{font=fonts/Museo500.otf}{#quick_page}Q{/font}") action FilePage("quick") text_style "custom_menu_style_footer_btn"


                    for page in range(1, 10):
                        textbutton "{font=fonts/Museo500.otf}[page]{/font}" action FilePage(page) text_style "custom_menu_style_footer_btn"

                hbox:
                    xalign 0.5
                    spacing 25

                    if FilePageName() != u'a' and FilePageName() != u'q' and int(FilePageName()) > 1:
                        textbutton _("{font=fonts/candara.ttf}<<{/font}") action FilePage(max(int(FilePageName())-5,1)) text_style "custom_menu_style_footer_btn"
                    else:
                        textbutton _("{font=fonts/candara.ttf}<<{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
                    if FilePageName() != u'a' and FilePageName() != u'q' and int(FilePageName()) > 1:
                        textbutton _("{font=fonts/candara.ttf}<{/font}") action FilePagePrevious() text_style "custom_menu_style_footer_btn"
                    else:
                        textbutton _("{font=fonts/candara.ttf}<{/font}") action NullAction() text_style "custom_menu_style_footer_btn"

                    if FilePageName() != u'a' and FilePageName() != u'q':
                        textbutton _("{font=fonts/candara.ttf}>{/font}") action FilePageNext() text_style "custom_menu_style_footer_btn"
                    else:
                        textbutton _("{font=fonts/candara.ttf}>{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
                    if FilePageName() != u'a' and FilePageName() != u'q':
                        textbutton _("{font=fonts/candara.ttf}>>{/font}") action FilePage(int(FilePageName())+5) text_style "custom_menu_style_footer_btn"
                    else:
                        textbutton _("{font=fonts/candara.ttf}>>{/font}") action NullAction() text_style "custom_menu_style_footer_btn"



default tmp_page = "1"

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

screen menu_gallery_left:

    modal False tag menu_gallery_left
    add "images/gui/episode_ol/menu_gallery_bg_rewards.png"

screen menu_gallery_right:

    modal False tag menu_gallery_right
    add "images/gui/episode_ol/menu_gallery_bg_scenes.png"

screen menu_gallery():

    modal False tag menu_gallery
    add "menu_gallery_bg"

    mousearea:
        area (0, 0, 960, 937)
        hovered Show("menu_gallery_left")
        unhovered Hide("menu_gallery_left")
    mousearea:
        area (961, 0, 1920, 937)
        hovered Show("menu_gallery_right")
        unhovered Hide("menu_gallery_right")

    imagebutton:
        focus_mask True
        idle Transform("menu_gallery_button")
        hover Transform("menu_gallery_button")
        action (Hide("menu_gallery"), Hide("menu_gallery_right"), Hide("menu_gallery_left"), ShowMenu("rewards"))
        xpos 0
        ypos 0
    imagebutton:
        focus_mask True
        idle Transform("menu_gallery_button")
        hover Transform("menu_gallery_button")
        action (Hide("menu_gallery"), Hide("menu_gallery_right"), Hide("menu_gallery_left"), ShowMenu("scenes"))
        xpos 955
        ypos 0



style my_bar:
    ysize gui.bar_size
    right_bar Frame("gui/slider/horizontal_idle_bar.png", gui.bar_borders, tile=gui.bar_tile)
    left_bar Frame("gui/slider/horizontal_idle_bar_full.png", gui.bar_borders, tile=gui.bar_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style my_vbar:
    ysize gui.bar_size
    right_bar Frame("gui/slider/vertical_idle_bar2.png", gui.bar_borders, tile=gui.bar_tile)
    left_bar Frame("gui/slider/vertical_idle_bar_full.png", gui.bar_borders, tile=gui.bar_tile)
    thumb "gui/slider/vertical_[prefix_]thumb2.png"

screen audio():
    tag menu

    use game_menu(_("")):
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 50
            xoffset 70
            yoffset 100

            hbox:
                xminimum 800
                xmaximum 800
                spacing 50
                label _("Music Volume") text_style "custom_menu_style_text" xminimum 260 xmaximum 260
                bar value Preference("music volume") style "my_bar"

            hbox:
                xminimum 800
                xmaximum 800
                spacing 50
                label _("Sound Volume") text_style "custom_menu_style_text" xminimum 260 xmaximum 260
                bar value Preference("sound volume") style "my_bar"

            vpgrid:
                xminimum 800
                xmaximum 800
                spacing 50
                cols 2
                rows 2


                label _("Mute All") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if preferences.get_mute("music") and preferences.get_mute("sfx"):
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    action Preference("all mute", "toggle")
                    xoffset -40

                label _("Phone Notifications") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if notifications:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                        action (SetVariable("notifications",False))
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                        action (SetVariable("notifications",True))
                    xoffset -40


screen dialogue():
    tag menu

    use game_menu(_("")):
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 50
            xoffset 70
            yoffset 40

            hbox:
                xminimum 800
                xmaximum 800
                spacing 10

                label _("Rollback Side") text_style "custom_menu_style_text" yoffset 5
                imagebutton:
                    idle "gui/preferences/custom_menu_separator.png"
                    hover "gui/preferences/custom_menu_separator.png"
                    action NullAction()
                    xoffset -15
                if preferences.desktop_rollback_side == "disable":
                    textbutton _("Disable") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                    textbutton _("Left") action Preference("rollback side", "left") text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Right") action Preference("rollback side", "right") text_style "custom_menu_style_text2" xoffset -5
                elif preferences.desktop_rollback_side == "left":
                    textbutton _("Disable") action Preference("rollback side", "disable") text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Left") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                    textbutton _("Right") action Preference("rollback side", "right") text_style "custom_menu_style_text2" xoffset -5
                else:
                    textbutton _("Disable") action Preference("rollback side", "disable") text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Left") action Preference("rollback side", "left") text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Right") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5

            hbox:
                xminimum 800
                xmaximum 800
                spacing 50
                label _("Text Speed") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                bar value Preference("text speed") style "my_bar" xoffset -20

            hbox:
                xminimum 800
                xmaximum 800
                spacing 50
                label _("Auto-Forward Time") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                bar value Preference("auto-forward time") style "my_bar" xoffset -20

            hbox:
                xminimum 800
                xmaximum 800
                spacing 50
                label _("Text box opacity") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                bar value FieldValue(persistent, "say_window_alpha", range=1.0, style="slider") style "my_bar" xoffset -20

            vpgrid:
                xminimum 800
                xmaximum 800
                spacing 50
                cols 2
                rows 4


                label _("Text Box") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if persistent.default_text_box_mode:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                        action (SetVariable("persistent.default_text_box_mode",False),Function(pick_style_centered))
                    else:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                        action (SetVariable("persistent.default_text_box_mode",True),Function(pick_style_default))
                    xoffset -40

                label _("Skip Unseen Text") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if preferences.skip_unseen:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    action Preference("skip", "toggle")
                    xoffset -40

                label _("Skip After Choice") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if preferences.skip_after_choices:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    action Preference("after choices", "toggle")
                    xoffset -40

                label _("Skip Transitions") text_style "custom_menu_style_text" xminimum 300
                imagebutton:
                    if preferences.transitions:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    action Preference("transitions", "toggle")
                    xoffset -40








style qm_custom_style:
    font "fonts/candara.ttf"
    size 23
    yoffset 7
    xoffset 5
    color "#fe9416"
    outlines [ (0, "#2b2b2b", 1, 1) ]

style qm_custom_style_text_disabled:
    font "fonts/candara.ttf"
    size 23
    yoffset 7
    xoffset 5
    hover_color "#fe9416"
    color "#636363"
    outlines [ (0, "#2b2b2b", 1, 1) ]

screen preferences():
    tag menu


    use game_menu(_("")):

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 50
            xoffset 70
            yoffset -20

            hbox:
                xminimum 500
                xmaximum 500
                spacing 10
                yoffset 20
                label _("Display") text_style "custom_menu_style_text" yoffset 5
                imagebutton:
                    idle "gui/preferences/custom_menu_separator.png"
                    hover "gui/preferences/custom_menu_separator.png"
                    action NullAction()
                    xoffset -10
                if preferences.fullscreen:
                    textbutton _("Window") action Preference("display", "window") text_style "custom_menu_style_text2"
                    textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "custom_menu_style_text2_enabled"
                else:
                    textbutton _("Window") action Preference("display", "window") text_style "custom_menu_style_text2_enabled"
                    textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "custom_menu_style_text2"

            vpgrid:
                xminimum 900
                xmaximum 900
                spacing 60
                cols 2
                yoffset 30
                rows 5
                label _("Tutorials") text_style "custom_menu_style_text" xminimum 500
                imagebutton:
                    if tutorials:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    action (SetVariable("tutorials",not tutorials))
                    xoffset -40

                label _("Fast Travel Button") text_style "custom_menu_style_text" xminimum 500
                imagebutton:
                    if persistent.map_fast_travel:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                    action (SetVariable("persistent.map_fast_travel", not persistent.map_fast_travel))
                    xoffset -40

                if persistent.autosave:
                    label _("Autosave (Occasional Lag Spikes)") text_style "custom_menu_style_text" xminimum 500
                else:
                    label _("Autosave (No Lag Spikes)") text_style "custom_menu_style_text" xminimum 500
                imagebutton:
                    if persistent.autosave:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                        action (SetVariable("persistent.autosave",False),SetVariable("config.has_autosave",False))
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                        action (SetVariable("persistent.autosave",True),SetVariable("config.has_autosave",True))
                    xoffset -40

                if persistent.fx:
                    label _("Special effects (Better experience)") text_style "custom_menu_style_text" xminimum 500
                else:
                    label _("Special effects (Better performance)") text_style "custom_menu_style_text" xminimum 550
                imagebutton:
                    if persistent.fx:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                        action SetVariable("persistent.fx",False)
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                        action SetVariable("persistent.fx",True)
                    xoffset -40

                label _("Color blind accessible mini-games") text_style "custom_menu_style_text" xminimum 500
                imagebutton:
                    if persistent.colorblind:
                        idle "gui/preferences/custom_menu_box_idle.png"
                        hover "gui/preferences/custom_menu_box_hover.png"
                        action SetVariable("persistent.colorblind",False)
                    else:
                        idle "gui/preferences/custom_menu_box_empty_idle.png"
                        hover "gui/preferences/custom_menu_box_empty_hover.png"
                        action SetVariable("persistent.colorblind",True)
                    xoffset -40

            hbox:
                xminimum 800
                xmaximum 800
                spacing 10
                yoffset 20

                label _("Gallery buttons") text_style "custom_menu_style_text" yoffset 5
                imagebutton:
                    idle "gui/preferences/custom_menu_separator.png"
                    hover "gui/preferences/custom_menu_separator.png"
                    action NullAction()
                    xoffset -15
                if not persistent.rewards_screen_on_hover:
                    textbutton _("Enabled") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                    textbutton _("On Hover") action SetVariable("persistent.rewards_screen_on_hover",True) text_style "custom_menu_style_text2" xoffset -5
                else:
                    textbutton _("Enabled") action SetVariable("persistent.rewards_screen_on_hover",False) text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("On Hover") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5

            hbox:
                xminimum 800
                xmaximum 800
                spacing 10
                yoffset 20

                label _("Quick Menu") text_style "custom_menu_style_text" yoffset 5
                imagebutton:
                    idle "gui/preferences/custom_menu_separator.png"
                    hover "gui/preferences/custom_menu_separator.png"
                    action NullAction()
                    xoffset -15
                if persistent.quick_menu == 2:
                    textbutton _("Enabled") action SetVariable("persistent.quick_menu",2) text_style "custom_menu_style_text2_enabled" xoffset -5
                    textbutton _("On Hover") action SetVariable("persistent.quick_menu",1) text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Disabled") action SetVariable("persistent.quick_menu",0) text_style "custom_menu_style_text2" xoffset -5
                elif persistent.quick_menu == 1:
                    textbutton _("Enabled") action SetVariable("persistent.quick_menu",2) text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("On Hover") action SetVariable("persistent.quick_menu",1) text_style "custom_menu_style_text2_enabled" xoffset -5
                    textbutton _("Disabled") action SetVariable("persistent.quick_menu",0) text_style "custom_menu_style_text2" xoffset -5
                else:
                    textbutton _("Enabled") action SetVariable("persistent.quick_menu",2) text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("On Hover") action SetVariable("persistent.quick_menu",1) text_style "custom_menu_style_text2" xoffset -5
                    textbutton _("Disabled") action SetVariable("persistent.quick_menu",0) text_style "custom_menu_style_text2_enabled" xoffset -5

            hbox:
                spacing 20
                text "Customize Quick Menu" style "custom_menu_style_text"
                if persistent.qm_back:
                    textbutton _("Back") action (SetVariable("persistent.qm_back",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Back") action (SetVariable("persistent.qm_back",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_history:
                    textbutton _("History") action (SetVariable("persistent.qm_history",False)) text_style "qm_custom_style"
                else:
                    textbutton _("History") action (SetVariable("persistent.qm_history",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_skip:
                    textbutton _("Skip") action (SetVariable("persistent.qm_skip",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Skip") action (SetVariable("persistent.qm_skip",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_auto:
                    textbutton _("Auto") action (SetVariable("persistent.qm_auto",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Auto") action (SetVariable("persistent.qm_auto",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_save:
                    textbutton _("Save") action (SetVariable("persistent.qm_save",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Save") action (SetVariable("persistent.qm_save",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_qsave:
                    textbutton _("Q.Save") action (SetVariable("persistent.qm_qsave",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Q.Save") action (SetVariable("persistent.qm_qsave",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_qload:
                    textbutton _("Q.Load") action (SetVariable("persistent.qm_qload",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Q.Load") action (SetVariable("persistent.qm_qload",True)) text_style "qm_custom_style_text_disabled"
                if persistent.qm_prefs:
                    textbutton _("Prefs") action (SetVariable("persistent.qm_prefs",False)) text_style "qm_custom_style"
                else:
                    textbutton _("Prefs") action (SetVariable("persistent.qm_prefs",True)) text_style "qm_custom_style_text_disabled"
                if (steamConfig or nonPatreonConfig) and renpy.loadable("walkthrough/season1/walkthrough_season1.rpyc") or renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
                    if persistent.qm_guide:
                        textbutton _("Guide") action (SetVariable("persistent.qm_guide",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Guide") action (SetVariable("persistent.qm_guide",True)) text_style "qm_custom_style_text_disabled"

style pref_custom_style:
    font "fonts/candara.ttf"
    color "#858585"
    size 30

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_custom_selected:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_selected_foreground.png"

style check_button_custom_deselected:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():




    predict False tag menu

    use game_menu(_(""), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what color "#FFFFFF" style "custom_menu_style_text" xmaximum 1050 xoffset 300 yoffset 4

        if not _history_list:
            label _("The dialogue history is empty.") style "custom_menu_style_text"




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


image dlc_season1_btn:
    "season1_dlc_idle"
    on idle:
        "season1_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "season1_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "season1_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "season1_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_season2_btn:
    "season2_dlc2_idle"
    on idle:
        "season2_dlc2_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "season2_dlc2_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "season2_dlc2_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "season2_dlc2_hover" with Dissolve(0.1, alpha=True)

image dlc_season2_installed_btn:
    "season2_dlc_idle"
    on idle:
        "season2_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "season2_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "season2_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "season2_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_guide_season1_btn:
    "guide_season1_dlc_idle2"
    on idle:
        "guide_season1_dlc_idle2" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season1_dlc_hover2" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season1_dlc_idle2" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season1_dlc_hover2" with Dissolve(0.1, alpha=True)

image dlc_guide_season1_installed_btn:
    "guide_season1_dlc_idle"
    on idle:
        "guide_season1_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season1_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season1_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season1_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_guide_season2_btn2:
    "guide_season2_dlc_idle2"
    on idle:
        "guide_season2_dlc_idle2" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season2_dlc_hover2" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season2_dlc_idle2" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season2_dlc_hover2" with Dissolve(0.1, alpha=True)

image dlc_guide_season2_installed_btn:
    "guide_season2_dlc_idle"
    on idle:
        "guide_season2_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season2_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season2_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season2_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_guide_season3_btn2:
    "guide_season3_dlc_idle2"
    on idle:
        "guide_season3_dlc_idle2" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season3_dlc_hover2" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season3_dlc_idle2" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season3_dlc_hover2" with Dissolve(0.1, alpha=True)

image dlc_guide_season3_installed_btn:
    "guide_season3_dlc_idle"
    on idle:
        "guide_season3_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "guide_season3_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "guide_season3_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "guide_season3_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_seasonx_btn:
    "seasonx_dlc_idle"
    on idle:
        "seasonx_dlc_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "seasonx_dlc_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "seasonx_dlc_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "seasonx_dlc_hover" with Dissolve(0.1, alpha=True)

image dlc_seasonX_btn:
    "seasonx_dlc_idle"

image al_game_btn:
    "al_game_idle"
    on idle:
        "al_game_idle" with Dissolve(0.1, alpha=True)
    on hover:
        "al_game_hover" with Dissolve(0.1, alpha=True)
    on selected_idle:
        "al_game_idle" with Dissolve(0.1, alpha=True)
    on selected_hover:
        "al_game_hover" with Dissolve(0.1, alpha=True)

image seasonx_dlc_idle:
    "seasonx_dlc_idle1" with Dissolve(1, alpha=True)
    pause 1
    "seasonx_dlc_idle2" with Dissolve(1, alpha=True)
    pause 1
    repeat
image seasonx_dlc_hover:
    "seasonx_dlc_hover1" with Dissolve(1, alpha=True)
    pause 1
    "seasonx_dlc_hover2" with Dissolve(1, alpha=True)
    pause 1
    repeat

style dlc_style_text:
    font "fonts/Museo500.otf"
    size 50
    color "#ffffff"
    hover_color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]
    drop_shadow [(2, 2)]
    drop_shadow_color "#000000"

style dlc_style_text_installed:
    font "fonts/Museo500.otf"
    size 50
    color "#fe9416"
    hover_color "#fe9416"
    outlines [(1, "#ffffff", 0, 0)]
    hover_outlines [(1, "#ffffff", 0, 0)]
    drop_shadow [(2, 2)]
    drop_shadow_color "#000000"

screen dlc():

    modal True tag dlc
    add "spr_bg_ep3"
    add "spr_mid_ep3"
    add "spr_top_ep3"
    add "dlc_bg"

    imagebutton:
        xalign 0.98
        yalign 0.02
        idle "dlc_x_idle"
        hover "dlc_x_hover"
        action (Hide("dlc"), Show("main_menu"))

    vpgrid:
        ypos 0.06
        draggable False
        mousewheel False
        scrollbars "horizontal"
        rows 1
        hbox:
            yalign 0.65
            xalign 0.5
            vbox:
                button:
                    focus_mask True
                    add "dlc_season1_btn"
                    action Function(activate_overlay_to_store_badik)
                    xalign 0.5
                if persistent.steam_owns_badik:
                    text "In library" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                else:
                    text "Available now" style "dlc_style_text" xalign 0.5 yoffset -60
            vbox:
                button:
                    focus_mask True
                    if persistent.steam_owns_guide_s1:
                        add "dlc_guide_season1_installed_btn"
                    else:
                        add "dlc_guide_season1_btn"
                    action Function(activate_overlay_to_store_badik_s1_guide)
                    xalign 0.5
                if persistent.steam_owns_guide_s1:
                    text "In library" style "dlc_style_text" xalign 0.5 yoffset -60
                else:
                    text "Available now" style "dlc_style_text" xalign 0.5 yoffset -60

            vbox:
                button:
                    focus_mask True
                    if persistent.steam_owns_s2:
                        add "dlc_season2_installed_btn"
                    else:
                        add "dlc_season2_btn"
                    action Function(activate_overlay_to_store_badik_s2)
                    xalign 0.5
                if persistent.steam_owns_s2:
                    text "In library" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                else:
                    text "Available now" style "dlc_style_text" xalign 0.5 yoffset -60
            vbox:
                button:
                    focus_mask True
                    if persistent.steam_owns_guide_s2:
                        add "dlc_guide_season2_installed_btn"
                    else:
                        add "dlc_guide_season2_btn2"
                    action Function(activate_overlay_to_store_badik_s2_guide)
                    xalign 0.5
                if persistent.steam_owns_guide_s2:
                    text "In library" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                else:
                    text "Available now" style "dlc_style_text" xalign 0.5 yoffset -60
            vbox:
                button:
                    focus_mask True
                    add "dlc_season3_installed_btn"
                    action Function(activate_overlay_to_store_badik_s3)
                    xalign 0.5
                text "Installed" style "dlc_style_text_installed" xalign 0.5 yoffset -60
            vbox:
                button:
                    focus_mask True
                    if persistent.steam_owns_guide_s3:
                        add "dlc_guide_season3_installed_btn"
                    else:
                        add "dlc_guide_season3_btn2"
                    action Function(activate_overlay_to_store_badik_s3_guide)
                    xalign 0.5
                if persistent.steam_owns_guide_s3 and renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
                    text "Installed" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                elif persistent.steam_owns_guide_s3:
                    text "Not installed" style "dlc_style_text" xalign 0.5 yoffset -60
                else:
                    text "Available now" style "dlc_style_text" xalign 0.5 yoffset -60









            vbox:
                button:
                    focus_mask True
                    add "al_game_btn"
                    action Function(activate_overlay_to_store_al)
                    xalign 0.5
                if persistent.steam_owns_al:
                    text "In library" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                else:
                    text "Other game" style "dlc_style_text" xalign 0.5 yoffset -60
init python:
    def mmma_set_startup_song():
        global cco_music_list
        
        tmpBool = False
        for x in range(0,len(persistent.mphone_music_list)):
            if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                persistent.mm_song[0] = persistent.mphone_music_list[x][0]
                persistent.mm_song[1] = persistent.mphone_music_list[x][1]
                tmpBool = True
        if not tmpBool:
            for x in range(0,len(cco_music_list)):
                if renpy.music.get_playing() == cco_music_list[x][1]:
                    persistent.mm_song[0] = cco_music_list[x][0]
                    persistent.mm_song[1] = cco_music_list[x][1]
        savePersistentData()
        return
init:
    $ mmma_music_genre = 0
    if persistent.mm_song == None:
        $ persistent.mm_song = ["Dirty Toy Company - Over the Horizon","music/patched/track_previous.mp3"]
    $ dik_tips_list = []
    $ dik_tips_list.append("Did you know that you can hide the GUI buttons when viewing art in the Rewards app? In the Settings menu, set the Rewards app buttons option to \"On hover\" to enjoy the art without the buttons in your way.")
    $ dik_tips_list.append("Pressing 'h' will hide GUI elements. It's perfect when you want to take a screenshot. Speaking of screenshots, press the 's' key to snap one.")
    $ dik_tips_list.append("A recommended setting for better immersion is to change the Quick Menu to \"On hover\" in the Settings menu.")
    $ dik_tips_list.append("Remember that you can click the middle mouse button to quickly open and close your phone. It also closes apps.")
    $ dik_tips_list.append("Want to get the most out of your phone wallpaper? Hide the music bar in the Music app. Set \"Home screen bar\" to Hide and enjoy more of your chosen wallpaper.")
    $ dik_tips_list.append("You can randomize wallpapers on your phone when opening and closing the phone. Go to the Settings app and click \"Edit Wallpaper Settings\". Click the heart button on the wallpapers you like and change the setting to \"Rotate favorite wallpapers: Yes\".")
    $ dik_tips_list.append("Did you figure out how to find the Vault app digits yet? Keep a lookout for green-colored numbers when playing an episode.")
    $ dik_tips_list.append("Are you playing on a laptop without a scrollwheel? You might want to try setting \"Rollback side\" to either left or right in the Preferences > Dialogue menu. This allows you to simply click the left or right part of your screen to rollback the dialogue.")
    $ dik_tips_list.append("Are you having a hard time reading the dialogue? Enable the text box from the Preferences > Dialogue menu. You can also set the opacity of it from there. No more squinting while reading dialogue.")
    $ dik_tips_list.append("Want to speed through the dialogue faster? Go to the Preferences > Dialogue menu and enable \"Skip Unseen Text\", \"Skip After Choice\" and \"Skip Transitions\". While playing, either hold Control or press TAB key to fly through the dialogue.")
    $ dik_tips_list.append("If you are playing for a long time, it's recommended to click the \"Save collectibles\" button in the Save menu once in a while. This will save any unlockables you've unlocked. If your game crashes for any reason, any unlockables that haven't been saved are lost.")
    $ dik_tips_list.append("Did you know that you can set any song from this music menu as your startup song? Just click the \"Set current song as startup song\" button below while listening to your favorite song and it will play the next time you launch the game.")
    $ dik_tips_list.append("Make your own favorite list by clicking the heart buttons next to the songs. The favorite list will be used in all your playthroughs and is synchronized with this music menu. Neat, huh?")
    $ dik_tips_list.append("Did you realize that special renders can be found in normal scenes with dialogue now? Keep a lookout for magazines or books that highlight when you hover them.")
    $ dik_tips_list.append("If you want to change between windowed and fullscreen mode, just press the 'f' key.")
    $ dik_tips_list.append("If you don't like playing mini-games, you can disable them by starting a new game. This choice cannot be changed later on.")
    $ dik_tips_list.append("If you purchased the official guide on Steam or GOG, you can bring it up by pressing 'g'. If you get the active renderer menu instead of the guide, you have caps lock activated. If you're using a keyboard without English characters, you have to change the keyboard layout to English as well.")
    $ dik_tips_list.append("There is a difference between DIK status and affinity. An easy way to keep them separate is to think of the DIK status as your mood, and the affinity as your personality. The affinity is shaped by all major choices and the status is affected by some of the other choices you make.")
    $ dik_tips_list.append("The girls in the game have different values and may or may not be attracted to you based on your choices. Can you resist the temptations along the way to get the girl of your dreams or will you relent and just...experiment? Hey, it's college, after all!")
    $ dik_tips_list.append("Did you know that the development of Being a DIK started in 2018? The entire story has been planned in advance, but the pacing is set on a per-episode basis.")
    $ dik_tips_list.append("Jill was the last main girl that was designed and added to the game. Fun fact, at the end of Acting Lessons there is a promo for Being a DIK that doesn't include Jill in the banner.")
    $ dik_tips_list.append("Did you know that Season 3 is not the last season? A fourth season has been confirmed.")
    $ dik_tips_list.append("When you order art from Jacob's art shop, it will unlock at the beginning of a later free roam event. He will send you a text message when the art is unlocked.")
    $ dik_tips_list.append("If you can't figure out which 2D art in the Rewards app you haven't unlocked, open the 2D art app on your phone and click through the different girls to find out if you didn't buy one of their art pieces.")
    $ dik_tips_list.append("You cannot unlock all of the art in Jacob's art shop yet. More art gets added with every new episode.")
    $ dik_tips_list.append("If you can't remember which choices you've made on your current save, open the Bios app and browse through the different characters. Your main character's bio includes many choices, including major choices.")
    $ dik_tips_list.append("Planning parties is not easy! Did you know that the different party activities unlock different events during the parties? Try different combinations to design the party you want.")
    $ dik_tips_list.append("Which party planning strategy is the best? There are many ways you can win the mini-game. Always try to satisfy joint needs at the same time and think before you purchase any item. Think long-term about the perks and it can be smart to increase the starting items of every kind.")
    $ dik_tips_list.append("If you need more save pages, you can click the arrows at the bottom of the save menu to get more. Don't forget to name your save pages by clicking the page title.")
    $ dik_tips_list.append("Did you know that you can view your sexual history from the Girls tab in the Stats app? Click any girl to filter events for her. It's a neat tool for when you want to find out what you did with someone in the past.")
    $ dik_tips_list.append("Starting episode 10, you can create your custom wallpaper from a special gallery on your phone.")


    $ dik_tip_int = renpy.random.randint(0, len(dik_tips_list)-1)

    $ cco_music_list = []
    $ cco_music_list.append(["A to Z guitars - Slow day blues","music/ep1/slow_day_blues.mp3"])
    $ cco_music_list.append(["Absentrealities - 03 Three's a crowd","music/ep1/threes_a_crowd.mp3"])
    $ cco_music_list.append(["Absentrealities - 04 Surf punk rock","music/ep1/surf_punk_rock.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Adventure","music/ep6/adventure2.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Blood And Steel","music/ep6/blood_and_steel.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Freedom","music/ep2/freedom.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Journey of hope","music/ep2/journey_of_hope.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Jack the Lumberer","music/ep4/jack_the_lumberer.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Medieval Loop One","music/ep6/medieval_loop_one.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Medieval Loop Two","music/ep6/medieval_loop_two.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Medieval Loop Three","music/ep6/medieval_loop_three.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Reaching the sky","music/ep2/reaching_the_sky.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Relaxing ballad","music/ep2/relaxing_ballad.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Rustic ballad","music/ep5/rustic_ballad.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Simple Ballad","music/ep2/simple_ballad.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Skeleton Keys","music/ep6/skeleton_keys.mp3"])
    $ cco_music_list.append(["Alexander Nakarada -  Spring in Russia","music/ep3/spring_in_russia.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - The crown","music/ep6/the_crown.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Uplifting ballad","music/ep6/uplifting_ballad.mp3"])
    $ cco_music_list.append(["Alexander Nakarada - Winter","music/ep2/winter.mp3"])
    $ cco_music_list.append(["Arlindo Detomi - STRYV Surge (Ivory Remix)","music/ep2/stryv.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Driving Rock","music/ep4/driving_rock.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Energetic","music/ep1/energetic.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Inspiring Acoustic Guitar","music/ep5/inspiring.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Inspirational Piano Ambient","music/ep4/inspirational_piano_ambient.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Inspiring Acoustic","music/ep4/inspiring_acoustic.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Optimistic","music/ep4/optimistic.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Piano Cinematic","music/ep4/piano_cinematic.mp3"])
    $ cco_music_list.append(["AShamaluevMusic - Romantic Piano","music/ep4/romantic_piano.mp3"])
    $ cco_music_list.append(["Bare weed - Cosmos","music/ep4/cosmos.mp3"])
    $ cco_music_list.append(["Bellsmarie - Just Peachy (Original)","music/ep4/just_peachy.mp3"])
    $ cco_music_list.append(["Chriszornstudios - Art nouveau","music/ep1/art_nouveau.mp3"])
    $ cco_music_list.append(["Chrys Guth - Metal","music/ep2/metal.mp3"])
    $ cco_music_list.append(["Chukura - Lonely","music/ep1/lonely.mp3"])
    $ cco_music_list.append(["Daniel Couper - Wise old river (Acoustic version)","music/ep6/wise_old_river.mp3"])
    $ cco_music_list.append(["DarkMoloko - Adventure","music/ep6/adventure.mp3"])
    $ cco_music_list.append(["Desert sharks - Feel bad","music/ep2/feel_bad.mp3"])
    $ cco_music_list.append(["Ds'Air - Jingle","music/ep2/jingle.mp3"])
    $ cco_music_list.append(["Emily Ventre - All of the pieces","music/ep4/all_of_the_pieces.mp3"])
    $ cco_music_list.append(["Free Royalty Free Music - Metal","music/ep2/metal2.mp3"])
    $ cco_music_list.append(["Ghostrifter Official - Merry Bay","music/ep4/merry_bay.mp3"])
    $ cco_music_list.append(["Ghostrifter Official - Midnight Stroll","music/ep4/midnight_stroll.mp3"])
    $ cco_music_list.append(["Ghostrifter Official - Morning Routine","music/ep7/morning_routine.mp3"])
    $ cco_music_list.append(["Ghostrifter Official - Subtle Break","music/ep5/subtle_break.mp3"])
    $ cco_music_list.append(["HodgeY - Unknown power","music/ep1/unknown_power.mp3"])
    $ cco_music_list.append(["HoliznaCC0 - Halloween","music/ep9/halloween.mp3"])
    $ cco_music_list.append(["Hyde - Acoustic/Pop/Rock/Alternative","music/ep1/apra_hyde.mp3"])
    $ cco_music_list.append(["Hyde - 60s & 70s Rock","music/ep4/fleetwood.mp3"])
    $ cco_music_list.append(["Hyde - Drum&Bass Rock","music/ep4/drum_bass.mp3"])
    $ cco_music_list.append(["Hyde - Mumford & Sons Inspired","music/ep1/mumford.mp3"])
    $ cco_music_list.append(["Jantrax - Good old days","music/ep7/good_old_days.mp3"])
    $ cco_music_list.append(["Jantrax - Rio","music/ep5/rio.mp3"])
    $ cco_music_list.append(["Jantrax - Second chance","music/ep5/second_chance.mp3"])
    $ cco_music_list.append(["Jet Voon - Roads (Original Mix)","music/ep3/roads.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Anachronist","music/ep1/anachronist.mp3"])
    $ cco_music_list.append(["Kevin Macleod - First call","music/ep2/first_call.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Fluffing a Duck","music/ep4/fluffing_a_duck.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Marty Gots A Plan","music/ep2/marty.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Octoblues","music/ep1/octoblues.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Radio Martini","music/ep1/radio_martini.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Sing along with Jim","music/ep3/sing_along_with_jim.mp3"])
    $ cco_music_list.append(["Kevin Macleod - Windswept","music/ep1/windswept.mp3"])
    $ cco_music_list.append(["Loudtech - Chill","music/ep3/chill.mp3"])
    $ cco_music_list.append(["Mason Carter Music - Acoustic","music/ep2/acoustic.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - Don't count on me","music/ep1/dont_count_on_me.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - EmptyV","music/ep1/emptyv.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - Faked Reality","music/ep10/faked_reality.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - Isolation","music/ep10/isolation.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - See You Smile","music/ep10/see_you_smile.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - This silence","music/ep1/this_silence.mp3"])
    $ cco_music_list.append(["Melodic In Fusion - Time goes by","music/ep1/time_goes_by.mp3"])
    $ cco_music_list.append(["Meizong - Fallen Colors (Original Mix)","music/ep2/fallen_colors.mp3"])
    $ cco_music_list.append(["Meizong - Night Lights (Original Mix)","music/ep2/night_lights.mp3"])
    $ cco_music_list.append(["Meizong - No Comments (Original Mix)","music/ep8/no_comments.mp3"])
    $ cco_music_list.append(["Meizong - Phate (Original Mix)","music/ep2/phate.mp3"])
    $ cco_music_list.append(["Meizong - Raveyard (Original Mix)","music/ep3/raveyard.mp3"])
    $ cco_music_list.append(["Meizong & Yeeflex - Reaching Halo","music/ep4/reaching_halo.mp3"])
    $ cco_music_list.append(["Meizong (Argofox) - Skyline (Original Mix)","music/ep2/skyline.mp3"])
    $ cco_music_list.append(["Meizong - Starfire (Original Mix)","music/ep8/starfire.mp3"])
    $ cco_music_list.append(["Meizong - The heat (Original Mix)","music/ep4/the_heat.mp3"])
    $ cco_music_list.append(["Mironov Sound - Funk rock instrumental","music/ep1/funk_rock.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - By your side","music/ep2/by_your_side.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Golden Alley","music/ep1/golden_alley.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Let's Begin","music/ep3/lets_begin.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Lost Souls","music/ep1/lost_souls.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Never give up","music/ep1/never_give_up.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Roadtrip","music/ep1/roadtrip.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Rockin' Riff","music/ep2/rockin_riff.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Someways","music/ep1/someways.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Sunny acoustic rock","music/ep3/sunny_acoustic_rock.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Wings","music/ep2/wings.mp3"])
    $ cco_music_list.append(["Nicolai Heidlas - Winter Sunshine","music/ep1/winter_sunshine.mp3"])
    $ cco_music_list.append(["Oskar Hill & Meizong - The Sound Of Summer","music/ep2/sound_of_summer.mp3"])
    $ cco_music_list.append(["PeriTune - Gentle theme2 Guitar","music/ep4/gentle_theme_guitar.mp3"])
    $ cco_music_list.append(["PeriTune - Gentle theme2 MusicBox","music/ep7/musicbox.mp3"])
    $ cco_music_list.append(["PeriTune - Gentle theme2 Piano","music/ep3/gentle_theme_piano.mp3"])
    $ cco_music_list.append(["PeriTune - Guitar gentle","music/ep3/guitar_gentle.mp3"])
    $ cco_music_list.append(["PeriTune - Guitar melancholy","music/ep4/guitar_melancholy.mp3"])
    $ cco_music_list.append(["PeriTune - Guitar melancholy2","music/ep3/guitar_melancholy2.mp3"])
    $ cco_music_list.append(["PeriTune - Suspense5","music/ep5/suspense5.mp3"])
    $ cco_music_list.append(["Punk rock mashed up - Classicals breakbeat","music/ep1/classicals_breakbeat.mp3"])
    $ cco_music_list.append(["Ryan Pollard TK-473 - Heavy","music/ep2/heavy.mp3"])
    $ cco_music_list.append(["Ryansyah R. Poetra - Credits","music/ep1/credits.mp3"])
    $ cco_music_list.append(["Sean Danielsen - Food chain","music/ep1/food_chain.mp3"])
    $ cco_music_list.append(["Silent Partner - Black box","music/ep3/black_box.mp3"])
    $ cco_music_list.append(["Silent Partner - DC love Go-Go","music/ep3/dc_love_go_go.mp3"])
    $ cco_music_list.append(["Silent Partner - Get back","music/ep3/get_back.mp3"])
    $ cco_music_list.append(["Silent Partner - Let her in","music/ep4/let_her_in.mp3"])
    $ cco_music_list.append(["Silent Partner - Scrapbook","music/ep1/scrapbook.mp3"])
    $ cco_music_list.append(["Silent Partner - Some obsession","music/ep3/some_obsession.mp3"])
    $ cco_music_list.append(["S Strong - Hot mustard","music/ep3/hot_mustard.mp3"])
    $ cco_music_list.append(["Summertime - My heart","music/ep1/my_heart.mp3"])
    $ cco_music_list.append(["Steven O'Brien - Slavic battle theme","music/ep3/slavic_battle_theme.mp3"])
    $ cco_music_list.append(["The Night - Down","music/ep5/down.mp3"])
    $ cco_music_list.append(["The Night - Medicate me","music/ep5/medicate_me.mp3"])
    $ cco_music_list.append(["The Sisonpyh - Relax","music/ep4/relax.mp3"])
    $ cco_music_list.append(["The Zombie Dandies - Halloween Again","music/ep9/halloween_again.mp3"])
    $ cco_music_list.append(["The Zombie Dandies - The Friendly Monster Shop","music/ep9/the_friendly_monster_shop.mp3"])
    $ cco_music_list.append(["TRow - Acoustic guitar arrangement","music/ep1/trow.mp3"])
    $ cco_music_list.append(["Valtteri Kujala - Your Smile","music/ep1/your_smile.mp3"])
    $ cco_music_list.append(["Wayne John Bradley - Fresh Air","music/ep1/fresh_air.mp3"])
    $ cco_music_list.append(["Wova - They Say","music/ep1/they_say.mp3"])

screen mmma_minimized_screen:

    modal True tag mmma_minimized_screen
    imagebutton:
        idle "big_invis"
        hover "big_invis"
        action (Hide("mmma_minimized_screen"), Show("music_credits"))

screen music_credits():


    modal True tag music_credits
    add "mmma_bg"
    timer 2 repeat True action SetVariable("tmpMusicInt",0)
    imagebutton:
        idle "dlc_x_idle"
        hover "dlc_x_hover"
        action (SetVariable("musicCreditsOpen",False),Hide("music_credits"))
        xalign 0.98
        yalign 0.02


    text "{color=ffed00}{u}Genre{/u}{/color}" style "mmma_style_header_style" xalign 0.025 yalign 0.2

    vbox:
        xalign 0.03
        yalign 0.5
        spacing 35
        textbutton "All" text_style "mmma_button_style" action SetVariable("mmma_music_genre",0)
        textbutton "Rock" text_style "mmma_button_style" action SetVariable("mmma_music_genre",1)
        textbutton "Party" text_style "mmma_button_style" action SetVariable("mmma_music_genre",2)
        textbutton "Relaxing" text_style "mmma_button_style" action SetVariable("mmma_music_genre",3)
        textbutton "Favorites" text_style "mmma_button_style" action SetVariable("mmma_music_genre",4)
        textbutton "CC0" text_style "mmma_button_style" action SetVariable("mmma_music_genre",5)


    hbox:
        xalign 0.2
        yalign 0.02
        if mmma_music_genre == 0:
            text "All songs" style "mmma_style_header_style"
        elif mmma_music_genre == 1:
            text "Rock songs" style "mmma_style_header_style"
        elif mmma_music_genre == 2:
            text "Party songs" style "mmma_style_header_style"
        elif mmma_music_genre == 3:
            text "Relaxing songs" style "mmma_style_header_style"
        elif mmma_music_genre == 4:
            text "Favorites" style "mmma_style_header_style"
        else:
            text "CC0" style "mmma_style_header_style"

    if mmma_music_genre == 5:
        text "{size=-25}{color=ffed00}Creative commons license for commercial use{/color}{/size}" style "mmma_style_header_style" xalign 0.325 yalign 0.043
        textbutton "View license" text_style "mmma_button_style" xalign 0.57 yalign 0.03 action OpenURL("https://creativecommons.org/licenses/by-sa/3.0/")


    vbox:
        xalign 0.94
        yalign 0.18
        xminimum 400
        xmaximum 400
        hbox:
            spacing 10
            text "{color=fe9416}DIK tip #%d{/color}" % (dik_tip_int+1) style "mmma_dik_tip_style" yoffset 7
            textbutton "Previous tip" text_style "mmma_dik_tip_button_style":
                if dik_tip_int - 1 >= 0:
                    action SetVariable("dik_tip_int",dik_tip_int-1)
                else:
                    action SetVariable("dik_tip_int",len(dik_tips_list)-1)
            textbutton "Next tip" text_style "mmma_dik_tip_button_style":
                if dik_tip_int + 1 < len(dik_tips_list):
                    action SetVariable("dik_tip_int",dik_tip_int+1)
                else:
                    action SetVariable("dik_tip_int",0)

    vbox:
        xalign 0.94
        yalign 0.255
        xminimum 400
        xmaximum 400
        text "%s" % dik_tips_list[dik_tip_int] style "mmma_dik_tip_style"

    hbox:
        xalign 0.25
        yalign .955
        xminimum 800
        xmaximum 800
        spacing 15
        imagebutton:
            yalign 0.5
            idle "mphone_music_play_active_idle"
            hover "mphone_music_play_active_idle"
            action NullAction()
        $ tmpBool = False
        hbox:
            yalign 0.5
            xminimum 740
            xmaximum 740
            for x in range(0,len(persistent.mphone_music_list)):
                if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                    text "%s" % persistent.mphone_music_list[x][0] style "mmma_style_header_style2"
                    $ tmpBool = True
            if not tmpBool:
                for x in range(0,len(cco_music_list)):
                    if renpy.music.get_playing() == cco_music_list[x][1]:
                        text "%s" % cco_music_list[x][0] style "mmma_style_header_style2"
                    $ tmpBool = True
            if not tmpBool:
                text "-" style "mmma_style_header_style2"
                text "-" style "mmma_style_header_style2"

    hbox:
        xalign 0.65
        yalign .95

        if mphone_music_genre == 4:
            textbutton "Play: Favorites" text_style "mmma_text_button_style" action (SetVariable("mphone_music_genre",0),Function(mphone_next_song))
        elif mphone_music_genre == 3:
            textbutton "Play: Relaxing songs" text_style "mmma_text_button_style" action (SetVariable("mphone_music_genre",4),Function(mphone_next_song))
        elif mphone_music_genre == 2:
            textbutton "Play: Party songs" text_style "mmma_text_button_style" action (SetVariable("mphone_music_genre",3),Function(mphone_next_song))
        elif mphone_music_genre == 1:
            textbutton "Play: Rock songs" text_style "mmma_text_button_style" action (SetVariable("mphone_music_genre",2),Function(mphone_next_song))
        else:
            textbutton "Play: Shuffle all" text_style "mmma_text_button_style" action (SetVariable("mphone_music_genre",1),Function(mphone_next_song))

    hbox:
        xalign 0.92
        yalign .955
        hbox:
            spacing 20
            imagebutton:
                yalign 0.5
                idle "mphone_music_bar_next_button_idle"
                hover "mphone_music_bar_next_button_hover"
                action Function(mphone_next_song)
            hbox:
                imagebutton:
                    yalign 0.5
                    if _preferences.get_volume('music') > 0:
                        idle "mphone_music_bar_sound"
                        hover "mphone_music_bar_sound"
                    else:
                        idle "mphone_music_bar_mute"
                        hover "mphone_music_bar_mute"
                    action NullAction()
                bar value Preference("music volume") style 'my_bar' yalign 0.5 xmaximum 300


    vbox:
        xminimum 660
        xmaximum 660
        xalign 1.0
        xoffset 40
        yalign 0.7
        textbutton "Minimize Music app" text_style "mmma_style_button_style2" action (Show("mmma_minimized_screen"), Hide("music_credits")) xoffset -7 yoffset 5
    vbox:
        xminimum 660
        xmaximum 660
        xalign 1.0
        xoffset 40
        yalign 0.82
        text "{color=#ffed00}Startup song: %s{/color}" % persistent.mm_song[0] style "mmma_style_header_style3"
        textbutton "Set current song as startup song" text_style "mmma_style_button_style2" action Function(mmma_set_startup_song) xoffset -7 yoffset 5
        textbutton "Reset startup song" text_style "mmma_style_button_style2" action (SetDict(persistent.mm_song, 0, "Dirty Toy Company - Over the Horizon"), SetDict(persistent.mm_song, 1, "music/patched/track_previous.mp3")) xoffset -7 yoffset 5

    fixed:
        vpgrid:
            xminimum 996
            xmaximum 996
            yminimum 833
            ymaximum 833
            xalign 0.3
            yalign 0.45

            cols 1
            draggable False
            mousewheel True
            scrollbars "vertical"

            $ tmpInt = 0
            for x in range(0,len(persistent.mphone_music_list)):
                if mmma_music_genre == 0 or (persistent.mphone_music_list[x][3] == mmma_music_genre) or (persistent.mphone_music_list[x][2] and mmma_music_genre == 4):
                    hbox:
                        yalign 0.5
                        xminimum 996 xmaximum 996
                        hbox:
                            yalign 0.5
                            spacing 15
                            imagebutton:
                                yalign 0.5
                                if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                                    idle "mphone_music_play_active_idle"
                                    hover "mphone_music_play_active_hover"
                                else:
                                    idle "mphone_music_play_inactive_idle"
                                    hover "mphone_music_play_inactive_hover"
                                action Function(mphone_play_song, persistent.mphone_music_list[x][1])
                            if persistent.mphone_music_list[x][2]:
                                imagebutton:
                                    yalign 0.5
                                    idle "mphone_fav_active_idle"
                                    hover "mphone_fav_active_hover"
                                    action SetDict(persistent.mphone_music_list[x],2,False)
                            else:
                                imagebutton:
                                    yalign 0.5
                                    idle "mphone_fav_inactive_idle"
                                    hover "mphone_fav_inactive_hover"
                                    action SetDict(persistent.mphone_music_list[x],2,True)
                        hbox:
                            yalign 0.5
                            xoffset 30
                            xminimum 760 xmaximum 760
                            $ tmpList = persistent.mphone_music_list[x][0].split(" - ", 1)

                            if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "{color=#fe9416}%s{/color}" % tmpList[1] style "mmma_song_style" yalign 0.5
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "{color=#fe9416}%s{/color}" % tmpList[0] style "mmma_song_style" yalign 0.5
                            else:
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "%s" % tmpList[1] style "mmma_song_style" yalign 0.5
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "%s" % tmpList[0] style "mmma_song_style" yalign 0.5
                    $ tmpInt += 1
            if mmma_music_genre == 5:
                for x in range(0,len(cco_music_list)):
                    hbox:
                        yalign 0.5
                        xminimum 996 xmaximum 996
                        hbox:
                            yalign 0.5
                            spacing 15
                            imagebutton:
                                yalign 0.5
                                if renpy.music.get_playing() == cco_music_list[x][1]:
                                    idle "mphone_music_play_active_idle"
                                    hover "mphone_music_play_active_hover"
                                else:
                                    idle "mphone_music_play_inactive_idle"
                                    hover "mphone_music_play_inactive_hover"
                                action Function(mphone_play_song, cco_music_list[x][1])

                        hbox:
                            yalign 0.5
                            xoffset 30
                            xminimum 760 xmaximum 760
                            $ tmpList = cco_music_list[x][0].split(" - ", 1)

                            if renpy.music.get_playing() == cco_music_list[x][1]:
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "{color=#fe9416}%s{/color}" % tmpList[1] style "mmma_song_style" yalign 0.5
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "{color=#fe9416}%s{/color}" % tmpList[0] style "mmma_song_style" yalign 0.5
                            else:
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "%s" % tmpList[1] style "mmma_song_style" yalign 0.5
                                vbox:
                                    xminimum 380 xmaximum 380
                                    text "%s" % tmpList[0] style "mmma_song_style" yalign 0.5

            if mmma_music_genre == 4 and tmpInt < 17:
                if tmpInt == 0:
                    for x in range(0,21):
                        hbox:
                            yalign 0.5
                            xminimum 996 xmaximum 996
                            text " "
                else:
                    for x in range(0,17-tmpInt):
                        hbox:
                            yalign 0.5
                            xminimum 996 xmaximum 996
                            text " "



style mmma_song_style:
    font "fonts/centurygothicregular.ttf"
    size 20
    color "#ffffff"

style mmma_dik_tip_style:
    font "fonts/centurygothicregular.ttf"
    size 20
    color "#ffffff"
style mmma_dik_tip_button_style:
    font "fonts/centurygothicregular.ttf"
    size 20
    color "#ffffff"
    hover_color "#fe9416"
style mmma_style_header_style:
    font "fonts/centurygothicregular.ttf"
    size 45
    color "#ffffff"
style mmma_style_header_style2:
    font "fonts/centurygothicregular.ttf"
    size 30
    color "#ffed00"

style mmma_style_header_style3:
    font "fonts/centurygothicregular.ttf"
    size 18
    color "#ffffff"

style mmma_style_button_style2:
    font "fonts/centurygothicregular.ttf"
    size 18
    color "#ffffff"
    hover_color "#fe9416"

style mmma_button_style:
    font "fonts/centurygothicregular.ttf"
    size 30
    color "#ffffff"
    hover_color "#fe9416"
    selected_color "#fe9416"

style mmma_text_button_style:
    font "fonts/centurygothicregular.ttf"
    size 20
    color "#ffffff"
    hover_color "#fe9416"
    selected_color "#fe9416"

screen music_credits_old():
    add "music_credits_bg"
    imagebutton:
        focus_mask True
        idle Transform("music_credits_header")
        hover Transform("music_credits_header")
        action NullAction()
        xpos 570
        ypos 10

    imagebutton:
        focus_mask None
        idle Transform("license_btn")
        hover Transform("license_btn_hover")
        action OpenURL("https://creativecommons.org/licenses/by-sa/3.0/")
        xpos 1100
        ypos 93

    vpgrid:
        xpos 900
        yfill True
        xmaximum 600
        xminimum 600
        ypos 170
        ymaximum 750
        yminimum 750
        cols 4
        spacing 15
        draggable False
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.502
        vbox xalign 0 yalign 0:
            textbutton "A to Z guitars - Slow day blues" text_style "music_button_text2" action Play('music',"music/ep1/slow_day_blues.mp3", True)
            textbutton "Absentrealities - 03 Three's a crowd" text_style "music_button_text2" action Play('music',"music/ep1/threes_a_crowd.mp3", True)
            textbutton "Absentrealities - 04 Surf punk rock" text_style "music_button_text2" action Play('music',"music/ep1/surf_punk_rock.mp3", True)
            textbutton "Alexander Nakarada - Adventure" text_style "music_button_text2" action Play('music',"music/ep6/adventure2.mp3", True)
            textbutton "Alexander Nakarada - Blood And Steel" text_style "music_button_text2" action Play('music',"music/ep6/blood_and_steel.mp3", True)
            textbutton "Alexander Nakarada - Freedom" text_style "music_button_text2" action Play('music',"music/ep2/freedom.mp3", True)
            textbutton "Alexander Nakarada - Journey of hope" text_style "music_button_text2" action Play('music',"music/ep2/journey_of_hope.mp3", True)
            textbutton "Alexander Nakarada - Jack the Lumberer" text_style "music_button_text2" action Play('music',"music/ep4/jack_the_lumberer.mp3", True)
            textbutton "Alexander Nakarada - Medieval Loop One" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_one.mp3", True)
            textbutton "Alexander Nakarada - Medieval Loop Two" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_two.mp3", True)
            textbutton "Alexander Nakarada - Medieval Loop Three" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_three.mp3", True)
            textbutton "Alexander Nakarada - Reaching the sky" text_style "music_button_text2" action Play('music',"music/ep2/reaching_the_sky.mp3", True)
            textbutton "Alexander Nakarada - Relaxing ballad" text_style "music_button_text2" action Play('music',"music/ep2/relaxing_ballad.mp3", True)
            textbutton "Alexander Nakarada - Rustic ballad" text_style "music_button_text2" action Play('music',"music/ep5/rustic_ballad.mp3", True)
            textbutton "Alexander Nakarada - Simple Ballad" text_style "music_button_text2" action Play('music',"music/ep2/simple_ballad.mp3", True)
            textbutton "Alexander Nakarada - Skeleton Keys" text_style "music_button_text2" action Play('music',"music/ep6/skeleton_keys.mp3", True)
            textbutton "Alexander Nakarada -  Spring in Russia" text_style "music_button_text2" action Play('music',"music/ep3/spring_in_russia.mp3", True)
            textbutton "Alexander Nakarada - The crown" text_style "music_button_text2" action Play('music',"music/ep6/the_crown.mp3", True)
            textbutton "Alexander Nakarada - Uplifting ballad" text_style "music_button_text2" action Play('music',"music/ep6/uplifting_ballad.mp3", True)
            textbutton "Alexander Nakarada - Winter" text_style "music_button_text2" action Play('music',"music/ep2/winter.mp3", True)
            textbutton "Arlindo Detomi - STRYV Surge (Ivory Remix)" text_style "music_button_text2" action Play('music',"music/ep2/stryv.mp3", True)
            textbutton "AShamaluevMusic - Driving Rock" text_style "music_button_text2" action Play('music',"music/ep4/driving_rock.mp3", True)
            textbutton "AShamaluevMusic - Energetic" text_style "music_button_text2" action Play('music',"music/ep1/energetic.mp3", True)
            textbutton "AShamaluevMusic - Inspiring Acoustic Guitar and Choir" text_style "music_button_text2" action Play('music',"music/ep5/inspiring.mp3", True)
            textbutton "AShamaluevMusic - Inspirational Piano Ambient" text_style "music_button_text2" action Play('music',"music/ep4/inspirational_piano_ambient.mp3", True)
            textbutton "AShamaluevMusic - Inspiring Acoustic" text_style "music_button_text2" action Play('music',"music/ep4/inspiring_acoustic.mp3", True)
            textbutton "AShamaluevMusic - Optimistic" text_style "music_button_text2" action Play('music',"music/ep4/optimistic.mp3", True)
            textbutton "AShamaluevMusic - Piano Cinematic" text_style "music_button_text2" action Play('music',"music/ep4/piano_cinematic.mp3", True)
            textbutton "AShamaluevMusic - Romantic Piano" text_style "music_button_text2" action Play('music',"music/ep4/romantic_piano.mp3", True)
            textbutton "Bare weed - Cosmos" text_style "music_button_text2" action Play('music',"music/ep4/cosmos.mp3", True)
            textbutton "Bellsmarie - Just Peachy (Original)" text_style "music_button_text2" action Play('music',"music/ep4/just_peachy.mp3", True)
            textbutton "Chriszornstudios - Art nouveau" text_style "music_button_text2" action Play('music',"music/ep1/art_nouveau.mp3", True)
            textbutton "Chrys Guth - Metal" text_style "music_button_text2" action Play('music',"music/ep2/metal.mp3", True)
            textbutton "Chukura - Lonely" text_style "music_button_text2" action Play('music',"music/ep1/lonely.mp3", True)
            textbutton "Daniel Couper - Wise old river (Acoustic version)" text_style "music_button_text2" action Play('music',"music/ep6/wise_old_river.mp3", True)
            textbutton "DarkMoloko - Adventure" text_style "music_button_text2" action Play('music',"music/ep6/adventure.mp3", True)
            textbutton "Desert sharks - Feel bad" text_style "music_button_text2" action Play('music',"music/ep2/feel_bad.mp3", True)
            textbutton "Ds'Air - Jingle" text_style "music_button_text2" action Play('music',"music/ep2/jingle.mp3", True)
            textbutton "Emily Ventre - All of the pieces" text_style "music_button_text2" action Play('music',"music/ep4/all_of_the_pieces.mp3", True)
            textbutton "Free Royalty Free Music - Metal" text_style "music_button_text2" action Play('music',"music/ep2/metal2.mp3", True)
            textbutton "Ghostrifter Official - Merry Bay" text_style "music_button_text2" action Play('music',"music/ep4/merry_bay.mp3", True)
            textbutton "Ghostrifter Official - Midnight Stroll" text_style "music_button_text2" action Play('music',"music/ep4/midnight_stroll.mp3", True)
            textbutton "Ghostrifter Official - Morning Routine" text_style "music_button_text2" action Play('music',"music/ep7/morning_routine.mp3", True)
            textbutton "Ghostrifter Official - Subtle Break" text_style "music_button_text2" action Play('music',"music/ep5/subtle_break.mp3", True)
            textbutton "HodgeY - Unknown power" text_style "music_button_text2" action Play('music',"music/ep1/unknown_power.mp3", True)
            textbutton "HoliznaCC0 - Halloween" text_style "music_button_text2" action Play('music',"music/ep9/halloween.mp3", True)
            textbutton "Hyde - Acoustic/Pop/Rock/Alternative" text_style "music_button_text2" action Play('music',"music/ep1/apra_hyde.mp3", True)
            textbutton "Hyde - 60s & 70s Rock Fleetwood Mac Inspired Instrumental" text_style "music_button_text2" action Play('music',"music/ep4/fleetwood.mp3", True)
            textbutton "Hyde - Drum&Bass Rock Pendulum Inspired Instrumental" text_style "music_button_text2" action Play('music',"music/ep4/drum_bass.mp3", True)
            textbutton "Hyde - Mumford & Sons Inspired" text_style "music_button_text2" action Play('music',"music/ep1/mumford.mp3", True)
            textbutton "Jantrax - Good old days" text_style "music_button_text2" action Play('music',"music/ep7/good_old_days.mp3", True)
            textbutton "Jantrax - Rio" text_style "music_button_text2" action Play('music',"music/ep5/rio.mp3", True)
            textbutton "Jantrax - Second chance" text_style "music_button_text2" action Play('music',"music/ep5/second_chance.mp3", True)
            textbutton "Jet Voon - Roads (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep3/roads.mp3", True)
            textbutton "Kevin Macleod - Anachronist" text_style "music_button_text2" action Play('music',"music/ep1/anachronist.mp3", True)
            textbutton "Kevin Macleod - First call" text_style "music_button_text2" action Play('music',"music/ep2/first_call.mp3", True)
            textbutton "Kevin Macleod - Fluffing a Duck" text_style "music_button_text2" action Play('music',"music/ep4/fluffing_a_duck.mp3", True)
            textbutton "Kevin Macleod - Marty Gots A Plan" text_style "music_button_text2" action Play('music',"music/ep2/marty.mp3", True)
            textbutton "Kevin Macleod - Octoblues" text_style "music_button_text2" action Play('music',"music/ep1/octoblues.mp3", True)
            textbutton "Kevin Macleod - Radio Martini" text_style "music_button_text2" action Play('music',"music/ep1/radio_martini.mp3", True)
            textbutton "Kevin Macleod - Sing along with Jim" text_style "music_button_text2" action Play('music',"music/ep3/sing_along_with_jim.mp3", True)
            textbutton "Kevin Macleod - Windswept" text_style "music_button_text2" action Play('music',"music/ep1/windswept.mp3", True)
            textbutton "Loudtech - Chill" text_style "music_button_text2" action Play('music',"music/ep3/chill.mp3", True)
            textbutton "Mason Carter Music - Acoustic" text_style "music_button_text2" action Play('music',"music/ep2/acoustic.mp3", True)
            textbutton "Melodic In Fusion - Don't count on me" text_style "music_button_text2" action Play('music',"music/ep1/dont_count_on_me.mp3", True)
            textbutton "Melodic In Fusion - EmptyV" text_style "music_button_text2" action Play('music',"music/ep1/emptyv.mp3", True)
            textbutton "Melodic In Fusion - This silence" text_style "music_button_text2" action Play('music',"music/ep1/this_silence.mp3", True)
            textbutton "Melodic In Fusion - Time goes by" text_style "music_button_text2" action Play('music',"music/ep1/time_goes_by.mp3", True)
            textbutton "Meizong - Fallen Colors (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/fallen_colors.mp3", True)
            textbutton "Meizong - Night Lights (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/night_lights.mp3", True)
            textbutton "Meizong - No Comments (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep8/no_comments.mp3", True)
            textbutton "Meizong - Phate (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/phate.mp3", True)
            textbutton "Meizong - Raveyard (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep3/raveyard.mp3", True)
            textbutton "Meizong & Yeeflex - Reaching Halo" text_style "music_button_text2" action Play('music',"music/ep4/reaching_halo.mp3", True)
            textbutton "Meizong (Argofox) - Skyline (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/skyline.mp3", True)
            textbutton "Meizong - Starfire (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep8/starfire.mp3", True)
            textbutton "Meizong - The heat (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep4/the_heat.mp3", True)
            textbutton "Mironov Sound - Funk rock instrumental" text_style "music_button_text2" action Play('music',"music/ep1/funk_rock.mp3", True)
            textbutton "Nicolai Heidlas - By your side" text_style "music_button_text2" action Play('music',"music/ep2/by_your_side.mp3", True)
            textbutton "Nicolai Heidlas - Golden Alley" text_style "music_button_text2" action Play('music',"music/ep1/golden_alley.mp3", True)
            textbutton "Nicolai Heidlas - Let's Begin" text_style "music_button_text2" action Play('music',"music/ep3/lets_begin.mp3", True)
            textbutton "Nicolai Heidlas - Lost Souls" text_style "music_button_text2" action Play('music',"music/ep1/lost_souls.mp3", True)
            textbutton "Nicolai Heidlas - Never give up" text_style "music_button_text2" action Play('music',"music/ep1/never_give_up.mp3", True)
            textbutton "Nicolai Heidlas - Roadtrip" text_style "music_button_text2" action Play('music',"music/ep1/roadtrip.mp3", True)
            textbutton "Nicolai Heidlas - Rockin' Riff" text_style "music_button_text2" action Play('music',"music/ep2/rockin_riff.mp3", True)
            textbutton "Nicolai Heidlas - Someways" text_style "music_button_text2" action Play('music',"music/ep1/someways.mp3", True)
            textbutton "Nicolai Heidlas - Sunny acoustic rock" text_style "music_button_text2" action Play('music',"music/ep3/sunny_acoustic_rock.mp3", True)
            textbutton "Nicolai Heidlas - Wings" text_style "music_button_text2" action Play('music',"music/ep2/wings.mp3", True)
            textbutton "Nicolai Heidlas - Winter Sunshine" text_style "music_button_text2" action Play('music',"music/ep1/winter_sunshine.mp3", True)
            textbutton "Oskar Hill & Meizong - The Sound Of Summer" text_style "music_button_text2" action Play('music',"music/ep2/sound_of_summer.mp3", True)
            textbutton "PeriTune - Gentle theme2 Guitar" text_style "music_button_text2" action Play('music',"music/ep4/gentle_theme_guitar.mp3", True)
            textbutton "PeriTune - Gentle theme2 MusicBox" text_style "music_button_text2" action Play('music',"music/ep7/musicbox.mp3", True)
            textbutton "PeriTune - Gentle theme2 Piano" text_style "music_button_text2" action Play('music',"music/ep3/gentle_theme_piano.mp3", True)
            textbutton "PeriTune - Guitar gentle" text_style "music_button_text2" action Play('music',"music/ep3/guitar_gentle.mp3", True)
            textbutton "PeriTune - Guitar melancholy" text_style "music_button_text2" action Play('music',"music/ep4/guitar_melancholy.mp3", True)
            textbutton "PeriTune - Guitar melancholy2" text_style "music_button_text2" action Play('music',"music/ep3/guitar_melancholy2.mp3", True)
            textbutton "PeriTune - Suspense5" text_style "music_button_text2" action Play('music',"music/ep5/suspense5.mp3", True)
            textbutton "Punk rock mashed up - Classicals breakbeat" text_style "music_button_text2" action Play('music',"music/ep1/classicals_breakbeat.mp3", True)
            textbutton "Ryan Pollard TK-473 - Heavy" text_style "music_button_text2" action Play('music',"music/ep2/heavy.mp3", True)
            textbutton "Ryansyah R. Poetra - Credits" text_style "music_button_text2" action Play('music',"music/ep1/credits.mp3", True)
            textbutton "Sean Danielsen - Food chain" text_style "music_button_text2" action Play('music',"music/ep1/food_chain.mp3", True)
            textbutton "Silent Partner - Black box" text_style "music_button_text2" action Play('music',"music/ep3/black_box.mp3", True)
            textbutton "Silent Partner - DC love Go-Go" text_style "music_button_text2" action Play('music',"music/ep3/dc_love_go_go.mp3", True)
            textbutton "Silent Partner - Get back" text_style "music_button_text2" action Play('music',"music/ep3/get_back.mp3", True)
            textbutton "Silent Partner - Let her in" text_style "music_button_text2" action Play('music',"music/ep4/let_her_in.mp3", True)
            textbutton "Silent Partner - Scrapbook" text_style "music_button_text2" action Play('music',"music/ep1/scrapbook.mp3", True)
            textbutton "Silent Partner - Some obsession" text_style "music_button_text2" action Play('music',"music/ep3/some_obsession.mp3", True)
            textbutton "S Strong - Hot mustard" text_style "music_button_text2" action Play('music',"music/ep3/hot_mustard.mp3", True)
            textbutton "Summertime - My heart" text_style "music_button_text2" action Play('music',"music/ep1/my_heart.mp3", True)
            textbutton "Steven O'Brien - Slavic battle theme" text_style "music_button_text2" action Play('music',"music/ep3/slavic_battle_theme.mp3", True)
            textbutton "The Night - Down" text_style "music_button_text2" action Play('music',"music/ep5/down.mp3", True)
            textbutton "The Night - Medicate me" text_style "music_button_text2" action Play('music',"music/ep5/medicate_me.mp3", True)
            textbutton "The Sisonpyh - Relax" text_style "music_button_text2" action Play('music',"music/ep4/relax.mp3", True)
            textbutton "The Zombie Dandies - Halloween Again" text_style "music_button_text2" action Play('music',"music/ep9/halloween_again.mp3", True)
            textbutton "The Zombie Dandies - The Friendly Monster Shop" text_style "music_button_text2" action Play('music',"music/ep9/the_friendly_monster_shop.mp3", True)
            textbutton "TRow - Acoustic guitar arrangement" text_style "music_button_text2" action Play('music',"music/ep1/trow.mp3", True)
            textbutton "Valtteri Kujala - Your Smile" text_style "music_button_text2" action Play('music',"music/ep1/your_smile.mp3", True)
            textbutton "Wayne John Bradley - Fresh Air" text_style "music_button_text2" action Play('music',"music/ep1/fresh_air.mp3", True)
            textbutton "Wova - They Say" text_style "music_button_text2" action Play('music',"music/ep1/they_say.mp3", True)








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_(""), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") text_style "custom_menu_style_header_btn"
                textbutton _("Mouse") action SetScreenVariable("device", "mouse") text_style "custom_menu_style_header_btn"

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") text_style "custom_menu_style_header_btn"

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

style keyboard_help_style:
    color "#ffffff"
    font "fonts/candara.ttf"

screen keyboard_help():

    hbox:
        label _("Enter") text_style "custom_menu_style_text3"
        text _("Advances dialogue and activates the interface.") style "keyboard_help_style"

    hbox:
        label _("Space") text_style "custom_menu_style_text3"
        text _("Advances dialogue without selecting choices.") style "keyboard_help_style"

    hbox:
        label _("Arrow Keys") text_style "custom_menu_style_text3"
        text _("Navigate the interface.") style "keyboard_help_style"

    hbox:
        label _("Escape") text_style "custom_menu_style_text3"
        text _("Accesses the game menu.") style "keyboard_help_style"

    hbox:
        label _("Ctrl") text_style "custom_menu_style_text3"
        text _("Skips dialogue while held down.") style "keyboard_help_style"

    hbox:
        label _("Tab") text_style "custom_menu_style_text3"
        text _("Toggles dialogue skipping.") style "keyboard_help_style"

    hbox:
        label _("Page Up") text_style "custom_menu_style_text3"
        text _("Rolls back to earlier dialogue.") style "keyboard_help_style"

    hbox:
        label _("Page Down") text_style "custom_menu_style_text3"
        text _("Rolls forward to later dialogue.") style "keyboard_help_style"

    hbox:
        label "H" text_style "custom_menu_style_text3"
        text _("Hides the user interface.") style "keyboard_help_style"

    hbox:
        label "S" text_style "custom_menu_style_text3"
        text _("Takes a screenshot.") style "keyboard_help_style"

    hbox:
        label "V" text_style "custom_menu_style_text3"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.") style "keyboard_help_style"


screen mouse_help():

    hbox:
        label _("Left Click") text_style "custom_menu_style_text3"
        text _("Advances dialogue and activates the interface.") style "keyboard_help_style"

    hbox:
        label _("Middle Click") text_style "custom_menu_style_text3"
        text _("Opens and closes the in-game phone.") style "keyboard_help_style"

    hbox:
        label _("Right Click") text_style "custom_menu_style_text3"
        text _("Accesses the game menu.") style "keyboard_help_style"

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side") text_style "custom_menu_style_text3"
        text _("Rolls back to earlier dialogue.") style "keyboard_help_style"

    hbox:
        label _("Mouse Wheel Down") text_style "custom_menu_style_text3"
        text _("Rolls forward to later dialogue.") style "keyboard_help_style"


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button") text_style "custom_menu_style_text3"
        text _("Advances dialogue and activates the interface.") style "keyboard_help_style"

    hbox:
        label _("Left Trigger\nLeft Shoulder") text_style "custom_menu_style_text3"
        text _("Rolls back to earlier dialogue.") style "keyboard_help_style"

    hbox:
        label _("Right Shoulder") text_style "custom_menu_style_text3"
        text _("Rolls forward to later dialogue.") style "keyboard_help_style"


    hbox:
        label _("D-Pad, Sticks") text_style "custom_menu_style_text3"
        text _("Navigate the interface.") style "keyboard_help_style"

    hbox:
        label _("Start, Guide") text_style "custom_menu_style_text3"
        text _("Accesses the game menu.") style "keyboard_help_style"

    hbox:
        label _("Y/Top Button") text_style "custom_menu_style_text3"
        text _("Hides the user interface.") style "keyboard_help_style"

    textbutton _("Calibrate") action GamepadCalibrate() text_style "custom_menu_style_header_btn"


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















style custom_frame_style:
    font "fonts/candara.ttf"
    idle_color "#ffffff"
    hover_color "#fe9416"
    size 32

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message) text_style "custom_menu_style_text":
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action text_style "custom_frame_style"
            textbutton _("No") action no_action text_style "custom_frame_style"


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        xalign 0.
        yalign 0.03
        has hbox:
            spacing 0


        imagebutton idle "gui/skip_dik.png" action NullAction() at delayed_blink(0.0, 1.0)







transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos

    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "fonts/DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

screen srmsg:

    modal False tag srmsg
    timer 5 action Hide('srmsg')
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "You unlocked a special render!" style "score_new_style" at show_hide_dissolve:
        xalign 0.97
        yalign 0.01

screen skillmsg:

    modal False tag skillmsg
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "{size=+3}{font=fonts/collegiate.ttf}{color=#ffffff}Your Skills app was updated.{/color}{/font}{/size}" at show_hide_dissolve:
        xalign 0.97
        yalign 0.018
        size 31
        color "#ffffff"

screen specialmsg:

    modal False tag specialmsg
    timer 3 action Hide('specialmsg')
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "[specialMessage]" style "score_new_style" at show_hide_dissolve:
        xalign 0.97
        yalign 0.01
screen specialmsglong:

    modal False tag specialmsglong
    timer 8 action Hide('specialmsglong')
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "[specialMessage]" style "score_new_style" at show_hide_dissolve:
        xalign 0.975
        yalign 0.01

style affinitymsgstyle:
    font "fonts/cabin-regular.ttf"
    size 40
    color "#fe9416"
    outlines [(2, "#ffffff", 0, 0)]

screen affinitymsg:

    modal False tag affinitymsg
    timer 2 action Hide('affinitymsg')
    text "[specialMessage]" style "affinitymsgstyle" at show_hide_dissolve:
        xalign 0.5
        yalign 0.16

screen scoremsg:

    modal False tag toprightmsg
    timer 3 action Hide('scoremsg')
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "Your DIK score was updated!" style "score_new_style" at show_hide_dissolve:
        xalign 0.97
        yalign 0.01

transform show_hide_dissolve:
    on show:
        alpha .0
        linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha .0


screen majorChoiceScale:

    modal False tag majorChoiceScale
    if not permanent_affinity:
        if not episodeIsEnding:
            add "dikscale_white_bg"

        if dpenalty < 4 and cpenalty < 20:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.236
                yalign 0.0
                action NullAction()
        if dpenalty < 8 and cpenalty < 16:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.36825
                yalign 0.0
                action NullAction()
        if dpenalty < 11 and cpenalty < 13:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.4675
                yalign 0.0
                action NullAction()
        if dpenalty < 13 and cpenalty < 11:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.5325
                yalign 0.0
                action NullAction()
        if dpenalty < 16 and cpenalty < 8:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.63175
                yalign 0.0
                action NullAction()
        if dpenalty < 20 and cpenalty < 4:
            imagebutton at show_hide_dissolve:
                idle "dik_bar"
                xalign 0.764
                yalign 0.0
                action NullAction()

        if dpenalty < 4 and cpenalty < 24:
            imagebutton at show_hide_dissolve:
                idle "massivedik"
                xalign 0.14
                yalign 0.05
                action NullAction()
        if dpenalty < 8 and cpenalty < 20:
            imagebutton at show_hide_dissolve:
                idle "hugedik"
                xalign 0.29
                yalign 0.05
                action NullAction()
        if dpenalty < 11 and cpenalty < 16:
            imagebutton at show_hide_dissolve:
                idle "dik"
                xalign 0.413
                yalign 0.05
                action NullAction()
        if dpenalty < 16 and cpenalty < 11:
            imagebutton at show_hide_dissolve:
                idle "chick"
                xalign 0.588
                yalign 0.05
                action NullAction()
        if dpenalty < 20 and cpenalty < 8:
            imagebutton at show_hide_dissolve:
                idle "hugechick"
                xalign 0.71
                yalign 0.05
                action NullAction()
        if dpenalty < 24 and cpenalty < 4:
            imagebutton at show_hide_dissolve:
                idle "massivechick"
                xalign 0.86
                yalign 0.05
                action NullAction()

        if dpenalty == 0 and cpenalty < 24:
            imagebutton at show_hide_dissolve:
                idle "d0"
                xalign 0.112
                yalign 0.0
                action NullAction()
        if dpenalty < 2 and cpenalty < 23:
            imagebutton at show_hide_dissolve:
                idle "d1"
                xalign 0.143
                yalign 0.0
                action NullAction()
        if dpenalty < 3 and cpenalty < 22:
            imagebutton at show_hide_dissolve:
                idle "d2"
                xalign 0.177
                yalign 0.0
                action NullAction()
        if dpenalty < 4 and cpenalty < 21:
            imagebutton at show_hide_dissolve:
                idle "d3"
                xalign 0.211
                yalign 0.0
                action NullAction()
        if dpenalty < 5 and cpenalty < 20:
            imagebutton at show_hide_dissolve:
                idle "d4"
                xalign 0.245
                yalign 0.0
                action NullAction()
        if dpenalty < 6 and cpenalty < 19:
            imagebutton at show_hide_dissolve:
                idle "d5"
                xalign 0.279
                yalign 0.0
                action NullAction()
        if dpenalty < 7 and cpenalty < 18:
            imagebutton at show_hide_dissolve:
                idle "d6"
                xalign 0.313
                yalign 0.0
                action NullAction()
        if dpenalty < 8 and cpenalty < 17:
            imagebutton at show_hide_dissolve:
                idle "d7"
                xalign 0.347
                yalign 0.0
                action NullAction()
        if dpenalty < 9 and cpenalty < 16:
            imagebutton at show_hide_dissolve:
                idle "d8"
                xalign 0.381
                yalign 0.0
                action NullAction()
        if dpenalty < 10 and cpenalty < 15:
            imagebutton at show_hide_dissolve:
                idle "d9"
                xalign 0.415
                yalign 0.0
                action NullAction()
        if dpenalty < 11 and cpenalty < 14:
            imagebutton at show_hide_dissolve:
                idle "d10"
                xalign 0.449
                yalign 0.0
                action NullAction()
        if dpenalty < 12 and cpenalty < 13:
            imagebutton at show_hide_dissolve:
                idle "d11"
                xalign 0.483
                yalign 0.0
                action NullAction()
        if dpenalty < 13 and cpenalty < 12:
            imagebutton at show_hide_dissolve:
                idle "c11"
                xalign 0.517
                yalign 0.0
                action NullAction()
        if dpenalty < 14 and cpenalty < 11:
            imagebutton at show_hide_dissolve:
                idle "c10"
                xalign 0.551
                yalign 0.0
                action NullAction()
        if dpenalty < 15 and cpenalty < 10:
            imagebutton at show_hide_dissolve:
                idle "c9"
                xalign 0.585
                yalign 0.0
                action NullAction()
        if dpenalty < 16 and cpenalty < 9:
            imagebutton at show_hide_dissolve:
                idle "c8"
                xalign 0.619
                yalign 0.0
                action NullAction()
        if dpenalty < 17 and cpenalty < 8:
            imagebutton at show_hide_dissolve:
                idle "c7"
                xalign 0.653
                yalign 0.0
                action NullAction()
        if dpenalty < 18 and cpenalty < 7:
            imagebutton at show_hide_dissolve:
                idle "c6"
                xalign 0.687
                yalign 0.0
                action NullAction()
        if dpenalty < 19 and cpenalty < 6:
            imagebutton at show_hide_dissolve:
                idle "c5"
                xalign 0.721
                yalign 0.0
                action NullAction()
        if dpenalty < 20 and cpenalty < 5:
            imagebutton at show_hide_dissolve:
                idle "c4"
                xalign 0.755
                yalign 0.0
                action NullAction()
        if dpenalty < 21 and cpenalty < 4:
            imagebutton at show_hide_dissolve:
                idle "c3"
                xalign 0.789
                yalign 0.0
                action NullAction()
        if dpenalty < 22 and cpenalty < 3:
            imagebutton at show_hide_dissolve:
                idle "c2"
                xalign 0.823
                yalign 0.0
                action NullAction()
        if dpenalty < 23 and cpenalty < 2:
            imagebutton at show_hide_dissolve:
                idle "c1"
                xalign 0.857
                yalign 0.0
                action NullAction()
        if dpenalty < 24 and cpenalty == 0:
            imagebutton at show_hide_dissolve:
                idle "c0"
                xalign 0.89
                yalign 0.0
                action NullAction()

image spr_ending_ep9:
    "ep9_diks_ph1_lib_mid" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ending_ep10:
    "ep10_diks_fr2_lib_mid" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ending_ep11:
    "ep11_diks_fr2_lib_mid" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

screen endingScreen:

    modal False tag endingScreen
    $ episodeIsEnding = True
    if currentEpisode == 9:
        add "spr_ending_ep9"
    elif currentEpisode == 10:
        add "spr_ending_ep10"
    elif currentEpisode == 11:
        add "spr_ending_ep11"

    if permanent_affinity:
        add "report_box_ol" yoffset -100
    else:
        add "report_box_ol"

    if money > 0:
        $ mny = "{color=#36ca2b}$%d{/color}" % money
    else:
        $ mny = "{color=#36ca2b}No money{/color}"

    if affinity == "DIK":
        $ affinityStr = "{color=#fe9416}{font=fonts/collegiate.ttf}DIK{/font}{/color} affinity"
    elif affinity == "CHICK":
        $ affinityStr = "{color=#00a0e6}{font=fonts/collegiate.ttf}CHICK{/font}{/color} affinity"
    else:
        $ affinityStr = "{color=#91f360}{font=fonts/collegiate.ttf}Neutral{/font}{/color} affinity"

    if minigames:
        $ totalPassedClasses = passedEnglish + passedMath + passedGender + passedEnglishS3 + passedMathS3 + passedScienceS3
        $ totalPerfectClasses = maxedEnglish + maxedMath + maxedGender + maxedMath_s2 + maxedEnglish_s2 + maxedGender_s2 + maxedEnglishS3 + maxedMathS3 + maxedScienceS3
        $ totalFailedClasses = failedEnglish + failedMath + failedGender + failedEnglishS3 + failedMathS3 + failedScienceS3
        text "{font=fonts/candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} score: [dik]\nPermanent affinity: [affinityStr]\nNumber of major {color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} choices: [cpenalty]\nNumber of {color=#ffffff}{size=+3}{font=fonts/collegiate.ttf}NEUTRAL{/font}{/size}{/color} choices: [npenalty]\nNumber of major {color=#00a0e6}{size=+3}{font=fonts/collegiate.ttf}Chick{/font}{/size}{/color} choices: [dpenalty]\nNumber of {color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} actions: [totalDikChoices]\nNumber of {color=#00a0e6}{size=+3}{font=fonts/collegiate.ttf}Chick{/font}{/size}{/color} actions: [totalChickChoices]\nMoney: [mny]\n{color=#ffed00}Perfect{/color} classes: [totalPerfectClasses]\n{color=#1df400}Passed{/color} classes: [totalPassedClasses]\n{color=#f72400}Failed{/color} classes: [totalFailedClasses]\nParty planner score: {color=#ffed00}[pp_score]{/color}{/size}{/font}" at show_hide_dissolve:
            yalign 0.76
            xalign 0.94
            text_align 0.0
            yoffset -100
            size 33
            hover_outlines [(1, "#660066", 0, 0)]
    else:
        text "{font=fonts/candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} score: [dik]\nPermanent affinity: [affinityStr]\nNumber of major {color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} choices: [cpenalty]\nNumber of {color=#ffffff}{size=+3}{font=fonts/collegiate.ttf}NEUTRAL{/font}{/size}{/color} choices: [npenalty]\nNumber of major {color=#00a0e6}{size=+3}{font=fonts/collegiate.ttf}Chick{/font}{/size}{/color} choices: [dpenalty]\nNumber of {color=#fe9416}{size=+3}{font=fonts/collegiate.ttf}DIK{/font}{/size}{/color} actions: [totalDikChoices]\nNumber of {color=#00a0e6}{size=+3}{font=fonts/collegiate.ttf}Chick{/font}{/size}{/color} actions: [totalChickChoices]\nMoney: [mny]{/size}{/font}" at show_hide_dissolve:
            yalign 0.6
            xalign 0.98
            text_align 0.0
            yoffset -100
            size 38
            hover_outlines [(1, "#660066", 0, 0)]

screen previous_screen:

    modal False tag previous_screen
    imagebutton:
        idle "skip_recap_button"
        hover "skip_recap_button_hover"
        xalign 1.0
        yalign 0.0
        action Jump(previousEpLabel)


transform transformSide:
    xpos 0
    ypos 0
    easein 2.5 xpos -1900 ypos 0
    easein 0.5 xpos -1600 ypos 0
transform transformSide2:
    xpos 0
    ypos 0
    easein 10 xpos -1900 ypos 0
    easein 10 xpos 0 ypos 0
    repeat
transform transformTop2:
    xpos 0
    ypos -3240
    easein 10 xpos 0 ypos 0

transform transformTop:
    xpos 0
    ypos -2000
    easein 10 xpos 0 ypos 0

transform transformBottom:
    xpos 0
    ypos 0
    linear 110 xpos 0 ypos -10113

style guide_style:
    font "fonts/Museo500.otf"
    size 50
    color "#ffffff"
    outlines [(1, "#4a0000", 0, 0)]
    text_align 0.5

screen keymap_screen:
    tag km_screen
    if (nonPatreonConfig or steamConfig) and renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
        if not persistent.walkthrough_tutorial:
            modal True
            add "bg_guide"
            key "K_RETURN" action Hide("nonexistent_screen")
            key "K_KP_ENTER" action Hide("nonexistent_screen")
            key "K_SPACE" action Hide("nonexistent_screen")
            key "mousedown_5" action Hide("nonexistent_screen")
            key "K_DOWN" action Hide("nonexistent_screen")
            key "K_PAGEUP" action Hide("nonexistent_screen")
            key "mousedown_4" action Hide("nonexistent_screen")
            key "K_UP" action Hide("nonexistent_screen")
            key "K_PAGEDOWN" action Hide("nonexistent_screen")
            key "mouseup_3" action Hide("nonexistent_screen")
            key "mouseup_1" action Hide("nonexistent_screen")

            text "Thank you for your purchase of\n{color=ffed00}Being a DIK: Season 3 - The complete official guide.{/color}\n\nPress '{color=#00ff00}g{/color}' to show and hide the guide.\nYou can also press the {color=fe9416}Guide{/color} button in the quick menu\nto open the guide.\n\nPress '{color=#00ff00}g{/color}' to continue." style "guide_style_s2" xalign 0.2 yalign 0.3
            key "g" action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0), SetVariable("persistent.walkthrough_tutorial", True),Function(show_guide_func))
        else:
            key "g" action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0),Function(show_guide_func))
    else:
        key "g" action NullAction()

style walkthrough_text:
    font "fonts/candara.ttf"
    size 25
    color "#ffffff"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_highlighted:
    font "fonts/candara.ttf"
    size 25
    color "#fe9416"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_s2:
    font "fonts/candara.ttf"
    size 30
    color "#ffffff"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_s2_highlighed:
    font "fonts/candara.ttf"
    size 30
    color "#fe9416"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_choice:
    font "fonts/candara.ttf"
    size 22
    color "#33d145"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_choice_disabled:
    font "fonts/candara.ttf"
    size 22
    color "#d15433"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_header:
    font "fonts/candara.ttf"
    size 40
    color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_scroll:
    font "fonts/candara.ttf"
    size 22
    color "#007db5"
    hover_color "#007db5"
    outlines [(1, "#000000", 0, 0)]
    xmaximum 500

style walkthrough_text_current:
    font "fonts/cabin-regular.ttf"
    size 22
    color "#000000"
    xmaximum 500

screen newmoneymsg:

    modal False tag newmoneymsg
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    if (money > 10 and wallet_lvl == 3):
        $ money = 10
    elif (money > 8 and wallet_lvl == 2):
        $ money = 8
    elif (money > 6 and wallet_lvl == 1):
        $ money = 6
    elif money > 5 and wallet_lvl == 0:
        $ money = 5
    elif money < 0:
        $ money = 0

    if money > 0:
        text "Pocket money: {color=#36ca2b}$%i{/color}" % money style "score_new_style" at show_hide_dissolve:
            xalign 0.97
            yalign 0.01
    else:
        text "Pocket money: {color=#36ca2b}No money{/color}" style "score_new_style" at show_hide_dissolve:
            xalign 0.97
            yalign 0.01

init python:
    def savePersistentData():
        renpy.save_persistent()
        return

screen saveMsg:

    modal False tag saveMsg
    timer 3 action Hide("saveMsg")
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "Collectible data saved!" style "score_new_style" at show_hide_dissolve:
        xalign 0.97
        yalign 0.01

style music_button_text:
    color "#000000"
    hover_color "00a0e6"
    selected_color "#fe9416"
    font "fonts/candara.ttf"
    size 22
style music_button_text2:
    color "#ffffff"
    hover_color "00a0e6"
    selected_color "#fe9416"
    font "fonts/candara.ttf"
    size 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

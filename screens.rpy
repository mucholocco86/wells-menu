init offset = -1










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





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                text who id "who" style "gotham_bold" size 48 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]







        text what id "what" style "gotham_office" size 34 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xmaximum 1300 xpos 25 ypos 50




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
    background None
    padding (0, 0, 0, 0)

    xalign 0.5
    xysize (1340, 240)
    yalign 0.945

style namebox:
    background None
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign -0.03

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:
        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "gotham_office" size 34 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
        input id "input" style "gotham_office" size 34 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"
    vbox:
        yalign 0.9

        for i in items:
            if i.kwargs.get("req") is False:
                textbutton "~ " + i.kwargs.get("msg") + " ~" action NullAction() text_color "#8b0000"

            else:
                button:
                    xysize (772, 60)
                    padding (0, 0, 0, 0)

                    idle_background Frame("gui/Choices-idle.webp", 30, 30, 30, 30)
                    hover_background Frame("gui/choice.webp", 30, 30, 30, 30)
                    text i.caption style "gotham_office" size 32 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xalign 0.5 yalign 0.5

                    action i.action












define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():
    zorder 100

    if quick_menu and persistent.quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            textbutton _("Back") text_style "gottham_office_button_text" text_size 18 action Rollback()
            textbutton _("Skip") text_style "gottham_office_button_text" text_size 18 action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") text_style "gottham_office_button_text" text_size 18 action Preference("auto-forward", "toggle")
            textbutton _("Save") text_style "gottham_office_button_text" text_size 18 action ShowMenu('save')
            textbutton _("Q.Save") text_style "gottham_office_button_text" text_size 18 action QuickSave()
            textbutton _("Q.Load") text_style "gottham_office_button_text" text_size 18 action QuickLoad()
            textbutton _("Prefs") text_style "gottham_office_button_text" text_size 18 action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()

        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Gallery") action [ui.callsinnewcontext("gallery_name"), ShowMenu("gallery")]
        textbutton _("Bonus") action ShowMenu("bonusGallery")
        textbutton _("Special") action ShowMenu("specialGallery")

        if not FOR_STEAM:
            textbutton _("Patreon"):
                text_color "#f11" text_hover_color "#cf6932"
                action OpenURL("https://www.patreon.com/KissKissStudios")

        textbutton _("Discord"):
            text_color "#87CEEB" text_hover_color "#437ba8"
            action OpenURL("https://discord.gg/7ratBZvAcZ")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








screen main_menu():
    tag menu

    default buttons = [
        ["NewGame", _("New Game"), _("Start a new game"), Start()],
        ["SaveLoad", _("Save / Load"), _("Save / Load previous game"), ShowMenu("load")],
        ["Preferences", _("Preferences"), _("Manage game settings"), ShowMenu("preferences")],
        ["Gallery", _("Gallery"), _("View scenes again"), ShowMenu("gallery_main")],
    ]

    add "gui/mainmenu/background.webp"
    text "v[config.version]" style "gotham_office" size 16 xalign 1.0 yalign 0.002

    imagebutton:
        idle "gui/mainmenu/Exit-button-idle.webp"
        hover "gui/mainmenu/Exit-button-hover.webp"

        action Quit(confirm=False)
        xpos 1804
        ypos 56

    hbox:
        xpos 63
        ypos 177
        spacing 23

        for im, name, desc, act in buttons:
            button:
                xysize (431, 727)
                padding (0, 0, 0, 0)

                idle_background f"gui/mainmenu/{im}-idle.webp"
                hover_background f"gui/mainmenu/{im}-hover.webp"

                text name style "gotham_bold" xpos 20 ypos 641
                text desc style "gotham_medium" xpos 20 ypos 668

                action act

    imagebutton:
        idle "gui/mainmenu/Achievements-button-idle.webp"
        hover "gui/mainmenu/Achievements-button-hover.webp"

        action ShowMenu("achievements")
        xpos 1429
        ypos 970

    use overlay_screen(_bonus=True)

screen bonus_box_screen():
    layer "over_screen"
    modal True

    on "show":
        action Function(renpy.show_layer_at, at_list=blur_show, layer="screens")
    on "hide":
        action Function(renpy.show_layer_at, at_list=blur_hide, layer="screens")

    default wrong_code_added = False

    add Solid("#00000050")
    dismiss action Hide()

    frame:
        xysize (457, 254)
        background f"gui/mainmenu/bonus/BonusCode-background.webp"
        padding (0, 0, 0, 0)
        xpos 731
        ypos 413

        if wrong_code_added:
            add "gui/mainmenu/bonus/BonusCode-WrongCode.webp"

        text _("BONUS CODE") style "gotham_bold" xpos 139 ypos 18
        text _("Enter the code:") style "gotham_office" size 15 color "#898e8f" xpos 46 ypos 78

        frame:
            xysize (353, 42)
            padding (0, 0, 0, 0)
            background None
            xpos 50
            ypos 102

            input value BonusContentInputValue("bonus_variable") length 15 style "gotham_office" color "#46e216" size 32 xalign 0.5 yalign 0.3

        button:
            xysize (180, 60)
            padding (0, 0, 0, 0)

            idle_background "gui/mainmenu/bonus/BonusCode-button-idle.webp"
            hover_background "gui/mainmenu/bonus/BonusCode-button-hover.webp"

            text _("Enter Code") style "gotham_office" xalign 0.5 yalign 0.5
            action ActivateContent()

            xpos 139
            ypos 170

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

    textbutton _("Return"):
        style "return_button"

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
    yoffset -45









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):
    default hovering_over = -1

    add "gui/saveload/background.webp"
    text title style "gotham_bold" size 21 xpos 64 ypos 146

    frame:
        xysize (582, 727)
        padding (0, 0, 0, 0)
        background f"gui/saveload/saveload-banner.webp"
        xpos 64
        ypos 177

        text title style "gotham_bold" xalign 0.5 ypos 665


    grid 3 3:
        xpos 668
        ypos 177

        xspacing 21
        yspacing 19

        for i in range(9):

            $ slot = i + 1

            button:
                xysize (384, 210)
                padding (0, 0, 0, 0)

                hovered SetLocalVariable("hovering_over", slot)
                unhovered SetLocalVariable("hovering_over", -1)
                action FileAction(slot)

                background "gui/saveload/empty-slot.webp"
                add AlphaMask(FileScreenshot(slot), "gui/saveload/GalleryPhoto-overlay-hover.webp")

                if hovering_over == slot:
                    add "gui/saveload/GalleryPhoto-overlay-hover.webp"
                    if title == "Load":
                        text _("Load") style "gotham_bold" size 15 xalign 0.5 yalign 0.5

                    elif FileLoad(slot).get_sensitive():
                        text _("Overwrite?") style "gotham_bold" size 15 xalign 0.5 yalign 0.5

                elif FileLoad(slot).get_sensitive():
                    add "gui/saveload/GalleryPhoto-black-label.webp"

                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty Slot")):
                    style "gotham_office"
                    size 15
                    xalign 0.5
                    if FileLoad(slot).get_sensitive():
                        ypos 177
                    else:
                        yalign 0.5

                text FileSaveName(slot):
                    style "gotham_office"
                    size 15
                    color "#898e8f"
                    xalign 0.5
                    ypos 177

                key "save_delete" action FileDelete(slot)

    button:
        xysize (102, 41)
        padding (0, 0, 0, 0)

        idle_background "gui/saveload/Auto-button-idle.webp"
        hover_background "gui/saveload/Auto-button-hover.webp"
        selected_background "gui/saveload/Auto-button-hover.webp"

        text _("Auto") style "gotham_office" size 15 xalign 0.5 yalign 0.5

        action FilePage("auto")
        xpos 668
        ypos 860
    imagebutton:
        idle "gui/saveload/LeftArrow-idle.webp"
        hover "gui/saveload/LeftArrow-hover.webp"

        action FilePagePrevious()
        xpos 1692
        ypos 860
    imagebutton:
        idle "gui/saveload/RightArrow-idle.webp"
        hover "gui/saveload/RightArrow-hover.webp"

        action FilePageNext()
        xpos 1803
        ypos 860

    if persistent._file_page == "auto":
        text "A" style "gotham_office" size 24 xpos 1767 ypos 867
    elif persistent._file_page == "quick":
        text "Q" style "gotham_office" size 24 xpos 1767 ypos 867
    else:
        text "[persistent._file_page]" style "gotham_office" size 24 xpos 1765 ypos 867:
            if int(persistent._file_page) > 9:
                xoffset -8

    use overlay_screen

screen overlay_screen(_bonus=False):
    default socials = [
        ["Patreon", OpenURL("https://www.patreon.com/KissKissStudios")],
        ["Discord", OpenURL("https://discord.gg/7ratBZvAcZ")],
        ["Steam", OpenURL("https://store.steampowered.com/app/2906370/Bright_Lord/")],
        ["X", OpenURL("https://x.com/DomisGi")],
    ]

    imagebutton:
        idle "gui/mainmenu/Exit-button-idle.webp"
        hover "gui/mainmenu/Exit-button-hover.webp"

        action Quit(confirm=False)
        xpos 1804
        ypos 56
    frame:
        xysize (52, 20)
        padding (0, 0, 0, 0)
        background None
        xpos 1804
        ypos 110

        text _("Exit") style "gotham_office" size 14 xalign 0.5 yalign 0.5

    frame:
        if FOR_STEAM:
            xysize (238, 83)
            padding (0, 0, 0, 0)
            background "gui/mainmenu/SocialMedia-3.webp"
        else:
            xysize (308, 83)
            padding (0, 0, 0, 0)
            background "gui/mainmenu/SocialMedia-4.webp"
        xpos 63
        ypos 970

        $ l = socials[1:] if FOR_STEAM else socials
        for index, (im, act) in enumerate(l):
            imagebutton:
                idle f"gui/mainmenu/sm/{im}.webp"
                action act
                at zoom_element(t=0.25)

                xpos 47 + 27*index + 44*index
                ypos 42

    if _bonus:
        button:
            xysize (322, 85)
            padding (0, 0, 0, 0)

            idle_background "gui/mainmenu/button-idle.webp"
            hover_background "gui/mainmenu/button-hover.webp"
            insensitive_background "gui/mainmenu/button-idle.webp"

            text _("BONUS CONTENT") style "gotham_office" xalign 0.5 yalign 0.5:
                if bonus_content_unlocked():
                    color "#46e216"
            sensitive not bonus_content_unlocked()
            action If(FOR_STEAM, true=OpenURL("https://store.steampowered.com/app/3316070/Bright_Lord__Bonus_Content/"), false=Show("bonus_box_screen"))

            xpos 1534
            ypos 970

    else:
        button:
            xysize (322, 85)
            padding (0, 0, 0, 0)

            idle_background "gui/gallery/main/return-button-idle.webp"
            hover_background "gui/gallery/main/return-button-hover.webp"

            text _("RETURN") style "gotham_office" xalign 0.5 yalign 0.5
            action If(main_menu, true=Return(), false=ShowMenu("pause_menu"))

            xpos 1534
            ypos 970









screen preferences():
    tag menu

    default lang_data = [
        ["US", "English", None],
        ["French", "French", "french"],
        ["Portugese", "Portuguese - Brazil", "portuguese"],
        ["Russian", "Russian", "russian"],
        ["Turkish", "Turkish", "turkish"],
        ["CHN-simplified", "Chinese Simplified", "simplified_chinese"],
        ["CHN-traditional", "Chinese Traditional", "traditional_chinese"],
    ]
    default hovering_over_lang = ""

    add "gui/preferences/Preferences-background.webp"
    text _("Preferences") style "gotham_bold" xpos 91 ypos 818
    text _("Manage game settings") style "gotham_medium" xpos 91 ypos 845

    text _("Display") style "gotham_bold" xpos 1000 ypos 194
    text _("Display Mode") style "gotham_office" size 15 xpos 1000 ypos 249
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 250

        if _preferences.fullscreen:
            textbutton _("Fullscreen") text_style "gottham_office_button_text":
                action Preference("display", "window")
                xalign 1.0
                yalign 0.5
        else:
            textbutton _("Window") text_style "gottham_office_button_text":
                action Preference("display", "fullscreen")
                xalign 1.0
                yalign 0.5
    text _("Quick Menu") style "gotham_office" size 15 xpos 1000 ypos 294
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 296

        if persistent.quick_menu:
            textbutton _("ON") text_style "gottham_office_button_text":
                action SetField(persistent, "quick_menu", False)
                xalign 1.0
                yalign 0.5
        else:
            textbutton _("OFF") text_style "gottham_office_button_text":
                action SetField(persistent, "quick_menu", True)
                xalign 1.0
                yalign 0.5
    text _("Text Speed") style "gotham_office" size 15 xpos 1000 ypos 338
    bar:
        style "preference_bar"
        value Preference("text speed")
        xpos 1599
        ypos 340
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 338

        if _preferences.text_cps == 0:
            text "200" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5
        else:
            text f"{_preferences.text_cps:.0f}" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5
    text _("Auto-Forward Speed") style "gotham_office" size 15 xpos 1000 ypos 383
    bar:
        style "preference_bar"
        value Preference("auto-forward time")
        xpos 1599
        ypos 385
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 383

        text f"{_preferences.afm_time:.0f}" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5

    text _("Skip") style "gotham_bold" xpos 1000 ypos 432
    text _("Unseen Text") style "gotham_office" size 15 xpos 1000 ypos 486
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 488

        if _preferences.skip_unseen:
            textbutton _("ON") text_style "gottham_office_button_text":
                action Preference("skip", "seen")
                xalign 1.0
                yalign 0.5
        else:
            textbutton _("OFF") text_style "gottham_office_button_text":
                action Preference("skip", "all")
                xalign 1.0
                yalign 0.5
    text _("After Choices") style "gotham_office" size 15 xpos 1000 ypos 531
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 534

        if _preferences.skip_after_choices:
            textbutton _("ON") text_style "gottham_office_button_text":
                action Preference("after choices", "stop")
                xalign 1.0
                yalign 0.5
        else:
            textbutton _("OFF") text_style "gottham_office_button_text":
                action Preference("after choices", "skip")
                xalign 1.0
                yalign 0.5
    text _("Transitions") style "gotham_office" size 15 xpos 1000 ypos 577
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 577

        if _preferences.transitions:
            textbutton _("ON") text_style "gottham_office_button_text":
                action Preference("transitions", "none")
                xalign 1.0
                yalign 0.5
        else:
            textbutton _("OFF") text_style "gottham_office_button_text":
                action Preference("transitions", "all")
                xalign 1.0
                yalign 0.5

    text _("Audio") style "gotham_bold" xpos 1000 ypos 626
    text _("Music Volume") style "gotham_office" size 15 xpos 1000 ypos 680
    bar:
        style "preference_bar"
        value Preference("music volume")
        xpos 1599
        ypos 682
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 681

        text f"{preferences.get_mixer('music')*100:.0f}%" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5
    text _("Sound Volume") style "gotham_office" size 15 xpos 1000 ypos 725
    bar:
        style "preference_bar"
        value Preference("sfx volume")
        xpos 1599
        ypos 727
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 726

        text f"{preferences.get_mixer('sfx')*100:.0f}%" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5
    text _("Voice Volume") style "gotham_office" size 15 xpos 1000 ypos 771
    bar:
        style "preference_bar"
        value Preference("voice volume")
        xpos 1599
        ypos 773
    frame:
        xysize (100, 16)
        padding (0, 0, 0, 0)
        background None
        xpos 1720
        ypos 772

        text f"{preferences.get_mixer('voice')*100:.0f}%" style "gottham_office_button_text" color "#ffffff" xalign 1.0 yalign 0.5

    frame:
        xysize (827, 83)
        padding (0, 0, 0, 0)
        background "gui/preferences/Language-bar.webp"
        if FOR_STEAM:
            xpos 326
        else:
            xpos 396
        ypos 970

        hbox:
            xpos 24
            yalign 0.5
            spacing 16

            text _("Language") style "gotham_bold" size 20 yalign 0.5
            text "[hovering_over_lang]" style "gotham_office" size 20 color "#898e8f" yalign 0.5 yoffset 1

        hbox:
            xpos 403
            ypos 17
            spacing 13

            for im, name, lang in lang_data:
                imagebutton:
                    idle f"gui/preferences/Languages/{im}-inactive.webp"
                    hover f"gui/preferences/Languages/{im}-active.webp"
                    selected_idle f"gui/preferences/Languages/{im}-active.webp"

                    hovered SetScreenVariable("hovering_over_lang", name)
                    unhovered SetScreenVariable("hovering_over_lang", "")
                    action Language(lang)

    use overlay_screen









screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = { "alt", "noalt" }


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








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


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















screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add Solid("#000000dd")

    frame:
        xysize (457, 254)
        padding (0, 0, 0, 0)
        background "gui/confirm/Confirm-Background.webp"
        xalign 0.5
        yalign 0.5

        text _("Confirm") style "gotham_bold" xalign 0.5 ypos 19

        frame:
            xysize (336, 69)
            padding (0, 0, 0, 0)
            background None
            xalign 0.5
            ypos 65

            text message style "gotham_office" size 15 xalign 0.5 yalign 0.5

        button:
            xysize (161, 60)
            padding (0, 0, 0, 0)

            idle_background "gui/confirm/YesNoButton-idle.webp"
            hover_background "gui/confirm/YesNoButton-hover.webp"

            text _("Yes") style "gotham_office" xalign 0.5 yalign 0.5
            action yes_action
            xpos 61
            ypos 148
        button:
            xysize (161, 60)
            padding (0, 0, 0, 0)

            idle_background "gui/confirm/YesNoButton-idle.webp"
            hover_background "gui/confirm/YesNoButton-hover.webp"

            text _("No") style "gotham_office" xalign 0.5 yalign 0.5
            action no_action
            xpos 236
            ypos 148


    key "game_menu" action no_action








screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



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
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):
    layer "over_screen"

    zorder 100
    style_prefix "notify"

    frame at notify_appear(Text(message).size()[0]):
        text "[message!tq]" style "gotham_office"

    timer 3.5 action Hide('notify')


transform notify_appear(x):
    on show:
        xoffset -x
        easein 1.25 xoffset 0
    on hide:
        easeout 1.25 xoffset x*-1

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
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

            has fixed
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

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"


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

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

screen end_of_content_screen():
    modal True






    frame:
        xysize (756, 383)
        background "gui/eoc/frame.webp"
        padding (0, 0, 0, 0)
        xalign 0.5
        yalign 0.5

        add "gui/eoc/end-of-content.webp" xpos -30 ypos -35

        if FOR_STEAM:
            text _("""This is the end of the journey. {color=#f33}Thank you for playing the game.{/color}"""):

                size 30
                justify True
                text_align 0.5
                xmaximum 650
                xalign 0.5
                yalign 0.5
        else:
            text _("""This is the end of the journey. {color=#f33}Thank you for playing the game.{/color}

    {a=https://www.patreon.com/KissKissStudios}{color=#FF8C00}Check our Patreon!{/color}{/a}"""):

                size 30
                justify True
                text_align 0.5
                xmaximum 650
                xalign 0.5
                yalign 0.5

        imagebutton:
            idle "gui/eoc/Okey-idle.webp"
            hover "gui/eoc/Okey-hover.webp"

            action Hide("end_of_content_screen")

            xpos 633
            ypos 344

screen pause_menu():
    tag menu

    on "show":
        action Function(renpy.show_layer_at, at_list=blur_show, layer="master")
    on "hide":
        action Function(renpy.show_layer_at, at_list=blur_hide, layer="master")

    default buttons = [
        [_("Save"), ShowMenu("save")],
        [_("Load"), ShowMenu("load")],
        [_("Settings"), ShowMenu("preferences")],
        [_("Credits"), ShowMenu("credits")],
        [_("Main Menu"), MainMenu()],
        [_("Return"), Return()],
        [_("Quit"), Quit()],
    ]

    frame:
        xysize (489, 739)
        padding (0, 0, 0, 0)
        background "gui/pause/PauseMenu-background.webp"
        xpos 715
        ypos 149

        text _("Paused") style "gotham_bold" size 32 color "#ff424d" xalign 0.5 ypos 141

        vbox:
            xpos 85
            ypos 202
            spacing 13

            for name, act in buttons:
                button:
                    xysize (321, 60)
                    padding (0, 0, 0, 0)

                    idle_background "gui/pause/Button-idle.webp"
                    hover_background "gui/pause/Button-hover.webp"

                    if name == _("Main Menu") and _in_replay:
                        text _("End Replay") style "gotham_office" size 21 xalign 0.5 yalign 0.5
                        action EndReplay()
                    else:
                        text name style "gotham_office" size 21 xalign 0.5 yalign 0.5
                        action act

screen achievements():
    tag menu

    add "gui/achievements/Background.webp"
    add "gui/achievements/Achievements-banner.webp" xpos 64 ypos 177
    text _("ACHIEVEMENTS") style "gotham_bold" size 21 xpos 63 ypos 146

    vpgrid:
        cols 1
        xysize (1188, 682)

        xpos 668
        ypos 222

        draggable True
        mousewheel True

        scrollbars "vertical"
        vscrollbar_unscrollable "hide"

        vscrollbar_ysize 680
        vscrollbar_base_bar "gui/gallery/screen//SliderGuide.webp"
        vscrollbar_thumb "gui/gallery/screen//SliderButon.webp"
        vscrollbar_thumb_offset 4
        vscrollbar_xoffset 40

        vbox:
            xpos 25
            ypos 24
            spacing 7

            for key, (name, desc, im) in ACHIEVEMENTS_DATA.items():
                if im in ["ACH_75", "ACH_76"]:
                    continue

                frame:
                    xysize (1163, 83)
                    padding (0, 0, 0, 0)
                    background None

                    if achievement.has(key):
                        add f"gui/achievements/icons/{im}.webp"
                    else:
                        add f"gui/achievements/icons/{im}.webp" at greyed_out

                    text name style "gotham_bold" xpos 95 ypos 16
                    text desc style "gotham_office" xpos 95 ypos 39
                    add Solid("#474546", xysize=(1139, 2)) yalign 1.0

            null height 14

    use overlay_screen

screen credits():
    tag menu

    dismiss action [With(dissolve), Return(), With(dissolve)]
    add "gui/blcredits.webp"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

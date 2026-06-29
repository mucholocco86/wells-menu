###############################################################################
## 1. DEFINIÇÃO DINÂMICA DAS FONTES E ESTILOS GERAIS
################################################################################

define 999 gui.text_font = 'wells/Roboto-Regular.ttf'
define 999 gui.name_text_font = 'wells/Roboto-Regular.ttf'
define 999 gui.interface_text_font = 'wells/Roboto-Regular.ttf'

#### STYLES DEFINE
define wells_namebox_borders = Borders(5, 5, 5, 5)
define wells_text_size = 30

default persistent.pref_text_size_label = 28
default persistent.pref_text_size_dialogue = 28
default wells_menu_tab = "main"
default persistent.font_escolhida = None
default persistent.wells_line_spacing = 5
default persistent.wells_text_size_mult = 1.0 
default persistent.wells_dialogue_y_offset = 0
default persistent.wells_dual_dialogue_offset = 200 
default persistent.wells_dual_dialog_offset = 300
default persistent.wells_dual_dialogue_fix = False
default persistent.wells_say_mode = 0
default quick_menu = True

################################################################################
## DEVELOPER CONFIG
################################################################################
init 999 python:
    config.language = "brazil"
    config.default_language = "brazil"
    config.developer = True
    config.console = True
    config.rollback_enabled = True
    config.hard_rollback_limit = 128
    config.rollback_length = 128

################################################################################
## NATIVE PYTHON LOGIC
################################################################################
init python:
    import os

    # Inicializa a variável persistente caso ela não exista
    if persistent.multiple_dialogue is None:
        persistent.multiple_dialogue = False

    def toggle_power_save():
        # O Ren'Py moderno usa None para taxa máxima ou um número inteiro.
        # Ajustamos para alternar corretamente entre 30 FPS e o padrão da tela.
        if preferences.gl_framerate == 30:
            preferences.gl_framerate = None
        else:
            preferences.gl_framerate = 30
        renpy.restart_interaction()

    def get_all_languages():
        languages = ["Default"]
        # Boa prática: Usar renpy.config.gamedir para garantir compatibilidade em Android/iOS
        path = os.path.join(renpy.config.gamedir, 'tl')
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isdir(os.path.join(path, entry)):
                    languages.append(entry)
        return languages

    def toggle_multiple_dialogue():
        persistent.multiple_dialogue = not persistent.multiple_dialogue
        renpy.restart_interaction()

    def listar_fontes():
        fontes = []
        path = os.path.join(renpy.config.gamedir, 'wells')
        if os.path.exists(path):
            for f in os.listdir(path):
                # Converte o nome para minúsculo antes de checar a extensão (.TTF / .ttf)
                if f.lower().endswith((".ttf", ".otf")):
                    fontes.append(f)
        return fontes

    def wells_font_transformer(old_font):
        if persistent.font_escolhida:
            return persistent.font_escolhida
        return old_font

    config.font_transforms["wells_custom"] = wells_font_transformer
    config.overlay_screens.append("quick_menu")

    if renpy.variant("touch"):
        style.wells_menu_quick_button_text.size = 40
        style.wells_menu_quick_frame.padding = (30, 20)
    else:
        style.wells_menu_quick_button_text.size = 25

# --- Definições de Estilos Visuais ---
init -1 style wells_menu_quick_button:
    padding (10, 4, 10, 4)

init -1 style wells_menu_quick_button_text:
    size 22
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    hover_color "#2bff00"

init -1 style wells_menu_quick_text is wells_menu_quick_button_text:
    size 22

init -1 python:
    if persistent.use_hw_video is None:
        persistent.use_hw_video = True
    config.hw_video = persistent.use_hw_video
    
    if persistent.multiple_dialogue is None:
        persistent.multiple_dialogue = True

    if persistent.font_escolhida:
        _preferences.font_transform = "wells_custom"
################################################################################
## 2. SCREEN MENU PRINCIPAL (WELLS MENU LANGUAGE)
################################################################################

screen wells_menu_language():
    modal True
    zorder 200
    tag menu
    add Solid("#00000080") 

    frame:
        xalign 0.5 yalign 0.4
        background Frame("wells/gui/frame_menu.png", 10, 10)

        # --- LÓGICA DE RESOLUÇÃO E MOBILE ---
        if config.screen_width == 1920:
            if renpy.variant("small"):
                xsize 1600 ysize 950 padding (60, 50)
            else:
                xsize 1450 ysize 820 padding (50, 40)
        else:
            xsize 1150 ysize 680 padding (40, 35)

        vbox:
            xfill True
            spacing 25

            # --- TÍTULO PRINCIPAL (TEXT) COM MOLDURA ---
            frame:
                xalign 0.5
                background Frame("wells/gui/label_frame.png", 10, 10)
                padding (40, 10) # Espaço interno para o texto respirar dentro da moldura
                
                text "WELLS MENU" xalign 0.5 size 42 color "#ff4444" outlines [(2, "#000", 0, 0)]

            hbox:
                xalign 0.5 spacing 60 

                # --- COLUNA 1: SISTEMA (FONTES) ---
                vbox:
                    xsize 420 spacing 15 
                    
                    # --- SUBTÍTULO (LABEL) COM MOLDURA ---
                    label _("FONTS"):
                        xalign 0.5 
                        text_size 26 
                        text_color "#347bff"
                        padding (25, 6) # Margem interna menor para combinar com o tamanho do texto
                        background Frame("wells/gui/label_frame.png", 10, 10)

                    frame:
                        xsize 380 ysize 220 background Solid("#00000066")
                        viewport:
                            id "vp_fonts" scrollbars "vertical" mousewheel True draggable True
                            vbox spacing 8 xfill True:
                                for fonte in listar_fontes():
                                    $ f_path = "wells/" + fonte
                                    textbutton fonte:
                                        action [SetField(persistent, "font_escolhida", f_path), Preference("font transform", "wells_custom")]
                                        text_font f_path text_size 24
                                        text_selected_color "#2bff00"
                                        text_hover_color "#ff0000"
                                        selected (persistent.font_escolhida == f_path)

                # --- BOTÃO RESET DE FONTES ---
                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 45)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action [SetField(persistent, "font_escolhida", "wells/Roboto-Regular.ttf"), Preference("font transform", "wells_custom")] 
                        xalign 0.5

                        text _("Reset Font") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                # --- COLUNA 2: TODOS OS SLIDERS (CONTROLES) ---
                vbox:
                    xsize 420 spacing 8
                    
                    # --- TÍTULO DA COLUNA COM MOLDURA ---
                    label _("SOUNDS"):
                        xalign 0.5 
                        text_size 26 
                        text_color "#347bff"
                        padding (25, 6)
                        background Frame("wells/gui/label_frame.png", 10, 10)

                    vbox spacing 4:
                        # --- CONTROLE DE MÚSICA ---
                        label _("Music"):
                            text_size 24 
                            text_color "#2cf1ff"
                            padding (15, 4) # Margem menor para textos menores das barras
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        
                        bar:
                            value Preference("music volume") 
                            xsize 400 ysize 25
                            
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1

                        # --- CONTROLE DE EFEITOS (SFX) ---
                        label _("SFX"):
                            text_size 24 
                            text_color "#2cf1ff"
                            padding (15, 4)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        
                        bar:
                            value Preference("sound volume") 
                            xsize 400 ysize 25
                            
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1

                        # --- CONTROLE DE VOZ ---
                        label _("Voice"):
                            text_size 24 
                            text_color "#2cf1ff"
                            padding (15, 4)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        
                        bar:
                            value Preference("voice volume") 
                            xsize 400 ysize 25
                            
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1

                    vbox spacing 10:

                    # --- BOTÃO MUDO ---
                        button:
                            padding (0, 0, 0, 0)
                            xysize (180, 45)
                            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                            action Preference("all mute", "toggle")
                            xalign 0.5

                            text _("MUTE") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

        # --- BOTÕES DE NAVEGAÇÃO INFERIORES SUBST. POR IMAGENS ---
        # --- BOTÃO 1: IDIOMAS ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45)
            xpos 180 ypos 650 xanchor 0.5 # Mantém a posição exata da esquerda
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action [Show("idioma_seletor"), Hide("wells_menu_language")]

            text _("Idiomas") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

        # --- BOTÃO 2: PERFORMANCE ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45)
            xpos 420 ypos 650 xanchor 0.5
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action [Show("menu_performance"), Hide("wells_menu_language")]

            text _("Performance") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

        # --- BOTÃO 3: DIÁLOGO ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45)
            xpos 660 ypos 650 xanchor 0.5
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action [Show("dialogue_adjusts"), Hide("wells_menu_language")]

            text _("Diálogo") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

        # --- BOTÃO 4: FECHAR ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45)
            xpos 900 ypos 650 xanchor 0.5 # Mantém a posição exata da direita
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action [Hide("wells_menu_language")]

            text _("Fechar") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

################################################################################
## 3. SCREEN IDIOMA SELETOR (COM MOLDURAS)
################################################################################

screen idioma_seletor():
    modal True
    zorder 200
    tag menu
    add Solid("#00000080") 

    frame:
        xalign 0.5 yalign 0.4
        background Frame("wells/gui/frame_menu.png", 10, 10)

        # --- LÓGICA DE RESOLUÇÃO E MOBILE ---
        if config.screen_width == 1920:
            if renpy.variant("small"):
                xsize 1600 ysize 950 padding (60, 50)
            else:
                xsize 1450 ysize 820 padding (50, 40)
        else:
            xsize 1150 ysize 680 padding (40, 35)

        # Usamos uma vbox principal contendo o título e a lista centralizada
        vbox:
            xfill True
            yalign 0.25         # Subi levemente para compensar o espaço das novas molduras
            spacing 35          
            
            # --- TÍTULO PRINCIPAL COM MOLDURA ---
            frame:
                xalign 0.5
                background Frame("wells/gui/label_frame.png", 10, 10)
                padding (40, 10)
                
                text "LANGUAGE SELECTOR" xalign 0.5 size 42 color "#ff4444" outlines [(2, "#000", 0, 0)]

            # Bloco de tradução isolado e centralizado para ignorar quebras do jogo
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15
                
                if renpy.variant("small"):
                    xsize 400 
                else:
                    xsize 380
                    
                # --- SUBTÍTULO COM MOLDURA ---
                label _("TRANSLATION"):
                    xalign 0.5 
                    text_size 26 
                    text_color "#347bff"
                    padding (25, 6)
                    background Frame("wells/gui/label_frame.png", 10, 10)
                
                # Uma vbox dedicada apenas aos botões, com alinhamento forçado ao centro
                vbox:
                    xalign 0.5
                    spacing 6
                    style_prefix "radio"
                    
                    $ langs = get_all_languages()
                    for lang in langs:
                        textbutton "[lang]".capitalize():
                            action Language(None if lang=="Default" else lang)
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_selected_idle_color "#2bff00"
                            text_selected_hover_color "#2bff00"
                            text_size 22
                            xalign 0.5

        # --- BOTÃO VOLTAR CONVERTIDO PARA O NOVO PADRÃO ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45) # Mantém o tamanho idêntico de toda a interface
            xpos 900 ypos 590 xanchor 0.5 # Mantém a posição exata na direita
            
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action Show("wells_menu_language")
            
            text _("Voltar") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

################################################################################
## 4. SCREEN DE DIALOGOS (PARTE 1)
################################################################################

screen dialogue_adjusts():
    modal True
    zorder 200
    tag menu
    add Solid("#00000080") 

    frame:
        xalign 0.5 yalign 0.4
        background Frame("wells/gui/frame_menu.png", 10, 10)

        # --- LÓGICA DE RESOLUÇÃO E MOBILE ---
        if config.screen_width == 1920:
            if renpy.variant("small"):
                xsize 1600 ysize 950 padding (60, 50)
            else:
                xsize 1450 ysize 820 padding (50, 40)
        else:
            xsize 1150 ysize 680 padding (40, 35)

        vbox:
            xfill True
            spacing 25

            # --- TÍTULO DO DIÁLOGO COM MOLDURA ---
            frame:
                xpos 550
                xanchor 0.5
                ypos 25
                background Frame("wells/gui/label_frame.png", 10, 10)
                padding (40, 10)
                
                text "DIALOGUE MENU":
                    size 42
                    color "#ff4444"
                    outlines [(2, "#000", 0, 0)]

        # CONTEÚDO PRINCIPAL DIVIDIDO EM DUAS COLUNAS
        hbox:
            xalign 0.5
            yalign 0.45          # Centraliza o bloco principal verticalmente com mais precisão
            spacing 60           # Ajuste leve no espaço horizontal entre colunas

            # COLUNA DA ESQUERDA (Barras + Configurações de Texto Organizadas)
            hbox:
                spacing 40 
                yalign 0.0

                # SUBCOLUNA 1: Barras Principais de Diálogo
                vbox:
                    spacing 12   # Espaçamento levemente reduzido para ganhar área vertical
                    yalign 0.0

                    vbox spacing 4:
                        label _("Tam. Nome: [persistent.pref_text_size_label]"):
                            text_size 22 
                            text_color "#2cf1ff"
                            padding (15, 2)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        bar:
                            value FieldValue(persistent, 'pref_text_size_label', range=60, step=2) 
                            xsize 380 ysize 25
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        
                    vbox spacing 4:
                        label _("Tam. Diálogo: [persistent.pref_text_size_dialogue]"):
                            text_size 22 
                            text_color "#2cf1ff"
                            padding (15, 2)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        bar:
                            value FieldValue(persistent, 'pref_text_size_dialogue', range=60, step=2) 
                            xsize 380 ysize 25
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        
                    vbox spacing 4:
                        label _("Velocidade do texto"):
                            text_size 22 
                            text_color "#2cf1ff"
                            padding (15, 2)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        bar:
                            value Preference("text speed") 
                            xsize 380 ysize 25
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        
                    vbox spacing 4:
                        label _("Tempo do texto"):
                            text_size 22 
                            text_color "#2cf1ff"
                            padding (15, 2)
                            background Frame("wells/gui/label_frame.png", 10, 10)
                        bar:
                            value Preference("auto-forward time") 
                            xsize 380 ysize 25
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                # SUBCOLUNA 2: Ajustes Avançados de Escala e Espaçamento (Compactada)
                vbox:
                    spacing 8     # Menos espaço entre os blocos avançados
                    yalign 0.0

                    # Bloco Text Scaling
                    vbox spacing 2:
                        frame:
                            xalign 0.5
                            background Frame("wells/gui/label_frame.png", 10, 10)
                            padding (15, 2)
                            text "Text Scaling:" size 22 color "#2cf1ff" xalign 0.5
                        bar:
                            value Preference("font size") 
                            xsize 320 ysize 25 xalign 0.5
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        textbutton _("Reset Size"):
                            action Preference("font size", 1.0)
                            xalign 0.5 text_size 16 text_hover_color "#ff4444" yoffset -2

                    # Bloco Line Spacing
                    vbox spacing 2:
                        frame:
                            xalign 0.5
                            background Frame("wells/gui/label_frame.png", 10, 10)
                            padding (15, 2)
                            text "Line Spacing:" size 22 color "#2cf1ff" xalign 0.5
                        bar:
                            value FieldValue(persistent, "wells_line_spacing", range=50, offset=0) 
                            xsize 320 ysize 25 xalign 0.5
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        textbutton _("Reset Spacing"):
                            action Preference("font line spacing", 1.0)
                            xalign 0.5 text_size 16 text_hover_color "#ff4444" yoffset -2

                    # Bloco Dialogue V offset
                    vbox spacing 2:
                        frame:
                            xalign 0.5
                            background Frame("wells/gui/label_frame.png", 10, 10)
                            padding (15, 2)
                            text "Dialogue V offset:" size 22 color "#2cf1ff" xalign 0.5
                        bar:
                            value FieldValue(persistent, "wells_dialogue_y_offset", range=100, offset=-50) 
                            xsize 320 ysize 25 xalign 0.5
                            idle_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            hover_right_bar Frame("wells/gui/barra_vazia.png", 5, 5)
                            idle_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            hover_left_bar Frame("wells/gui/barra_cheia.png", 5, 5)
                            thumb "wells/gui/pino.png"
                            thumb_shadow None
                            thumb_offset 1
                        textbutton "Reiniciar Altura":
                            action SetField(persistent, "wells_dialogue_y_offset", 0)
                            xalign 0.5 text_size 16 text_hover_color "#ff4444" yoffset -2
            # COLUNA DA DIREITA (Compatibilidade e Modos)
            vbox:
                spacing 8       # Reduzido de 15 para 8 para caber perfeitamente no frame vertical
                yalign 0.0

                # Seção CONFIGURAÇÕES DE CLIQUE
                vbox:
                    spacing 6
                    style_prefix "wells_menu_check"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Preference("skip", "toggle")
                        xalign 0.5
                        text _("Pular Texto") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Preference("after choices", "toggle")
                        xalign 0.5
                        text _("Após Escolhas") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-hover.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action InvertSelected(Preference("transitions", "toggle"))
                        xalign 0.5
                        text _("Transições") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                # Seção CLIQUE LATERAL (ROLLBACK)
                vbox:
                    spacing 6
                    style_prefix "wells_menu_radio"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Preference("rollback side", "disable")
                        xalign 0.5
                        text _("Desabilitado") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Preference("rollback side", "left")
                        xalign 0.5
                        text _("Esquerda") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Preference("rollback side", "right")
                        xalign 0.5
                        text _("Direita") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                # SELEÇÃO DO MODO DA TEXTBOX (MODO CAMALEÃO)
                vbox:
                    spacing 6
                    style_prefix "wells_menu_radio"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action SetField(persistent, "wells_say_mode", 0)
                        selected (persistent.wells_say_mode == 0)
                        xalign 0.5
                        text _("Padrão") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action SetField(persistent, "wells_say_mode", 1)
                        selected (persistent.wells_say_mode == 1)
                        xalign 0.5
                        text _("Camaleão") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Function(toggle_multiple_dialogue)
                        xalign 0.5
                        text "Dual Dialogue" xalign 0.5 yalign 0.5 size 16 color ("#2bff00" if persistent.multiple_dialogue else "#ffffff") hover_color "#2bff00"

                    button:
                        padding (0, 0, 0, 0)
                        xysize (180, 42)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action ToggleField(persistent, "wells_dual_dialogue_fix")
                        xalign 0.5
                        text "Diag. Fix: [persistent.wells_dual_dialogue_fix]" xalign 0.5 yalign 0.5 size 18 color "#42bef8" hover_color "#2bff00"


        # --- BOTÃO VOLTAR CONVERTIDO PARA O NOVO PADRÃO ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45)
            xpos 550 ypos 600 xanchor 0.5 # Leve ajuste em ypos para dar folga de segurança

            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action Show("wells_menu_language")

            text _("Voltar") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

################################################################################
## 5. SCREEN PERFORMANCE (VERSÃO PADRONIZADA COM MOLDURAS)
################################################################################

screen menu_performance():
    modal True
    zorder 200
    tag menu
    add Solid("#00000080") 

    frame:
        xalign 0.5 yalign 0.4
        background Frame("wells/gui/frame_menu.png", 10, 10)

        # --- LÓGICA DE RESOLUÇÃO E MOBILE ---
        if config.screen_width == 1920:
            if renpy.variant("small"):
                xsize 1600 ysize 950 padding (60, 50)
            else:
                xsize 1450 ysize 820 padding (50, 40)
        else:
            xsize 1150 ysize 680 padding (40, 35)

        vbox:
            xfill True
            spacing 25
            
            # --- TÍTULO PRINCIPAL COM MOLDURA ---
            frame:
                xalign 0.5
                background Frame("wells/gui/label_frame.png", 10, 10)
                padding (40, 10)
                
                text "PERFORMANCE" xalign 0.5 size 42 color "#ff4444" outlines [(2, "#000", 0, 0)]

            hbox:
                xalign 0.5 spacing 60 
                vbox:
                    spacing 15 xfill True   # Reduzido de 20 para 15 para dar margem vertical
                    hbox:
                        xalign 0.5 spacing 40

                        # --- COLUNA: PERFORMANCE (configuração) ---
                        vbox:
                            xsize 400 spacing 12
                            
                            # --- SUBTÍTULO SYSTEM COM MOLDURA ---
                            frame:
                                xalign 0.5
                                background Frame("wells/gui/label_frame.png", 10, 10)
                                padding (25, 4)
                                text "SYSTEM" xalign 0.5 size 28 color "#3d8afd"

                            vbox:
                                spacing 6 xfill True
                                
                                # --- SUBTÍTULO VIDEO PERFORMANCE COM MOLDURA ---
                                frame:
                                    xalign 0.5
                                    background Frame("wells/gui/label_frame.png", 10, 10)
                                    padding (15, 2)
                                    text "VIDEO PERFORMANCE" size 24 color "#2cf1ff" xalign 0.5

                                $ current_fps = "30 FPS" if preferences.gl_framerate == 30 else "60 FPS"
                                textbutton "Limit FPS: [current_fps]":
                                    xalign 0.5
                                    action Function(toggle_power_save)
                                    text_hover_color "#2bff00"
                                    text_size 28

                                $ gl_ps_status = "ON" if preferences.gl_powersave else "OFF"
                                textbutton "Economia de energia: [gl_ps_status]":
                                    xalign 0.5
                                    action Preference("gl powersave", "toggle")
                                    text_hover_color "#2bff00"
                                    text_size 28

                            vbox:
                                spacing 6 xfill True
                                
                                # --- SUBTÍTULO RENDERIZAÇÃO COM MOLDURA ---
                                frame:
                                    xalign 0.5
                                    background Frame("wells/gui/label_frame.png", 10, 10)
                                    padding (15, 2)
                                    text "RENDERIZAÇÃO DE VÍDEO" size 22 color "#aaa" xalign 0.5
                                
                                $ hw_label = "Hardware (GPU)" if persistent.use_hw_video else "Software (CPU)"
                                textbutton "Decoding: [hw_label]":
                                    xalign 0.5
                                    action [ToggleField(persistent, "use_hw_video"), Notify("Restart game to apply changes")]
                                    text_hover_color "#2bff00"
                                    text_size 28

                                text "Use o software se você vir uma tela preta." size 22 color "#666" xalign 0.5

        # --- BOTÃO VOLTAR CONVERTIDO PARA O NOVO PADRÃO ---
        button:
            padding (0, 0, 0, 0)
            xysize (180, 45) # Mantém o tamanho padrão dos outros botões
            xpos 550 ypos 560 xanchor 0.5 # Mantém a posição original dele na tela
            
            idle_background Frame("wells/gui/Button-idle.png", 5, 5)
            hover_background Frame("wells/gui/Button-hover.png", 5, 5)
            action Show("wells_menu_language")
            
            text _("Voltar") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"


################################################################################
## PARTE 1: O BOTÃO AZUL MÓVEL (ESTÁVEL E SEM CONFLITOS)
################################################################################

# Variáveis originais mantidas para o botão lembrar a posição onde foi solto
init python:
    if not hasattr(store, 'wells_x'):
        store.wells_x = 14
    if not hasattr(store, 'wells_y'):
        store.wells_y = 500

    def salvar_pos_botao(drags, drop):
        store.wells_x = drags[0].x
        store.wells_y = drags[0].y
        return

transform wells_float_right:
    xanchor 0.0 yanchor 1.0
    on show:
        xpos -1000
        easein 0.5 xpos 0.0
    on hide:
        easeout 0.5 xpos -1000

# Esta tela agora SÓ cuida do botão azul pequeno
screen quick_menu():
    zorder 199
    tag quick_menu
    modal False 

    if quick_menu:
        draggroup:
            drag:
                drag_name "id_botao_fechado" 
                draggable True
                drag_raise True
                dragged salvar_pos_botao

                xanchor 0.0
                yanchor 0.0
                xpos store.wells_x
                ypos store.wells_y

                frame:
                    at wells_float_right
                    background Frame("wells/gui/base_nova.png", 3, 3)
                    padding (30, 10, 30, 10)  # Ajustado um pouco para não sobrar muita borda

                    # A MÁGICA ACONTECE AQUI: Organizador horizontal
                    hbox:
                        spacing 6 # Deixa um espaço de 15 pixels entre os dois botões
                        yalign 0.5 # Centraliza os dois botões na linha vertical

                    # PRIMEIRO BOTÃO: Quick
                        button:
                            padding (0, 0, 0, 0)
                            xysize (70, 40) 
                            idle_background Frame("wells/gui/Button-idle.png", 3, 3)
                            hover_background Frame("wells/gui/Button-hover.png", 3, 3)
                            action [Hide("quick_menu"), Show("quick_mod")]
                            text _("Quick") xalign 0.5 yalign 0.5 size 20 hover_color "#2bff00"

                    # --- BOTÃO 2: VOLTAR ---
                        button:
                            padding (0, 0, 0, 0)
                            xysize (70, 40)
                            idle_background Frame("wells/gui/Button-idle.png", 3, 3)
                            hover_background Frame("wells/gui/Button-hover.png", 3, 3)
                            action [Rollback()]
                            xalign 0.5
                            text _("Back") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                    # --- BOTÃO 3: PULAR ---
                        button:
                            padding (0, 0, 0, 0)
                            xysize (70, 40)
                            idle_background Frame("wells/gui/Button-idle.png", 3, 3)
                            hover_background Frame("wells/gui/Button-hover.png", 3, 3)
                            action [Skip()] 
                            alternate Skip(fast=True, confirm=True)
                            xalign 0.5
                            text _("Skip") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

################################################################################
## PARTE 2 TELA DE PAUSA CENTRALIZADA
################################################################################
screen quick_mod():
    zorder 199          # Fica por cima de tudo
    tag quick_menu_tela # Tag própria para não conflitar
    modal True          # Bloqueia TOTALMENTE cliques fora da caixinha

    # Frame em tela cheia com a sombra suave de fundo
    frame:
        style "empty"
        background Solid("#00000060") 
        xsize 1.0 ysize 1.0   

        # CAIXINHA CENTRALIZADA: Com tamanho travado para não esticar!
        frame:
            xalign 0.5
            yalign 0.5
            style "empty"

            # Carrega a sua imagem personalizada
            background Frame("wells/gui/quickbox.png", 20, 20)

            # AJUSTE DE TAMANHO: Define a largura e altura exatas da caixinha
            # Se faltar ou sobrar espaço, basta mudar esses dois números abaixo
            xsize 340
            ysize 600

            # AJUSTE DE MARGENS: (Esquerda, Topo, Direita, Baixo)
            padding (35, 45, 35, 5)

            # O vbox empilha os novos botões inteligentes na vertical
            vbox:
                spacing 12
                xalign 0.5
                yalign 0.5
                xsize 220 # Força a largura interna para alinhar os botões
                style_prefix "wells_menu_quick"

                # --- BOTÃO 1: FECHAR ---
                button:
                    padding (0, 0, 0, 0)
                    xysize (180, 45) # TRAVA O TAMANHO DO BOTÃO (Largura, Altura)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action [Hide("quick_mod"), Show("quick_menu")]
                    xalign 0.5

                    text _("Close") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                # --- BOTÃO 4: SALVAR ---
                button:
                    padding (0, 0, 0, 0)
                    xysize (180, 45)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action [ShowMenu("save"), Hide("quick_mod"), Show("quick_menu")] 
                    xalign 0.5
                    text _("Save") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                # --- BOTÃO 5: CARREGAR ---
                button:
                    padding (0, 0, 0, 0)
                    xysize (180, 45)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action [ShowMenu("load"), Hide("quick_mod"), Show("quick_menu")] 
                    xalign 0.5
                    text _("Load") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                # --- BOTÃO 6: OPÇÕES ---
                button:
                    padding (0, 0, 0, 0)
                    xysize (180, 45)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action [ShowMenu("preferences"), Hide("quick_mod"), Show("quick_menu")] 
                    xalign 0.5
                    text _("Config") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"

                # --- BOTÃO 7: MENU UNIVERSAL ---
                button:
                    padding (0, 0, 0, 0)
                    xysize (180, 45)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action [Show("wells_menu_language"), Hide("quick_mod")] 
                    xalign 0.5
                    text _("Wells Menu") xalign 0.5 yalign 0.5 size 22 hover_color "#2bff00"


################################################################################
## ESTILOS ADICIONAIS E ESTRUTURA GLOBAL
################################################################################
init -1 style wells_menu_slider_label is pref_label
init -1 style wells_menu_slider_label_text is label_text
init -1 style wells_menu_slider_slider is gui_slider
init -1 style wells_menu_slider_button is gui_button
init -1 style wells_menu_slider_button_text is gui_button_text
init -1 style wells_menu_slider_pref_vbox is pref_vbox
init -1 style wells_menu_check_button_text is button_text
init -1 style wells_menu_radio_button_text is button_text

if not renpy.variant("small"):
    init -1 style wells_menu_slider_label_text:
        size 28
    init -1 style wells_menu_check_button_text:
        size 28
    init -1 style wells_menu_radio_button_text:
        size 28
    init -1 style wells_menu_slider_slider:
        xsize 400
    init -1 style wells_menu_slider_button:
        yalign 0.5
        left_margin 15
    init -1 style wells_menu_slider_button_text:
        size 18
        font "Roboto-Regular.ttf"
    init -1 style wells_menu_slider_vbox:
        xsize 675
################################################################################
## SCREEN SAY (SISTEMA ADAPTATIVO CAMALEÃO)
################################################################################
init 999 screen say(who, what, multiple=None):
    if config.screen_width == 1280:
        style_prefix "say_wells_1280"
    if config.screen_width == 1920:
        style_prefix "say_wells_1920"

    if persistent.wells_say_mode == 0:
        if persistent.wells_dual_dialogue_fix:
            window:
                id "window"
                if multiple and multiple > 0:
                    yoffset (persistent.wells_dual_dialogue_offset * multiple)
                else:
                    yoffset (persistent.wells_dialogue_y_offset if persistent.wells_dialogue_y_offset is not None else 0)

                if config.screen_width == 1280:
                    style "say_wells_1280"
                if config.screen_width == 1920:
                    style "say_wells_1920"

                if who is not None:
                    window:
                        if config.screen_width == 1280:
                            style "namebox_wells_1280"
                        if config.screen_width == 1920:
                            style "namebox_wells_1920"
                        text who id "who":
                            size (persistent.pref_text_size_label or 22)

                text what id "what":
                    if config.screen_width == 1920:
                        ypos -15
                        xpos (255 if who else 0.2)
                        xsize 1316
                        line_spacing (persistent.wells_line_spacing or 5)
                        size (persistent.pref_text_size_dialogue or 28)
                        color "#FFFFFF"
                        outlines [(absolute(4), "#000000", 0, 0)]
        else:
            window:
                if multiple and multiple > 0:
                    yoffset (persistent.wells_dual_dialogue_offset * multiple)
                else:
                    yoffset (persistent.wells_dialogue_y_offset if persistent.wells_dialogue_y_offset is not None else 0)

                if config.screen_width == 1280:
                    style "say_wells_1280"
                if config.screen_width == 1920:
                    style "say_wells_1920"

                if who is not None:
                    window:
                        if config.screen_width == 1280:
                            style "namebox_wells_1280"
                        if config.screen_width == 1920:
                            style "namebox_wells_1920"
                        text who id "who":
                            size (persistent.pref_text_size_label or 22)

                text what id "what":
                    if config.screen_width == 1920:
                        ypos -15
                        xpos (255 if who else 0.2)
                        xsize 1316
                        line_spacing (persistent.wells_line_spacing or 5)
                        size (persistent.pref_text_size_dialogue or 28)
                        color "#FFFFFF"
                        outlines [(absolute(4), "#000000", 0, 0)]

    elif persistent.wells_say_mode == 1:
        style_prefix "say"
        window:
            id "window"
            if multiple and multiple > 0:
                yoffset (persistent.wells_dual_dialogue_offset * multiple)
            else:
                yoffset (persistent.wells_dialogue_y_offset if persistent.wells_dialogue_y_offset is not None else 0)

            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who":
                        size (persistent.pref_text_size_label or 22)

            text what id "what":
                line_spacing (persistent.wells_line_spacing or 5)
                size (persistent.pref_text_size_dialogue or 28)
                color "#FFFFFF"
                outlines [(absolute(4), "#000000", 0, 0)]

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

################################################################################
## ESTILOS DA SCREEN SAY (1280 E 1920)
################################################################################
init -1 style say_wells_1280_window is default
init -1 style say_wells_1280_label is default
init -1 style say_wells_1280_dialogue is default
init -1 style say_wells_1280_thought is say_wells_1280_dialogue
init -1 style namebox_wells_1280 is default
init -1 style namebox_wells_1280_label is say_wells_1280_label

init -1 style say_wells_1280:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 195
    background Image("wells/gui/textbox1280.png", xalign=0.5, yalign=1.0)

init -1 style namebox_wells_1280:
    xpos 240
    xanchor 0.5
    xsize None
    ypos 0
    ysize None
    background Frame("wells/gui/namebox1280.png", wells_namebox_borders, tile=False, xalign=0.0)
    padding wells_namebox_borders.padding

init -1 style say_wells_1280_label:
    outlines [ (absolute(2), "#000000", absolute(0), absolute(10)) ]
    xalign 0.0
    yalign 1.5

init -1 style say_wells_1280_dialogue:
    outlines [ (absolute(5), "#000000", absolute(0), absolute(0)) ]
    xpos 268
    xsize 1100
    ypos 50

# --- SEÇÃO 1920 ---
init -1 style say_wells_1920_window is default
init -1 style say_wells_1920_label is default
init -1 style say_wells_1920_dialogue is default
init -1 style say_wells_1920_thought is say_wells_1920_dialogue
init -1 style namebox_wells_1920 is default
init -1 style namebox_wells_1920_label is say_wells_1920_label

init -1 style say_wells_1920:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 195
    background Image("wells/gui/textbox1920.png", xalign=0.5, yalign=1.0)

init -1 style namebox_wells_1920:
    xpos 400
    xanchor 0.5
    xsize None
    ypos -80
    ysize None
    background Frame("wells/gui/namebox1920.png", wells_namebox_borders, tile=False, xalign=0.0)
    padding wells_namebox_borders.padding

init -1 style say_wells_1920_label:
    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    xalign 0.5
    yalign 1.5

init -1 style say_wells_1920_dialogue:
    outlines [ (absolute(5), "#000000", absolute(0), absolute(0)) ]
    xpos 268
    xsize 1100
    ypos 50

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background Image("wells/gui/frame.png")

init -501 screen input(prompt):
    style_prefix "input"
    window:
        if renpy.variant("small"):
            yalign 0.2
        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

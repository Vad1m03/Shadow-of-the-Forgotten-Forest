# ============================================================
# ПЕРСОНАЖИ
# ============================================================
define e = Character('Элара', color="#c8ffc8")
define a = Character('Ариан', color="#aaaaff")
define narrator = Character(None)
define whisper = Character('Шёпот', color="#666666")
define demon = Character('???', color="#ff0000")

init:
    $ Flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# ============================================================
# ПЕРЕМЕННЫЕ
# ============================================================
default sanity = 10
default clues = 0
default trust = 0

# ============================================================
# СПРАЙТЫ
# ============================================================
image elara neutral = Transform("elara_neutral.png", xysize=(600, 900), fit="contain")
image elara scared  = Transform("elara_scared.png",  xysize=(600, 900), fit="contain")
image elara angry   = Transform("elara_angry.png",   xysize=(600, 900), fit="contain")

image arian normal  = Transform("arian_normal.png",  xysize=(600, 900), fit="contain")
image arian demon   = Transform("arian_demon.png",   xysize=(600, 900), fit="contain")
image elara corrupted = Transform("elara_shadow.png", xysize=(600, 900), fit="contain")

# ============================================================
# ФОНЫ
# ============================================================
image white = Solid("#ffffff")  # Белый экран для вспышки
image black = Solid("#000000")  # Чёрный экран (уже есть)
image bg_village       = Transform("bg_village.png", xysize=(1920,1080), fit="cover")
image bg_forest_dark   = Transform("bg_forest_dark.png", xysize=(1920,1080), fit="cover")
image bg_labyrinth     = Transform("bg_labyrinth.png", xysize=(1920,1080), fit="cover")
image bg_cave          = Transform("bg_cave.png", xysize=(1920,1080), fit="cover")
image bg_swamp         = Transform("bg_swamp.png", xysize=(1920,1080), fit="cover")
image bg_ruins         = Transform("bg_ruins.png", xysize=(1920,1080), fit="cover")
image bg_dark_forest   = Transform("bg_dark_forest.png", xysize=(1920,1080), fit="cover")
image bg_heart_chamber = Transform("bg_heart_chamber.png", xysize=(1920,1080), fit="cover")
image bg_village_saved1 = Transform("bg_village_saved1.png", xysize=(1920,1080), fit="cover")
image bg_village_saved2 = Transform("bg_village_saved2.png", xysize=(1920,1080), fit="cover")
image bg_eternal_dark   = Transform("bg_eternal_dark.png", xysize=(1920,1080), fit="cover")
image bg_shadow_throne = Transform("bg_eternal_dark.png", xysize=(1920,1080), fit="cover")

# ============================================================
# ПОЗИЦИИ
# ============================================================
transform hero_pos:
    xalign 0.15 yalign 1.0

transform companion_pos:
    xalign 0.85 yalign 1.0

transform center_pos:
    xalign 0.5 yalign 1.0

# ============================================================
# СТИЛИ МЕНЮ ВЫБОРА (ниже экрана, меньше шрифт)
# ============================================================
style choice_button:
    xalign 0.5
    yalign 0.78
    xsize 900
    ysize 90
    background "#000000cc"
    hover_background "#ffffff33"
    padding (30, 20)

style choice_button_text:
    size 30
    xalign 0.5
    color "#eeeeee"
    hover_color "#ffffff"
    outlines [(3, "#000000", 0, 0)]

# ============================================================
# СЦЕНАРИЙ
# ============================================================

label start:
    scene black
    pause 1.5

    narrator "Три недели. Столько деревня Ольховка протянет без лекарства."
    narrator "Теневая Чума не убивает сразу. Она крадёт тебя по кусочкам."
    pause 1.0

    scene bg_village with Dissolve(2.5)
    play music "village_ominous.ogg" fadein 3.0 loop volume 0.45
    pause 1.2

    show elara neutral at hero_pos with Dissolve(1.0)

    narrator "Элара стоит на краю деревни. За спиной — кашель умирающих. Впереди — Запретный Лес."

    e "Мама говорила — лес забирает тех, кто входит."
    e "Но если я останусь, забирать будет некого."

    show elara scared with Dissolve(0.5)
    pause 0.7

    narrator "Старейшина рассказал о Сердце Тени — артефакте в глубине леса. Единственном средстве против Чумы."

    e "Соберись, Элара. Ты травница. Ты знаешь яды и лекарства."
    e "Этот лес — просто ещё один яд. Нужно найти противоядие."

    show elara neutral with Dissolve(0.5)

    menu:
        "Взять отцовский нож":
            $ sanity += 1
            e "Он не волшебный. Но с ним я чувствую себя... не одной."
        "Взять мамин гербарий":
            $ clues += 1
            e "Здесь есть записи о лесных травах. Может пригодиться."

    e "Прости, папа. Я вернусь. Обещаю."

    scene black with Dissolve(1.8)
    pause 1.0
    jump entry


label entry:
    scene bg_forest_dark with Dissolve(2.5)
    pause 0.8
    play music "forest_tension.ogg" fadein 2.0 loop volume 0.4
    play sound "whispers_loop.ogg" loop volume 0.3

    show elara neutral at hero_pos with Dissolve(1.0)

    narrator "Первые шаги — и мир меняется. Свет гаснет, будто лес проглотил солнце."

    e "Тихо. Слишком тихо. Даже птиц нет."

    pause 0.8

    show elara scared with Dissolve(0.5)

    whisper "Вернись..."
    whisper "Здесь нечего искать..."
    whisper "Ты уже мертва..."

    e "Что... Кто здесь?!"

    narrator "Шёпот идёт отовсюду. Из деревьев, из земли, из собственной головы."

    menu:
        "Шагнуть вперёд, не оглядываясь":
            $ sanity += 1
            show elara angry with Dissolve(0.5)
            e "Я пришла не болтать с деревьями. Прочь с дороги."
            narrator "Шёпот стихает. Ненадолго."
            show elara neutral with Dissolve(0.5)
        "Идти тихо, прислушиваясь":
            $ sanity -= 1
            show elara scared with Dissolve(0.5)
            narrator "Каждый шорох — как чьё-то дыхание за спиной."
            e "Мне кажется... кто-то идёт за мной."

    pause 0.8
    narrator "Треск ветки. Совсем рядом."

    show arian normal at companion_pos with Dissolve(1.0)

    narrator "Из тени выходит юноша. Бледный, с серебристыми глазами. Улыбается, будто встретил старую подругу."

    a "Тише. Ты разбудишь то, что лучше не будить."

    e "Ты... живой? Что ты делаешь в этом лесу?"

    a "Живой — это сильно сказано. Я — Ариан. Можно сказать, местный проводник."

    e "Проводник? Сюда никто не заходит годами."

    a "Именно поэтому мне так скучно."

    narrator "Он говорит легко, почти весело. Но его глаза не улыбаются."

    a "Ты ищешь Сердце Тени, верно? Все, кто приходят, ищут его."

    e "Все? Значит, были другие?"

    a "..."

    a "Идём. Одна ты не дойдёшь и до первого поворота."

    menu:
        "Довериться Ариану":
            $ trust += 1
            $ sanity += 1
            show elara neutral with Dissolve(0.5)
            e "У меня нет выбора. Веди."
            a "Разумно. Держись рядом и не трогай ничего светящегося."
        "Держать дистанцию":
            $ trust -= 1
            show elara neutral with Dissolve(0.5)
            e "Я пойду за тобой. Но не слишком близко."
            a "Как хочешь. Только не отставай."
            narrator "Что-то в его голосе... Слишком спокоен для человека в проклятом лесу."

    pause 0.6
    jump labyrinth


label labyrinth:
    scene bg_labyrinth with Dissolve(2.0)
    play music "labyrinth_dark.ogg" loop fadein 1.5 volume 0.45

    show elara neutral at hero_pos with Dissolve(1.0)
    if trust >= 1:
        show arian normal at companion_pos with Dissolve(1.0)

    narrator "Стены из переплетённых корней. Они двигаются — медленно, почти незаметно."

    e "Этот проход... его только что не было."

    if trust >= 1:
        a "Лес меняется. Не пытайся запомнить дорогу — она не повторяется."
        e "Откуда ты всё это знаешь?"
        a "Я здесь давно, Элара. Очень давно."
        e "Я не говорила тебе своё имя."
        a "..."
        a "Наверное, услышал в шёпоте. Лес знает тех, кто входит."
    else:
        narrator "Ариан идёт впереди молча. Иногда оглядывается — проверяет."

    narrator "На стене — древние символы. Один из них пульсирует слабым светом."

    menu:
        "Коснуться светящегося символа":
            $ clues += 1
            $ sanity -= 1
            show elara scared with Dissolve(0.5)
            narrator "Вспышка. В голове — чужой голос, древний и холодный."
            whisper "Руна первая: Тень — не снаружи. Тень — В ТЕБЕ."
            e "Что это значит?.."
            if trust >= 1:
                a "Стены врут. Не забивай голову."
                narrator "Он говорит быстро. Слишком быстро."
            show elara neutral with Dissolve(0.5)
        "Пройти мимо":
            $ sanity -= 2
            show elara scared with Dissolve(0.5)
            narrator "Тени на стенах вытягиваются, тянутся к ногам."
            e "Быстрее... нужно идти быстрее!"

    pause 0.6

    if trust >= 1:
        a "Элара. Здесь есть правило: лес показывает то, чего ты боишься."
        e "А если я ничего не боюсь?"
        a "Тогда он найдёт, чего тебе бояться."
        narrator "Впервые Ариан говорит без улыбки."

    jump cave


label cave:
    scene bg_cave with Dissolve(2.0)
    play music "cave_mystery.ogg" loop fadein 2.0 volume 0.4

    show elara neutral at hero_pos with Dissolve(1.0)
    if trust >= 1:
        show arian normal at companion_pos with Dissolve(1.0)

    narrator "Капли воды. Эхо. На стене — ещё один символ, покрытый мхом."

    if trust >= 1:
        a "Передохнём здесь. Дальше будет... сложнее."
        e "Ариан, сколько до Сердца Тени?"
        a "Зависит не от расстояния. От тебя."
        e "Ты всегда говоришь загадками?"
        a "Только когда правда звучит хуже загадки."

    narrator "У дальней стены — каменная плита с вырезанным символом."

    menu:
        "Расчистить и прочитать символ":
            $ clues += 1
            narrator "Мох осыпается. Под ним — вторая руна."
            show elara scared with Dissolve(0.5)
            whisper "Руна вторая: Сердце бьётся не в камне. Сердце бьётся В КРОВИ."
            e "Опять... Что за «в крови»? Это про Чуму?"
            if trust >= 1:
                a "Хватит читать стены. Серьёзно."
                e "Почему тебя это так беспокоит?"
                a "Не беспокоит. Просто... бесполезно."
                narrator "Он отводит взгляд."
            show elara neutral with Dissolve(0.5)
        "Не трогать":
            $ sanity -= 1
            play sound "drip.ogg"
            narrator "Капли громче. Или это пульс в ушах?"

    if trust >= 1:
        narrator "Ариан сидит у стены, смотрит на свои руки."
        e "Ты никогда не рассказывал, как попал сюда."
        a "Не попадал. Я просто... всегда здесь."
        e "Это невозможно."
        a "В этом лесу — всё невозможно. И всё реально. Привыкай."
    else:
        narrator "Ариан стоит у входа в пещеру спиной к тебе. Неподвижный, как статуя."
        e "(Он вообще дышит?..)"

    jump swamp


label swamp:
    scene bg_swamp with Dissolve(2.0)
    play music "forest_tension.ogg" loop fadein 1.5 volume 0.45
    play sound "squelch.ogg"

    show elara neutral at hero_pos with Dissolve(1.0)
    if trust >= 1:
        show arian normal at companion_pos with Dissolve(1.0)

    narrator "Корни торчат из чёрной воды. Они шевелятся."

    e "Это... они живые?"

    if trust >= 1:
        a "Не совсем. Они реагируют на страх. Чем больше боишься — тем агрессивнее."
        e "Удобно."
        a "Лес — идеальный хищник. Жертва сама себя убивает."

    narrator "Корень обвивает лодыжку. Медленно, настойчиво."

    menu:
        "Рубить корни":
            $ sanity += 2
            show elara angry with Dissolve(0.5)
            e "НЕ ТРОГАЙ МЕНЯ!"
            narrator "Корень отдёргивается. Остальные замирают."
            if trust >= 1:
                a "Ха. Впечатляет."
                narrator "Первая искренняя реакция Ариана."
        "Замереть, не дышать":
            $ sanity -= 2
            show elara scared with Dissolve(0.5)
            narrator "Корни ползут выше. Колени, бёдра, талия..."
            if trust >= 1:
                narrator "Ариан хватает за руку и дёргает."
                a "Двигайся! Сейчас!"
                $ trust += 1
            else:
                narrator "Рывок — вырываешься сама. Еле-еле."

    show elara neutral with Dissolve(0.5)
    pause 0.6

    if trust >= 2:
        e "Ариан... Спасибо."
        a "Не благодари. Мне нужно, чтобы ты дошла."
        e "Нужно? Зачем?"
        a "У каждого свои причины."
        narrator "Он улыбается. Но глаза — пустые."

    jump ruins


label ruins:
    scene bg_ruins with Dissolve(2.0)
    play music "cave_mystery.ogg" loop fadein 1.5 volume 0.45

    show elara neutral at hero_pos with Dissolve(1.0)
    if trust >= 1:
        show arian normal at companion_pos with Dissolve(1.0)

    narrator "Древний храм. Колонны покрыты теми же символами. Три прохода."

    if trust >= 1:
        a "Центральный путь — самый быстрый. И самый опасный."
        e "А ты какой советуешь?"
        a "Левый. Безопасный. Скучный."
        narrator "Почему он не хочет, чтобы ты шла в центр?"

    menu:
        "Левый проход":
            $ clues += 1
            narrator "Узкий коридор. На стене — третья руна."
            show elara scared with Dissolve(0.5)
            whisper "Руна третья: Проводник и Чума — одно дыхание."
            e "Проводник и Чума..."
            show elara neutral with Dissolve(0.5)
            narrator "Элара оглядывается на Ариана."
            if trust >= 1:
                a "Что? Почему так смотришь?"
                e "Ничего."
                narrator "(Проводник... Он же проводник.)"
        "Правый проход":
            $ sanity -= 1
            show elara scared with Dissolve(0.5)
            narrator "Тупик. Стены сжимаются. Едва успеваешь выбраться."
        "Центральный проход":
            if sanity > 5:
                $ clues += 1
                show elara angry with Dissolve(0.5)
                narrator "Зал. В центре — алтарь. На нём четвёртая руна, пылающая."
                whisper "Руна четвёртая: ВЫЖГИ ИЗНУТРИ. Демон не в лесу. Демон в крови."
                e "Демон в крови..."
                if trust >= 1:
                    narrator "Ариан стоит в дверях. Не заходит."
                    a "Элара, идём. Здесь нечего смотреть."
                    e "Почему ты не заходишь в этот зал, Ариан?"
                    a "...Не люблю алтари."
            else:
                $ sanity -= 2
                show elara scared with Dissolve(0.5)
                narrator "Темнота. Удар. Очнулась на полу у входа."

    show elara neutral with Dissolve(0.5)
    jump guardians


label guardians:
    scene bg_dark_forest with Dissolve(2.0)
    play music "labyrinth_dark.ogg" loop fadein 1.0 volume 0.5
    play sound "scream.ogg"

    show elara scared at hero_pos with Dissolve(1.0)
    show arian normal at companion_pos with Dissolve(1.0)

    narrator "Тени обретают форму. Стражи леса — чёрные силуэты с горящими глазами."

    e "Их... слишком много."

    a "Они не настоящие. Как и всё здесь."

    e "Что значит «как и всё»?"

    a "Потом объясню. Сейчас — сражайся или беги."

    menu:
        "Сражаться вместе с Арианом":
            if trust >= 2:
                $ sanity += 1
                show elara angry with Dissolve(0.5)
                narrator "Ариан встаёт рядом. Спина к спине."
                a "Как в старые времена."
                e "Какие старые времена?!"
                a "Не обращай внимания. Бей!"
                narrator "Стражи рассыпаются. Слишком легко."
                e "(Слишком легко... Будто они его слушаются.)"
            else:
                $ sanity -= 1
                narrator "Ариан помогает, но неохотно. Стражи отступают."
                a "Видишь? Не доверяла — а без меня никуда."
        "Сражаться одной":
            $ sanity += 1
            show elara angry with Dissolve(0.5)
            narrator "Элара кричит — и стражи отшатываются. Злость сильнее страха."
            e "Я! Не! Остановлюсь!"
            narrator "Ариан наблюдает. На его лице — странное выражение. Гордость? Или разочарование?"

    show elara neutral with Dissolve(0.5)
    narrator "Путь открыт. Впереди — пульсирующий свет."

    if trust >= 2:
        e "Ариан. Прежде чем мы войдём туда."
        a "Да?"
        e "Ты ведь не человек, правда?"
        pause 1.0
        a "...А ты умнее, чем я думал."
        a "Идём. Ты заслужила правду."
    else:
        narrator "Ариан идёт вперёд. Его тень на стене... неправильной формы."

    pause 0.6
    jump heart


label heart:
    scene bg_heart_chamber with Dissolve(2.5)
    play music "climax_heart.ogg" fadein 2.0 volume 0.5
    stop sound fadeout 2.0

    show elara neutral at hero_pos with Dissolve(1.0)
    show arian normal at companion_pos with Dissolve(1.0)

    narrator "В центре зала — пульсирующий чёрный кристалл. Сердце Тени."

    e "Вот оно... Я нашла."

    narrator "Ариан стоит неподвижно. Его серебристые глаза отражают свет кристалла."

    a "Элара."

    e "Да?"

    a "Возьми его. Просто возьми — и всё закончится. Деревня будет спасена."

    narrator "Его голос изменился. Стал глубже. Старше."

    e "Ариан, что происходит?"

    if clues >= 3:
        e "Руны... Тень в крови. Проводник и Чума — одно дыхание."
        e "Это ты. ТЫ — Чума."
        narrator "Долгая тишина."

    if trust >= 2:
        a "Знаешь, ты первая, кто дошёл сюда и задавал вопросы."
        a "Остальные просто хватали."

    narrator "Пауза."

    a "Лес не настоящий, Элара."

    e "Что?"

    a "Ты не входила ни в какой лес. Ты лежишь в своей хижине. Уже три дня."
    a "Чума — не болезнь. Это я."
    a "Демон в твоей крови. А этот лес, шёпоты, стражи — всё это твой разум, который пытается меня отторгнуть."

    show elara scared with Dissolve(0.5)

    e "Нет..."

    a "Сердце Тени — это ловушка. Если возьмёшь его, ты впустишь меня полностью."
    a "Если не возьмёшь..."

    narrator "Он замолкает."

    menu:
        "Взять Сердце Тени":
            jump false_end
        "Вспомнить руны и осмотреться":
            if clues >= 4 and sanity > 6:
                jump true_end
            elif sanity > 4:
                jump normal_end
            else:
                jump bad_end
        "Отказаться от всего":
            if sanity > 4:
                jump normal_end
            else:
                jump bad_end


label true_end:
    narrator "Четыре руны вспыхивают в памяти."
    narrator "Тень — в тебе. Сердце — в крови. Проводник — Чума. ВЫЖГИ ИЗНУТРИ."

    show elara angry with Dissolve(0.5)

    e "Я не возьму твой кристалл."
    e "И я не буду с тобой сражаться."

    show arian normal with Dissolve(0.5)
    a "Тогда что?.."

    e "Ты — в моей крови. Значит, я — твоя клетка."
    e "Руна сказала — ВЫЖГИ ИЗНУТРИ."

    narrator "Элара закрывает глаза. Руны горят под кожей — все четыре."

    scene white with Flash          # первая вспышка
    play music "true_end_victory.ogg" fadein 1.0 volume 0.5

    hide arian
    narrator "Крик. Нечеловеческий, древний."

    show arian demon at center_pos with vpunch

    demon "НЕТ! ТЫ НЕ МОЖЕШЬ—"

    narrator "Свет. Ослепительный, выжигающий."

    scene white with Flash          # вторая вспышка
    pause 0.8

    scene black with Dissolve(1.5)
    pause 1.0

    scene bg_village_saved1 with Dissolve(3.0)
    pause 1.0
    show elara neutral at center_pos with Dissolve(1.0)

    narrator "Элара открывает глаза. Потолок хижины. Запах трав."
    narrator "Руки дрожат. В венах — слабые серебристые линии. Шрамы от огня, которого не было."

    e "Я дома."

    narrator "За окном — деревня просыпается. Кашель стих. Чума отступает."

    e "Прости, Ариан. Кем бы ты ни был."

    narrator "Шёпот — последний, еле слышный:"
    whisper "До встречи, травница..."

    narrator "Но на этот раз Элара не боится."

    "TRUE END: Очищение."
    return


label normal_end:
    show elara neutral with Dissolve(0.5)

    e "Я не возьму это. И я ухожу."

    show arian normal with Dissolve(0.5)
    a "Уйти нельзя. Я — часть тебя."

    e "Тогда будем жить вместе. Но ТЫ будешь молчать."

    narrator "Не победа. Перемирие."

    scene bg_village_saved2 with Dissolve(2.5)
    play music "normal_end_bittersweet.ogg" fadein 2.0 volume 0.45
    show elara scared at center_pos with Dissolve(1.0)

    narrator "Деревня спасена. Чума ослабла, но не ушла."
    narrator "Иногда по ночам Элара слышит шёпот. Знакомый голос."

    whisper "Скучаешь по мне?"

    e "Замолчи."

    narrator "Он смеётся. Тихо, почти ласково."

    e "Я спасла их. Этого достаточно."
    e "...Должно быть достаточно."

    "NORMAL END: Шёпоты Вечны."
    return


label bad_end:
    show elara scared with Dissolve(0.5)

    narrator "Разум рассыпается. Слишком много страха, слишком мало ответов."

    e "Я не... я не могу..."

    show arian normal with Dissolve(0.5)
    a "Тише. Тише. Всё почти закончилось."

    narrator "Ариан подходит ближе. Ещё ближе. Его рука — ледяная."

    hide arian normal
    show arian demon at companion_pos with vpunch

    demon "Спи, Элара. Я позабочусь обо всём."

    scene bg_eternal_dark with hpunch
    play music "bad_end_despair.ogg" loop fadein 1.0 volume 0.4

    show elara corrupted at center_pos with Dissolve(1.5)  # ← здесь появляется изменённая версия

    narrator "Темнота. Бесконечная, тёплая, удушающая."
    narrator "Где-то далеко деревня кашляет. Никто не придёт."

    whisper "Ты моя. Навсегда."

    "BAD END: Поглощение."
    return


label false_end:
    show elara angry with Dissolve(0.5)

    narrator "Пальцы смыкаются на кристалле. Холод. Потом — жар."

    scene white with Dissolve(0.8)
    pause 0.5

    scene bg_eternal_dark with Dissolve(2.0)
    play music "bad_end_despair.ogg" loop fadein 1.0 volume 0.4

    show elara corrupted at hero_pos with Dissolve(1.5)  # ← здесь появляется изменённая версия

    narrator "Мир меняется. Лес склоняется. Тени преклоняют колени."

    hide arian
    show arian demon at companion_pos with Dissolve(1.0)

    demon "Добро пожаловать, хозяйка."

    e "Что... что со мной?"

    narrator "Голос Элары — другой. Глубже. Древнее."

    demon "Ты взяла Сердце. Теперь ты — Тень."
    demon "Деревня? Забудь. У тебя новый дом."

    narrator "Элара смотрит на свои руки. Чёрные вены. Серебристые глаза."
    narrator "Она улыбается. И улыбка — не её."

    show elara corrupted with Dissolve(0.5)  # можно повторить или оставить

    e "Пусть придут другие. Я буду ждать."

    narrator "В умирающей деревне начинается последняя ночь."

    "FALSE END: Новая Хозяйка Теней."
    return
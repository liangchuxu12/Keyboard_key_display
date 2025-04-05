import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 1350, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("键盘可视化工具 - 区分主键盘和小键盘数字键")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# 键盘布局定义 (x, y, width, height, 主字符, 上档字符)
key_layout = [
    # 第一行
    (10, 10, 60, 60, "`", "~"), (80, 10, 60, 60, "1", "!"), (150, 10, 60, 60, "2", "@"),
    (220, 10, 60, 60, "3", "#"), (290, 10, 60, 60, "4", "$"), (360, 10, 60, 60, "5", "%"),
    (430, 10, 60, 60, "6", "^"), (500, 10, 60, 60, "7", "&"), (570, 10, 60, 60, "8", "*"),
    (640, 10, 60, 60, "9", "("), (710, 10, 60, 60, "0", ")"), (780, 10, 60, 60, "-", "_"),
    (850, 10, 60, 60, "=", "+"), (920, 10, 80, 60, "Backspace", ""),

    # 第二行
    (10, 80, 80, 60, "Tab", ""), (100, 80, 60, 60, "q", "Q"), (170, 80, 60, 60, "w", "W"),
    (240, 80, 60, 60, "e", "E"), (310, 80, 60, 60, "r", "R"), (380, 80, 60, 60, "t", "T"),
    (450, 80, 60, 60, "y", "Y"), (520, 80, 60, 60, "u", "U"), (590, 80, 60, 60, "i", "I"),
    (660, 80, 60, 60, "o", "O"), (730, 80, 60, 60, "p", "P"), (800, 80, 60, 60, "[", "{"),
    (870, 80, 60, 60, "]", "}"), (940, 80, 60, 60, "\\", "|"),

    # 第三行
    (10, 150, 90, 60, "Caps Lock", ""), (110, 150, 60, 60, "a", "A"), (180, 150, 60, 60, "s", "S"),
    (250, 150, 60, 60, "d", "D"), (320, 150, 60, 60, "f", "F"), (390, 150, 60, 60, "g", "G"),
    (460, 150, 60, 60, "h", "H"), (530, 150, 60, 60, "j", "J"), (600, 150, 60, 60, "k", "K"),
    (670, 150, 60, 60, "l", "L"), (740, 150, 60, 60, ";", ":"), (810, 150, 60, 60, "'", "\""),
    (880, 150, 120, 60, "Enter", ""),

    # 第四行
    (10, 220, 100, 60, "Shift", ""), (120, 220, 60, 60, "z", "Z"), (190, 220, 60, 60, "x", "X"),
    (260, 220, 60, 60, "c", "C"), (330, 220, 60, 60, "v", "V"), (400, 220, 60, 60, "b", "B"),
    (470, 220, 60, 60, "n", "N"), (540, 220, 60, 60, "m", "M"), (610, 220, 60, 60, ",", "<"),
    (680, 220, 60, 60, ".", ">"), (750, 220, 60, 60, "/", "?"), (820, 220, 180, 60, "Shift", ""),

    # 第五行
    (10, 290, 70, 60, "L Ctrl", ""), (90, 290, 70, 60, "L Win", ""), (170, 290, 70, 60, "L Alt", ""),
    (250, 290, 300, 60, "Space", ""), (560, 290, 70, 60, "R Alt", ""), (640, 290, 70, 60, "R Win", ""),
    (720, 290, 70, 60, "Menu", ""), (800, 290, 70, 60, "R Ctrl", ""),

    # 数字小键盘区（带Num前缀）
    (1020, 10, 60, 60, "Num\nLock", ""), (1090, 10, 60, 60, "Num /", ""), (1160, 10, 60, 60, "Num *", ""),
    (1230, 10, 60, 60, "Num -", ""),
    (1020, 80, 60, 60, "Num 7", "Home"), (1090, 80, 60, 60, "Num 8", "↑"), (1160, 80, 60, 60, "Num 9", "PgUp"),
    (1230, 80, 60, 120, "Num +", ""),
    (1020, 150, 60, 60, "Num 4", "←"), (1090, 150, 60, 60, "Num 5", ""), (1160, 150, 60, 60, "Num 6", "→"),
    (1020, 220, 60, 60, "Num 1", "End"), (1090, 220, 60, 60, "Num 2", "↓"), (1160, 220, 60, 60, "Num 3", "PgDn"),
    (1230, 220, 60, 120, "Num Enter", ""),
    (1020, 290, 120, 60, "Num 0", "Ins"), (1150, 290, 60, 60, "Num .", "Del")
]

# 特殊键映射（已区分主键盘和小键盘数字键）
special_keys = {
    # 主键盘区功能键
    pygame.K_BACKSPACE: "Backspace",
    pygame.K_TAB: "Tab",
    pygame.K_CAPSLOCK: "Caps Lock",
    pygame.K_RETURN: "Enter",
    pygame.K_LSHIFT: "L Shift",
    pygame.K_RSHIFT: "R Shift",
    pygame.K_LCTRL: "L Ctrl",
    pygame.K_RCTRL: "R Ctrl",
    pygame.K_LALT: "L Alt",
    pygame.K_RALT: "R Alt",
    pygame.K_LGUI: "L Win",
    pygame.K_RGUI: "R Win",
    pygame.K_MENU: "Menu",
    pygame.K_SPACE: "Space",

    # 主键盘数字键（0-9）
    pygame.K_0: "0",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9",

    # 小键盘区功能键
    pygame.K_NUMLOCK: "Num\nLock",
    pygame.K_KP_DIVIDE: "Num /",
    pygame.K_KP_MULTIPLY: "Num *",
    pygame.K_KP_MINUS: "Num -",
    pygame.K_KP_PLUS: "Num +",
    pygame.K_KP_ENTER: "Num Enter",
    pygame.K_KP_PERIOD: "Num .",

    # 小键盘数字键（带Num前缀）
    pygame.K_KP0: "Num 0",
    pygame.K_KP1: "Num 1",
    pygame.K_KP2: "Num 2",
    pygame.K_KP3: "Num 3",
    pygame.K_KP4: "Num 4",
    pygame.K_KP5: "Num 5",
    pygame.K_KP6: "Num 6",
    pygame.K_KP7: "Num 7",
    pygame.K_KP8: "Num 8",
    pygame.K_KP9: "Num 9",

    # 其他符号键
    pygame.K_EQUALS: "=",
    pygame.K_MINUS: "-",
    pygame.K_LEFTBRACKET: "[",
    pygame.K_RIGHTBRACKET: "]",
    pygame.K_BACKSLASH: "\\",
    pygame.K_SEMICOLON: ";",
    pygame.K_QUOTE: "'",
    pygame.K_COMMA: ",",
    pygame.K_PERIOD: ".",
    pygame.K_SLASH: "/",
}

# 存储按下的键
pressed_keys = set()

# 主循环
clock = pygame.time.Clock()
shift_pressed = False
caps_lock = False


def draw_keyboard():
    screen.fill(WHITE)

    # 绘制主键盘区和数字小键盘区之间的分隔线
    pygame.draw.line(screen, (180, 180, 180), (1000, 10), (1000, 350), 2)

    for key in key_layout:
        x, y, w, h, char, shift_char = key
        key_rect = pygame.Rect(x, y, w, h)

        # 检查这个键是否被按下
        key_name = char if char not in ["", "Shift"] else shift_char if shift_char else char
        if key_name in pressed_keys:
            color = GREEN
        else:
            color = GRAY

        pygame.draw.rect(screen, color, key_rect)
        pygame.draw.rect(screen, BLACK, key_rect, 2)

        # 显示键上的字符（移除Num前缀）
        font = pygame.font.SysFont('Arial', 24)
        display_char = char.replace("Num ", "") if char else key_name.replace("Num ", "")

        if "\n" in display_char:  # 处理多行文本
            lines = display_char.split("\n")
            line_height = font.get_height()
            total_height = len(lines) * line_height
            start_y = y + (h - total_height) // 2

            for i, line in enumerate(lines):
                text = font.render(line, True, BLACK)
                text_x = x + (w - text.get_width()) // 2
                screen.blit(text, (text_x, start_y + i * line_height))

        elif shift_char and char:  # 有上下两个字符的键
            # 上档字符（小字体）
            small_font = pygame.font.SysFont('Arial', 18)
            shift_text = small_font.render(shift_char.replace("Num ", ""), True, BLACK)
            screen.blit(shift_text, (x + w - shift_text.get_width() - 5, y + 5))

            # 主字符
            char_text = font.render(display_char, True, BLACK)
            screen.blit(char_text, (x + 5, y + h - char_text.get_height() - 5))

        else:  # 单字符或功能键
            if len(display_char) > 5 and ' ' in display_char:  # 如"Caps Lock"
                parts = display_char.split(' ')
                part1 = font.render(parts[0], True, BLACK)
                part2 = font.render(parts[1], True, BLACK)
                screen.blit(part1, (x + (w - part1.get_width()) // 2, y + h // 2 - 20))
                screen.blit(part2, (x + (w - part2.get_width()) // 2, y + h // 2 + 5))
            else:
                text = font.render(display_char, True, BLACK)
                text_rect = text.get_rect(center=key_rect.center)
                screen.blit(text, text_rect)

    # 显示说明
    # font = pygame.font.SysFont('Arial', 24)
    # instruction = font.render("Press any key (ESC to quit) - 主键盘和小键盘数字键已区分", True, BLACK)
    # screen.blit(instruction, (10, HEIGHT - 30))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # 检查Shift和Caps Lock状态
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                shift_pressed = True
            elif event.key == pygame.K_CAPSLOCK:
                caps_lock = not caps_lock

            # 获取按下的键名
            if event.key in special_keys:
                key_name = special_keys[event.key]
            else:
                try:
                    key_name = chr(event.key)
                    if shift_pressed or caps_lock:
                        # 查找上档字符
                        for key in key_layout:
                            if key[4].replace("Num ", "") == key_name.lower():
                                if key[5]:  # 如果有上档字符
                                    key_name = key[5] if shift_pressed else key_name.upper() if caps_lock else key_name
                                break
                except ValueError:
                    key_name = ""

            if key_name:
                pressed_keys.add(key_name)

        elif event.type == pygame.KEYUP:
            # 检查Shift状态
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                shift_pressed = False

            # 获取释放的键名
            if event.key in special_keys:
                key_name = special_keys[event.key]
            else:
                try:
                    key_name = chr(event.key)
                    if shift_pressed or caps_lock:
                        # 查找上档字符
                        for key in key_layout:
                            if key[4].replace("Num ", "") == key_name.lower():
                                if key[5]:  # 如果有上档字符
                                    key_name = key[5] if shift_pressed else key_name.upper() if caps_lock else key_name
                                break
                except ValueError:
                    key_name = ""

            if key_name in pressed_keys:
                pressed_keys.remove(key_name)

    draw_keyboard()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

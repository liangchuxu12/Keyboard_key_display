import pygame
import sys
import os

# 初始化pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 1000, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("键盘可视化工具")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
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
    (10, 290, 70, 60, "L Ctrl", ""),  # 修改为L Ctrl
    (90, 290, 70, 60, "L Win", ""),  # 左Win键
    (170, 290, 70, 60, "L Alt", ""),  # 修改为L Alt
    (250, 290, 300, 60, "Space", ""),
    (560, 290, 70, 60, "R Alt", ""),  # 修改为R Alt
    (640, 290, 70, 60, "R Win", ""),  # 右Win键
    (720, 290, 70, 60, "Menu", ""),
    (800, 290, 70, 60, "R Ctrl", "")  # 修改为R Ctrl
]

# 特殊键映射
special_keys = {
    pygame.K_BACKSPACE: "Backspace",
    pygame.K_TAB: "Tab",
    pygame.K_CAPSLOCK: "Caps Lock",
    pygame.K_RETURN: "Enter",
    pygame.K_LSHIFT: "L Shift",  # 修改为L Shift
    pygame.K_RSHIFT: "R Shift",  # 修改为R Shift
    pygame.K_LCTRL: "L Ctrl",    # 修改为L Ctrl
    pygame.K_RCTRL: "R Ctrl",    # 修改为R Ctrl
    pygame.K_LALT: "L Alt",      # 修改为L Alt
    pygame.K_RALT: "R Alt",      # 修改为R Alt
    pygame.K_LGUI: "L Win",      # 左Win键
    pygame.K_RGUI: "R Win",      # 右Win键
    pygame.K_MENU: "Menu",
    pygame.K_SPACE: "Space"
}

# 存储按下的键
pressed_keys = set()

# 主循环
clock = pygame.time.Clock()
shift_pressed = False
caps_lock = False


def draw_keyboard():
    screen.fill(WHITE)

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

        # 显示键上的字符
        font = pygame.font.SysFont(None, 24)
        if shift_char and char:  # 有上下两个字符的键
            # 上档字符
            shift_text = font.render(shift_char, True, BLACK)
            screen.blit(shift_text, (x + 5, y + 5))

            # 主字符
            char_text = font.render(char, True, BLACK)
            screen.blit(char_text, (x + w - char_text.get_width() - 5, y + h - char_text.get_height() - 5))
        else:  # 单字符或功能键
            text = font.render(char if char else key_name, True, BLACK)
            text_rect = text.get_rect(center=key_rect.center)
            screen.blit(text, text_rect)

    # 显示说明
    font = pygame.font.SysFont(None, 24)
    instruction = font.render("按下键盘上的键，对应键位会亮起。按ESC退出。", True, BLACK)
    screen.blit(instruction, (10, HEIGHT - 30))


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
                            if key[4] == key_name.lower():
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
                            if key[4] == key_name.lower():
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
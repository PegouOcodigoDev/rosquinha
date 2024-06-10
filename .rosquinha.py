import pygame
import math
import colorsys

pygame.init()

largura = 400
altura = 400

matiz = 0

x_start, y_start = 0, 0

# espaçamento entre os caracteres
x_espacamento = 5
y_espacamento = 10 

linhas = altura // y_espacamento
colunas = largura // x_espacamento

#Calcula o deslocamento para centralizar a rosquinha
x_offset = colunas / 2
y_offset = linhas / 2

tamanho_da_tela = linhas * colunas

#angulos utilizados
rotacao1, rotacao2 = 0,0
theta_espacamento = 10
#voce pode aumentar o phi para aumentar a velocidade de rotação
phi_espacamento = 2

chars = ".,-~:;=!*#$@"

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Rosquinha')
font = pygame.font.SysFont('Arial', 18, bold=True)

#Função auxiliar que convert hsv para RGB
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def criar_texto_na_tela(letra, x_start, y_start):
    texto = font.render(str(letra), True, hsv2rgb(matiz, 1, 1))
    tela.blit(texto, (x_start, y_start))

run = True
while run:

    #preenche o fundo com a cor preta
    tela.fill((0,0,0))

    #inicializa as listas de profundidade e caracteres
    z = [0] * tamanho_da_tela
    b = [''] * tamanho_da_tela

    #calculos de posição
    for j in range(0, 628, theta_espacamento):
        for i in range(0,628, phi_espacamento):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(rotacao1)
            f = math.sin(j)
            g = math.cos(rotacao1)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(rotacao2)
            n = math.sin(rotacao2)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + colunas * y)
            N = int( 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if linhas > y and y > 0 and x > 0 and colunas > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]
            
    y_start = 0

    #desenha os caracteres na tela
    for i in range(len(b)):
        rotacao1 += 0.00004
        rotacao2 += 0.00002
        if i % colunas == 0 and i != 0:
            y_start += y_espacamento
            x_start = 0
        criar_texto_na_tela(b[i], x_start, y_start)
        x_start += x_espacamento

    pygame.display.update()

    #atualiza o matiz para criar efeito arco iris
    matiz += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run = False
    




#segue a gente e deixa aquela curtida :-)
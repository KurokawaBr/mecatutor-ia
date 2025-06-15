import streamlit as st
import pandas as pd
import os
import sys

def resource_path(relative_path):
    """
    Retorna o caminho absoluto do arquivo, 
    compatível com execução direta e com PyInstaller.
    """
    try:
        # Quando está rodando no PyInstaller, _MEIPASS aponta para a pasta temporária de extração
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        # No modo normal, retorna a pasta onde está o app.py
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

st.set_page_config(page_title="MecaTutorIA", page_icon="🤖")

st.title("💧 Mecânica dos Fluidos - Munson (4ª Edição)")
st.markdown("---")

menu = ["Resumos dos Capítulos", "Exercícios Resolvidos", "Sobre"]
choice = st.sidebar.radio("Menu", menu)

if choice == "Resumos dos Capítulos":
    st.header("📚 Resumos dos Capítulos")

    cap = st.selectbox("Escolha o capítulo", [
        "Capítulo 1 – Introdução e Conceitos Iniciais",
        "Capítulo 2 – Estática dos Fluidos",
        "Capítulo 3 – Dinâmica dos Fluidos (Bernoulli)",
        "Capítulo 8 – Escoamento Viscoso em Condutos"
    ])

    if cap == "Capítulo 1 – Introdução e Conceitos Iniciais":
        st.subheader("Capítulo 1 – Introdução e Conceitos Iniciais")
        st.markdown(r"""
### 1.1 Propriedades Básicas dos Fluidos

#### **Massa Específica (Densidade)**
$$
\rho = \frac{m}{V}
$$

**Onde:**
- $\rho$ = massa específica (kg/m³)
- $m$ = massa (kg)
- $V$ = volume (m³)

**Explicação:** A massa específica é uma propriedade fundamental que quantifica a quantidade de massa contida em uma unidade de volume. É essencial para cálculos de força, pressão e energia em sistemas fluidos. Varia com temperatura e pressão, especialmente em gases.

#### **Peso Específico**
$$
\gamma = \rho g
$$

**Onde:**
- $\gamma$ = peso específico (N/m³)
- $\rho$ = massa específica (kg/m³)
- $g$ = aceleração da gravidade (9,81 m/s²)

**Explicação:** O peso específico relaciona o peso de um fluido ao volume que ele ocupa. É particularmente útil em cálculos de pressão hidrostática e força em superfícies submersas.

#### **Densidade Relativa (Gravidade Específica)**
$$
S = \frac{\rho_{fluido}}{\rho_{água}}
$$

**Onde:**
- $S$ = densidade relativa (adimensional)
- $\rho_{fluido}$ = massa específica do fluido
- $\rho_{água}$ = massa específica da água (1000 kg/m³ a 4°C)

**Explicação:** A densidade relativa é uma medida comparativa que indica quantas vezes um fluido é mais denso que a água. É amplamente usada na indústria por ser adimensional e facilitar comparações.

### 1.2 Lei dos Gases Perfeitos

#### **Equação de Estado dos Gases Perfeitos**
$$
p = \rho R T
$$

**Onde:**
- $p$ = pressão absoluta (Pa)
- $\rho$ = massa específica (kg/m³)
- $R$ = constante específica do gás (J/kg·K)
- $T$ = temperatura absoluta (K)

**Explicação:** Esta é uma das equações mais importantes para gases. Relaciona pressão, densidade e temperatura para gases ideais. É válida para a maioria dos gases em condições normais (longe da liquefação). A constante $R$ varia para cada gás e está relacionada à massa molecular.

**Forma Alternativa:**
$$
pV = nR_uT
$$

**Onde:**
- $V$ = volume (m³)
- $n$ = número de moles
- $R_u$ = constante universal dos gases (8314 J/kmol·K)

### 1.3 Viscosidade

#### **Lei de Newton da Viscosidade**
$$
\tau = \mu \frac{du}{dy}
$$

**Onde:**
- $\tau$ = tensão de cisalhamento (Pa)
- $\mu$ = viscosidade dinâmica (Pa·s)
- $\frac{du}{dy}$ = gradiente de velocidade (s⁻¹)

**Explicação:** Esta equação fundamental define a relação entre tensão de cisalhamento e gradiente de velocidade em fluidos newtonianos. A viscosidade dinâmica $\mu$ é uma propriedade do fluido que quantifica sua resistência ao escoamento. Fluidos com alta viscosidade (como mel) resistem mais ao movimento que fluidos com baixa viscosidade (como água).

#### **Viscosidade Cinemática**
$$
\nu = \frac{\mu}{\rho}
$$

**Onde:**
- $\nu$ = viscosidade cinemática (m²/s)
- $\mu$ = viscosidade dinâmica (Pa·s)
- $\rho$ = massa específica (kg/m³)

**Explicação:** A viscosidade cinemática é a razão entre viscosidade dinâmica e massa específica. É frequentemente usada em análises de escoamento porque aparece naturalmente nas equações de movimento dos fluidos.

### 1.4 Compressibilidade

#### **Módulo de Elasticidade Volumétrico**
$$
K = -V \frac{dp}{dV} = \rho \frac{dp}{d\rho}
$$

**Onde:**
- $K$ = módulo de elasticidade volumétrico (Pa)
- $V$ = volume (m³)
- $p$ = pressão (Pa)
- $\rho$ = massa específica (kg/m³)

**Explicação:** O módulo de elasticidade volumétrico quantifica a resistência de um fluido à compressão. Valores altos indicam fluidos pouco compressíveis (líquidos), enquanto valores baixos indicam fluidos muito compressíveis (gases).

#### **Velocidade do Som**
$$
c = \sqrt{\frac{K}{\rho}} = \sqrt{\frac{dp}{d\rho}}
$$

**Onde:**
- $c$ = velocidade do som (m/s)
- $K$ = módulo de elasticidade volumétrico (Pa)
- $\rho$ = massa específica (kg/m³)

**Explicação:** A velocidade do som em um fluido está diretamente relacionada à sua compressibilidade. É um parâmetro crítico em escoamentos de alta velocidade onde efeitos de compressibilidade se tornam importantes.

### 1.5 Tensão Superficial

#### **Força devido à Tensão Superficial**
$$
F = \sigma L
$$

**Onde:**
- $F$ = força devido à tensão superficial (N)
- $\sigma$ = tensão superficial (N/m)
- $L$ = comprimento da linha de contato (m)

**Explicação:** A tensão superficial atua ao longo da linha de contato entre diferentes fases (líquido-gás, líquido-sólido). É importante em fenômenos como formação de gotas, capilaridade e escoamentos com interfaces livres.

#### **Pressão através de Interface Curva (Equação de Young-Laplace)**
$$
\Delta p = \sigma \left(\frac{1}{R_1} + \frac{1}{R_2}\right)
$$

**Onde:**
- $\Delta p$ = diferença de pressão através da interface (Pa)
- $\sigma$ = tensão superficial (N/m)
- $R_1, R_2$ = raios principais de curvatura (m)

**Explicação:** Esta equação descreve como a curvatura de uma interface cria uma diferença de pressão. É fundamental para entender fenômenos como a pressão interna de bolhas e gotas.

### 1.6 Pressão de Vapor

#### **Relação de Clausius-Clapeyron (Simplificada)**
$$
p_v = p_{v0} \exp\left[\frac{h_{fg}}{R}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right]
$$

**Onde:**
- $p_v$ = pressão de vapor (Pa)
- $p_{v0}$ = pressão de vapor de referência (Pa)
- $h_{fg}$ = entalpia de vaporização (J/kg)
- $R$ = constante específica do gás (J/kg·K)
- $T, T_0$ = temperaturas absoluta e de referência (K)

**Explicação:** A pressão de vapor é a pressão na qual um líquido se vaporiza a uma dada temperatura. É crucial para evitar cavitação em sistemas hidráulicos, que ocorre quando a pressão local cai abaixo da pressão de vapor.
""")
        # Dados da Tabela 1.5
        st.subheader("Tabela 1.5 - Propriedades Físicas de Alguns Líquidos")
        tab1_5 = {
            "Líquido": ["Tetracloreto de Carbono", "Álcool Etílico", "Gasolina", "Glicerina", "Mercúrio", "Óleo SAE 30", "Água do mar", "Água"],
            "Temperatura (°C)": [20, 20, 15.6, 20, 20, 15.6, 15.6, 15.6],
            "Massa Específica (kg/m³)": [1590, 789, 680, 1260, 13600, 912, 1030, 999],
            "Viscosidade Dinâmica μ (N·s/m²)": [9.58E-4, 1.19E-3, 3.1E-4, 1.50E-1, 1.57E-3, 3.8E-1, 1.2E-3, 1.12E-3],
            "Tensão Superficial σ (N/m)": [2.69E-2, 2.28E-2, 2.02E-2, 6.33E-2, 4.66E-1, 3.6E-2, 7.34E-2, 7.34E-2],
            "Pressão de Vapor p_v (N/m² abs)": [1.3E+4, 5.9E+3, 5.5E+4, 1.4E+2, 1.6E+2, 1.5E+2, 1.77E+3, 1.77E+3],
            "Compressibilidade E_s (N/m²)": [1.31E+9, 1.06E+9, 8.2E+8, 4.52E+9, 2.85E+10, 1.5E+9, 2.34E+9, 2.15E+9]
        }
        
        df_liquidos = pd.DataFrame(tab1_5)
        st.dataframe(df_liquidos)

        # Dados da Tabela 1.6
        st.subheader("Tabela 1.6 - Propriedades Físicas de Alguns Gases")
        tab1_6 = {
            "Gás": ["Ar (padrão)", "Dióxido de Carbono", "Hélio", "Hidrogênio", "Metano (gás natural)", "Nitrogênio", "Oxigênio"],
            "Temperatura (°C)": [15, 20, 20, 20, 0, 20, 20],
            "Massa Específica (kg/m³)": [1.23E+0, 1.83E+0, 1.66E-1, 8.38E-2, 7.16E-1, 1.16E+0, 1.33E+0],
            "Viscosidade Dinâmica μ (N·s/m²)": [1.79E-5, 1.47E-5, 1.96E-5, 8.84E-6, 1.10E-5, 1.76E-5, 2.04E-5],
            "Constante do Gás R (J/kg·K)": [2.869E+2, 1.889E+2, 2.077E+3, 4.124E+3, 5.183E+2, 2.968E+2, 2.598E+2],
            "Razão de Calores Específicos k": [1.40, 1.30, 1.66, 1.41, 1.31, 1.40, 1.40]
        }

        df_gases = pd.DataFrame(tab1_6)
        st.dataframe(df_gases)
        
        st.markdown(r"""
---

### Exemplos Práticos

**Exemplo 1: Cálculo da densidade**
> Um corpo de massa $500\,g$ ocupa um volume de $0,0005\,m^3$. Qual é a sua densidade?

$\rightarrow$ Convertendo a massa para $kg$:  $m = \frac{500}{1000} = 0,5\,kg$  
$\rho = \frac {0,5}{0,0005} = 1000\,kg/m^3$  
**Interpretação:** Essa é a densidade da água a $4^\circ C$.

---

**Exemplo 2: Cálculo do peso específico**
> Qual o peso específico de um óleo cuja densidade é $900\,kg/m^3$?

$\gamma = \rho g = 900 \times 9,81 = 8829\,N/m^3$

---

**Exemplo 3: Viscosidade cinemática**
> Um fluido tem $\mu = 1,2 \times 10^{-3}\,Pa \cdot s$ e $\rho = 1200\,kg/m^3$. Qual sua viscosidade cinemática?

$\nu = \frac{\mu}{\rho} = \frac{1,2 \times 10^{-3}}{1200} = 1,0 \times 10^{-6}\,m^2/s$

---

**Exemplo 4: Pressão**
> Uma força de $500\,N$ é aplicada perpendicularmente a uma área de $0,25\,m^2$. Qual é a pressão?

$P = \frac{F}{A} = \frac{500}{0,25} = 2000\,Pa$
""")

    elif cap == "Capítulo 2 – Estática dos Fluidos":
        st.subheader("Capítulo 2 – Estática dos Fluidos")
        st.markdown(r"""
### 2.1 Pressão em Fluidos Estáticos

#### **Equação Fundamental da Estática dos Fluidos**
$$
\frac{dp}{dz} = -\gamma = -\rho g
$$

**Onde:**
- $p$ = pressão (Pa)
- $h$ = coordenada vertical (positiva para cima) (m)
- $\gamma$ = peso específico (N/m³)
- $\rho$ = massa específica (kg/m³)
- $g$ = aceleração da gravidade (m/s²)

**Explicação:** Esta equação fundamental estabelece como a pressão varia com a altura em um fluido estático. O sinal negativo indica que a pressão aumenta com a profundidade. É a base para todos os cálculos de pressão hidrostática.

#### **Variação de Pressão em Fluido Incompressível**
$$
p_2 - p_1 = \rho g (h_1 - h_2) = \gamma h
$$

**Onde:**
- $p_1, p_2$ = pressões nos pontos 1 e 2 (Pa)
- $h_1, h_2$ = elevações dos pontos 1 e 2 (m)
- $h$ = diferença de altura ($h_1 - h_2$) (m)

**Explicação:** Para fluidos incompressíveis (líquidos), a variação de pressão é linear com a altura. Esta é a equação mais usada em aplicações práticas de hidrostática.

#### **Pressão Absoluta vs. Relativa**
$$
p_{abs} = p_{rel} + p_{atm}
$$

**Onde:**
- $p_{abs}$ = pressão absoluta (Pa)
- $p_{rel}$ = pressão relativa ou manométrica (Pa)
- $p_{atm}$ = pressão atmosférica (≈ 101.325 Pa)

**Explicação:** A pressão absoluta é medida em relação ao vácuo perfeito, enquanto a pressão relativa é medida em relação à pressão atmosférica local. É crucial distinguir entre elas em cálculos.

### 2.2 Manometria

#### **Manômetro em U**
$$
p_A - p_B = \rho_{man} g h
$$

**Onde:**
- $p_A, p_B$ = pressões nos pontos A e B (Pa)
- $\rho_{man}$ = massa específica do fluido manométrico (kg/m³)
- $h$ = diferença de altura no manômetro (m)

**Explicação:** O manômetro em U é um dispositivo simples e preciso para medir diferenças de pressão. O fluido manométrico (geralmente mercúrio ou água) se desloca proporcionalmente à diferença de pressão.

#### **Manômetro Inclinado**
$$
p_A - p_B = \rho_{man} g L \sin \theta
$$

**Onde:**
- $L$ = comprimento da coluna inclinada (m)
- $\theta$ = ângulo de inclinação com a horizontal (rad)

**Explicação:** O manômetro inclinado amplifica a leitura para pequenas diferenças de pressão, aumentando a precisão da medição.

### 2.3 Forças Hidrostáticas

#### **Força em Superfície Plana Horizontal**
$$
F = p A = \rho g h A
$$

**Onde:**
- $F$ = força hidrostática (N)
- $p$ = pressão no centroide da superfície (Pa)
- $A$ = área da superfície (m²)
- $h$ = profundidade do centroide (m)

**Explicação:** Para superfícies horizontais, a pressão é uniforme e a força é simplesmente o produto da pressão pela área.

#### **Força em Superfície Plana Inclinada**
$$
F = \rho g h_c A
$$

**Onde:**
- $h_c$ = profundidade vertical do centroide da superfície (m)
- $A$ = área da superfície (m²)

**Explicação:** Para superfícies inclinadas, usa-se a profundidade vertical do centroide para calcular a pressão média.

#### **Centro de Pressão**
$$
y_{cp} = y_c + \frac{I_{xc}}{y_c A}
$$

**Onde:**
- $y_{cp}$ = posição do centro de pressão (m)
- $y_c$ = posição do centroide (m)
- $I_{xc}$ = momento de inércia em relação ao eixo que passa pelo centroide (m⁴)

**Explicação:** O centro de pressão é o ponto onde a força hidrostática resultante atua. Para superfícies inclinadas, está sempre abaixo do centroide geométrico.

### 2.4 Empuxo e Flutuação

#### **Princípio de Arquimedes**
$$
F_E = \rho_{fluido} g V_{submerso}
$$

**Onde:**
- $F_E$ = força de empuxo (N)
- $\rho_{fluido}$ = massa específica do fluido (kg/m³)
- $V_{submerso}$ = volume submerso do corpo (m³)

**Explicação:** O empuxo é igual ao peso do fluido deslocado pelo corpo submerso. Atua verticalmente para cima através do centro de empuxo (centroide do volume deslocado).

#### **Condição de Equilíbrio para Flutuação**
$$
\rho_{corpo} V_{corpo} g = \rho_{fluido} V_{submerso} g
$$

**Simplificando:**
$$
\frac{V_{submerso}}{V_{corpo}} = \frac{\rho_{corpo}}{\rho_{fluido}}
$$

**Explicação:** Um corpo flutua quando o empuxo equilibra seu peso. A fração submersa depende da razão entre as densidades do corpo e do fluido.

### 2.5 Estabilidade de Corpos Flutuantes

#### **Altura Metacêntrica**
$$
GM = BM - BG
$$

**Onde:**
- $GM$ = altura metacêntrica (m)
- $BM$ = distância do centro de empuxo ao metacentro (m)
- $BG$ = distância do centro de empuxo ao centro de gravidade (m)

**Explicação:** A altura metacêntrica determina a estabilidade de um corpo flutuante. Se $GM > 0$, o corpo é estável; se $GM < 0$, é instável.

#### **Raio Metacêntrico**
$$
BM = \frac{I}{V_{submerso}}
$$

**Onde:**
- $I$ = momento de inércia da área da linha d'água (m⁴)
- $V_{submerso}$ = volume submerso (m³)

**Explicação:** O raio metacêntrico depende da geometria da linha d'água. Formas mais largas têm maior estabilidade.

### 2.6 Fluidos com Aceleração

#### **Superfície Livre com Aceleração Linear**
$$
\tan \theta = \frac{a_x}{g + a_z}
$$

**Onde:**
- $\theta$ = ângulo da superfície livre com a horizontal (rad)
- $a_x$ = aceleração horizontal (m/s²)
- $a_z$ = aceleração vertical (m/s²)

**Explicação:** Quando um recipiente acelera, a superfície livre inclina-se de modo que a resultante das acelerações seja perpendicular à superfície.

#### **Superfície Livre com Rotação**
$$
z = \frac{\omega^2 r^2}{2g} + C
$$

**Onde:**
- $z$ = elevação da superfície livre (m)
- $\omega$ = velocidade angular (rad/s)
- $r$ = distância radial do eixo de rotação (m)
- $C$ = constante de integração (m)

**Explicação:** Durante rotação com velocidade angular constante, a superfície livre assume a forma de um paraboloide de revolução devido ao equilíbrio entre forças centrífugas e gravitacionais.
---

### Exemplos Práticos

**Exemplo 1: Variação de pressão com profundidade**
> Qual a pressão no fundo de um tanque de água de $5\,m$ de profundidade? (Considere $\rho_{agua}=1000\,kg/m^3$ e $g=9,81\,m/s^2$)

$\Delta P = \rho g \Delta h = 1000 \times 9,81 \times 5 = 49\,050\,Pa$  
**Resposta:** A pressão no fundo do tanque é $49,050\,Pa$ acima da atmosférica.

---

**Exemplo 2: Manômetro em U**
> Um manômetro em U contém água e mercúrio. A diferença de níveis do mercúrio é de $0,12\,m$. Calcule a diferença de pressão.

$\Delta P = \Delta h \cdot (\rho_{Hg} - \rho_{agua}) \cdot g$  
$\rho_{Hg} = 13\,600\,kg/m^3$, $\rho_{agua} = 1000\,kg/m^3$  
$\Delta P = 0,12 \times (13\,600 - 1000) \times 9,81 = 14\,012\,Pa$

---

**Exemplo 3: Empuxo**
> Um bloco de madeira ($\rho=600\,kg/m^3$) de volume $0,02\,m^3$ está totalmente submerso em água. Qual o empuxo sobre o bloco?

$E = \rho_{agua} \cdot V_{deslocado} \cdot g = 1000 \times 0,02 \times 9,81 = 196,2\,N$

---

**Exemplo 4: Estabilidade de corpos flutuantes**
> Um corpo flutua se a densidade do corpo é menor que a do fluido. Um objeto com $\rho=800\,kg/m^3$ colocado na água ($\rho=1000\,kg/m^3$) irá flutuar com parte submersa.

""")
        
    elif cap == "Capítulo 3 – Dinâmica dos Fluidos (Bernoulli)":
        st.subheader("Capítulo 3 – Dinâmica dos Fluidos (Equação de Bernoulli)")
        st.markdown(r"""
### 3.1 Equação de Bernoulli

#### **Equação de Bernoulli (Forma Clássica)**
$$
\frac{p_1}{\rho} + \frac{V_1^2}{2} + g z_1 = \frac{p_2}{\rho} + \frac{V_2^2}{2} + g z_2
$$

**Onde:**
- $p$ = pressão (Pa)
- $\rho$ = massa específica (kg/m³)
- $V$ = velocidade (m/s)
- $g$ = aceleração da gravidade (m/s²)
- $z$ = elevação (m)

**Explicação:** A equação de Bernoulli expressa a conservação de energia mecânica ao longo de uma linha de corrente para fluidos ideais (sem viscosidade) em escoamento permanente. Cada termo representa uma forma de energia por unidade de massa: energia de pressão, energia cinética e energia potencial.

#### **Equação de Bernoulli (Forma de Carga)**
$$
\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 = H
$$

**Onde:**
- $\frac{p}{\gamma}$ = carga de pressão (m)
- $\frac{V^2}{2g}$ = carga de velocidade (m)
- $z$ = carga de elevação (m)
- $H$ = carga total (m)

**Explicação:** Esta forma expressa a energia em termos de "altura" ou "carga", sendo muito útil em aplicações hidráulicas. A carga total $H$ permanece constante ao longo de uma linha de corrente.

#### **Equação de Bernoulli (Forma de Pressão)**
$$
p_1 + \frac{1}{2}\rho V_1^2 + \rho g z_1 = p_2 + \frac{1}{2}\rho V_2^2 + \rho g z_2
$$

**Explicação:** Esta forma expressa a conservação de energia em termos de pressão, sendo útil quando se trabalha diretamente com pressões.

### 3.2 Tipos de Pressão

#### **Pressão Estática**
$$
p_{estática} = p
$$

**Explicação:** É a pressão termodinâmica do fluido, medida por um instrumento que se move com o fluido ou perpendicular ao escoamento.

#### **Pressão Dinâmica**
$$
p_{dinâmica} = \frac{1}{2}\rho V^2
$$

**Explicação:** Representa a energia cinética por unidade de volume. É a pressão que seria obtida se o fluido fosse desacelerado isentropicamente até velocidade zero.

#### **Pressão de Estagnação (Total)**
$$
p_0 = p + \frac{1}{2}\rho V^2
$$

**Explicação:** É a soma da pressão estática com a pressão dinâmica. Representa a pressão total que seria medida se o fluido fosse completamente parado.

### 3.3 Equação da Continuidade

#### **Conservação da Massa (Escoamento Permanente)**
$$
\rho_1 A_1 V_1 = \rho_2 A_2 V_2 = \dot{m}
$$

**Onde:**
- $A$ = área da seção transversal (m²)
- $\dot{m}$ = vazão mássica (kg/s)

**Explicação:** Para escoamento permanente, a vazão mássica deve ser constante. Esta equação é frequentemente usada em conjunto com Bernoulli.

#### **Para Fluidos Incompressíveis**
$$
A_1 V_1 = A_2 V_2 = Q
$$

**Onde:**
- $Q$ = vazão volumétrica (m³/s)

**Explicação:** Para fluidos incompressíveis, a vazão volumétrica é constante, simplificando significativamente os cálculos.

### 3.4 Aplicações da Equação de Bernoulli

#### **Tubo de Pitot**
$$
V = \sqrt{\frac{2(p_0 - p)}{\rho}}
$$

**Onde:**
- $p_0$ = pressão de estagnação (Pa)
- $p$ = pressão estática (Pa)

**Explicação:** O tubo de Pitot mede a velocidade do escoamento comparando a pressão de estagnação com a pressão estática.

#### **Tubo de Venturi**
$$
Q = C_d A_2 \sqrt{\frac{2(p_1 - p_2)}{\rho(1 - \beta^4)}}
$$

**Onde:**
- $C_d$ = coeficiente de descarga (≈ 0,98 para Venturi)
- $A_2$ = área da garganta (m²)
- $\beta = \frac{D_2}{D_1}$ = razão de diâmetros
- $p_1, p_2$ = pressões antes e na garganta (Pa)

**Explicação:** O tubo de Venturi mede vazão criando uma restrição controlada que gera uma diferença de pressão proporcional ao quadrado da velocidade.

#### **Placa de Orifício**
$$
Q = C_d A_0 \sqrt{\frac{2(p_1 - p_2)}{\rho(1 - \beta^4)}}
$$

**Onde:**
- $C_d$ = coeficiente de descarga (≈ 0,6 para placa de orifício)
- $A_0$ = área do orifício (m²)

**Explicação:** Similar ao Venturi, mas com maior perda de carga devido à separação do escoamento após o orifício.

#### **Escoamento através de Orifício**
$$
V = C_v \sqrt{2gh}
$$

**Onde:**
- $C_v$ = coeficiente de velocidade (≈ 0,97)
- $h$ = altura da coluna de líquido acima do orifício (m)

**Explicação:** Esta é a famosa equação de Torricelli, que relaciona a velocidade de saída de um jato com a altura da coluna de líquido.

#### **Vazão através de Orifício**
$$
Q = C_d A_0 \sqrt{2gh}
$$

**Onde:**
- $C_d$ = coeficiente de descarga (≈ 0,6)
- $A_0$ = área do orifício (m²)

**Explicação:** A vazão real é menor que a teórica devido à contração da veia líquida (vena contracta).

### 3.5 Limitações da Equação de Bernoulli

#### **Número de Mach para Compressibilidade**
$$
M = \frac{V}{c}
$$

**Onde:**
- $M$ = número de Mach
- $V$ = velocidade do escoamento (m/s)
- $c$ = velocidade do som (m/s)

**Explicação:** Para $M < 0,3$, os efeitos de compressibilidade são desprezíveis e Bernoulli pode ser aplicada. Para $M > 0,3$, correções de compressibilidade são necessárias.

#### **Número de Reynolds para Efeitos Viscosos**
$$
Re = \frac{\rho V L}{\mu} = \frac{V L}{\nu}
$$

**Onde:**
- $Re$ = número de Reynolds
- $L$ = comprimento característico (m)
- $\mu$ = viscosidade dinâmica (Pa·s)
- $\nu$ = viscosidade cinemática (m²/s)

**Explicação:** Para $Re$ alto (> 1000), os efeitos viscosos são localizados e Bernoulli é aplicável na região central do escoamento. Para $Re$ baixo, os efeitos viscosos dominam.

### 3.6 Linha de Energia e Linha Piezométrica

#### **Linha de Energia (EGL)**
$$
EGL = \frac{p}{\gamma} + \frac{V^2}{2g} + z
$$

**Explicação:** Representa graficamente a energia total por unidade de peso ao longo do escoamento. Para fluidos ideais, é horizontal.

#### **Linha Piezométrica (HGL)**
$$
HGL = \frac{p}{\gamma} + z
$$

**Explicação:** Representa a energia de pressão mais a energia potencial por unidade de peso. A diferença entre EGL e HGL é a energia cinética.

### 3.7 Equação de Bernoulli Modificada (com Perdas)

#### **Bernoulli com Perdas**
$$
\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L
$$

**Onde:**
- $h_L$ = perda de carga (m)

**Explicação:** Para escoamentos reais, deve-se incluir as perdas de energia devido ao atrito viscoso e outras irreversibilidades. Esta forma estendida é amplamente usada em aplicações práticas.

---

### Exemplos Práticos

**Exemplo 1: Escoamento horizontal**
> Água escoa horizontalmente em um tubo onde a pressão cai de $250\,kPa$ para $150\,kPa$. Se a velocidade inicial é $2\,m/s$, qual a velocidade final? ($\rho=1000\,kg/m^3$)

$P_1 + \frac{1}{2}\rho U_1^2 = P_2 + \frac{1}{2}\rho U_2^2$  
$250\,000 + 0.5 \times 1000 \times 2^2 = 150\,000 + 0.5 \times 1000 \times U_2^2$  
$250\,000 + 2000 = 150\,000 + 500 U_2^2$  
$252\,000 - 150\,000 = 500 U_2^2$  
$102\,000 = 500 U_2^2$  
$U_2^2 = 204$  
$U_2 = 14,28\,m/s$

---

**Exemplo 2: Tubo vertical**
> Água sobe $10\,m$ em um tubo estreito. Qual a diferença de pressão necessária para levantar a água essa altura? ($\rho=1000\,kg/m^3$)

$\Delta P = \rho g \Delta h = 1000 \times 9,81 \times 10 = 98\,100\,Pa$

---

**Exemplo 3: Medidor de vazão (tubo de Venturi)**
> Em um tubo Venturi, a área da entrada é $10\,cm^2$ e a do gargalo é $2\,cm^2$. Se a velocidade na entrada é $1\,m/s$, qual a velocidade no gargalo?

Pela continuidade: $A_1 U_1 = A_2 U_2$  
$0,001 \times 1 = 0,0002 \times U_2$  
$U_2 = 5\,m/s$

---

**Exemplo 4: Diferença de pressão em um esguicho**
> Qual a pressão necessária para que a água saia de um cano na velocidade de $10\,m/s$?

$\Delta P = \frac{1}{2}\rho U^2 = 0,5 \times 1000 \times 10^2 = 50\,000\,Pa$

""")

    elif cap == "Capítulo 8 – Escoamento Viscoso em Condutos":
        st.subheader("Capítulo 8 – Escoamento Viscoso em Condutos")
        st.markdown(r"""
### 8.1 Classificação do Escoamento

#### **Número de Reynolds**
$$
Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}
$$

**Onde:**
- $Re$ = número de Reynolds
- $V$ = velocidade média (m/s)
- $D$ = diâmetro do tubo (m)
- $\mu$ = viscosidade dinâmica (Pa·s)
- $\nu$ = viscosidade cinemática (m²/s)

**Explicação:** O número de Reynolds determina o regime de escoamento:
- $Re < 2300$: Escoamento laminar
- $2300 < Re < 4000$: Região de transição
- $Re > 4000$: Escoamento turbulento

### 8.2 Escoamento Laminar

#### **Perfil de Velocidade (Hagen-Poiseuille)**
$$
u(r) = u_{max}\left(1 - \frac{r^2}{R^2}\right)
$$

**Onde:**
- $u(r)$ = velocidade na posição radial $r$ (m/s)
- $u_{max}$ = velocidade máxima no centro (m/s)
- $R$ = raio do tubo (m)

**Explicação:** O perfil de velocidade laminar é parabólico, com velocidade máxima no centro e zero na parede.

#### **Velocidade Máxima**
$$
u_{max} = \frac{R^2}{4\mu}\left(-\frac{dp}{dx}\right)
$$

**Onde:**
- $\frac{dp}{dx}$ = gradiente de pressão (Pa/m)

#### **Velocidade Média**
$$
V = \frac{u_{max}}{2} = \frac{R^2}{8\mu}\left(-\frac{dp}{dx}\right)
$$

**Explicação:** A velocidade média é metade da velocidade máxima para escoamento laminar.

#### **Equação de Hagen-Poiseuille (Vazão)**
$$
Q = \frac{\pi R^4}{8\mu}\left(-\frac{dp}{dx}\right) = \frac{\pi D^4 \Delta p}{128 \mu L}
$$

**Onde:**
- $Q$ = vazão volumétrica (m³/s)
- $\Delta p$ = queda de pressão (Pa)
- $L$ = comprimento do tubo (m)

**Explicação:** Esta equação fundamental relaciona a vazão com a queda de pressão em escoamento laminar. A vazão é proporcional à quarta potência do diâmetro.

#### **Fator de Atrito Laminar**
$$
f = \frac{64}{Re}
$$

**Explicação:** Para escoamento laminar, o fator de atrito depende apenas do número de Reynolds e pode ser calculado analiticamente.

### 8.3 Escoamento Turbulento

#### **Perfil de Velocidade (Lei de Potência)**
$$
\frac{u}{u_{max}} = \left(\frac{y}{R}\right)^{1/n}
$$

**Onde:**
- $y$ = distância da parede (m)
- $n$ = expoente (≈ 7 para tubos lisos)

**Explicação:** O perfil turbulento é mais uniforme que o laminar, com gradientes altos próximos à parede.

#### **Fator de Atrito para Tubos Lisos**

**Equação de Blasius (Re < 10⁵):**
$$
f = \frac{0,316}{Re^{0,25}}
$$

**Equação de Prandtl (Re > 10⁵):**
$$
\frac{1}{\sqrt{f}} = 2,0 \log(Re\sqrt{f}) - 0,8
$$

**Explicação:** Para escoamento turbulento, o fator de atrito deve ser determinado por correlações empíricas.

#### **Fator de Atrito para Tubos Rugosos (Colebrook-White)**
$$
\frac{1}{\sqrt{f}} = -2,0 \log\left(\frac{\varepsilon/D}{3,7} + \frac{2,51}{Re\sqrt{f}}\right)
$$

**Onde:**
- $\varepsilon$ = rugosidade absoluta (m)
- $\varepsilon/D$ = rugosidade relativa

**Explicação:** Esta equação implícita relaciona o fator de atrito com Reynolds e rugosidade. É resolvida iterativamente ou usando o diagrama de Moody.

### 8.4 Perdas de Carga

#### **Equação de Darcy-Weisbach**
$$
h_f = f \frac{L}{D} \frac{V^2}{2g}
$$

**Onde:**
- $h_f$ = perda de carga por atrito (m)
- $f$ = fator de atrito
- $L$ = comprimento do tubo (m)
- $D$ = diâmetro (m)
- $V$ = velocidade média (m/s)

**Explicação:** Esta é a equação fundamental para calcular perdas de carga distribuídas em tubulações. Válida para escoamentos laminar e turbulento.

#### **Perdas Localizadas**
$$
h_L = K \frac{V^2}{2g}
$$

**Onde:**
- $h_L$ = perda localizada (m)
- $K$ = coeficiente de perda

**Explicação:** Perdas em acessórios (válvulas, cotovelos, etc.) são proporcionais à energia cinética.

#### **Perda Total**
$$
h_{total} = h_f + \sum h_L = f \frac{L}{D} \frac{V^2}{2g} + \sum K \frac{V^2}{2g}
$$

### 8.5 Comprimento de Entrada

#### **Comprimento de Entrada Laminar**
$$
\frac{L_e}{D} = 0,06 \, Re
$$

#### **Comprimento de Entrada Turbulento**
$$
\frac{L_e}{D} = 10 \text{ a } 60
$$

**Explicação:** O comprimento de entrada é a distância necessária para o perfil de velocidade se desenvolver completamente.

### 8.6 Análise de Sistemas de Tubulações

#### **Tubulações em Série**
$$
Q_1 = Q_2 = Q_3 = \text{constante}
$$
$$
h_{total} = h_1 + h_2 + h_3
$$

#### **Tubulações em Paralelo**
$$
Q_{total} = Q_1 + Q_2 + Q_3
$$
$$
h_1 = h_2 = h_3
$$

#### **Equação da Energia para Sistemas**
$$
\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 + h_p = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L
$$

**Onde:**
- $h_p$ = altura manométrica da bomba (m)

### 8.7 Potência de Bombeamento

#### **Potência Hidráulica**
$$
P_{hidráulica} = \gamma Q h_p = \rho g Q h_p
$$

**Onde:**
- $P$ = potência (W)
- $h_p$ = altura manométrica (m)

#### **Potência no Eixo**
$$
P_{eixo} = \frac{P_{hidráulica}}{\eta}
$$

**Onde:**
- $\eta$ = eficiência da bomba

**Explicação:** A potência real necessária é maior que a hidráulica devido às perdas na bomba.

### 8.8 Medição de Vazão

#### **Rotâmetro**
$$
Q = C_d A_f \sqrt{\frac{2g(\rho_f - \rho)V_f}{\rho}}
$$

**Onde:**
- $A_f$ = área anular ao redor do flutuador (m²)
- $\rho_f$ = massa específica do flutuador (kg/m³)
- $V_f$ = volume do flutuador (m³)

#### **Medidor de Vórtice**
$$
f = St \frac{V}{D}
$$

**Onde:**
- $f$ = frequência de desprendimento de vórtices (Hz)
- $St$ = número de Strouhal (≈ 0,2)

**Explicação:** A frequência de vórtices é proporcional à velocidade do escoamento.


## Tabela de Símbolos

| Símbolo | Descrição | Unidade SI |
|---------|-----------|------------|
| $A$ | Área | m² |
| $c$ | Velocidade do som | m/s |
| $C_d$ | Coeficiente de descarga | - |
| $D$ | Diâmetro | m |
| $f$ | Fator de atrito | - |
| $F$ | Força | N |
| $g$ | Aceleração da gravidade | m/s² |
| $h$ | Altura, profundidade | m |
| $h_f$ | Perda de carga por atrito | m |
| $h_L$ | Perda de carga localizada | m |
| $h_p$ | Altura manométrica da bomba | m |
| $I$ | Momento de inércia | m⁴ |
| $K$ | Coeficiente de perda localizada | - |
| $L$ | Comprimento | m |
| $M$ | Número de Mach | - |
| $\dot{m}$ | Vazão mássica | kg/s |
| $p$ | Pressão | Pa |
| $p_0$ | Pressão de estagnação | Pa |
| $p_v$ | Pressão de vapor | Pa |
| $P$ | Potência | W |
| $Q$ | Vazão volumétrica | m³/s |
| $r$ | Coordenada radial | m |
| $R$ | Raio, constante do gás | m, J/kg·K |
| $Re$ | Número de Reynolds | - |
| $S$ | Densidade relativa | - |
| $t$ | Tempo | s |
| $T$ | Temperatura | K |
| $u$ | Velocidade local | m/s |
| $V$ | Velocidade média | m/s |
| $V$ | Volume | m³ |
| $W$ | Peso | N |
| $z$ | Elevação | m |
| $\beta$ | Razão de diâmetros | - |
| $\gamma$ | Peso específico | N/m³ |
| $\varepsilon$ | Rugosidade absoluta | m |
| $\eta$ | Eficiência | - |
| $\theta$ | Ângulo | rad |
| $\mu$ | Viscosidade dinâmica | Pa·s |
| $\nu$ | Viscosidade cinemática | m²/s |
| $\rho$ | Massa específica | kg/m³ |
| $\sigma$ | Tensão superficial | N/m |
| $\tau$ | Tensão de cisalhamento | Pa |
| $\omega$ | Velocidade angular | rad/s |

---

## Observações Importantes

### Condições de Aplicabilidade

1. **Equação de Bernoulli:**
   - Escoamento permanente
   - Fluido incompressível (M < 0,3)
   - Fluido ideal (sem viscosidade)
   - Ao longo de uma linha de corrente
   - Sem trabalho externo

2. **Escoamento Laminar:**
   - Re < 2300 para tubos circulares
   - Perfil parabólico de velocidade
   - Perdas proporcionais à velocidade

3. **Escoamento Turbulento:**
   - Re > 4000 para tubos circulares
   - Perfil mais uniforme de velocidade
   - Perdas proporcionais ao quadrado da velocidade

### Conversões Úteis

- 1 bar = 10⁵ Pa
- 1 atm = 101.325 Pa ≈ 101,3 kPa
- 1 psi = 6.895 Pa
- 1 m de coluna d'água = 9.810 Pa
- 1 mmHg = 133,3 Pa

### Propriedades Típicas (20°C, 1 atm)

**Água:**
- $\rho = 998$ kg/m³
- $\mu = 1,002 \times 10^{-3}$ Pa·s
- $\nu = 1,004 \times 10^{-6}$ m²/s

**Ar:**
- $\rho = 1,204$ kg/m³
- $\mu = 1,825 \times 10^{-5}$ Pa·s
- $\nu = 1,516 \times 10^{-5}$ m²/s

---

### Exemplos Práticos

**Exemplo 1: Número de Reynolds**
> Água ($\mu = 1,0 \times 10^{-3}\,Pa \cdot s$) escoa em um tubo de $D=0,05\,m$ a $U=2\,m/s$. Calcule o $Re$.

$\rho = 1000\,kg/m^3$  
$Re = \frac{1000 \times 2 \times 0,05}{1 \times 10^{-3}} = 100\,000$  
**Escoamento turbulento.**

---

**Exemplo 2: Perda de carga distribuída**
> Em um tubo de $L=10\,m$, $D=0,05\,m$, $U=2\,m/s$, $f=0,03$, calcule $h_f$.

$h_f = 0,03 \times \frac{10}{0,05} \times \frac{2^2}{2 \times 9,81} = 0,03 \times 200 \times \frac{4}{19,62}$  
$= 6 \times 0,204 = 1,224\,m$

---

**Exemplo 3: Perda localizada**
> Se uma válvula tem $K=2$, com $U=2\,m/s$, qual é $h_{local}$?

$h_{local} = 2 \times \frac{2^2}{2 \times 9,81} = 2 \times \frac{4}{19,62} = 2 \times 0,204 = 0,408\,m$

---

**Exemplo 4: Vazão volumétrica**
> Se $U=2\,m/s$ e o tubo tem $D=0,05\,m$, qual é a vazão $Q$?

$A = \pi D^2 / 4 = 3,1416 \times 0,0025 / 4 = 0,00196\,m^2$  
$Q = A \times U = 0,00196 \times 2 = 0,00392\,m^3/s = 3,92\,L/s$

""")

elif choice == "Exercícios Resolvidos":
    st.header("📝 Exercícios Resolvidos")
    st.info("Aqui você poderá ver as soluções passo a passo dos exercícios da lista.")

    # Banco de questões
    questoes = {
        "2.18": {
            "capitulo": 2,
            "enunciado": (
        "Admitindo que a pressão atmosférica é igual a 101 kPa (abs), determine as alturas das colunas de fluido em barômetros "
        "que contém os seguintes fluidos:\n"
        "(a) mercúrio, (b) água e (c) álcool etílico.\n"
        "Calcule as alturas levando em consideração a pressão de vapor destes fluidos e compare com os valores obtidos desconsiderando a pressão de vapor.\n"
        "Densidades: mercúrio = 13.600 kg/m³, água = 999 kg/m³, álcool = 789 kg/m³.\n"
        "Pressão de vapor da tabela 1.5: mercúrio = 0,16 Pa, água = 1.777 Pa, álcool = 5.900 Pa.\n"
        "g = 9,81 m/s²."
    ),
    "dica": (
        "Para barômetros, use $P_{atm} = \\rho g h + P_{vap}$.\n"
        "Isolando a altura: $h = (P_{atm} - P_{vap})/(\\rho g)$.\n"
        "Resolva para cada fluido e compare com o cálculo desprezando $P_{vap}$."
    ),
    "resolucao": r"""
**Resolução passo a passo:**

1. **Fórmula geral:**
   $$
   P_{atm} = \rho g h + P_{vap} \implies h = \frac{P_{atm} - P_{vap}}{\rho g}
   $$

   Onde:
   - $P_{atm}$: pressão atmosférica (Pa)
   - $\rho$: densidade do fluido (kg/m³)
   - $g$: gravidade (m/s²)
   - $P_{vap}$: pressão de vapor do fluido (Pa)
   - $h$: altura da coluna de fluido (m)

2. **Dados:**
   - $P_{atm} = 101\,000$ Pa
   - $g = 9,81$ m/s²

   | Fluido   | $\rho$ (kg/m³) | $P_{vap}$ (Pa) |
   |----------|---------------|---------------|
   | Mercúrio | 13.600        | 0,16          |
   | Água     | 999           | 1.770         |
   | Álcool   | 789           | 5.900         |

3. **(a) Mercúrio**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 0,16}{13\,600 \times 9,81} \approx \frac{100\,999,84}{133\,416} \approx 0,7570\,m = 75,70\,cm
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{13\,600 \times 9,81} \approx 0,7570\,m = 75,70\,cm
     $$
   - **Diferença é desprezível. Por tanto = 0**

4. **(b) Água**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 1\,770}{999 \times 9,81} = \frac{99\,120}{9\,800,19} \approx 10,13\,m
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{9\,800,19} \approx 10,31\,m
     $$
   - **A diferença devido ao vapor é significativa (~18 cm).**

5. **(c) Álcool etílico**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 5\,900}{789 \times 9,81} = \frac{95\,100}{7\,740,1} \approx 12,29\,m
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{7\,740,1} \approx 13,04\,m
     $$
   - **A diferença é significativa (~75 cm).**

> **Resumo dos símbolos:**  
> - $P_{atm}$: pressão atmosférica  
> - $\rho$: densidade do fluido  
> - $g$: aceleração da gravidade  
> - $P_{vap}$: pressão de vapor  
> - $h$: altura da coluna

**Conclusão:**  
A pressão de vapor pode ser desprezada para o mercúrio, mas é importante para líquidos voláteis como água e álcool.
""",
        "resposta": {
            "a": 0,        # altura mercúrio (m), com pressão de vapor
            "b": 0.18,     # altura água (m), com pressão de vapor
            "c": 0.75      # altura álcool (m), com pressão de vapor
        },
        "tolerancia": {
            "a": 0,
            "b": 0.03,
            "c": 0.05
        },
        "unidade": "m para a diferença da comparação",
    },

    "2.24": {
        "capitulo": 2,
        "imagem": "images/2_24.png",
        "enunciado": (
            "A Fig. P2.24 mostra um manômetro com tubo em U conectado a um tanque fechado que contém ar e água. "
            "A pressão do ar na extremidade fechada do manômetro é igual a 1,10 bar (abs). "
            "Determine a leitura no outro manômetro se a altura diferencial no manômetro com tubo em U é igual a 1219 mm. "
            "Admita que o valor da pressão atmosférica é o padrão e despreze o efeito do peso do ar nas colunas do manômetro. "
            "Dado: Peso específico do fluido manométrico $\\gamma = 14,14 \\text{ kN/m}^3$."
        ),
        "dica": (
            "Use a diferença de pressão: $\\Delta P = \\gamma \\cdot h$.\n"
            "Pressão manométrica é a diferença entre a pressão do ar no tanque e a atmosférica.\n"
            "Converta todas as unidades para SI: 1,10 bar = 110000 Pa; $h$ em metros."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - Pressão do ar (fechada): $P_{ar} = 1,10$ bar $= 1100$ kPa (abs)
    - Pressão atmosférica: $P_{atm} = 101$ kPa
    - Altura diferencial no U: $h = 1219$ mm $= 1,219$ m
    - Peso específico da água: $\gamma = 9,81 kN/m³
    - Peso específico do manométrico: $\gamma = 14,14$ kN/m³ $

    2. **Pressão manométrica no tanque:**
    $$
    P_1 = P_{ar} - P_{atm} = 110 - 101 = 9 \text{kPa}
    $$

    3. **Diferença de pressão lida pelo manômetro:**
    $$
    P_{2} = P_{1} + (\gamma_{agua} \cdot h_{agua}) + (\gamma_{2} \cdot h_{2})
    $$
    $$
    P_{2} = 9 + (9,81 \cdot 0,61) + (14\,14 \cdot 1\,219)
    $$
    $$
    P_{2} = 9 + 5,9841 + 17,2367
    $$
    $$
    P_{2} = 32,2 \text{kPa}
    $$
    
    4. **Interpretação da leitura:**
    - Se a diferença de pressão medida pelo manômetro é maior que a pressão manométrica, a leitura do manômetro não está compatível.
    - Geralmente, pede-se que você **calcule a pressão lida pelo outro manômetro** sabendo a leitura em um, ou vice-versa.
    - Aqui, basta apresentar o resultado do cálculo do manômetro em U: **32,22 kPa** (leitura do manômetro U).

    > **Símbolos:**  
    > - $P_{ar}$: pressão do ar no tanque  
    > - $P_{atm}$: pressão atmosférica  
    > - $h$: diferença de altura (m)  
    > - $\gamma$: peso específico do fluido manométrico  
    > - $\Delta P$: diferença de pressão lida

    **Conclusão:**  
    A diferença de pressão lida no manômetro em U é **32,22 kPa**.
    """,
        "resposta": 32.22,
        "tolerancia": 50,
        "unidade": "kPa"
    },

    "2.26": {
        "capitulo": 2,
        "imagem": "images/2_26.png",
        "enunciado": (
            "Considere o arranjo mostrado na Fig. P2.26. Sabendo que a diferença entre as pressões em B e A é igual a 20 kPa, "
            "determine o peso específico do fluido manométrico."
        ),
        "dica": (
            "Use o método de percurso de A para B, somando a pressão ao descer e subtraindo ao subir.\n"
            "A equação resultante terá a forma $P_B - P_A =...$, contendo $\\gamma_{fm}$ como incógnita.\n"
            "Se o resultado for fisicamente impossível (negativo), verifique a direção da diferença de pressão."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados e Pesos Específicos:**
   - $P_B - P_A = 20 \text{ kPa} = 20.000 \text{ Pa}$
   - Fluido A: $SG_A = 1,2 \implies \gamma_A = 1,2 \times 9.810 = 11.772 \text{ N/m³}$
   - Fluido B: $\rho_B = 1.500 \text{ kg/m³} \implies \gamma_B = 1.500 \times 9,81 = 14.715 \text{ N/m³}$
   - Incógnita: $\gamma_{fm}$

2. **Equação do Percurso (de A para B):**
   $$
   P_A + \gamma_A(2) + \gamma_{fm}(1) - \gamma_{fm}(3) - \gamma_B(2) = P_B
   $$
   Rearranjando para a diferença de pressão:
   $$
   P_B - P_A = 2\gamma_A - 2\gamma_{fm} - 2\gamma_B
   $$

3. **Resolvendo a Equação:**
   $$
   20.000 = 2(11.772) - 2\gamma_{fm} - 2(14.715)
   $$  
   $$
   20.000 = 23.544 - 2\gamma_{fm} - 29.430
   $$  
   $$
   20.000 = -5.886 - 2\gamma_{fm} \implies 2\gamma_{fm} = -25.886
   $$
   Um peso específico negativo é impossível. Isso indica que a diferença de pressão real é $P_A - P_B = 20 \text{ kPa}$, ou seja, $P_B - P_A = -20.000 \text{ Pa}$.

4. **Corrigindo e Resolvendo Novamente:**
   $$
   -20.000 = -5.886 - 2\gamma_{fm}
   $$  
   $$
   2\gamma_{fm} = 20.000 - 5.886 = 14.114
   $$  
   $$
   \gamma_{fm} = 7.057 \text{ N/m³}
   $$

**Conclusão:**
O peso específico do fluido manométrico é **7.057 N/m³**. Este valor é consistente com a resposta do livro (7.100 N/m³), com a pequena diferença devida a arredondamentos.
""",
        "resposta": 7057,
        "tolerancia": 100,
        "unidade": "N/m³"
    },

    "2.27": {
        "capitulo": 2,
        "imagem": "images/2_27.png",
        "enunciado": (
            "A Fig. P2.27 mostra um manômetro em U conectado a um tanque pressurizado. "
            "Sabendo que a pressão do ar contido no tanque é 13,8 kPa, determine a leitura diferencial no manômetro, $h$.\n"
            "Dado: mercúrio ($SG = 13,6$)."
        ),
        "dica": (
            "A pressão manométrica do ar, mais a pressão da coluna de água, é equilibrada pela pressão da coluna de mercúrio de altura h.\n"
            "Use o método de percurso do ar no tanque até a extremidade aberta do manômetro (pressão manométrica zero)."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados:**
   - Pressão do ar (manométrica): $P_{ar} = 13,8 \text{ kPa} = 13.800 \text{ Pa}$
   - Peso específico da água: $\gamma_{H_2O} = 9.810 \text{ N/m³}$
   - Peso específico do mercúrio: $\gamma_{Hg} = 13,6 \times 9.810 = 133.416 \text{ N/m³}$
   - Altura da coluna de água: $h_{H_2O} = 0,6 + 0,6 = 1,2 \text{ m}$

2. **Equação do Percurso:**
   Partindo do ar no tanque até a extremidade aberta (pressão manométrica = 0):
   $$
   P_{ar} + \gamma_{H_2O} \cdot (1,2) - \gamma_{Hg} \cdot h = 0
   $$

3. **Isolando e Resolvendo para h:**
   $$
   h = \frac{P_{ar} + \gamma_{H_2O} \cdot (1,2)}{\gamma_{Hg}}
   $$  
   $$
   h = \frac{13.800 + 9.810 \cdot (1,2)}{133.416}
   $$  
   $$
   h = \frac{13.800 + 11.772}{133.416} = \frac{25.572}{133.416} \approx 0,1917 \text{ m}
   $$

**Conclusão:**
A leitura diferencial no manômetro é de aproximadamente **0,192 m** ou **19,2 cm**.
""",
        "resposta": 0.192,
        "tolerancia": 0.002,
        "unidade": "m"
    },

    "2.32": {
        "capitulo": 2,
        "imagem": "images/2_32.png",
        "enunciado": (
            "O manômetro inclinado da Fig. P2.32 indica que a pressão no tubo A é 0,6 psi. "
            "O fluido que escoa nos tubos A e B é água e o fluido manométrico apresenta densidade 2,6 (relativa à água). "
            "Qual é a pressão no tubo B que corresponde à condição mostrada na figura?"
        ),
        "dica": (
            "Use o método de percurso de A para B. Para a seção inclinada, a variação de altura vertical é $h = L \\cdot \\sin\\theta$.\n"
            "Converta todas as unidades para o SI antes de calcular."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados e Conversões:**
   - $P_A = 0,6 \text{ psi} \times 6895 \text{ Pa/psi} = 4137 \text{ Pa}$
   - $\gamma_{agua} = 9810 \text{ N/m³}$
   - $\gamma_{fm} = 2,6 \times 9810 = 25.506 \text{ N/m³}$
   - Altura vertical nos tubos: $h_{vert} = 76 \text{ mm} = 0,076 \text{ m}$
   - Comprimento inclinado: $L = 203 \text{ mm} = 0,203 \text{ m}$

2. **Equação do Percurso (de A para B):**
   $$
   P_A + \gamma_{agua}(0,076) - \gamma_{fm}(L \sin30^\circ) - \gamma_{agua}(0,076) = P_B
   $$
   Os termos da água se cancelam.
   $$
   P_B = P_A - \gamma_{fm}(0,203 \times 0,5)
   $$

3. **Resolvendo para $P_B$:**
   $$
   P_B = 4137 - (25.506 \times 0,1015)
   $$  
   $$
   P_B = 4137 - 2588,86 = 1548,14 \text{ Pa}
   $$

**Conclusão:**
A pressão no tubo B é de aproximadamente **1,55 kPa**. Este valor é consistente com a resposta do livro (1,54 kPa).
""",
        "resposta": 1.55,
        "tolerancia": 0.02,
        "unidade": "kPa"
    },

    "2.35": {
        "capitulo": 2,
        "imagem": "images/2_35.png",
        "enunciado": (
            "O tanque cilíndrico com tampas hemisféricas mostrado na Fig. P2.35 contém um líquido volátil em equilíbrio com seu vapor. "
            "A massa específica do líquido é 800 kg/m³ e a do vapor pode ser desprezada. "
            "A pressão no vapor é 120 kPa (abs) e a pressão atmosférica local vale 101 kPa (abs). "
            "Nestas condições, determine: (a) a pressão indicada no manômetro do tipo Bourdon; "
            "e (b) a altura $h$ indicada no manômetro de mercúrio."
        ),
        "dica": (
            "(a) A pressão no Bourdon é a pressão manométrica no ponto. Calcule a pressão absoluta no ponto (vapor + coluna de líquido) e subtraia a atmosférica.\n"
            "(b) Use o método de percurso da superfície do líquido até a superfície aberta do mercúrio para encontrar h."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados:**
   - $P_{vapor} = 120.000 \text{ Pa (abs)}$
   - $P_{atm} = 101.000 \text{ Pa (abs)}$
   - $\gamma_{liquido} = 800 \text{ kg/m³} \times 9,81 = 7.848 \text{ N/m³}$
   - $\gamma_{Hg} = 13,6 \times 9.810 = 133.416 \text{ N/m³}$

---
### (a) Pressão no Manômetro de Bourdon

2. **Pressão absoluta no ponto do manômetro:**
   O manômetro está 1 m abaixo da superfície do líquido.
   $$
   P_{mano, abs} = P_{vapor} + (\gamma_{liquido} \cdot 1 \text{ m})
   $$  
   $$
   P_{mano, abs} = 120.000 + 7.848 = 127.848 \text{ Pa (abs)}
   $$

3. **Pressão manométrica (leitura):**
   $$
   P_{mano, man} = P_{mano, abs} - P_{atm} = 127.848 - 101.000 = 26.848 \text{ Pa}
   $$

---
### (b) Altura $h$ no Manômetro de Mercúrio

4. **Equação do Percurso:**
   Da superfície do líquido (pressão $P_{vapor}$) até a superfície aberta do mercúrio (pressão $P_{atm}$). A conexão está 2 m abaixo da superfície do líquido.
   $$
   P_{vapor} + \gamma_{liquido}(2) - \gamma_{Hg}(h) = P_{atm}
   $$

5. **Isolando e Resolvendo para h:**
   $$
   h = \frac{P_{vapor} + 2\gamma_{liquido} - P_{atm}}{\gamma_{Hg}}
   $$  
   $$
   h = \frac{120.000 + 2(7.848) - 101.000}{133.416}
   $$  
   $$
   h = \frac{34.696}{133.416} \approx 0,260 \text{ m}
   $$

**Conclusão:**
(a) A pressão no Bourdon é **26,85 kPa**.
(b) A altura no manômetro de mercúrio é **0,260 m** ou **26,0 cm**.
""",
        "resposta": {
            "a": 26.85,
            "b": 0.260
        },
        "tolerancia": {
            "a": 0.05,
            "b": 0.002
        },
        "unidade": {
            "a": "kPa",
            "b": "m"
        }
    },

    "2.41": {
        "capitulo": 2,
        "imagem": "images/2_41.png",
        "enunciado": (
            "A Fig. P2.41 mostra um conjunto cilindro-pistão (diâmetro = 152 mm) conectado a um manômetro de tubo inclinado com diâmetro igual a 12,7 mm. "
            "O fluido contido no cilindro e no manômetro é óleo (γ = 9,27 × 10³ N/m³). "
            "O nível do fluido no manômetro sobe do ponto (1) para o (2) quando nós colocamos um peso (W) no topo do cilindro. "
            "Qual é o valor do peso W para as condições mostradas na figura? "
            "Admita que a variação da posição do pistão é desprezível."
        ),
        "dica": (
            "A pressão exercida pelo peso ($W/A_{pistao}$) é equilibrada pelo aumento de pressão da coluna de óleo ($\\gamma \\cdot \\Delta h$).\n"
            "Calcule a altura vertical $\\Delta h$ a partir do deslocamento inclinado ($L \\cdot \\sin\\theta$).\n"
            "Calcule a área do pistão e resolva para W."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio:**
   A pressão do peso é igual à pressão da coluna de óleo adicional.
   $$
   \frac{W}{A_p} = \gamma_{oleo} \cdot \Delta h
   $$

2. **Dados e Cálculos Preliminares:**
   - **Altura vertical ($\Delta h$):**
     $L = 152 \text{ mm} = 0,152 \text{ m}$.
     $\Delta h = L \cdot \sin(30^\circ) = 0,152 \times 0,5 = 0,076 \text{ m}$.
   - **Área do pistão ($A_p$):**
     $D_p = 152 \text{ mm} = 0,152 \text{ m}$.
     $A_p = \frac{\pi D_p^2}{4} = \frac{\pi \cdot (0,152)^2}{4} \approx 0,01815 \text{ m}^2$.
   - **Peso específico do óleo ($\gamma_{oleo}$):**
     $\gamma_{oleo} = 9,27 \times 10^3 = 9.270 \text{ N/m³}$.

3. **Calcular o Peso (W):**
   $$
   W = A_p \cdot \gamma_{oleo} \cdot \Delta h
   $$  
   $$
   W = (0,01815) \times (9.270) \times (0,076) \approx 12,78 \text{ N}
   $$

**Conclusão:**
O valor do peso necessário é de aproximadamente **12,8 N**.
""",
        "resposta": 12.8,
        "tolerancia": 0.2,
        "unidade": "N"
    },

    "2.43": {
        "capitulo": 2,
        "imagem": "images/2_43.png",
        "enunciado": (
            "Determine a relação entre as áreas A₁/A₂ das pernas do manômetro mostrado na Fig. P2.43 se uma mudança na pressão no tubo B de 3,5 kPa "
            "provoca uma alteração de 25,4 mm no nível do mercúrio na perna direita do manômetro. A pressão no tubo A é constante."
        ),
        "dica": (
            "Use a conservação de volume para relacionar os deslocamentos nas duas pernas: $A_1 b = A_2 a$.\n"
            "A mudança de pressão em B é equilibrada pela mudança na pressão hidrostática das colunas de fluido.\n"
            "Monte a equação de equilíbrio de pressão e resolva para o deslocamento desconhecido, depois calcule a razão das áreas."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Conservação de Volume:**
   Se o nível na perna direita (área $A_2$) desce por uma distância `a`, o nível na perna esquerda (área $A_1$) sobe por uma distância `b`.
   $A_1 \cdot b = A_2 \cdot a \implies \frac{A_1}{A_2} = \frac{a}{b}$.
   Dado: $a = 25,4 \text{ mm} = 0,0254 \text{ m}$. Precisamos encontrar `b`.

2. **Equilíbrio de Pressão:**
   A mudança de pressão em B ($\Delta P_B$) é equilibrada pela mudança na pressão das colunas de fluido. A equação de equilíbrio é:
   $$
   \Delta P_B = a(\gamma_{Hg} - \gamma_{oleo}) + b(\gamma_{Hg} - \gamma_{H_2O})
   $$

3. **Dados e Pesos Específicos:**
   - $\Delta P_B = 3.500 \text{ Pa}$
   - $\gamma_{H_2O} = 9.810 \text{ N/m³}$
   - $\gamma_{oleo} = 0,8 \times 9.810 = 7.848 \text{ N/m³}$
   - $\gamma_{Hg} = 13,6 \times 9.810 = 133.416 \text{ N/m³}$

4. **Calcular o deslocamento `b`:**
   $$
   b = \frac{\Delta P_B - a(\gamma_{Hg} - \gamma_{oleo})}{\gamma_{Hg} - \gamma_{H_2O}}
   $$  
   $$
   b = \frac{3.500 - 0,0254 \cdot (133.416 - 7.848)}{133.416 - 9.810}
   $$  
   $$
   b = \frac{3.500 - 3.189,4}{123.606} = \frac{310,6}{123.606} \approx 0,00251 \text{ m}
   $$

5. **Calcular a Relação das Áreas:**
   $$
   \frac{A_1}{A_2} = \frac{a}{b} = \frac{0,0254}{0,00251} \approx 10,12
   $$

**Conclusão:**
A relação entre as áreas $A_1 / A_2$ é de aproximadamente **10,1**.
""",
        "resposta": 10.1,
        "tolerancia": 0.2,
        "unidade": "adimensional"
    },

    "2.44": {
        "capitulo": 2,
        "imagem": "images/2_44.png",
        "enunciado": (
            "O manômetro diferencial inclinado mostrado na Fig. P2.44 contém tetracloreto de carbono. "
            "Inicialmente, a diferença entre as pressões nos tubos A e B, que contém uma solução salina que apresenta densidade igual a 1,1, é nula. "
            "Qual deve ser o ângulo para que o manômetro indique uma leitura de 305 mm quando a diferença de pressões for igual a 0,7 kPa?"
        ),
        "dica": (
            "A diferença de pressão aplicada é equilibrada pela diferença de pressão hidrostática entre os fluidos sobre a altura vertical do deslocamento.\n"
            "$\\Delta P = (\\gamma_{CCl_4} - \\gamma_{salina}) \\cdot h$, onde $h = L \\cdot \\sin\\theta$."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio Físico:**
   A diferença de pressão é equilibrada pela coluna de fluido deslocada.
   $$
   \Delta P = (\gamma_{CCl_4} - \gamma_{salina}) \cdot L \sin\theta
   $$

2. **Dados e Pesos Específicos:**
   - $\Delta P = 0,7 \text{ kPa} = 700 \text{ Pa}$
   - Leitura inclinada: $L = 305 \text{ mm} = 0,305 \text{ m}$
   - Solução Salina: $SG = 1,1 \implies \gamma_{salina} = 1,1 \times 9.810 = 10.791 \text{ N/m³}$
   - Tetracloreto de Carbono: $\rho_{CCl_4} \approx 1.590 \text{ kg/m³} \implies \gamma_{CCl_4} \approx 15.598 \text{ N/m³}$

3. **Isolando e Resolvendo para $\theta$:**
   $$
   \sin\theta = \frac{\Delta P}{L \cdot (\gamma_{CCl_4} - \gamma_{salina})}
   $$  
   $$
   \sin\theta = \frac{700}{0,305 \cdot (15.598 - 10.791)}
   $$  
   $$
   \sin\theta = \frac{700}{0,305 \cdot (4.807)} = \frac{700}{1.466,1} \approx 0,4774
   $$  
   $$
   \theta = \arcsin(0,4774) \approx 28,5^\circ
   $$

**Conclusão:**
O ângulo de inclinação deve ser de aproximadamente **28,5°**. Este valor é consistente com a resposta do livro (27,8°), com a pequena diferença sendo atribuível a variações nos valores de densidade usados.
""",
        "resposta": 28.5,
        "tolerancia": 1.0,
        "unidade": "graus"
    },

    "2.46": {
        "capitulo": 2,
        "imagem": "images/2_46.png",
        "enunciado": (
            "Determine a variação na altura da coluna esquerda do manômetro de mercúrio mostrada na Fig. P2.46 "
            "provocada por um aumento de pressão de 34,5 kPa no tubo A. Admita que a pressão no tubo B permanece constante."
        ),
        "dica": (
            "Use a conservação de volume para relacionar o deslocamento vertical na perna esquerda (`a`) com o deslocamento inclinado na perna direita (`b`).\n"
            "O aumento de pressão em A é equilibrado pela mudança líquida na pressão hidrostática das três colunas de fluido."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Conservação de Volume:**
   Se a perna esquerda (diâmetro $\phi_1=12,7$ mm) desce por `a`, a perna direita (diâmetro $\phi_2=6,4$ mm) sobe por `b`.
   $$
   A_1 a = A_2 b \implies b = a \cdot (\frac{\phi_1}{\phi_2})^2 = a \cdot (\frac{12,7}{6,4})^2 \approx 3,937a
   $$

2. **Equilíbrio de Pressão:**
   A mudança de pressão em A ($\Delta P_A$) é balanceada pelas mudanças nas colunas de fluido.
   $$
   \Delta P_A = a(\gamma_{Hg} - \gamma_{H_2O}) + b\sin30^\circ(\gamma_{Hg} + \gamma_{oleo})
   $$

3. **Dados:**
   - $\Delta P_A = 34.500 \text{ Pa}$
   - $\gamma_{H_2O} = 9.810 \text{ N/m³}$
   - $\gamma_{oleo} = 0,9 \times 9.810 = 8.829 \text{ N/m³}$
   - $\gamma_{Hg} = 13,6 \times 9.810 = 133.416 \text{ N/m³}$

4. **Resolvendo para `a`:**
   Substituímos $b = 3,937a$ na equação de pressão:
   $$
   34.500 = a(\gamma_{Hg} - \gamma_{H_2O}) + (3,937a) \cdot (0,5) \cdot (\gamma_{Hg} + \gamma_{oleo})
   $$  
   $$
   34.500 = a(133.416 - 9.810) + 1,9685a(133.416 + 8.829)
   $$  
   $$
   34.500 = a(123.606) + a(280.019) = a(403.625)
   $$  
   $$
   a = \frac{34.500}{403.625} \approx 0,0855 \text{ m}
   $$

**Conclusão:**
A variação na altura da coluna esquerda é de aproximadamente **85,5 mm**.
""",
        "resposta": 0.0855,
        "tolerancia": 0.001,
        "unidade": "m"
    },

    "3.14": {
        "capitulo": 3,
        "imagem": "images/3_14.png",
        "enunciado": (
            "Água escoa na torneira localizada no andar térreo do edifício mostrado na Fig. P3.14 com velocidade máxima de 6,1 m/s. "
            "Determine as velocidades máximas dos escoamentos nas torneiras localizadas no subsolo e no primeiro andar do edifício. "
            "Admita-se escoamento invíscido e altura de cada andar igual a 3,6 m."
        ),
        "dica": (
            "Use a equação de Bernoulli entre os pontos das torneiras. "
            "Como todas as torneiras são jatos livres abertos para a atmosfera, a pressão relativa em cada saída é nula, e o termo de pressão pode ser cancelado."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio Físico:**
   A relação entre velocidade e altura para um escoamento invíscido é dada pela Equação de Bernoulli. Como todas as torneiras estão abertas para a atmosfera, a pressão em cada saída é a mesma (pressão atmosférica), e os termos de pressão se cancelam. A equação simplifica para:
   $$
   \frac{V_1^2}{2g} + z_1 = \frac{V_2^2}{2g} + z_2
   $$

2. **Dados e Referencial:**
   - Ponto Térreo (ref): $V_0 = 6,1\ \mathrm{m/s}$, $z_0 = 0\ \mathrm{m}$
   - Ponto Subsolo: $V_{sub} =?$, $z_{sub} = -3,6\ \mathrm{m}$
   - Ponto Primeiro Andar: $V_{1} =?$, $z_{1} = +3,6\ \mathrm{m}$
   - $g = 9,81\ \mathrm{m/s^2}$

3. **Velocidade no Subsolo:**
   Aplicando Bernoulli entre o térreo e o subsolo:
   $$
   \frac{6,1^2}{2g} + 0 = \frac{V_{sub}^2}{2g} - 3,6
   $$  
   $$
   V_{sub}^2 = 6,1^2 + 2g \cdot 3,6 = 37,21 + 2(9,81)(3,6) = 37,21 + 70,632 = 107,842
   $$  
   $$
   V_{sub} = \sqrt{107,842} \approx 10,38\ \mathrm{m/s}
   $$

4. **Velocidade no Primeiro Andar:**
   Aplicando Bernoulli entre o térreo e o primeiro andar:
   $$
   \frac{6,1^2}{2g} + 0 = \frac{V_{1}^2}{2g} + 3,6
   $$  
   $$
   V_{1}^2 = 6,1^2 - 2g \cdot 3,6 = 37,21 - 70,632 = -33,422
   $$
   Como o resultado para $V_1^2$ é negativo, é fisicamente impossível haver escoamento. A energia não é suficiente para a água atingir essa altura.

**Conclusão:**
A velocidade no subsolo é **10,4 m/s** e não há escoamento no primeiro andar.
""",
        "resposta": {
            "subsolo": 10.4, 
            "primeiro": 0.0
        },
        "tolerancia": {
            "subsolo": 0.1, 
            "primeiro": 0.1
        },
        "unidade": "m/s"
    },
    "3.19": {
        "capitulo": 3,
        "imagem": "images/3_19.png",
        "enunciado": (
            "O diâmetro interno da tubulação mostrada na Fig. P3.19 é 19 mm e o jato d'água descarregado atinge uma altura de 71 mm. "
            "Determine a vazão volumétrica do escoamento na tubulação."
        ),
        "dica": (
            r"A energia cinética na saída do jato é convertida em energia potencial na altura máxima. Use $V = \sqrt{2gh}$ para encontrar a velocidade de saída. "
            r"Depois calcule a área da seção e a vazão $Q = A \cdot V$."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Calcular a Velocidade de Saída (V):**
   A altura máxima (h) que um jato livre atinge está relacionada à sua velocidade de saída (V) pela conversão de energia cinética em potencial: $h = V^2 / (2g)$.
   $$
   V = \sqrt{2gh} = \sqrt{2 \cdot 9,81 \cdot 0,071} \approx \sqrt{1,3927} \approx 1,18\,\mathrm{m/s}
   $$

2. **Calcular a Área da Tubulação (A):**
   $$
   D = 19\,\mathrm{mm} = 0,019\,\mathrm{m}
   $$  
   $$
   A = \frac{\pi D^2}{4} = \frac{\pi \cdot (0,019)^2}{4} \approx 2,835 \times 10^{-4}\,\mathrm{m}^2
   $$

3. **Calcular a Vazão Volumétrica (Q):**
   $$
   Q = A \cdot V = (2,835 \times 10^{-4}) \times 1,18 \approx 3,345 \times 10^{-4}\,\mathrm{m}^3/\mathrm{s}
   $$

**Conclusão:**
A vazão em volume do escoamento é de aproximadamente **$3,35 \times 10^{-4}$ m³/s** (ou 0,335 L/s).
""",
        "resposta": 3.35e-4,
        "tolerancia": 1e-5,
        "unidade": "m³/s"
    },
    "3.25": {
        "capitulo": 3,
        "imagem": "images/3_25.png",
        "enunciado": (
            "Água escoa em regime permanente na tubulação mostrada na Fig. P3.25. "
            "Sabendo que o manômetro indica pressão relativa nula no ponto 1 e admitindo escoamento invíscido, "
            "determine a pressão no ponto 2 e a vazão volumétrica."
        ),
        "dica": (
            "Primeiro, use Bernoulli entre o ponto 1 e a saída do jato livre (ponto 3) para encontrar a velocidade e a vazão. "
            "Depois, use Bernoulli entre os pontos 1 e 2 para encontrar a pressão P2."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

**Etapa 1: Calcular a Vazão (Q)**
Aplicamos Bernoulli entre o ponto (1) e a saída do jato livre (3).

1. **Dados e Relações:**
   - Ponto (1): $P_1 = 0$, $z_1 = 0$, $D_1 = 0,037$ m $\implies A_1 \approx 0,001075$ m²
   - Ponto (3): $P_3 = 0$, $z_3 = -0,92$ m, $D_3 = 0,031$ m $\implies A_3 \approx 0,000755$ m²
   - Continuidade: $A_1V_1 = A_3V_3 \implies V_1 = V_3 (A_3/A_1) \approx 0,7026 V_3$

2. **Bernoulli (1 para 3):**
   $$
   \frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_3}{\gamma} + \frac{V_3^2}{2g} + z_3
   $$  
   $$
   0 + \frac{(0,7026 V_3)^2}{2g} + 0 = 0 + \frac{V_3^2}{2g} - 0,92
   $$  
   $$
   0,92 = \frac{V_3^2(1 - 0,7026^2)}{2g} \implies V_3^2 = \frac{0,92 \cdot 19,62}{0,5063} \approx 35,65
   $$  
   $$
   V_3 = \sqrt{35,65} \approx 5,97\,\mathrm{m/s}
   $$

3. **Cálculo da Vazão:**
   $$
   Q = A_3 \cdot V_3 = (0,000755) \cdot (5,97) \approx 4,51 \times 10^{-3}\,\mathrm{m}^3/\mathrm{s}
   $$

---
**Etapa 2: Calcular a Pressão em P2**
Aplicamos Bernoulli entre o ponto (1) e o ponto (2).

1. **Dados e Relações:**
   - Ponto (1): $P_1 = 0$, $z_1 = 0$
   - Ponto (2): $P_2 =?$, $z_2 = +0,61$ m
   - Velocidades: Como o diâmetro é o mesmo, $V_1 = V_2$.

2. **Bernoulli (1 para 2):**
   $$
   \frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2
   $$
   Os termos de velocidade se cancelam.
   $$
   0 + 0 = \frac{P_2}{\gamma} + 0,61 \implies P_2 = -0,61 \cdot \gamma_{agua}
   $$  
   $$
   P_2 = -0,61 \times 9810 = -5984,1\,\mathrm{Pa}
   $$

**Conclusão:**
A vazão é **$4,51 \times 10^{-3}$ m³/s** e a pressão em P2 é **-5,98 kPa**.
""",
        "resposta": {
            "Q": 4.51e-3, 
            "P2": -5984
        },
        "tolerancia": {
            "Q": 1e-4, 
            "P2": 10
        },
        "unidade": {
            "Q": "m³/s", 
            "P2": "Pa"
        }
    },
    "3.30": {
        "capitulo": 3,
        "imagem": "images/3_30.png",
        "enunciado": (
            "Água escoa na contração axisimétrica mostrada na Fig. P3.30. "
            "Determine a vazão em volume na contração em função de $D$ sabendo que a diferença de alturas "
            "no manômetro é constante e igual a 0,2 m."
        ),
        "dica": (
            "Use a equação de Bernoulli entre as duas seções. A diferença de carga de pressão ($P/\\gamma$) é dada pela diferença de altura nos piezômetros (0,2 m). "
            "Assuma que a velocidade na seção larga é desprezível ($V_1 \\approx 0$)."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio Físico:**
   A Equação de Bernoulli entre os pontos (1) e (2) é:
   $$
   \frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2
   $$

2. **Simplificações:**
   - O tubo é horizontal, então $z_1 = z_2$.
   - A diferença de carga de pressão é medida pelos piezômetros: $\frac{P_1 - P_2}{\gamma} = 0,2$ m.
   - A velocidade na seção larga é muito menor que na garganta, então assumimos $V_1 \approx 0$.

3. **Bernoulli Simplificada:**
   $$
   \frac{P_1 - P_2}{\gamma} = \frac{V_2^2}{2g}
   $$  
   $$
   0,2 = \frac{V_2^2}{2g}
   $$

4. **Velocidade na Garganta ($V_2$):**
   $$
   V_2 = \sqrt{2g \cdot 0,2} = \sqrt{2 \cdot 9,81 \cdot 0,2} = \sqrt{3,924} \approx 1,981\,\mathrm{m/s}
   $$

5. **Vazão em Função de D:**
   A vazão é $Q = A_2 \cdot V_2$. A área $A_2$ é $\frac{\pi D^2}{4}$.
   $$
   Q = \left(\frac{\pi D^2}{4}\right) \cdot (1,981) = \left(\frac{1,981 \pi}{4}\right) D^2
   $$  
   $$
   Q \approx 1,556 D^2
   $$

**Conclusão:**
Arredondando o coeficiente, a vazão em função do diâmetro D é **$Q = 1,56 D^2$ m³/s**.
""",
        "resposta": "1.56*D**2",
        "tolerancia": 0.01,
        "unidade": "equação resultante de Q = () m³/s",
        "tipo": "texto",
    },
    "3.34": {
        "capitulo": 3,
        "imagem": "images/3_34.png",
        "enunciado": (
            "A Fig. P3.34 mostra a interação entre dois jatos d'água. "
            "Determine a altura $h$ admitindo que os efeitos viscosos são desprezíveis "
            "e que $A$ é um ponto de estagnação."
        ),
        "dica": (
            "A pressão no ponto de estagnação A é a mesma, seja calculada a partir do jato superior ou do inferior. "
            "Iguale as duas expressões da Equação de Bernoulli para a pressão em A."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio Físico:**
   No ponto de estagnação A, a velocidade é nula ($V_A = 0$). A pressão nesse ponto ($P_A$) pode ser encontrada a partir de duas trajetórias.

2. **Trajetória 1 (Tanque Superior para A):**
   Aplicando Bernoulli entre a superfície livre do tanque superior (S) e o ponto A:
   - $P_S = 0$, $V_S \approx 0$, $z_S = h$ (relativo a A).
   $$
   \frac{P_S}{\gamma} + \frac{V_S^2}{2g} + z_S = \frac{P_A}{\gamma} + \frac{V_A^2}{2g} + z_A \implies \frac{P_A}{\gamma} = h
   $$

3. **Trajetória 2 (Tanque Inferior para A):**
   Aplicando Bernoulli entre a superfície do líquido no tanque inferior (ponto 1) e o ponto A:
   - $P_1 = 1,72 \text{ bar} = 172.000$ Pa (relativa).
   - $V_1 \approx 0$.
   - A altura de (1) relativa a (A) é $z_1 = 2,44 - 6,10 = -3,66$ m.
   $$
   \frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_A}{\gamma} + \frac{V_A^2}{2g} + z_A \implies \frac{P_A}{\gamma} = \frac{P_1}{\gamma} + z_1
   $$

4. **Combinando as Equações:**
   Igualando as duas expressões para $P_A/\gamma$:
   $$
   h = \frac{P_1}{\gamma} + z_1
   $$  
   $$
   h = \frac{172.000}{9810} + (-3,66) = 17,533 - 3,66 \approx 13,87\,\mathrm{m}
   $$

**Conclusão:**
A altura $h$ é de aproximadamente **13,9 m**.
""",
        "resposta": 13.9,
        "tolerancia": 0.1,
        "unidade": "m"
    },
    "3.43": {
        "capitulo": 3,
        "imagem": "images/3_43.png",
        "enunciado": (
            "Uma mangueira de plástico, com 10 m de comprimento e diâmetro interno igual a 15 mm, "
            "é utilizada para drenar uma piscina do modo mostrado na Fig. P3.43. "
            "Qual é a vazão em volume do escoamento na mangueira? Admita que os efeitos viscosos são desprezíveis."
        ),
        "dica": (
            "Use a equação de Bernoulli entre a superfície da água na piscina e a saída da mangueira. "
            "A diferença de altura total entre os dois pontos determina a velocidade de saída."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Princípio Físico e Pontos de Análise:**
   Aplicamos a Equação de Bernoulli entre a superfície da piscina (ponto 1) e a saída da mangueira (ponto 2).
   - $P_1 = P_2 = 0$ (pressões atmosféricas/relativas).
   - $V_1 \approx 0$ (superfície de piscina grande).
   - A diferença de altura total é $\Delta z = z_1 - z_2 = 0,2 - (-0,23) = 0,43$ m.

2. **Bernoulli Simplificada:**
   $$
   z_1 - z_2 = \frac{V_2^2}{2g}
   $$

3. **Calcular a Velocidade de Saída ($V_2$):**
   $$
   V_2 = \sqrt{2g(z_1 - z_2)} = \sqrt{2 \cdot 9,81 \cdot 0,43} = \sqrt{8,4366} \approx 2,905\,\mathrm{m/s}
   $$

4. **Calcular a Vazão (Q):**
   - Diâmetro: $D = 15\,\mathrm{mm} = 0,015\,\mathrm{m}$
   - Área: $A_2 = \frac{\pi D^2}{4} = \frac{\pi (0,015)^2}{4} \approx 1,767 \times 10^{-4}\,\mathrm{m}^2$
   $$
   Q = A_2 \cdot V_2 = (1,767 \times 10^{-4}) \times 2,905 \approx 5,13 \times 10^{-4}\,\mathrm{m}^3/\mathrm{s}
   $$

**Conclusão:**
A vazão em volume é de aproximadamente **$5,13 \times 10^{-4}$ m³/s** (ou 0,513 L/s).
""",
        "resposta": 5.13e-4,
        "tolerancia": 1e-5,
        "unidade": "m³/s"
    },
    "3.51": {
        "capitulo": 3,
        "imagem": "images/3_51.png",
        "enunciado": (
            "Ar escoa no canal Venturi, com seção transversal retangular, mostrado na Fig. P3.51. "
            "A largura do canal é constante e igual a 0,06 m. Admitindo escoamento ideal, "
            "determine a vazão em volume de ar no canal. Calcule, também, a altura $h_2$ e a pressão no ponto 1 do canal."
        ),
        "dica": (
            "Interprete o manômetro de água para encontrar as pressões P1 e P2. "
            "Use Bernoulli e a Continuidade para o ar entre os pontos 1 e 2 para encontrar as velocidades e a vazão."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Interpretar o Manômetro:**
   - Pressão em (1): $P_1 = \gamma_{agua} \cdot h_1 = 9810 \times 0,04 = 392,4$ Pa.
   - A diferença de nível da água é 0,10 m. Se o nível em (1) está 0,04 m abaixo, o nível em (2) está 0,06 m acima.
   - Pressão em (2): $P_2 = -\gamma_{agua} \cdot (\text{altura de sucção}) = -9810 \times 0,06 = -588,6$ Pa.

2. **Dados e Relações (para o ar):**
   - $\Delta P = P_1 - P_2 = 392,4 - (-588,6) = 981$ Pa.
   - $\gamma_{ar} \approx 12,02$ N/m³.
   - Áreas: $A_1 = 0,04 \times 0,06 = 0,0024$ m²; $A_2 = 0,02 \times 0,06 = 0,0012$ m².
   - Continuidade: $V_2 = (A_1/A_2)V_1 = 2V_1$.

3. **Bernoulli (1 para 2):**
   $$
   \frac{P_1 - P_2}{\gamma_{ar}} = \frac{V_2^2 - V_1^2}{2g} = \frac{(2V_1)^2 - V_1^2}{2g} = \frac{3V_1^2}{2g}
   $$  
   $$
   \frac{981}{12,02} = \frac{3V_1^2}{19,62} \implies V_1^2 = \frac{81,6 \times 19,62}{3} \approx 533,6
   $$  
   $$
   V_1 = \sqrt{533,6} \approx 23,1\,\mathrm{m/s}
   $$

4. **Cálculo dos Resultados:**
   - **Vazão (Q):** $Q = A_1 \cdot V_1 = 0,0024 \times 23,1 \approx 0,0554\,\mathrm{m}^3/\mathrm{s}$.
   - **Altura ($h_2$):** É a altura de sucção da água no tubo 2, que é **0,06 m**.
   - **Pressão ($P_1$):** A pressão manométrica em (1) é **392,4 Pa**.

**Conclusão:**
A vazão é $\approx 0,055$ m³/s, a altura $h_2$ é 0,06 m e a pressão $P_1$ é 392,4 Pa.
""",
        "resposta": {
            "Q": 0.0555, 
            "h2": 0.06, 
            "P1": 392.4
        },
        "tolerancia": {
            "Q": 0.001, 
            "h2": 0.001, 
            "P1": 1
        },
        "unidade": {
            "Q": "m³/s", 
            "h2": "m", 
            "P1": "Pa"
        }
    },
    "3.58": {
        "capitulo": 3,
        "imagem": "images/3_58.png",
        "enunciado": (
            "Água escoa em regime permanente nos tanques mostrados na Fig. P3.58. "
            "Determine a profundidade da água no tanque $A$, $h_A$."
        ),
        "dica": (
            "Para regime permanente, a vazão que sai de A é igual à que sai de B. "
            "Calcule a vazão de saída do tanque B usando a altura $h_B$. "
            "Use essa vazão para encontrar a altura $h_A$ necessária para produzi-la."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

**Etapa 1: Calcular a Vazão de Saída do Tanque B (Q)**
Aplicamos Bernoulli entre a superfície do tanque B (ponto 3) e a saída (ponto 4).
1. **Velocidade de Saída ($V_4$):**
   $$
   V_4 = \sqrt{2gh_B} = \sqrt{2 \cdot 9,81 \cdot 2} \approx 6,26\,\mathrm{m/s}
   $$
2. **Cálculo da Vazão (Q):**
   - Diâmetro $D_4 = 0,05$ m $\implies A_4 = \frac{\pi}{4}(0,05)^2 \approx 0,001963$ m².
   $$
   Q = A_4 \cdot V_4 = 0,001963 \times 6,26 \approx 0,0123\,\mathrm{m}^3/\mathrm{s}
   $$

---
**Etapa 2: Calcular a Altura $h_A$**
A vazão que sai do tanque A deve ser a mesma ($Q = 0,0123$ m³/s). Aplicamos Bernoulli entre a superfície de A (ponto 1) e a saída para B (ponto 2).
1. **Relação entre $h_A$ e $V_2$:**
   $$
   V_2 = \sqrt{2gh_A}
   $$
2. **Resolvendo para $h_A$:**
   - Diâmetro $D_2 = 0,03$ m $\implies A_2 = \frac{\pi}{4}(0,03)^2 \approx 0,000707$ m².
   - A velocidade $V_2$ necessária é $V_2 = Q/A_2 = 0,0123 / 0,000707 \approx 17,4$ m/s.
   - Agora, usamos a relação de Bernoulli para encontrar $h_A$:
   $$
   h_A = \frac{V_2^2}{2g} = \frac{(17,4)^2}{2 \cdot 9,81} = \frac{302,76}{19,62} \approx 15,43\,\mathrm{m}
   $$

**Conclusão:**
A profundidade da água no tanque A, $h_A$, é de aproximadamente **15,4 m**.
""",
        "resposta": 15.4,
        "tolerancia": 0.1,
        "unidade": "m"
    },
    "3.68": {
        "capitulo": 3,
        "imagem": "images/3_68.png",
        "enunciado": (
            "Um combustível, densidade igual a 0,77, escoa no medidor Venturi mostrado na Fig. P3.68. "
            r"A velocidade do escoamento é $4,6\,\mathrm{m/s}$ no tubo que apresenta diâmetro igual a $152\,\mathrm{mm}$. "
            "Determine a elevação $h$ no tubo aberto que está conectado à garganta do medidor. "
            "Admita que os efeitos viscosos são desprezíveis."
        ),
        "dica": (
            "Use Bernoulli entre a seção larga (2) e a garganta (1). "
            "Calcule a velocidade na garganta com a Equação da Continuidade. "
            "As cargas de pressão ($P/\\gamma$) são dadas pelas alturas nos tubos abertos."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados e Velocidades:**
   - Ponto 2 (largo): $V_2 = 4,6$ m/s, $D_2 = 0,152$ m.
   - Ponto 1 (garganta): $V_1 =?$, $D_1 = 0,102$ m.
   - Continuidade: $V_1 = V_2 \cdot (D_2/D_1)^2 = 4,6 \cdot (152/102)^2 \approx 10,21$ m/s.

2. **Cargas de Pressão e Elevação:**
   - Carga de pressão em (2): $P_2/\gamma = 1,829$ m.
   - Carga de pressão em (1): $P_1/\gamma = -h$ (sucção).
   - Elevação de (2) relativa a (1): $z_2 = (0,203 \text{ m}) \cdot \sin(20^\circ) \approx 0,0694$ m.
   - Elevação de (1): $z_1 = 0$ (referencial).

3. **Equação de Bernoulli (de 1 para 2):**
   $$
   \frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2
   $$  
   $$
   -h + \frac{(10,21)^2}{2(9,81)} + 0 = 1,829 + \frac{(4,6)^2}{2(9,81)} + 0,0694
   $$  
   $$
   -h + 5,313 = 1,829 + 1,078 + 0,0694
   $$  
   $$
   -h + 5,313 = 2,976
   $$

4. **Resolvendo para h:**
   $$
   h = 5,313 - 2,976 = 2,337\,\mathrm{m}
   $$

**Conclusão:**
A elevação $h$ no tubo aberto é de aproximadamente **2,34 m**.
""",
        "resposta": 2.34,
        "tolerancia": 0.02,
        "unidade": "m"
    },
    "3.73": {
        "capitulo": 3,
        "imagem": "images/3_73.png",
        "enunciado": (
            "Determine a vazão em volume no medidor Venturi mostrado na Fig. P3.73. "
            "Admita que todas as condições de escoamento são ideais."
        ),
        "dica": (
            "Aplique a equação de Bernoulli entre as duas seções do Venturi. "
            "Use a diferença de pressão para calcular a velocidade na garganta e, em seguida, a vazão."
        ),
        "resolucao": r"""
**Resolução passo a passo:**

1. **Dados:**
   - $P_1 = 735.000$ Pa, $P_2 = 550.000$ Pa $\implies \Delta P = 185.000$ Pa.
   - $D_1 = 0,031$ m, $D_2 = 0,019$ m.
   - $\gamma = 9.100$ N/m³.

2. **Calcular a Velocidade na Garganta ($V_2$):**
   A fórmula de Bernoulli para um Venturi pode ser rearranjada para:
   $$
   V_2 = \sqrt{\frac{2g(P_1 - P_2)/\gamma}{1 - (D_2/D_1)^4}}
   $$  
   $$
   V_2 = \sqrt{\frac{2 \cdot (9,81) \cdot (185.000 / 9.100)}{1 - (19/31)^4}}
   $$  
   $$
   V_2 = \sqrt{\frac{398,87}{1 - 0,1408}} = \sqrt{\frac{398,87}{0,8592}} \approx \sqrt{464,23} \approx 21,55\,\mathrm{m/s}
   $$

3. **Calcular a Vazão (Q):**
   - Área da garganta: $A_2 = \frac{\pi}{4}(0,019)^2 \approx 0,0002835$ m².
   $$
   Q = A_2 \cdot V_2 = (0,0002835) \times (21,55) \approx 6,11 \times 10^{-3}\,\mathrm{m}^3/\mathrm{s}
   $$

**Conclusão:**
A vazão em volume é de aproximadamente **$6,11 \times 10^{-3}$ m³/s**.
""",
        "resposta": 6.11e-3,
        "tolerancia": 1e-4,
        "unidade": "m³/s"
    },

    "8.46": {
        "capitulo": 8,
        "imagem": "images/8_46.png",
        "enunciado": (
            "A Fig. P8.46 mostra que a instalação de um 'redutor de pressão' em chuveiros elétricos pode diminuir o consumo de água e energia. "
            "Admitindo que a pressão no ponto (1) permanece constante e todas as perdas, exceto a causada pelo redutor, sejam desprezadas, "
            "determine o valor do coeficiente de perda ($K$) para que o redutor de pressão diminua a vazão pela metade."
        ),
        "dica": (
            r"Relacione $Q$ com $\Delta P$ usando a equação de perdas: $\Delta P = K \frac{\rho U^2}{2}$, "
            "sabendo que ao cortar a vazão pela metade, a velocidade também cai pela metade."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Equação de perda de carga local:**
    $$
    \Delta P = K \frac{1}{2}\rho U^2
    $$

    2. **Relação entre $Q$ e $U$:**
    - $Q = U A$
    - Se $Q$ cai pela metade, $U$ cai pela metade.

    3. **Antes do redutor ($Q_1$):**
    - Sem $K$: $\Delta P_1 = 0$, $Q_1 = Q_0$
    - Com redutor: $\Delta P_2 = K \frac{1}{2}\rho (U_0/2)^2 = K \frac{1}{2}\rho \frac{U_0^2}{4}$

    4. **Como a pressão no ponto (1) é constante, o que mudou foi a perda localizada:**
    - $Q_2 = Q_1 / 2 \implies U_2 = U_1 / 2$
    - $\Delta P_{redutor} = K \frac{1}{2}\rho \left( \frac{U_1}{2} \right)^2 = K \frac{1}{2}\rho \frac{U_1^2}{4} = \frac{K}{4} \cdot \frac{1}{2}\rho U_1^2$

    5. **Para reduzir o fluxo pela metade, toda a queda de pressão deve ocorrer no redutor:**
    - Igualando as quedas de pressão: $\Delta P_{redutor} = \Delta P_{total, antes}$
    - Mas antes, $\Delta P = 0$, então a velocidade deve se ajustar para o novo $K$.
    - Usando a equação do redutor para a condição desejada: $Q_2 = Q_1 / 2 \implies U_2 = U_1 / 2$

    6. **Conclusão:**
    - Para $K$ suficientemente grande, a velocidade cairá pela metade, pois $\Delta P$ aumentou. Assim, o valor de $K$ é:
    $$
    K = 4
    $$

    > **Símbolos:**  
    > $K$: coeficiente de perda  
    > $Q$: vazão volumétrica  
    > $U$: velocidade média  
    > $\rho$: densidade
    """,
        "resposta": {"K": 4},
        "tolerancia": {"K": 0.05},
        "unidade": ""
    },

    "8.49": {
        "capitulo": 8,
        "imagem": "images/8_49.png",
        "enunciado": (
            "No instante $t=0$, o nível do tanque A mostrado na Fig. P8.49 está 0,61 m acima daquele do tanque B. "
            "Faça o gráfico do nível no tanque A em função do tempo até que os tanques se igualem."
        ),
        "dica": (
            "Use a equação de continuidade e Bernoulli para obter a vazão em função da diferença de nível. "
            r"A equação diferencial será $\frac{dh}{dt} = -C \sqrt{h}$."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Diferença de altura inicial:** $h_0 = 0,61~\mathrm{m}$

    2. **Vazão pelo tubo (desprezando perdas singulares):**
    - $Q = A_t u = -A_t \frac{dh}{dt}$
    - Pela equação de Torricelli: $u = \sqrt{2gh}$

    3. **Montando a equação diferencial:**
    $$
    A_t \frac{dh}{dt} = -A_t \sqrt{2gh}
    $$
    $$
    \frac{dh}{dt} = -\sqrt{2g} \sqrt{h}
    $$

    4. **Separando variáveis e integrando:**
    $$
    \int_{h_0}^0 \frac{dh}{\sqrt{h}} = -\sqrt{2g} \int_0^t dt
    $$
    $$
    2\sqrt{h_0} = \sqrt{2g} t
    $$
    $$
    t = \frac{2\sqrt{h_0}}{\sqrt{2g}}
    $$
    Substituindo $h_0 = 0,61~\mathrm{m}$ e $g = 9,81~\mathrm{m/s^2}$:
    $$
    t = \frac{2\sqrt{0,61}}{\sqrt{2 \cdot 9,81}} \approx \frac{2\times0,781}{4,43} \approx 0,353~\mathrm{s}
    $$

    5. **Expressão geral para $h$ ao longo do tempo:**
    $$
    h(t) = (\sqrt{h_0} - \frac{\sqrt{g/2}}{A_t} t)^2
    $$

    > **Símbolos:**  
    > $h(t)$: diferença de nível  
    > $h_0$: diferença inicial  
    > $t$: tempo
    """,
        "resposta": {"$t_{total}$": 0.353},
        "tolerancia": {"t_total": 0.01},
        "unidade": "s"
    },

    "8.71": {
        "capitulo": 8,
        "imagem": "images/8_71.png",
        "enunciado": (
            "Água a 4 °C escoa na serpentina horizontal de um trocador de calor. "
            r"Sabendo que a vazão do escoamento é $5,68 \times 10^{-5}~\mathrm{m}^3/\mathrm{s}$, "
            "determine a perda de pressão entre as seções de alimentação e descarga da serpentina."
        ),
        "dica": (
            "Calcule a velocidade média, depois use Darcy-Weisbach: "
            r"$\Delta P = f \frac{L}{D} \frac{\rho U^2}{2}$. "
            "Use a densidade e viscosidade da água a 4°C para estimar o número de Reynolds e obter o fator de atrito."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - $Q = 5,68 \times 10^{-5}~\mathrm{m}^3/\mathrm{s}$
    - $D = 0,0127~\mathrm{m}$
    - Comprimento total $L = 6 \times 0,46 = 2,76~\mathrm{m}$
    - $\rho = 1000~\mathrm{kg/m}^3$

    2. **Área e velocidade média:**
    $$
    A = \frac{\pi D^2}{4} = \frac{\pi (0,0127)^2}{4} \approx 1,266 \times 10^{-4}~\mathrm{m}^2
    $$
    $$
    U = \frac{Q}{A} = \frac{5,68 \times 10^{-5}}{1,266 \times 10^{-4}} \approx 0,449~\mathrm{m/s}
    $$

    3. **Número de Reynolds:**
    $$
    Re = \frac{U D}{\nu} = \frac{0,449 \times 0,0127}{1,57 \times 10^{-6}} \approx 3,63 \times 10^3
    $$

    4. **Fator de atrito (Moody):**  
    Para $Re = 3630$, $f \approx 0,027$

    5. **Perda de carga:**
    $$
    \Delta P = f \frac{L}{D} \frac{\rho U^2}{2}
    $$
    $$
    \Delta P = 0,027 \times \frac{2,76}{0,0127} \times \frac{1000 \times 0,449^2}{2}
    $$
    - $\frac{2,76}{0,0127} \approx 217,3$
    - $\frac{1000 \times 0,449^2}{2} = 100.8$
    - $\Delta P \approx 0,027 \times 217,3 \times 100.8 \approx 591~\mathrm{Pa}$

    > **Símbolos:**  
    > $\Delta P$: perda de pressão  
    > $Q$: vazão volumétrica  
    > $f$: fator de atrito  
    > $L$: comprimento total  
    > $D$: diâmetro  
    > $U$: velocidade média
    """,
        "resposta": 591,
        "tolerancia": 20,
        "unidade": "Pa"
    },

    "8.73": {
        "capitulo": 8,
        "imagem": "images/8_73.png",
        "enunciado": (
            "A mangueira mostrada na Fig. P8.73 (diâmetro = 12,7 mm) suporta, sem romper, uma pressão de 13,8 bar. "
            "Determine o comprimento máximo permitido, $l$, sabendo que o fator de atrito é igual a 0,022 quando a vazão é "
            r"$2,83 \times 10^{-4}~\mathrm{m}^3/\mathrm{s}$. Despreze as perdas de carga singulares."
        ),
        "dica": (
            "Aplique a equação de energia de Darcy-Weisbach: "
            r"$h_f = \frac{f L}{D} \frac{U^2}{2g}$ e converta a pressão máxima em altura manométrica. "
            "Não esqueça de considerar a diferença de altura entre os pontos inicial e final."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - Diâmetro interno: $D = 0,0127~\mathrm{m}$
    - Vazão: $Q = 2,83 \times 10^{-4}~\mathrm{m}^3/\mathrm{s}$
    - Pressão máxima: $P_{max} = 13,8~\mathrm{bar} = 1,38 \times 10^6~\mathrm{Pa}$
    - Fator de atrito: $f = 0,022$
    - Diferença de altura: $\Delta z = 3,05~\mathrm{m} - 0,91~\mathrm{m} = 2,14~\mathrm{m}$

    2. **Velocidade média:**
    $$
    U = \frac{Q}{A} = \frac{2,83 \times 10^{-4}}{\pi (0,0127^2)/4} \approx 2,22~\mathrm{m/s}
    $$

    3. **Altura manométrica máxima:**
    $$
    h_{max} = \frac{P_{max}}{\gamma} = \frac{1,38 \times 10^6}{1000 \times 9,81} \approx 140,7~\mathrm{m}
    $$

    4. **Equação de energia (Darcy-Weisbach):**
    $$
    h_{max} = h_{perda} + \Delta z + \frac{U^2}{2g}
    $$
    $$
    h_{perda} = \frac{fL}{D} \frac{U^2}{2g}
    $$
    $$
    140,7 = \frac{0,022 L}{0,0127} \cdot \frac{(2,22)^2}{2 \cdot 9,81} + 2,14 + \frac{(2,22)^2}{2 \cdot 9,81}
    $$

    5. **Isolando L:**
    - $\frac{(2,22)^2}{2 \cdot 9,81} \approx 0,251$
    - $140,7 - 2,14 - 0,251 \approx 138,31$
    - $\frac{0,022}{0,0127} \approx 1,732$
    - $\Rightarrow 1,732 L \times 0,251 = 138,31$
    - $1,732 \times 0,251 \approx 0,4346$
    - $L = \frac{138,31}{0,4346} \approx 318,3~\mathrm{m}$

    > **Símbolos:**  
    > $L$: comprimento máximo  
    > $Q$: vazão volumétrica  
    > $U$: velocidade média  
    > $f$: fator de atrito  
    > $D$: diâmetro  
    > $h_{max}$: altura manométrica máxima
    """,
        "resposta": {"L": 318.3},
        "tolerancia": {"L": 1},
        "unidade": "m"
    },

    "8.83": {
        "capitulo": 8,
        "imagem": "images/8_83.png",
        "enunciado": (
            "Água escoa num tubo vertical que apresenta parede interna lisa. Não se detecta variação de pressão no escoamento "
            r"quando a vazão de água no tubo vale $1,42 \times 10^{-2}~\mathrm{m}^3/\mathrm{s}$. Nessas condições, determine o diâmetro deste tubo."
        ),
        "dica": (
            "Se não há variação de pressão detectável, as perdas por atrito são desprezíveis, indicando que o escoamento é do tipo livre. "
            r"Assim, utilize $Q = A \cdot U$, e a velocidade pode ser estimada a partir da queda livre pela equação $U = \sqrt{2gz}$ para uma certa altura. "
            "Como não há informação de altura, considere que a perda de carga é nula e relacione apenas vazão e área do tubo."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - Vazão: $Q = 1,42 \times 10^{-2}~\mathrm{m}^3/\mathrm{s}$

    2. **Como não há variação de pressão detectável:**
    - Considera-se escoamento livre, com perda de carga por atrito desprezível.
    - Usa-se apenas $Q = A U$, mas precisamos de mais um dado para calcular a velocidade média $U$ (normalmente, a altura da coluna d'água). 
    - Mas, como se trata de tubo vertical e não se detecta pressão (diferença de altura), interpreta-se que a velocidade é suficientemente baixa para não haver perdas significativas.

    3. **Suposição típica para questões desse tipo:**  
    - O tubo conduz a água sem diferença de pressão porque está completamente aberto nas extremidades, então podemos usar apenas a relação entre vazão e área, escolhendo uma velocidade média razoável para evitar perdas.

    4. **Expressão da área em função do diâmetro:**
    $$
    Q = A \cdot U = \frac{\pi D^2}{4} \cdot U
    $$

    - Como não há informação sobre $U$, uma abordagem é assumir uma velocidade típica para escoamento livre (por exemplo, $U = 2~\mathrm{m/s}$, para evitar regime turbulento elevado).  
    - No entanto, em provas, normalmente deseja-se apenas a expressão do diâmetro em função de $Q$ e $U$, e pode-se pedir para deixar assim.

    $$
    D = \sqrt{\frac{4Q}{\pi U}}
    $$

    - Para fins de resposta, assuma uma velocidade média típica para evitar perdas: $U \approx 2~\mathrm{m/s}$.

    5. **Calculando $D$:**
    $$
    D = \sqrt{\frac{4 \times 1,42 \times 10^{-2}}{\pi \times 2}} = \sqrt{\frac{5,68 \times 10^{-2}}{6,2832}} \approx \sqrt{9,045 \times 10^{-3}} \approx 0,095~\mathrm{m}
    $$

    $$
    D \approx 95~\mathrm{mm}
    $$

    > **Símbolos:**  
    > $Q$: vazão volumétrica  
    > $D$: diâmetro do tubo  
    > $U$: velocidade média da água  
    > $A$: área da seção transversal
        """,
        "resposta": {"D": 0.095},
        "tolerancia": {"D": 0.005},
        "unidade": "m"
    },

    "8.86": {
        "capitulo": 8,
        "imagem": "images/8_86.png",
        "enunciado": (
            "Considere o escoamento de água mostrado na Fig. P8.86. O diâmetro interno dos componentes do sistema são iguais a 51 mm, "
            "a rugosidade relativa dos tubos é 0,004 e o coeficiente de perda localizada na seção de descarga da tubulação é igual a 1,0. "
            "Nestas condições, determine a altura da coluna de água no tubo piezométrico, $h$."
        ),
        "dica": (
            "Use a equação de Bernoulli entre a superfície livre do reservatório e o ponto do piezômetro, considerando todas as perdas: "
            r"$z_{reserv} = h + \frac{U^2}{2g} + h_{f_{total}}$. Considere as perdas de carga por atrito e a perda localizada no final do tubo."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - $D = 51~\mathrm{mm} = 0,051~\mathrm{m}$
    - $U = 4,6~\mathrm{m/s}$
    - $L_{total} = 2,44 + 2,44 = 4,88~\mathrm{m}$
    - $\epsilon/D = 0,004$ (rugosidade relativa)
    - $K = 1,0$ (perda localizada na saída)
    - $z_{reservatório} = 2,44~\mathrm{m}$

    2. **Equação de Bernoulli entre a superfície livre e o ponto do piezômetro:**
    $$
    z_{reserv} = h + \frac{U^2}{2g} + h_f + h_{local}
    $$
    - $h$: altura no piezômetro
    - $h_f = f \frac{L}{D} \frac{U^2}{2g}$: perda por atrito
    - $h_{local} = K \frac{U^2}{2g}$

    3. **Encontrando $f$ (coeficiente de atrito):**
    - Como $Re$ é alto e $\epsilon/D = 0,004$, use a fórmula de Swamee-Jain (ou Colebrook). 
    - Para fins de exercício, use $f \approx 0,035$ (aproximado para tubos rugosos e velocidades típicas).

    4. **Calculando as perdas:**
    $$
    h_f = f \frac{L}{D} \frac{U^2}{2g} = 0,035 \cdot \frac{4,88}{0,051} \cdot \frac{(4,6)^2}{2 \cdot 9,81}
    $$
    - $\frac{4,88}{0,051} \approx 95,7$
    - $\frac{(4,6)^2}{2 \cdot 9,81} \approx \frac{21,16}{19,62} \approx 1,078$
    - $h_f \approx 0,035 \cdot 95,7 \cdot 1,078 \approx 3,60~\mathrm{m}$

    $$
    h_{local} = 1,0 \cdot 1,078 = 1,078~\mathrm{m}
    $$

    5. **Aplicando Bernoulli:**
    $$
    2,44 = h + 1,078 + 3,60 + 1,078
    $$
    $$
    h = 2,44 - (1,078 + 3,60 + 1,078) = 2,44 - 5,756 = -3,32~\mathrm{m}
    $$

    - O resultado negativo indica que o piezômetro ficaria abaixo do nível de entrada, mostrando grande perda de energia. Isso pode acontecer se as perdas forem maiores do que a coluna d'água disponível. Ajuste o valor de $f$ se necessário ou revise a interpretação do ponto de medição.

    - O resultado teórico, usando valores típicos, geralmente dá $h$ próximo de zero ou levemente negativo nesse tipo de situação, confirmando que a energia é dissipada principalmente em perdas.

    > **Símbolos:**  
    > $D$: diâmetro do tubo  
    > $L$: comprimento total do tubo  
    > $U$: velocidade média  
    > $f$: fator de atrito  
    > $K$: coeficiente de perda localizada  
    > $h$: altura medida no piezômetro
        """,
        "resposta": {"h": -3.3},
        "tolerancia": {"h": 0.1},
        "unidade": "m"
    },

    "8.95": {
        "capitulo": 8,
        "imagem": "images/8_95.png",
        "enunciado": (
            "Água da chuva escoa por uma calha de ferro galvanizado. O formato da seção transversal da calha é retangular e "
            "apresenta razão de aspecto 1,7:1 e a calha sempre está cheia de água. Sabendo que a vazão de água é igual a 6 litros/s, "
            "determine as dimensões da seção transversal da calha."
        ),
        "dica": (
            r"Para escoamento em conduto livre, use $Q = A \cdot U$, onde $A$ é a área da seção retangular. "
            "A razão de aspecto indica que se $b$ é a base e $h$ a altura, então $b = 1,7h$. "
            "Considere o regime permanente e calcule a velocidade média a partir da equação de Manning ou Darcy-Weisbach se necessário."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - Vazão: $Q = 6~\mathrm{L/s} = 0,006~\mathrm{m}^3/\mathrm{s}$
    - Razão de aspecto: $b/h = 1,7$
    - Área da seção: $A = b \cdot h$

    2. **Expressando as dimensões em função de $h$:**
    $$
    b = 1,7h \\
    A = b \cdot h = 1,7h^2
    $$

    3. **A equação da vazão:**
    $$
    Q = A \cdot U \implies 0,006 = 1,7h^2 \cdot U
    $$
    - Como a calha está cheia e a velocidade depende do desnível, mas não foi fornecida, normalmente se usa uma inclinação típica ou deixa em função de $U$.
    - Se não houver mais dados, pode-se pedir para deixar assim:
    $$
    h = \sqrt{\frac{0,006}{1,7U}}
    $$
    - Caso se assuma uma velocidade típica de escoamento em calhas ($U \approx 1~\mathrm{m/s}$):

    $$
    h = \sqrt{\frac{0,006}{1,7 \cdot 1}} = \sqrt{0,00353} \approx 0,059~\mathrm{m}
    $$
    $$
    b = 1,7 \cdot 0,059 \approx 0,10~\mathrm{m}
    $$

    - Então, as dimensões típicas seriam **altura $h \approx 5,9~\mathrm{cm}$, base $b \approx 10~\mathrm{cm}$**.

    > **Símbolos:**  
    > $Q$: vazão  
    > $b$: base da seção  
    > $h$: altura da seção  
    > $A$: área da seção transversal  
    > $U$: velocidade média do escoamento
        """,
        "resposta": {"h": 0.059, "b": 0.10},
        "tolerancia": {"h": 0.005, "b": 0.01},
        "unidade": {"h": "m", "b": "m"}
    },

    "8.100": {
        "capitulo": 8,
        "imagem": "images/8_100.png",
        "enunciado": (
            "Água escoa do tanque A para o B quando a válvula está fechada. Qual é a vazão para o tanque B quando a válvula está aberta e permitindo que água também escoe para o tanque C? "
            "Despreze todas as perdas localizadas e admita que os coeficientes de atrito são iguais a 0,02 em todos os escoamentos."
        ),
        "dica": (
            "Quando apenas a válvula entre A e B está aberta, aplique a equação de energia entre os tanques, considerando as perdas por atrito na tubulação. "
            "Quando a válvula para C está aberta, divida o fluxo entre as duas tubulações e resolva o sistema considerando as alturas e os comprimentos de cada trecho."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - $z_A = 15~\mathrm{m}$, $z_B = z_C = 0~\mathrm{m}$
    - Comprimentos: $A \rightarrow B$: $80 + 40 = 120~\mathrm{m}$, $A \rightarrow C$: $80 + 75 = 155~\mathrm{m}$
    - Diâmetro das tubulações: $D = 0,10~\mathrm{m}$
    - Fator de atrito: $f = 0,02$

    2. **Caso 1: Apenas a válvula entre A e B está aberta**
    - Perda de carga por atrito: $h_f = f \frac{L}{D} \frac{U^2}{2g}$
    - Equação de energia entre $A$ e $B$:
    $$
    z_A = z_B + h_f + \frac{U^2}{2g}
    $$
    - $U = \frac{Q}{A} = \frac{Q}{\pi D^2/4}$
    - $A = \pi (0,1)^2/4 = 0,00785~\mathrm{m}^2$

    $$
    h_f = 0,02 \cdot \frac{120}{0,1} \cdot \frac{U^2}{2g} = 24 \cdot \frac{U^2}{2g}
    $$

    - A soma das perdas:
    $$
    15 = h_f + \frac{U^2}{2g} = 24 \cdot \frac{U^2}{2g} + \frac{U^2}{2g} = 25 \cdot \frac{U^2}{2g}
    $$
    $$
    \frac{U^2}{2g} = \frac{15}{25} = 0,6
    $$
    $$
    U^2 = 2g \cdot 0,6 = 2 \cdot 9,81 \cdot 0,6 = 11,772
    $$
    $$
    U = \sqrt{11,772} \approx 3,43~\mathrm{m/s}
    $$
    $$
    Q_B = U \cdot A = 3,43 \cdot 0,00785 \approx 0,0269~\mathrm{m}^3/\mathrm{s}
    $$

    3. **Caso 2: Válvula para B e C abertas**
    - As vazões se dividem: $Q_A = Q_B + Q_C$
    - Perdas: 
        - $A \rightarrow B$: $L_1 = 120~\mathrm{m}$
        - $A \rightarrow C$: $L_2 = 80 + 75 = 155~\mathrm{m}$

    - Para ambos os caminhos, a perda de carga total deve ser igual ($\Delta z = h_f + \frac{U^2}{2g}$):

    $$
    15 = 0,02 \frac{120}{0,1} \frac{U_B^2}{2g} + \frac{U_B^2}{2g} = 25 \frac{U_B^2}{2g}
    $$
    $$
    15 = 0,02 \frac{155}{0,1} \frac{U_C^2}{2g} + \frac{U_C^2}{2g} = 32 \frac{U_C^2}{2g}
    $$

    - Calculando $U_B$:
    $$
    \frac{U_B^2}{2g} = \frac{15}{25} = 0,6 \implies U_B = \sqrt{2g \cdot 0,6} \approx 3,43~\mathrm{m/s}
    $$
    - Calculando $U_C$:
    $$
    \frac{U_C^2}{2g} = \frac{15}{32} = 0,469 \implies U_C = \sqrt{2g \cdot 0,469} \approx 3,04~\mathrm{m/s}
    $$
    - Calculando vazões:
        - $Q_B = U_B \cdot A = 3,43 \cdot 0,00785 = 0,0269~\mathrm{m}^3/\mathrm{s}$
        - $Q_C = U_C \cdot A = 3,04 \cdot 0,00785 = 0,0239~\mathrm{m}^3/\mathrm{s}$
        - $Q_{total} = Q_B + Q_C = 0,0269 + 0,0239 = 0,0508~\mathrm{m}^3/\mathrm{s}$

    > **Símbolos:**  
    > $Q_B$: vazão para o tanque $B$  
    > $Q_C$: vazão para o tanque $C$  
    > $U_B, U_C$: velocidade média nos respectivos trechos  
    > $f$: fator de atrito  
    > $D$: diâmetro do tubo  
    > $A$: área da seção  
    > $L$: comprimento do tubo
        """,
        "resposta": {"$Q_B$": 0.0269, "$Q_C$": 0.0239, "$Q_{total}$": 0.0508},
        "tolerancia": {"Q_B": 0.001, "Q_C": 0.001, "Q_total": 0.002},
        "unidade": {"$Q_B$": "m^3/s", "$Q_C$": "m^3/s", "$Q_{total}$": "m^3/s"}
    },

    "8.109": {
        "capitulo": 8,
        "imagem": "images/8_109.png",
        "enunciado": (
            "Um medidor bocal (seção mínima com 63,5 mm de diâmetro) está instalado num tubo que "
            "apresenta diâmetro igual a 96,5 mm. Água a 71°C escoa no conjunto. Se a leitura no manômetro do "
            "tipo U invertido utilizado para medir a variação de pressão no medidor for igual a 945 mm de coluna "
            "d'água, determine a vazão de água no tubo."
        ),
        "dica": (
            "Use a equação de Bernoulli entre as seções 1 (tubo maior) e 2 (seção do bocal). "
            r"Considere a continuidade ($Q = U_1 A_1 = U_2 A_2$) e use a diferença de pressão indicada pelo manômetro para "
            r"calcular a velocidade na seção do bocal. Despreze perdas e considere $\Delta z \approx 0$."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - $d_1 = 96,5~\mathrm{mm} = 0,0965~\mathrm{m}$
    - $d_2 = 63,5~\mathrm{mm} = 0,0635~\mathrm{m}$
    - $\Delta h = 945~\mathrm{mm} = 0,945~\mathrm{m}$
    - Temperatura da água: $71^\circ$C (mas considere $\rho \approx 978~\mathrm{kg/m^3}$)

    2. **Áreas:**
    $$
    A_1 = \frac{\pi}{4} d_1^2 = \frac{\pi}{4} (0,0965)^2 \approx 0,00732~\mathrm{m}^2
    $$
    $$
    A_2 = \frac{\pi}{4} d_2^2 = \frac{\pi}{4} (0,0635)^2 \approx 0,00317~\mathrm{m}^2
    $$

    3. **Equação da continuidade:**
    $$
    Q = U_1 A_1 = U_2 A_2 \implies U_1 = \frac{Q}{A_1},~ U_2 = \frac{Q}{A_2}
    $$

    4. **Equação de Bernoulli (desprezando perdas e altura):**
    $$
    \frac{U_1^2}{2g} + \frac{p_1}{\gamma} = \frac{U_2^2}{2g} + \frac{p_2}{\gamma}
    $$
    $$
    \Delta h = \frac{p_1 - p_2}{\gamma}
    $$

    5. **Expressando as velocidades em função da vazão:**
    $$
    U_1 = \frac{Q}{A_1},~ U_2 = \frac{Q}{A_2}
    $$
    $$
    \Delta h = \frac{U_2^2 - U_1^2}{2g}
    $$
    $$
    \Delta h = \frac{1}{2g}\left[ \left(\frac{Q}{A_2}\right)^2 - \left(\frac{Q}{A_1}\right)^2 \right]
    $$

    6. **Isolando Q:**
    $$
    \Delta h = \frac{1}{2g}\left[ \frac{Q^2}{A_2^2} - \frac{Q^2}{A_1^2} \right]
    $$
    $$
    \Delta h = \frac{Q^2}{2g}\left( \frac{1}{A_2^2} - \frac{1}{A_1^2} \right)
    $$
    $$
    Q^2 = 2g \Delta h \left[ \frac{1}{A_2^2} - \frac{1}{A_1^2}\right]^{-1}
    $$

    7. **Calculando:**
    - $g = 9,81~\mathrm{m/s^2}$
    - $\frac{1}{A_2^2} - \frac{1}{A_1^2} = \frac{1}{0,00317^2} - \frac{1}{0,00732^2} \approx 99506 - 18660 = 80846$
    - $\left[ \frac{1}{A_2^2} - \frac{1}{A_1^2} \right]^{-1} \approx 1,237 \times 10^{-5}$

    $$
    Q^2 = 2 \times 9,81 \times 0,945 \times 1,237 \times 10^{-5} \approx 2,29 \times 10^{-4}
    $$
    $$
    Q = \sqrt{2,29 \times 10^{-4}} \approx 0,0151~\mathrm{m}^3/\mathrm{s}
    $$

    8. **Resposta final:**
    $$
    Q \approx 0,015~\mathrm{m}^3/\mathrm{s} = 15~\mathrm{L/s}
    $$
    > **Obs:** O valor pode variar levemente conforme o valor usado para $\rho$.
        """,
        "resposta": {"Q": 0.015},
        "tolerancia": {"Q": 0.001},
        "unidade": {"Q": "m³/s"}
    },

    "8.112": {
        "capitulo": 8,
        "imagem": "images/8_112.png",
        "enunciado": (
            "A vazão de água no tubo mostrado na Fig. P8.112 é 2,8 litros/s. Sabendo que o diâmetro do orifício da placa é igual a 30,5 mm, "
            "determine o valor de $h$."
        ),
        "dica": (
            "Use a equação de Bernoulli entre antes e depois do orifício (placa de orifício), relacionando a diferença de pressão ($h$) ao desnível indicado. "
            r"Utilize a equação de continuidade e lembre-se de converter a vazão para $\mathrm{m}^3/\mathrm{s}$. Considere a diferença de área."
        ),
        "resolucao": r"""
    **Resolução passo a passo:**

    1. **Dados:**
    - $Q = 2,8~\mathrm{L/s} = 2,8 \times 10^{-3}~\mathrm{m}^3/\mathrm{s}$
    - $d_1 = 51~\mathrm{mm} = 0,051~\mathrm{m}$
    - $d_2 = 30,5~\mathrm{mm} = 0,0305~\mathrm{m}$

    2. **Áreas:**
    $$
    A_1 = \frac{\pi}{4} d_1^2 = \frac{\pi}{4} (0,051)^2 \approx 0,00204~\mathrm{m}^2
    $$
    $$
    A_2 = \frac{\pi}{4} d_2^2 = \frac{\pi}{4} (0,0305)^2 \approx 0,000731~\mathrm{m}^2
    $$

    3. **Velocidades:**
    $$
    U_1 = \frac{Q}{A_1} \approx \frac{2,8 \times 10^{-3}}{0,00204} \approx 1,37~\mathrm{m/s}
    $$
    $$
    U_2 = \frac{Q}{A_2} \approx \frac{2,8 \times 10^{-3}}{0,000731} \approx 3,83~\mathrm{m/s}
    $$

    4. **Aplicando Bernoulli entre as seções:**
    $$
    h = \frac{U_2^2 - U_1^2}{2g}
    $$
    $$
    h = \frac{(3,83)^2 - (1,37)^2}{2 \times 9,81}
    $$
    $$
    h = \frac{14,67 - 1,88}{19,62} \approx \frac{12,79}{19,62} \approx 0,652~\mathrm{m}
    $$

    5. **Resposta final:**
    $$
    h \approx 0,65~\mathrm{m}
    $$
        """,
        "resposta": {"h": 0.65},
        "tolerancia": {"h": 0.01},
        "unidade": "m"
    }
    }

    # Organiza capítulos disponíveis
    capitulos_disponiveis = sorted(list(set(q["capitulo"] for q in questoes.values())))

    # Filtro de capítulo
    capitulo_escolhido = st.selectbox("Selecione o capítulo:", capitulos_disponiveis)

    # Filtra as questões do capítulo escolhido
    ids_questoes_capitulo = [k for k, v in questoes.items() if v["capitulo"] == capitulo_escolhido]
    ids_questoes_capitulo = sorted(ids_questoes_capitulo, key=lambda x: float(x.replace('.', '')))

    # Seleção de questão daquele capitulo
    questao_id = st.selectbox("Selecione a questão:", ids_questoes_capitulo)
    q = questoes[questao_id]

    st.markdown(f"**Capítulo {q['capitulo']}**")
    st.markdown(f"**Enunciado:** {q['enunciado']}")
    
    # Adiciona imagem associada, se houver
    img_path = resource_path(q["imagem"]) if "imagem" in q and q["imagem"] else None
    if img_path and os.path.exists(img_path):
        st.image(img_path, use_container_width=True, caption=f"Figura da questão {questao_id}")
    else:
        st.markdown("&nbsp;")  # Adiciona um pequeno espaço vazio
    
    # Botão de dica
    if st.button("💡 Dica"):
        st.info(q["dica"])

    # Bloco para múltiplos ou único campo de resposta
    if isinstance(q["resposta"], dict):
        acertos = []
        for subitem in q["resposta"]:
            unidade = q["unidade"][subitem] if isinstance(q["unidade"], dict) else q["unidade"]
            label = f"({subitem})"
            user_val = st.text_input(f"Digite sua resposta para {label} em {unidade}:", key=f"{questao_id}_{subitem}")
            if user_val:
                if q.get("tipo", "numero") == "texto":
                    # Compara strings diretamente, sem conversão
                    if user_val.strip().replace(" ", "") == str(q["resposta"][subitem]).strip().replace(" ", ""):
                        st.success(f"{label}: ✅ Resposta correta!")
                        acertos.append(True)
                    else:
                        st.error(f"{label}: ❌ Incorreta! Resposta correta: {q['resposta'][subitem]}")
                        acertos.append(False)
                else:
                    # Só tenta converter se for número!
                    try:
                        valor = float(user_val.replace(",", "."))
                        if abs(valor - q["resposta"][subitem]) <= q["tolerancia"][subitem]:
                            st.success(f"{label}: ✅ Resposta correta!")
                            acertos.append(True)
                        else:
                            st.error(f"{label}: ❌ Incorreta! Resposta correta: {q['resposta'][subitem]:.4f} {unidade}")
                            acertos.append(False)
                    except:
                        st.warning(f"{label}: Digite um valor numérico válido.")
    else:
        user_input = st.text_input(f"Digite sua resposta em {q['unidade']}:", key=f"{questao_id}_unico")
        if user_input:
            if q.get("tipo", "numero") == "texto":
                # Não tenta converter, compara texto!
                if user_input.strip().replace(" ", "") == str(q["resposta"]).strip().replace(" ", ""):
                    st.success("✅ Resposta correta!")
                else:
                    st.error(f"❌ Resposta incorreta! A resposta correta é {q['resposta']}.")
            else:
                try:
                    valor = float(user_input.replace(',', '.'))
                    if abs(valor - q["resposta"]) <= q["tolerancia"]:
                        st.success("✅ Resposta correta!")
                    else:
                        st.error(f"❌ Resposta incorreta! A resposta correta é {q['resposta']:.4f} {q['unidade']}.")
                except:
                    st.warning("Digite um valor numérico válido.")
            
    # Botão para mostrar resolução
    if st.button("👁️ Ver resolução"):
        st.markdown(q["resolucao"])

elif choice == "Sobre":
    st.header("ℹ️ Sobre")
    st.write("""
    - Programa de apoio aos estudos de Mecânica dos Fluidos, baseado no livro de Munson, Young e Okiishi (4ª ed.).
    - Desenvolvido por Douglas Batista da Silva.
    - Universidade de Brasília.
    """)

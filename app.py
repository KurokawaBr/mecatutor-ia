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
### O que é um fluido?
Um fluido é uma substância que se deforma continuamente sob ação de uma tensão de cisalhamento, não importando o quão pequena seja essa força. Inclui líquidos e gases.

#### Principais propriedades e fórmulas:
- **Densidade ($\rho$):**
  $$
  \rho = \frac{m}{V}
  $$
  Onde:
  - $\rho$ = densidade do fluido ($kg/m^3$)
  - $m$ = massa ($kg$)
  - $V$ = volume ($m^3$)

- **Peso específico ($\gamma$):**
  $$
  \gamma = \rho g
  $$
  Onde:
  - $\gamma$ = peso específico ($N/m^3$)
  - $\rho$ = densidade ($kg/m^3$)
  - $g$ = aceleração da gravidade ($9,81\, m/s^2$)

- **Viscosidade dinâmica ($\mu$):** 
  Mede a resistência do fluido ao escoamento. 
  - Unidade: $Pa \cdot s$ ou $kg/(m \cdot s)$

- **Viscosidade cinemática ($\nu$):**
  $$
  \nu = \frac{\mu}{\rho}
  $$
  Onde:
  - $\nu$ = viscosidade cinemática ($m^2/s$)
  - $\mu$ = viscosidade dinâmica ($Pa \cdot s$)
  - $\rho$ = densidade ($kg/m^3$)

- **Pressão ($P$):**
  $$
  P = \frac{F}{A}
  $$
  Onde:
  - $P$ = pressão ($Pa$)
  - $F$ = força normal à superfície ($N$)
  - $A$ = área ($m^2$)
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

        st.subheader("Tabela 1.6 - Propriedades Físicas de Alguns Gases")
        # Dados da Tabela 1.6
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
### Pressão em um fluido em repouso
- **Pressão em um ponto:** Igual em todas as direções no fluido parado.

- **Variação da pressão com a profundidade:**
  $$
  \Delta P = \rho g \Delta h
  $$
  Onde:
  - $\Delta P$ = variação de pressão ($Pa$)
  - $\rho$ = densidade ($kg/m^3$)
  - $g$ = gravidade ($m/s^2$)
  - $\Delta h$ = diferença de profundidade ($m$)
  - **Significado:** A pressão aumenta com a profundidade em líquidos.

### Manometria
- **Pressão manométrica:**
  $$
  P_{man} = P_{abs} - P_{atm}
  $$
  Onde:
  - $P_{man}$ = pressão manométrica
  - $P_{abs}$ = pressão absoluta
  - $P_{atm}$ = pressão atmosférica

### Empuxo – Princípio de Arquimedes
- **Empuxo ($E$):**
  $$
  E = \rho_{fluido} \cdot V_{deslocado} \cdot g
  $$
  Onde:
  - $E$ = força de empuxo ($N$)
  - $\rho_{fluido}$ = densidade do fluido ($kg/m^3$)
  - $V_{deslocado}$ = volume do fluido deslocado pelo corpo ($m^3$)
  - $g$ = gravidade ($m/s^2$)

- **Princípio de Arquimedes:** O empuxo sobre o corpo imerso é igual ao peso do fluido deslocado.

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
### Equação de Bernoulli (forma geral)
$$
P + \frac{1}{2}\rho U^2 + \rho g h = \text{constante}
$$
Onde:
- $P$ = pressão estática do fluido ($Pa$)
- $\rho$ = densidade ($kg/m^3$)
- $U$ = velocidade do escoamento ($m/s$)
- $h$ = altura em relação a um referencial ($m$)
- $g$ = aceleração da gravidade ($m/s^2$)

#### Restrições de uso:
- Fluido incompressível
- Escoamento permanente
- Sem perdas (sem atrito)

#### Aplicações:
- Determinação de velocidades e pressões em diferentes pontos de tubulações, bocais, Venturi, etc.

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
### Número de Reynolds ($Re$)
$$
Re = \frac{\rho U D}{\mu}
$$
- $Re < 2300$: laminar
- $Re > 4000$: turbulento

### Perda de carga distribuída (fórmula de Darcy-Weisbach)
$$
h_f = f \frac{L}{D} \frac{U^2}{2g}
$$
- $f$: fator de atrito (diagrama de Moody)

### Perdas localizadas
$$
h_{local} = K \frac{U^2}{2g}
$$

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
        "Densidades: mercúrio = 13.600 kg/m³, água = 1000 kg/m³, álcool = 789 kg/m³.\n"
        "Pressão de vapor a 20°C: mercúrio = 0,17 Pa, água = 2.340 Pa, álcool = 5.850 Pa.\n"
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
   | Mercúrio | 13.600        | 0,17          |
   | Água     | 1.000         | 2.340         |
   | Álcool   | 789           | 5.850         |

3. **(a) Mercúrio**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 0,17}{13\,600 \times 9,81} \approx \frac{100\,999,83}{133\,416} \approx 0,7574\,m = 75,74\,cm
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{13\,600 \times 9,81} \approx 0,7576\,m = 75,76\,cm
     $$
   - **Diferença é desprezível.**

4. **(b) Água**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 2\,340}{1\,000 \times 9,81} = \frac{98\,660}{9\,810} \approx 10,06\,m
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{9\,810} \approx 10,29\,m
     $$
   - **A diferença devido ao vapor é significativa (~23 cm).**

5. **(c) Álcool etílico**

   - **Com pressão de vapor:**
     $$
     h = \frac{101\,000 - 5\,850}{789 \times 9,81} = \frac{95\,150}{7\,736,09} \approx 12,30\,m
     $$
   - **Sem pressão de vapor:**
     $$
     h = \frac{101\,000}{7\,736,09} \approx 13,06\,m
     $$
   - **A diferença é significativa (~76 cm).**

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
            "a": 0.7574,   # altura mercúrio (m), com pressão de vapor
            "b": 10.06,    # altura água (m), com pressão de vapor
            "c": 12.30     # altura álcool (m), com pressão de vapor
        },
        "tolerancia": {
            "a": 0.002,
            "b": 0.03,
            "c": 0.05
        },
        "unidade": "m",
    }
    }

    # Interface para seleção de questões
    questao_selecionada = st.selectbox(
        "Escolha uma questão:",
        list(questoes.keys()),
        format_func=lambda x: f"Questão {x} - Capítulo {questoes[x]['capitulo']}"
    )

    if questao_selecionada:
        questao = questoes[questao_selecionada]
        
        st.subheader(f"📋 Questão {questao_selecionada}")
        
        # Enunciado
        st.markdown("**Enunciado:**")
        st.markdown(questao["enunciado"])
        
        # Dica (expansível)
        with st.expander("💡 Ver dica"):
            st.markdown(questao["dica"])
        
        # Resolução (expansível)
        with st.expander("📝 Ver resolução completa"):
            st.markdown(questao["resolucao"])

elif choice == "Sobre":
    st.header("ℹ️ Sobre o MecaTutorIA")
    st.markdown("""
    ### 🎯 Objetivo
    O **MecaTutorIA** é uma ferramenta educacional desenvolvida para auxiliar estudantes de Engenharia no aprendizado de **Mecânica dos Fluidos**, baseada no livro **Munson (4ª Edição)**.

    ### 📚 Conteúdo
    - **Resumos dos Capítulos**: Conceitos fundamentais, fórmulas e exemplos práticos
    - **Exercícios Resolvidos**: Soluções passo a passo com explicações detalhadas
    - **Tabelas de Propriedades**: Dados de fluidos para consulta rápida

    ### 🔧 Tecnologias
    - **Streamlit**: Interface web interativa
    - **Python**: Processamento e cálculos
    - **LaTeX**: Renderização de fórmulas matemáticas

    ### 👨‍💻 Desenvolvido por
    [Seu Nome] - Estudante de Engenharia

    ### 📖 Referência
    **Munson, B. R.; Young, D. F.; Okiishi, T. H.** *Fundamentos da Mecânica dos Fluidos*. 4ª ed. São Paulo: Edgard Blücher, 2004.

    ---
    *Versão 1.0 - 2024*
    """)

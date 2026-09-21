---
titulo: "Redes"
categoria: "Redes"
nivel: "Intermediário"
status: "Estudando"
atualizado_em: "2026-09-20T21:59:00.000Z"
---

# Redes


> Página viva de estudo sobre Redes de Computadores. Organizada por tópicos e subtópicos, atualizada e expandida sempre que novos materiais forem estudados.

# Fundamentos de Redes

## Tipos e Escala de Redes

### Resumo simples

Redes de computadores podem ter praticamente qualquer tamanho: desde duas máquinas ligadas na mesma sala até bilhões de dispositivos espalhados pelo mundo. As redes menores, usadas em casas ou pequenos escritórios (redes SOHO), servem principalmente para compartilhar coisas do dia a dia, como impressora, arquivos, fotos e músicas entre poucos computadores. Já as redes de empresas grandes vão além: são usadas para vender produtos, pedir suprimentos e se comunicar com clientes, porque a comunicação em rede costuma ser mais rápida e mais barata do que meios tradicionais como correio ou ligações de longa distância — ela permite e-mail, mensagens instantâneas e acesso a informações guardadas em servidores. A internet, por sua vez, é a "rede das redes": literalmente milhares de redes locais conectadas entre si.

### Conceitos principais

- Rede SOHO: rede pequena, doméstica ou de escritório pequeno, focada em compartilhamento simples de recursos

- Rede empresarial: rede maior, usada para operações de negócio (vendas, suprimentos, atendimento ao cliente)

- Internet: conjunto de milhares de redes locais interligadas ("rede de redes")

- Vantagem da comunicação em rede: mais rápida e barata que meios tradicionais (correio, telefone de longa distância)

### Perguntas-guia

- O que caracteriza uma rede SOHO e o que ela normalmente compartilha?

- Por que a comunicação em rede tende a ser mais barata que os meios tradicionais?

- Por que a internet é descrita como uma "rede de redes"?

## Meios e Sinais de Transmissão de Dados

### Resumo simples

Para os dados viajarem de um dispositivo a outro, eles primeiro viram uma sequência de bits e depois precisam ser transformados em algum tipo de sinal físico capaz de percorrer a mídia de rede (o "caminho" físico por onde a informação passa). Existem três formas principais de fazer isso: sinais elétricos, que usam pulsos de eletricidade em fios de cobre; sinais ópticos, que convertem a informação em pulsos de luz, normalmente em cabos de fibra óptica, ideais para longas distâncias com boa confiabilidade; e sinais sem fio, que usam ondas de rádio, micro-ondas ou infravermelho viajando pelo ar. Um mesmo sinal pode até mudar de tipo várias vezes no trajeto entre a origem e o destino, dependendo da mídia usada em cada trecho do caminho.

### Conceitos principais

- Bit → sinal: os dados são convertidos em bits e depois em sinais físicos para serem transmitidos

- Mídia de rede: o meio físico por onde o sinal trafega (cobre, fibra, ar)

- Sinal elétrico: pulsos de eletricidade em fio de cobre

- Sinal óptico: pulsos de luz, tipicamente em fibra óptica, usado em longas distâncias

- Sinal sem fio: ondas de rádio, micro-ondas ou infravermelho pelo ar

- Um sinal pode ser convertido mais de uma vez até chegar ao destino

### Perguntas-guia

- Quais são os três métodos comuns de transmissão de sinal e o que cada um usa como meio físico?

- Por que a fibra óptica costuma ser preferida em redes de longa distância?

- O que acontece com um sinal quando a mídia de transmissão muda no meio do caminho?

## Largura de Banda e Taxa de Transferência

### Resumo simples

Aplicações como assistir filme ou jogar online com várias pessoas exigem conexões rápidas e estáveis, porque a rede precisa enviar e receber bits numa taxa muito alta. Cada meio físico aguenta uma velocidade diferente de transferência de dados, e essa capacidade tem nome: largura de banda — a quantidade de dados que um meio consegue transportar de um lugar a outro num determinado tempo, normalmente medida em quantos bits (teoricamente) podem passar por segundo (Kbps, Mbps ou Gbps). Já a taxa de transferência é o que acontece de fato, na prática — e quase nunca bate com a largura de banda teórica. Isso muda de acordo com a quantidade de dados trafegando, o tipo de dado, e a latência (o tempo, incluindo atrasos, que os dados levam para ir de um ponto a outro). A taxa de transferência conta todo o tráfego que passa pela rede, incluindo mensagens de controle que nem chegam a um aplicativo do usuário. E numa rede com vários trechos, a velocidade final nunca é maior que a do trecho mais lento: um único gargalo no caminho já derruba o desempenho da rede inteira, mesmo que o resto seja rápido.

### Conceitos principais

- Largura de banda: capacidade teórica de um meio, medida em bits por segundo (Kbps, Mbps, Gbps)

- Taxa de transferência: medida real de bits transferidos num período — quase sempre menor que a largura de banda

- Fatores que afetam a taxa de transferência: volume de dados, tipo de dado, latência

- Latência: tempo que os dados levam para ir de origem a destino, incluindo atrasos no caminho

- A taxa de transferência inclui tráfego que não é "útil" pro usuário (ex: mensagens de controle da rede)

- Efeito gargalo: numa rede com vários trechos, a velocidade final é limitada pelo trecho mais lento

### Perguntas-guia

- Qual a diferença entre largura de banda e taxa de transferência?

- Quais são as três unidades comuns de largura de banda, da menor para a maior?

- Quais três fatores influenciam a taxa de transferência real de uma conexão?

- O que é latência?

- Por que um único segmento lento numa rede pode derrubar o desempenho da rede inteira, mesmo que os outros segmentos sejam rápidos?

# Papéis dos Dispositivos e Modelos de Comunicação

## Hosts: Clientes e Servidores

### Resumo simples

Todo computador que participa de uma rede — enviando ou recebendo mensagens — é chamado de host. Um host pode ter papéis diferentes dentro da comunicação: ser cliente, servidor, ou até os dois ao mesmo tempo. O que define esse papel não é o hardware da máquina, e sim o software instalado nela.

### Conceitos principais

- Host: qualquer computador conectado à rede que participa diretamente da comunicação (envia e recebe mensagens)

- Cliente: um dos papéis que um host pode desempenhar na rede

- Servidor: o outro papel que um host pode desempenhar

- Um mesmo host pode atuar como cliente e servidor ao mesmo tempo

- O papel do host (cliente, servidor ou ambos) é definido pelo software instalado, não pelo hardware

### Perguntas-guia

- O que define se um computador é considerado um "host" numa rede?

- Quais papéis um host pode assumir?

- O que determina qual papel um host vai desempenhar em um dado momento?

- Um computador com software para fornecer e-mail ou páginas web a outros dispositivos é considerado o quê?

- Um smartphone usando um navegador pra pedir e exibir uma página web está atuando como o quê?

## Redes Ponto-a-Ponto (P2P)

### Resumo simples

Softwares de cliente e de servidor geralmente rodam em computadores separados, mas um mesmo computador também pode fazer as duas funções ao mesmo tempo. É bem comum, em casas e pequenas empresas, que vários computadores atuem como cliente e servidor dentro da mesma rede — isso é chamado de rede ponto-a-ponto (P2P). A forma mais simples de P2P é só dois computadores ligados diretamente (com ou sem fio), trocando dados e serviços entre si. Pra crescer além disso e conectar vários PCs, já é preciso um dispositivo de rede, como um switch. O problema é que, quando um host faz o papel de cliente e servidor ao mesmo tempo, seu desempenho pode cair. Por isso, empresas grandes — que lidam com bem mais tráfego — costumam preferir servidores dedicados em vez de um modelo P2P.

### Conceitos principais

- Rede P2P: computadores atuando como cliente e servidor ao mesmo tempo, comum em casas e pequenas empresas

- P2P mais simples: dois computadores conectados diretamente (com ou sem fio)

- P2P maior: precisa de um dispositivo de rede (ex: switch) pra interligar vários computadores

- Vantagens: fácil de configurar, menos complexo, menor custo (menos necessidade de dispositivos dedicados), bom pra tarefas simples (compartilhar arquivo ou impressora)

- Desvantagens: sem administração centralizada, menos segura, não escalável, desempenho pode cair quando o host atua como cliente e servidor ao mesmo tempo

- Empresas grandes preferem servidores dedicados por causa do volume alto de tráfego

### Perguntas-guia

- O que caracteriza a rede ponto-a-ponto mais simples possível?

- O que é necessário pra montar uma rede P2P maior, com vários PCs?

- Qual a principal desvantagem de um host atuar como cliente e servidor ao mesmo tempo?

- Por que empresas grandes preferem servidores dedicados em vez de um modelo P2P?

- Como se chama uma rede em que dois computadores se comunicam simultaneamente como cliente e como servidor?

## Aplicações Ponto-a-Ponto

### Resumo simples

Uma aplicação P2P permite que o mesmo dispositivo seja cliente e servidor dentro da mesma comunicação — ou seja, todo cliente é também um servidor, e vice-versa. Pra isso funcionar, cada dispositivo precisa oferecer uma interface pro usuário e, ao mesmo tempo, rodar um serviço em segundo plano. Algumas aplicações P2P usam um esquema híbrido: o compartilhamento dos recursos em si é descentralizado, mas existe um índice centralizado que guarda onde cada recurso está — cada participante (peer) consulta esse índice pra descobrir a localização do que precisa. Um exemplo simples desse modelo é uma conversa por mensagem instantânea, em que as duas máquinas enviam e recebem mensagens ao mesmo tempo, cada uma agindo como cliente e servidor.

### Conceitos principais

- Aplicação P2P: o mesmo dispositivo atua como cliente e servidor dentro da mesma comunicação

- Cada dispositivo precisa fornecer uma interface de usuário e rodar um serviço em segundo plano

- Sistema híbrido: compartilhamento de recursos descentralizado, mas localização dos recursos fica num índice centralizado

- Exemplo: numa mensagem instantânea, ambos os lados enviam e recebem ao mesmo tempo, agindo como cliente e servidor simultaneamente

### Perguntas-guia

- O que significa dizer que "todo cliente é um servidor e todo servidor é um cliente" numa aplicação P2P?

- O que cada dispositivo precisa fazer/ter pra participar de uma aplicação P2P?

- Num sistema híbrido de P2P, o que é centralizado e o que não é?

## Múltiplas Funções na Rede

### Resumo simples

Um computador com software de servidor pode atender vários clientes ao mesmo tempo. Além disso, uma única máquina pode rodar mais de um tipo de servidor simultaneamente — por exemplo, ser servidor de arquivos, servidor web e servidor de e-mail ao mesmo tempo. O mesmo vale pro lado do cliente: um computador pode ter vários softwares de cliente instalados (um pra cada serviço) e, com isso, se conectar a vários servidores diferentes ao mesmo tempo — como checar e-mail, navegar na web, mandar mensagem instantânea e ouvir rádio pela internet, tudo em paralelo.

### Conceitos principais

- Um servidor pode atender vários clientes ao mesmo tempo

- Um único computador pode rodar vários tipos de servidor (arquivo, web, e-mail) simultaneamente

- Um único computador também pode rodar vários softwares de cliente (um por serviço), conectando-se a vários servidores ao mesmo tempo

### Perguntas-guia

- Um mesmo computador pode ser servidor de arquivos, servidor web e servidor de e-mail ao mesmo tempo?

- O que é necessário pra um computador se conectar a vários serviços diferentes ao mesmo tempo?

# Infraestrutura de Redes

## Componentes da Infraestrutura de Rede

### Resumo simples

O caminho que uma mensagem percorre da origem até o destino pode ser tão simples quanto um único cabo ligando dois computadores, ou tão complexo quanto uma rede que atravessa o mundo inteiro. Toda essa estrutura por trás da comunicação é a infraestrutura de rede — a plataforma que dá suporte à rede e garante um canal estável e confiável pra comunicação acontecer. Ela é formada por três categorias de componentes: dispositivos finais, dispositivos intermediários e meios físicos de rede. Dispositivos e meios físicos são o "hardware" da rede — geralmente visíveis, como um laptop, um switch, um roteador, um ponto de acesso sem fio ou os próprios cabos. Já a mídia sem fio é uma exceção: as mensagens viajam pelo ar usando ondas de rádio ou infravermelho, invisíveis a olho nu.

### Conceitos principais

- Infraestrutura de rede: a plataforma/canal estável que sustenta toda a comunicação em rede

- Dispositivos finais: exemplos incluem computador desktop, laptop, impressora, telefone IP, tablet sem fio, dispositivo de telepresença

- Dispositivos intermediários: exemplos incluem roteador sem fio, switch LAN, roteador, switch multicamada, dispositivo de firewall

- Meios de rede: mídia sem fio, mídia LAN, mídia WAN

- Mídia sem fio é o único componente "invisível" — transmite via radiofrequência ou infravermelho pelo ar

### Perguntas-guia

- Quais são as três categorias de componentes que formam a infraestrutura de rede?

- Por que a mídia sem fio é considerada um componente menos "visível" da rede?

- Qual dispositivo intermediário permite compartilhar uma única conexão a cabo entre vários dispositivos em casa, inclusive sem fio?

## Dispositivos Finais

### Resumo simples

Dispositivos finais são os equipamentos de rede com que as pessoas mais têm contato no dia a dia — eles formam a interface entre o usuário e a rede de comunicação. Alguns exemplos: computadores (estações de trabalho, laptops, servidores de arquivo ou web), impressoras de rede, telefones e equipamentos de teleconferência, câmeras de segurança, e dispositivos móveis (smartphones, tablets, PDAs, leitores de cartão sem fio, scanners de código de barras). Um dispositivo final — também chamado de host — é sempre a origem ou o destino de uma mensagem que trafega pela rede. Pra identificar cada host de forma única, usam-se endereços: quando um host inicia uma comunicação, ele usa o endereço do host de destino pra indicar pra onde a mensagem deve ir.

> 📝 **Observação — LAN x LAN:** uma mensagem pode se originar em um dispositivo final de uma LAN e ter como destino um dispositivo final de uma LAN diferente. Para isso, ela atravessa uma rede interconectada (internetwork) que liga as duas LANs — passando por switches e roteadores de borda — e pode inclusive seguir rotas alternativas até chegar ao destino final.

### Conceitos principais

- Dispositivo final (host): origem ou destino de uma mensagem na rede; forma a interface entre usuário e rede

- Exemplos: computadores, impressoras de rede, telefones/equipamento de teleconferência, câmeras de segurança, dispositivos móveis

- Endereços identificam cada host de forma exclusiva na rede

- Uma mensagem pode viajar de um host numa LAN até um host em outra LAN, atravessando uma internetwork e possivelmente seguindo rotas alternativas

### Perguntas-guia

- O que faz de um dispositivo um "dispositivo final" (host)?

- Pra que servem os endereços na comunicação entre hosts?

- Que tipo de dispositivo final costuma ser mais viável em locais sem cabeamento fixo, como uma área rural isolada?

- Que tipo de dispositivo final e de mídia tende a ser usado por alguém que trabalha em campo mas precisa de acesso à internet e videoconferência?

- Como uma mensagem consegue ir de um dispositivo final numa LAN até um dispositivo final em outra LAN?

## Porta LAN

### Resumo simples

Uma porta LAN é apenas um ponto de conexão físico, uma "entrada" em um roteador ou em outro aparelho. Ela geralmente é do tipo RJ45, que é o encaixe onde se pluga o cabo de rede (parecido com o plugue de telefone, só que um pouco maior). Ela serve para ligar um aparelho específico, como um computador ou um videogame, à rede local (LAN). Em um roteador comum de operadora, as portas LAN ficam na parte de trás e costumam ser poucas, de 1 a 4. Pense nelas como tomadas na parede: cada uma recebe um plugue, mas a tomada sozinha não cria mais tomadas.

### Conceitos principais

- Porta LAN: entrada física onde se pluga o cabo de rede

- Conector RJ45: tipo de encaixe mais comum da porta LAN

- Função: conectar um aparelho específico (computador, videogame) à rede local

- Onde fica: em roteadores e outros aparelhos; num roteador comum de operadora costuma haver de 1 a 4 portas, na parte de trás

- Limite: a quantidade de portas é fixa; quando elas acabam, não dá para ligar mais aparelhos por cabo sem ajuda de outro equipamento (o switch)

### Perguntas-guia

- O que é uma porta LAN e para que ela serve?

- Qual é o tipo de conector mais comum de uma porta LAN?

- Quantas portas LAN um roteador comum de operadora costuma ter e onde elas ficam?

- O que acontece quando as portas LAN do roteador acabam?

## Switch

### Resumo simples

Um switch é um aparelho de hardware independente, criado para multiplicar as portas de conexão e organizar a rede local. Ele tem várias portas LAN, geralmente 5, 8, 16 ou mais. Quando as portas do roteador acabam, você liga um cabo do roteador ao switch, e o switch passa a oferecer muitas novas portas para conectar outros aparelhos. Além de expandir a rede, o switch é inteligente: ele gerencia o tráfego de dados entre os aparelhos ligados a ele. Em vez de gritar a mensagem para todo mundo, ele entrega os dados só para o aparelho certo, como um carteiro que sabe o endereço de cada casa.

> 📝 **Observação — Porta LAN x Switch:** a porta LAN é só a entrada, a peça onde o cabo é plugado. O switch é o aparelho completo que reúne várias dessas portas e ainda organiza o tráfego entre elas. Uma analogia: a porta LAN é uma tomada, e o switch é uma régua de tomadas, só que inteligente.

### Conceitos principais

- Switch: aparelho de hardware independente com várias portas LAN (5, 8, 16 ou mais)

- Função: expandir o número de conexões da rede local

- Como expandir: liga-se um cabo do roteador ao switch, e o switch oferece novas portas para vários outros aparelhos

- Inteligência: gerencia o tráfego de dados entre os aparelhos conectados a ele

- Diferença para a porta LAN: a porta é só um ponto de conexão; o switch é o aparelho que multiplica e organiza essas portas

### Perguntas-guia

- O que é um switch e para que ele serve?

- Quantas portas um switch costuma ter?

- O que fazer quando as portas do roteador acabam e ainda é preciso ligar mais aparelhos?

- O que significa dizer que o switch gerencia o tráfego "de forma inteligente"?

- Qual é a diferença entre uma porta LAN e um switch?

# Conectividade com a Internet

## Provedor de Serviços de Internet (ISP)

### Resumo simples

O ISP (Internet Service Provider, ou provedor de serviços de Internet) é a empresa que faz a "ponte" entre a rede da sua casa e a internet. Imagine que a internet é uma grande rodovia: o ISP é a estradinha que liga a sua rua a essa rodovia. Um ISP pode ser a empresa de TV a cabo da sua região, a empresa de telefonia fixa, a operadora de celular que dá sinal ao seu smartphone, ou um provedor independente que aluga espaço (largura de banda) na infraestrutura física de outra empresa. Muitos ISPs também vendem serviços extras, como contas de e-mail, armazenamento na rede, hospedagem de sites, segurança e backup automático. Os ISPs são essenciais para a internet global: cada um se conecta a outros ISPs, formando uma teia de ligações que interliga pessoas do mundo inteiro. Eles se organizam de forma hierárquica (em níveis, como uma árvore), o que garante que o tráfego da internet geralmente siga o caminho mais curto da origem até o destino.

### Conceitos principais

- ISP: empresa que fornece o link (a ligação) entre a rede doméstica e a Internet

- Tipos de ISP: provedor de TV a cabo, provedor de telefonia fixa, rede celular, provedor independente (que aluga largura de banda da infraestrutura de outra empresa)

- Serviços adicionais: e-mail, armazenamento de rede, hospedagem de sites, segurança e backup automático

- Cada ISP se conecta a outros ISPs, formando uma rede de links que liga usuários no mundo todo

- Organização hierárquica: garante que o tráfego siga, em geral, o caminho mais curto entre origem e destino

### Perguntas-guia

- O que é um ISP e qual o papel dele entre a rede doméstica e a Internet?

- Quais tipos de empresa podem atuar como ISP?

- Que serviços adicionais um ISP costuma oferecer além do acesso à internet?

- Por que os ISPs precisam se conectar uns aos outros?

- Qual a vantagem de os ISPs serem organizados de forma hierárquica?

## Backbone da Internet

### Resumo simples

O backbone (que significa "espinha dorsal") da Internet é como uma superautoestrada de informações: um conjunto de ligações de dados de altíssima velocidade que conecta as redes dos vários provedores nas grandes áreas metropolitanas do mundo todo. O principal meio físico que sustenta esse backbone é o cabo de fibra óptica (aquele que transporta a informação como pulsos de luz). Esse cabo normalmente é enterrado no subterrâneo para ligar cidades dentro de um mesmo continente, e também passa por baixo do mar para conectar continentes, países e cidades.

### Conceitos principais

- Backbone da Internet: "autoestrada" de dados de alta velocidade que conecta as redes dos provedores em grandes áreas metropolitanas do mundo

- Principal meio físico do backbone: cabo de fibra óptica

- Em terra: cabo instalado no subterrâneo, conectando cidades dentro dos continentes

- No mar: cabo submarino, conectando continentes, países e cidades

### Perguntas-guia

- Por que o backbone é comparado a uma autoestrada de informações?

- Qual é o principal meio físico usado no backbone da Internet?

- Como os cabos de fibra óptica conectam cidades dentro de um continente? E entre continentes?

## Conexões de Cabo e DSL

### Resumo simples

A maioria das pessoas que têm rede em casa não se liga ao provedor por fibra óptica. Para casas e pequenos escritórios, os dois método

> 📝 **Observação — Quem usa essas conexões:** os usuários típicos são o usuário doméstico, o funcionário remoto (teletrabalhador) e os pequenos escritórios. Todos se ligam ao ISP por uma das opções (DSL, cabo, celular, satélite ou discada), e o ISP faz a ligação com a Internet.

### Conceitos principais

- Cabo: sinal de internet no mesmo cabo coaxial da TV a cabo; conexão sempre ativa e com alta largura de banda

- Cable modem: separa o sinal de internet dos outros sinais do cabo e fornece uma conexão Ethernet para um computador ou LAN

- DSL (Linha Digital do Assinante): internet pela linha telefônica; sempre ativa e com alta largura de banda

- Modem DSL de alta velocidade: separa o sinal DSL do sinal de telefone e fornece uma conexão Ethernet

- Os três canais da DSL: voz (chamadas), download (mais rápido) e upload (um pouco mais lento)

- Fatores que afetam a DSL: qualidade da linha telefônica e distância até a central da operadora (quanto mais longe, mais lenta)

### Perguntas-guia

- Quais são os dois métodos de conexão mais comuns para casas e pequenos escritórios?

- Por que um cable modem é necessário? O que ele separa?

- Em quais três canais a linha DSL é dividida e para que serve cada um?

- Por que dá para receber uma ligação telefônica sem se desconectar da internet na DSL?

- Como a distância até a central telefônica afeta a velocidade da DSL?

## Outras Opções de Conectividade

### Resumo simples

Além do cabo e da DSL, existem outras formas de um usuário doméstico se conectar a um ISP: a rede celular, o satélite, a conexão discada (dial-up) e, em áreas metropolitanas, a fibra óptica ligada diretamente ao apartamento ou pequeno escritório. Com a fibra até o local, o provedor consegue oferecer velocidades de largura de banda mais altas e mais serviços ao mesmo tempo, como internet, telefone e TV. No caso do satélite, o computador se liga a um modem de satélite, que se comunica com o satélite usando uma antena parabólica (aquela "antena de prato"); o satélite, por sua vez, conversa com um roteador do provedor de satélite, também por meio de uma antena no local dele. Qual conexão escolher varia de acordo com a localização geográfica e com a disponibilidade de cada provedor na sua região.

### Conceitos principais

- Opções adicionais de conexão: celular, satélite, conexão discada (dial-up) e fibra óptica direta

- Fibra direta (áreas metropolitanas): maior largura de banda e suporte a mais serviços (internet, telefone e TV)

- Satélite: computador → modem satélite → antena parabólica → satélite → antena do ISP → roteador do ISP (provedor de serviço de satélite)

- A escolha da conexão depende da localização geográfica e da disponibilidade do provedor

### Perguntas-guia

- Quais são as opções de conexão com um ISP além de cabo e DSL?

- O que a fibra óptica direta permite que um provedor ofereça em áreas metropolitanas?

- Qual é o caminho que os dados percorrem numa conexão via satélite, do computador até o ISP?

- De que depende a escolha do tipo de conexão?

# Tecnologias de Rede na Residência

## Frequências de LAN Sem Fio

### Resumo simples

As tecnologias sem fio mais usadas nas redes de casa trabalham em duas faixas de frequência não licenciadas: 2,4 GHz e 5 GHz. Frequência é quantas vezes por segundo a onda de rádio "vibra" (1 GHz são 1 bilhão de vibrações por segundo), e "não licenciada" quer dizer que a faixa é livre: qualquer pessoa pode usar sem pedir permissão, como uma praça pública em vez de um terreno com dono. Essas faixas fazem parte do espectro eletromagnético, que é como uma escada gigante que organiza todas as ondas invisíveis, das frequências mais baixas (como o áudio) até as mais altas (como os raios X). Só algumas áreas dessa escada podem ser usadas sem permissão, e é nelas que moram o Bluetooth e as LANs sem fio modernas.

> 📝 **Observação — Onde ficam as tecnologias no espectro:** das frequências mais baixas para as mais altas: áudio, transmissão AM, ondas curtas de rádio, transmissão FM, televisão, celular (840 MHz), NPCs (930 MHz), telefones sem fio (902 a 928 MHz), LANs sem fio em 2,4 GHz (2,400 a 2,4835 GHz) e em 5 GHz (5,725 a 5,850 GHz), LAN sem fio infravermelha, luz visível, ultravioleta e raios X. As classificações do espectro vão de extremamente baixa, muito baixa, baixa, média, alta, muito alta, ultra alta e super alta até chegar ao infravermelho.

### Conceitos principais

- Faixas mais usadas em redes residenciais: 2,4 GHz e 5 GHz (não licenciadas, ou seja, de uso livre)

- Espectro eletromagnético: organização de todas as ondas por frequência, do áudio aos raios X

- Só algumas áreas do espectro podem ser usadas sem permissão

- Bluetooth e as LANs sem fio modernas (padrões IEEE 802.11) usam essas faixas

### Perguntas-guia

- Quais são as duas faixas de frequência não licenciadas mais usadas em redes residenciais?

- O que significa uma faixa ser "não licenciada"?

- O que é o espectro eletromagnético?

- Onde as tecnologias de LAN sem fio ficam no espectro, em relação ao celular e ao infravermelho?

## Bluetooth

### Resumo simples

O Bluetooth é uma tecnologia sem fio que usa a banda de 2,4 GHz. Ele é limitado a comunicações de curto alcance e baixa velocidade, mas tem uma grande vantagem: consegue se comunicar com vários dispositivos ao mesmo tempo (comunicação um para muitos), como um celular que fala com o fone, o relógio e a caixinha de som ao mesmo tempo. Por isso virou o método preferido para conectar periféricos de computador (os acessórios que ligamos ao PC), como mouses, teclados e impressoras sem fio. Ele também é muito útil para transmitir áudio para alto-falantes e fones de ouvido.

### Conceitos principais

- Bluetooth: tecnologia sem fio que usa a banda de 2,4 GHz

- Limitações: curto alcance e baixa velocidade

- Vantagem: comunicação um para muitos (vários dispositivos ao mesmo tempo)

- Usos: periféricos de computador (mouse, teclado, impressora sem fio) e transmissão de áudio (alto-falantes e fones de ouvido)

### Perguntas-guia

- Em qual banda de frequência o Bluetooth funciona?

- Quais são as limitações do Bluetooth?

- O que significa comunicação "um para muitos" e por que isso é uma vantagem?

- Para quais tipos de dispositivo o Bluetooth é o método preferido?

## LAN Sem Fio (Wi-Fi e Padrões IEEE 802.11)

### Resumo simples

As LANs sem fio modernas, conhecidas como Wi-Fi, seguem vários padrões IEEE 802.11. O IEEE é uma organização que cria os "manuais de regras" técnicos, e o 802.11 é o manual que define como o Wi-Fi funciona. Elas também usam as bandas de 2,4 GHz e 5 GHz, mas a grande diferença para o Bluetooth é que transmitem com um nível de potência muito maior. Isso dá a elas maior alcance e melhor rendimento (mais velocidade na prática). É a diferença entre sussurrar no ouvido de alguém (Bluetooth) e falar em voz alta numa sala grande (Wi-Fi).

> 📝 **Observação — Padrões por faixa (segundo a figura do material):** na faixa de 2,4 GHz aparecem os padrões 802.11 b, g e n; na faixa de 5 GHz aparecem os padrões 802.11 a, n e ac.

### Conceitos principais

- LAN sem fio moderna (Wi-Fi): segue vários padrões IEEE 802.11

- Bandas usadas: 2,4 GHz e 5 GHz (as mesmas do Bluetooth)

- Diferença para o Bluetooth: potência de transmissão muito maior

- Resultado: maior alcance e melhor rendimento

- 2,4 GHz: padrões 802.11 b, g e n; 5 GHz: padrões 802.11 a, n e ac

### Perguntas-guia

- O que é o IEEE 802.11 e o que ele define?

- Qual a principal diferença entre o Wi-Fi e o Bluetooth?

- Por que o Wi-Fi tem maior alcance e melhor rendimento que o Bluetooth?

- Quais padrões 802.11 aparecem nas faixas de 2,4 GHz e de 5 GHz?

## Tecnologias de Redes com Fio

### Resumo simples

Mesmo com tanta coisa sem fio, ainda existem aplicações em que os dispositivos usam uma conexão com fio ligada a um switch, e essa conexão não é compartilhada com outros usuários da rede. Pense numa linha exclusiva só sua, enquanto o Wi-Fi é como uma conversa numa sala cheia, em que todos dividem o mesmo ar. O protocolo com fio mais usado é o Ethernet: um conjunto de regras (protocolos) que permite aos dispositivos conversarem por uma LAN com fio, e que pode usar vários tipos de mídia de fiação. Dispositivos ligados diretamente usam um cabo de ligação Ethernet, normalmente de par trançado não blindado (UTP), que são fios de cobre trançados dois a dois, sem capa metálica extra de proteção. Esses cabos podem ser comprados já com os conectores RJ-45 nas pontas e vêm em vários comprimentos. Casas construídas recentemente podem já ter tomadas Ethernet na parede. Já as residências sem cabeamento UTP podem usar outras tecnologias, como a própria rede elétrica, para levar conectividade com fio aos cômodos.

### Conceitos principais

- Conexão por switch com fio: não é compartilhada com outros usuários da rede

- Ethernet: protocolo com fio mais usado; conjunto de protocolos que permite a comunicação numa LAN com fio, com vários tipos de mídia de fiação

- Cabo de ligação Ethernet: normalmente par trançado não blindado (UTP), com conectores RJ-45, vendido em vários comprimentos

- Casas novas: podem já ter tomadas Ethernet cabeadas nas paredes

- Sem cabeamento UTP: dá para usar outras tecnologias, como a rede elétrica, para distribuir conectividade com fio

### Perguntas-guia

- Por que algumas aplicações ainda usam conexão com fio, mesmo com o sem fio tão presente?

- O que é o Ethernet?

- Que tipo de cabo é normalmente usado para ligar dispositivos diretamente e que conector ele traz?

- O que fazer numa casa que não tem cabeamento UTP nas paredes?

## Tipos de Cabo em Redes com Fio

### Resumo simples

O material lista três tipos de cabo: categoria 5e, coaxial e fibra óptica. O cabo de fibra óptica pode ser feito de vidro ou de plástico, com espessura aproximadamente igual a de um fio de cabelo humano. Apesar de finíssimo, ele carrega informações digitais em velocidades muito altas e por longas distâncias. Ele tem uma largura de banda muito alta, o que significa que consegue transportar grandes quantidades de dados, como uma estrada larguíssima por onde passam muitos carros ao mesmo tempo.

### Conceitos principais

- Tipos de cabo listados: categoria 5e, coaxial e fibra óptica

- Fibra óptica: feita de vidro ou plástico, com diâmetro parecido com o de um cabelo humano

- Transporta informações digitais em velocidades muito altas por longas distâncias

- Largura de banda muito alta: permite transportar grandes quantidades de dados

### Perguntas-guia

- Quais são os três tipos de cabo listados no material?

- De que material a fibra óptica pode ser feita e qual é a espessura dela?

- Por que a fibra óptica é adequada para transportar grandes quantidades de dados por longas distâncias?

# Redes Wi-Fi

## Padrões Wi-Fi e Organizações Responsáveis

### Resumo simples

Para que aparelhos sem fio de marcas diferentes consigam conversar, foram criados vários padrões, que são conjuntos de regras. É como o padrão das tomadas: todas seguem o mesmo formato, então qualquer aparelho encaixa em qualquer parede. Os padrões sem fio especificam o espectro de RF usado (a faixa de ondas de rádio), as taxas de dados (a velocidade) e o modo como as informações são transmitidas. O principal organismo responsável por criar esses padrões técnicos é o IEEE (Instituto dos Engenheiros Eletricistas e Eletrônicos), o "comitê" que escreve as regras. O padrão IEEE 802.11 controla o ambiente WLAN (rede local sem fio), e suas alterações (como b, g, n e ac) descrevem as características de cada padrão de comunicação, como versões de um aplicativo. Esses padrões usam as bandas de 2,4 GHz e 5 GHz e, coletivamente, são conhecidos como Wi-Fi. Outro organismo, a Wi-Fi Alliance, é responsável por testar dispositivos de LAN sem fio de fabricantes diferentes. O logotipo Wi-Fi em um aparelho funciona como um selo de qualidade: significa que ele atende aos padrões e deve operar com outros dispositivos do mesmo padrão. Os padrões melhoram continuamente a conectividade e a velocidade, e os fabricantes os implementam rápido em produtos novos, por isso é importante saber quando surgem.

### Conceitos principais

- Padrão: conjunto de regras que garante a comunicação entre dispositivos sem fio de fabricantes diferentes

- O que um padrão especifica: o espectro de RF usado, as taxas de dados e o modo como as informações são transmitidas

- IEEE: principal organismo responsável por criar padrões técnicos sem fio

- IEEE 802.11: padrão que controla o ambiente WLAN; suas alterações descrevem as características dos diferentes padrões de comunicação sem fio

- WLAN: rede local sem fio

- Wi-Fi: nome coletivo dessas tecnologias, que usam as bandas de 2,4 GHz e 5 GHz

- Wi-Fi Alliance: testa dispositivos de LAN sem fio de fabricantes diferentes

- Logotipo Wi-Fi: indica que o equipamento atende aos padrões e deve operar com outros dispositivos do mesmo padrão

- Novos padrões surgem continuamente e os fabricantes os implementam rápido em produtos novos

### Perguntas-guia

- O que um padrão sem fio especifica?

- Qual organismo cria os padrões técnicos sem fio e qual padrão controla o ambiente WLAN?

- O que significa o logotipo Wi-Fi em um dispositivo?

- Qual é o papel da Wi-Fi Alliance?

- Por que é importante acompanhar a chegada de novos padrões?

- Quais padrões o roteador da minha casa suporta?

## Modo de Rede

### Resumo simples

O modo de rede define quais padrões 802.11 o roteador (ou ponto de acesso, o access point) aceita. Se todos os dispositivos sem fio se conectam com o mesmo padrão, é possível obter as velocidades máximas desse padrão. Mas, se o ponto de acesso estiver configurado para aceitar apenas um padrão 802.11, os dispositivos que não usam esse padrão não conseguem se conectar. Já num ambiente de modo misto, podem entrar dispositivos de qualquer padrão Wi-Fi atual, o que dá acesso fácil a aparelhos antigos que precisam de conexão sem fio, mas não são compatíveis com os padrões mais recentes. Pense numa sala de aula: um professor que só fala um idioma só é entendido por quem fala esse idioma, enquanto um professor que entende vários idiomas atende todo mundo.

### Conceitos principais

- Modo de rede: define quais padrões 802.11 o ponto de acesso aceita

- Todos os dispositivos no mesmo padrão: obtêm as velocidades máximas desse padrão

- Ponto de acesso configurado para um único padrão: dispositivos que não usam esse padrão não conseguem se conectar

- Modo misto: aceita dispositivos de qualquer padrão Wi-Fi atual, incluindo aparelhos antigos incompatíveis com os padrões mais recentes

### Perguntas-guia

- O que define o modo de rede de um roteador?

- O que acontece com um aparelho antigo se o roteador aceita apenas um padrão mais novo?

- Quando todos os dispositivos usam o mesmo padrão, o que se consegue obter?

- Qual a vantagem do modo misto para aparelhos antigos?

## Nome da Rede (SSID)

### Resumo simples

Ao criar uma rede sem fio, é importante que os componentes sem fio se conectem à WLAN apropriada, e isso é feito por meio do SSID (Identificador do Conjunto de Serviços). O SSID é basicamente o nome da rede Wi-Fi, aquele que aparece na lista do celular. Ele é uma string alfanumérica (um texto com letras e números) de até 32 caracteres e diferencia maiúsculas de minúsculas, então "Casa" é diferente de "casa". O SSID é enviado no cabeçalho de todos os quadros transmitidos pela WLAN (os quadros são os "pacotinhos" de dados, e o cabeçalho é como o remetente escrito no envelope). Ele serve para informar aos dispositivos sem fio, chamados de estações sem fio (STA), a qual WLAN eles pertencem e com quais outros dispositivos podem se comunicar.

### Conceitos principais

- SSID (Identificador do Conjunto de Serviços): o nome da rede sem fio, usado para identificar uma rede específica

- Formato: string alfanumérica, com até 32 caracteres, que diferencia maiúsculas de minúsculas

- Vai no cabeçalho de todos os quadros transmitidos pela WLAN

- Estação sem fio (STA): dispositivo sem fio que usa o SSID para saber a qual WLAN pertence e com quem pode se comunicar

### Perguntas-guia

- O que é o SSID e para que ele serve?

- Qual o tamanho máximo de um SSID e ele diferencia maiúsculas de minúsculas?

- Onde o SSID é enviado dentro dos quadros da rede?

- O que é uma estação sem fio (STA)?

## Broadcast de SSID e Segurança

### Resumo simples

O broadcast de SSID é o roteador anunciando o nome da rede para todos os dispositivos ao alcance, o que permite que aparelhos e clientes sem fio detectem a rede automaticamente. Por padrão, ele vem ativado. Se for desativado, a rede some da lista e é preciso digitar o SSID manualmente em cada aparelho. Desativar o broadcast pode dificultar a detecção da rede por clientes legítimos, mas não é suficiente para impedir que clientes não autorizados se conectem. É como tirar a placa da porta de uma loja: a porta continua destrancada. A "tranca" de verdade é a criptografia, que embaralha os dados para que só quem tem a senha consiga entendê-los. Por isso, todas as redes sem fio devem usar a criptografia mais forte disponível (por exemplo, o WPA3, quando o aparelho suporta) para restringir o acesso não autorizado.

> 📝 **Observação — SSID x Broadcast:** o SSID vai escrito no cabeçalho de todos os quadros da rede, com o broadcast ligado ou desligado. O broadcast só anuncia o nome da rede para os aparelhos ao redor. Desligá-lo não impede que os dados cheguem ao destino e também não protege a rede: quem protege é a criptografia.

### Conceitos principais

- Broadcast de SSID: transmissão do nome da rede para todos os dispositivos ao alcance; por padrão, vem ativado

- Ativado: aparelhos e clientes detectam a rede automaticamente

- Desativado: é preciso inserir o SSID manualmente nos dispositivos sem fio

- Desativar o broadcast dificulta a detecção da rede por clientes legítimos, mas não impede que clientes não autorizados se conectem

- Segurança de verdade: usar a criptografia mais forte disponível para restringir o acesso não autorizado

### Perguntas-guia

- O que é o broadcast de SSID e qual é o valor padrão dele?

- O que muda quando o broadcast de SSID é desativado?

- Por que desativar o broadcast não é suficiente para proteger a rede?

- O que deve ser usado para restringir o acesso não autorizado a uma rede sem fio?

- Qual a diferença entre o SSID nos quadros da rede e o broadcast de SSID?

---
titulo: "Redes"
categoria: "Redes"
nivel: "Intermediário"
status: "Estudando"
atualizado_em: "2026-09-19T20:14:00.000Z"
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

"""20 artigos adicionais sobre os principais temas de coluna buscados no Google.
Conteúdo de SEO em PT-BR, com estrutura H2/H3 didática.
"""

SPINE_IMG = "https://static.prod-images.emergentagent.com/jobs/11721837-3a81-4cef-8d93-7d18b3b33d31/images/1eeb3b0ba0fee19c4165662f2164805150ba354df0f6cb8a321f1e5037030fdd.png"
BRAIN_IMG = "https://static.prod-images.emergentagent.com/jobs/11721837-3a81-4cef-8d93-7d18b3b33d31/images/8ad4056b49063aee11fba39283788d82b8c525bb544a84374e8d7ab9c2cf8995.png"
BACK_IMG = "https://static.prod-images.emergentagent.com/jobs/11721837-3a81-4cef-8d93-7d18b3b33d31/images/91a26b912de9e855ca4fc419d0edf6b9421e57f838e4a3366c5678fda124bad9.png"

AUTHOR = "Dr. Matheus Lopes"
DISCLAIMER = '<p><em>Este artigo tem caráter exclusivamente educacional e não substitui a avaliação médica individualizada.</em></p>'


def make(slug, title, excerpt, category, image, reading_time, published_at, content):
    label = {"spine": "Coluna", "brain": "Cérebro", "prevention": "Prevenção"}[category]
    return {
        "slug": slug,
        "title": title,
        "excerpt": excerpt,
        "category": category,
        "category_label": label,
        "image_url": image,
        "reading_time": reading_time,
        "published_at": published_at,
        "author": AUTHOR,
        "content_html": content + DISCLAIMER,
    }


EXTRA_ARTICLES = [
    make(
        "lombalgia-cronica-causas-e-tratamento",
        "Lombalgia Crônica: O Que Causa a Dor Lombar Persistente e Como Tratar",
        "Entenda por que a dor lombar se torna crônica, quais são as principais causas e os tratamentos mais eficazes baseados em evidência.",
        "spine", BACK_IMG, 8, "2026-02-09",
        """
<p>A <strong>lombalgia crônica</strong> — dor na região lombar com duração superior a 12 semanas — é uma das principais causas de afastamento do trabalho no Brasil. Compreender suas origens é o primeiro passo para um tratamento eficaz.</p>

<h2>O que define a lombalgia como crônica?</h2>
<p>Quando a dor lombar persiste por mais de três meses, mesmo após o período natural de cicatrização tecidual, ela passa a ser classificada como crônica. Nessa fase, mecanismos neurológicos de sensibilização central frequentemente entram em ação, perpetuando o quadro doloroso mesmo na ausência de lesão estrutural óbvia.</p>

<h2>Principais causas da lombalgia crônica</h2>
<ul>
<li><strong>Discopatia degenerativa:</strong> desgaste progressivo dos discos intervertebrais.</li>
<li><strong>Artrose facetária:</strong> degeneração das articulações posteriores da coluna.</li>
<li><strong>Hérnia de disco:</strong> protrusão do núcleo discal que comprime raízes nervosas.</li>
<li><strong>Estenose de canal:</strong> estreitamento do canal vertebral, mais comum após os 60 anos.</li>
<li><strong>Espondilolistese:</strong> deslizamento de uma vértebra sobre a outra.</li>
<li><strong>Sensibilização central:</strong> alterações neurológicas que amplificam a percepção de dor.</li>
</ul>

<h2>Fatores de risco modificáveis</h2>
<p>Estudos mostram que sedentarismo, sobrepeso, tabagismo, postura inadequada no trabalho remoto e estresse crônico estão diretamente associados à perpetuação da dor lombar. A boa notícia é que todos podem ser modificados com mudanças de estilo de vida e acompanhamento adequado.</p>

<h2>Sinais de alerta que exigem investigação imediata</h2>
<ul>
<li>Dor irradiada para os membros inferiores com formigamento ou fraqueza;</li>
<li>Perda de controle urinário ou intestinal;</li>
<li>Febre, perda de peso inexplicada ou histórico de câncer;</li>
<li>Dor noturna que não melhora com o repouso.</li>
</ul>

<h2>Tratamento multimodal: o caminho de maior sucesso</h2>
<h3>Abordagens conservadoras</h3>
<p>A primeira linha de tratamento envolve fisioterapia especializada, exercícios de estabilização do core, RPG, Pilates clínico e analgesia adequada. O movimento, ao contrário do repouso prolongado, é fundamental para a recuperação.</p>

<h3>Procedimentos intervencionistas</h3>
<p>Quando o tratamento conservador é insuficiente, procedimentos minimamente invasivos como bloqueios facetários, infiltrações epidurais e radiofrequência podem oferecer alívio significativo, muitas vezes evitando cirurgias mais extensas.</p>

<h3>Cirurgia minimamente invasiva</h3>
<p>Em casos selecionados, a <strong>cirurgia endoscópica de coluna</strong> permite tratar hérnias e estenoses com incisões mínimas, recuperação rápida e excelente resultado funcional.</p>

<h2>Como prevenir a cronificação</h2>
<p>A regra fundamental é não banalizar a dor lombar aguda. Episódios recorrentes mal tratados se transformam em cronicidade. Atividade física regular, fortalecimento de core, ergonomia adequada e busca precoce por um especialista são as melhores armas contra a lombalgia crônica.</p>
"""
    ),
    make(
        "nervo-ciatico-inflamado-sintomas-e-tratamento",
        "Nervo Ciático Inflamado: Sintomas, Causas e Tratamentos que Funcionam",
        "Saiba como identificar a inflamação do nervo ciático, suas causas mais comuns e quais tratamentos têm respaldo científico para alívio rápido.",
        "spine", SPINE_IMG, 7, "2026-02-10",
        """
<p>A inflamação do <strong>nervo ciático</strong> — o maior nervo do corpo humano — é uma das queixas mais frequentes em consultórios de coluna. Compreender o mecanismo da dor é essencial para um tratamento direcionado.</p>

<h2>O que é a ciatalgia?</h2>
<p>O termo "ciatalgia" descreve a dor que percorre o trajeto do nervo ciático: parte da região lombar, desce pela nádega, posterior da coxa e perna, podendo chegar até o pé. Não é uma doença em si, mas um sintoma de algo que está comprimindo ou irritando o nervo.</p>

<h2>Principais causas da inflamação ciática</h2>
<ul>
<li><strong>Hérnia de disco lombar:</strong> causa mais frequente, geralmente nos níveis L4-L5 ou L5-S1.</li>
<li><strong>Estenose foraminal:</strong> estreitamento do canal por onde sai a raiz nervosa.</li>
<li><strong>Síndrome do piriforme:</strong> compressão do nervo por contratura do músculo piriforme.</li>
<li><strong>Espondilolistese:</strong> deslizamento vertebral comprimindo a raiz.</li>
<li><strong>Tumores ou cistos:</strong> causas raras, mas que devem ser excluídas em casos atípicos.</li>
</ul>

<h2>Sintomas típicos do nervo ciático inflamado</h2>
<ul>
<li>Dor em queimação ou "choque" que desce pela perna;</li>
<li>Formigamento ou dormência seguindo trajeto específico;</li>
<li>Fraqueza muscular (dificuldade para levantar a ponta do pé, por exemplo);</li>
<li>Piora ao tossir, espirrar ou fazer esforço;</li>
<li>Dor que aumenta ao sentar por longos períodos.</li>
</ul>

<h2>Diagnóstico: muito além da ressonância</h2>
<p>O diagnóstico é primariamente clínico, baseado em exame físico detalhado com testes neurodinâmicos como o sinal de Lasègue. A ressonância magnética confirma a causa estrutural, e a eletroneuromiografia pode quantificar o grau de comprometimento nervoso.</p>

<h2>Tratamentos com evidência científica</h2>
<h3>Fase aguda</h3>
<p>Anti-inflamatórios, analgésicos e neuromoduladores (gabapentina, pregabalina) ajudam a controlar a dor. Repouso relativo por 2-3 dias é aceitável, mas o retorno gradual ao movimento é fundamental.</p>

<h3>Fisioterapia especializada</h3>
<p>Programas de neurodinâmica, alongamento direcionado, estabilização lombar e fortalecimento progressivo são pilares do tratamento conservador, que resolve mais de 80% dos casos em 6 a 12 semanas.</p>

<h3>Procedimentos minimamente invasivos</h3>
<p>Bloqueios radiculares ou epidurais guiados por imagem oferecem alívio significativo e auxiliam no diagnóstico. Em casos refratários, a <strong>cirurgia endoscópica de coluna</strong> remove o fragmento herniado preservando estruturas vizinhas.</p>

<h2>Quando procurar um neurocirurgião com urgência</h2>
<p>Fraqueza muscular progressiva, perda de controle esfincteriano ou dor de intensidade extrema que não responde a medicação são sinais de alerta que exigem avaliação imediata.</p>
"""
    ),
    make(
        "hernia-de-disco-cervical-sintomas-tratamento",
        "Hérnia de Disco Cervical: Quando a Dor no Pescoço se Torna Grave",
        "Conheça os sintomas característicos da hérnia cervical, riscos da mielopatia e quando a cirurgia minimamente invasiva é indicada.",
        "spine", SPINE_IMG, 9, "2026-02-11",
        """
<p>A <strong>hérnia de disco cervical</strong> afeta a região do pescoço, podendo gerar sintomas que vão muito além da dor local — incluindo irradiação para os membros superiores e, em casos graves, comprometimento medular.</p>

<h2>Anatomia da coluna cervical</h2>
<p>A coluna cervical é composta por 7 vértebras, sustentando a cabeça e permitindo grande amplitude de movimento. Por essa mobilidade, está sujeita a maior desgaste, especialmente nos discos C5-C6 e C6-C7, os mais frequentemente acometidos por hérnias.</p>

<h2>Sintomas clássicos da hérnia cervical</h2>
<ul>
<li><strong>Cervicobraquialgia:</strong> dor que parte do pescoço e irradia para o braço, podendo chegar até os dedos.</li>
<li>Formigamento ou dormência em mãos e dedos, seguindo padrão específico;</li>
<li>Fraqueza no braço, ombro ou mão (dificuldade em segurar objetos);</li>
<li>Perda de reflexos no exame neurológico;</li>
<li>Rigidez cervical persistente com limitação de movimentos;</li>
<li>Dor de cabeça occipital (na nuca).</li>
</ul>

<h2>Mielopatia cervical: o sinal mais preocupante</h2>
<p>Quando a hérnia comprime não apenas uma raiz nervosa, mas a própria medula espinhal, surge a <strong>mielopatia</strong>. Os sinais incluem alterações na marcha, perda de destreza fina nas mãos (dificuldade para abotoar camisas), sensação de "choque" ao movimentar o pescoço (sinal de Lhermitte) e até alterações esfincterianas.</p>
<p>A mielopatia é uma indicação clara de tratamento cirúrgico, pois a evolução natural tende à piora progressiva.</p>

<h2>Diagnóstico preciso</h2>
<p>A ressonância magnética cervical é o exame padrão-ouro. A tomografia complementa a avaliação óssea, e a eletroneuromiografia pode quantificar o sofrimento nervoso. Testes provocativos como o sinal de Spurling são realizados no exame clínico.</p>

<h2>Tratamento conservador</h2>
<h3>Primeira linha</h3>
<p>Mais de 70% das hérnias cervicais melhoram com tratamento clínico: anti-inflamatórios, neuromoduladores, fisioterapia com tração cervical controlada, e reabilitação postural.</p>

<h3>Bloqueios e infiltrações</h3>
<p>Bloqueios radiculares cervicais guiados por radioscopia podem oferecer alívio rápido em casos refratários, mas devem ser realizados por profissionais experientes devido à anatomia delicada.</p>

<h2>Tratamento cirúrgico moderno</h2>
<h3>Discectomia cervical anterior com fusão (ACDF)</h3>
<p>Procedimento clássico, com excelentes resultados. A abordagem anterior permite remover o disco doente e estabilizar o segmento com cage e placa.</p>

<h3>Artroplastia cervical (prótese de disco)</h3>
<p>Alternativa moderna que preserva o movimento do segmento operado, indicada em pacientes selecionados.</p>

<h3>Endoscopia cervical posterior</h3>
<p>Para casos selecionados, técnicas endoscópicas posteriores oferecem recuperação ainda mais rápida com mínima agressão aos tecidos.</p>

<h2>Quando a cirurgia é indicada?</h2>
<ul>
<li>Falha do tratamento conservador após 6-12 semanas;</li>
<li>Déficit neurológico progressivo;</li>
<li>Mielopatia confirmada;</li>
<li>Dor incoercível que compromete qualidade de vida.</li>
</ul>
"""
    ),
    make(
        "bico-de-papagaio-osteofitos-coluna",
        "Bico de Papagaio na Coluna: O Que Realmente Significa e Como Tratar",
        "Entenda o que são os osteófitos (bicos de papagaio), por que aparecem e quando precisam de tratamento específico.",
        "spine", BACK_IMG, 6, "2026-02-12",
        """
<p>O termo popular <strong>"bico de papagaio"</strong> designa a presença de osteófitos — pequenas projeções ósseas que se formam nas margens das vértebras. É um dos achados mais comuns em radiografias de coluna após os 40 anos.</p>

<h2>O que são osteófitos?</h2>
<p>Osteófitos são uma resposta natural do corpo ao desgaste articular. Quando o disco intervertebral perde altura ou as articulações facetárias degeneram, o organismo tenta estabilizar o segmento formando essas projeções ósseas. Não são "espinhos crescendo na coluna", como muitos imaginam, mas sim um sinal de envelhecimento estrutural.</p>

<h2>Bico de papagaio causa dor?</h2>
<p>Nem sempre. Muitos osteófitos são <strong>achados incidentais</strong> em exames de imagem, encontrados em pessoas completamente assintomáticas. A dor surge quando essas formações comprimem estruturas vizinhas — especialmente raízes nervosas ou o canal vertebral.</p>

<h2>Quando o bico de papagaio gera sintomas</h2>
<ul>
<li>Dor lombar ou cervical mecânica, que piora com movimentos;</li>
<li>Rigidez articular, especialmente pela manhã;</li>
<li>Dor irradiada quando há compressão neural;</li>
<li>Limitação de movimentos da coluna;</li>
<li>Em casos avançados, sinais de estenose de canal.</li>
</ul>

<h2>Diagnóstico: contextualizar a imagem</h2>
<p>A radiografia simples mostra bem os osteófitos. A ressonância magnética é mais útil quando há suspeita de compressão neural ou outras alterações associadas. Lembre-se: tratar o paciente, não a imagem.</p>

<h2>Tratamentos eficazes</h2>
<h3>Conservador (primeira escolha)</h3>
<p>Fisioterapia, exercícios de fortalecimento muscular, perda de peso quando indicada, ajustes ergonômicos e analgesia adequada resolvem a maioria dos casos sintomáticos.</p>

<h3>Procedimentos minimamente invasivos</h3>
<p>Quando há dor articular específica (artrose facetária associada), bloqueios facetários e radiofrequência facetária oferecem alívio prolongado e excelente perfil de segurança.</p>

<h3>Cirurgia</h3>
<p>Reservada para casos de estenose de canal significativa com sintomas neurológicos. A cirurgia endoscópica de coluna pode remover osteófitos compressivos com mínima agressão.</p>

<h2>Prevenção: é possível?</h2>
<p>Não há como evitar completamente o aparecimento de osteófitos, pois fazem parte do envelhecimento natural. Porém, manter peso adequado, praticar atividade física regular, evitar sobrecargas excessivas e cuidar da postura retarda significativamente sua formação e impacto clínico.</p>
"""
    ),
    make(
        "escoliose-em-adultos-causas-tratamento",
        "Escoliose em Adultos: Tipos, Sintomas e Tratamentos Modernos",
        "Saiba quando a escoliose precisa de tratamento na idade adulta, opções conservadoras e cirúrgicas com técnicas atuais.",
        "spine", SPINE_IMG, 8, "2026-02-13",
        """
<p>A <strong>escoliose</strong> é o desvio lateral da coluna vertebral, frequentemente associado a uma rotação dos corpos vertebrais. Embora seja mais conhecida na adolescência, sua manifestação ou progressão em adultos exige abordagem específica.</p>

<h2>Tipos de escoliose no adulto</h2>
<ul>
<li><strong>Escoliose idiopática do adulto:</strong> persistência de uma escoliose iniciada na adolescência;</li>
<li><strong>Escoliose degenerativa (de novo):</strong> desenvolve-se após os 50 anos, decorrente do envelhecimento das estruturas vertebrais;</li>
<li><strong>Escoliose secundária:</strong> consequência de outras condições como osteoporose, traumas ou cirurgias prévias.</li>
</ul>

<h2>Sintomas mais comuns</h2>
<ul>
<li>Dor lombar ou torácica crônica;</li>
<li>Assimetria de ombros, escápulas ou pelve;</li>
<li>Dor irradiada quando há compressão de raízes nervosas;</li>
<li>Sensação de cansaço ao ficar muito tempo em pé;</li>
<li>Em casos avançados, alteração da silhueta e da função respiratória.</li>
</ul>

<h2>Quando a escoliose precisa de tratamento ativo?</h2>
<p>Nem toda escoliose requer intervenção. Os principais fatores que justificam tratamento ativo são: curvatura superior a 30°, progressão documentada, dor refratária, déficit neurológico ou comprometimento funcional importante.</p>

<h2>Diagnóstico e mensuração</h2>
<p>A radiografia panorâmica de coluna em ortostase mensura o ângulo de Cobb — padrão-ouro para classificar a magnitude da curva. Ressonância magnética e tomografia são úteis para planejamento cirúrgico e avaliação de compressões neurais.</p>

<h2>Tratamentos conservadores</h2>
<p>Para curvas pequenas e estáveis, fisioterapia específica (método Schroth), Pilates clínico, RPG e exercícios de fortalecimento postural são pilares. Tratamento medicamentoso da dor é coadjuvante. Coletes ortopédicos têm papel limitado em adultos, mas podem ser indicados em situações específicas.</p>

<h2>Tratamento cirúrgico</h2>
<p>Quando indicada, a cirurgia visa corrigir a deformidade, descomprimir estruturas neurais e estabilizar a coluna. Técnicas modernas incluem:</p>
<ul>
<li><strong>Artrodese instrumentada:</strong> fixação com parafusos pediculares e hastes;</li>
<li><strong>Osteotomias seletivas:</strong> para correção de deformidades rígidas;</li>
<li><strong>Cirurgia minimamente invasiva (MIS):</strong> reduz sangramento, dor pós-operatória e tempo de internação;</li>
<li><strong>Cirurgia robótica e navegação:</strong> aumenta a precisão da colocação de parafusos.</li>
</ul>

<h2>Recuperação e prognóstico</h2>
<p>O tratamento da escoliose no adulto exige equipe multidisciplinar e expectativas realistas. A maioria dos pacientes apresenta melhora significativa de dor e função, especialmente quando o tratamento é individualizado.</p>
"""
    ),
    make(
        "estenose-de-canal-lombar-sintomas-cirurgia",
        "Estenose de Canal Lombar: Quando Caminhar Vira um Desafio",
        "Entenda por que a estenose lombar provoca dor ao caminhar, como é diagnosticada e quais tratamentos modernos existem.",
        "spine", SPINE_IMG, 8, "2026-02-14",
        """
<p>A <strong>estenose de canal lombar</strong> é o estreitamento do canal vertebral, comprimindo as raízes nervosas que saem da coluna para os membros inferiores. É uma das principais causas de dor lombar e nas pernas em pacientes acima dos 60 anos.</p>

<h2>O que causa a estenose?</h2>
<p>Trata-se quase sempre de um processo degenerativo progressivo: hipertrofia do ligamento amarelo, osteófitos, abaulamentos discais e artrose facetária reduzem o espaço disponível para os nervos. Algumas pessoas já nascem com um canal vertebral estreito (estenose congênita), o que predispõe à manifestação mais precoce.</p>

<h2>Sintomas característicos</h2>
<h3>Claudicação neurogênica: o sinal típico</h3>
<p>É o sintoma mais clássico. O paciente caminha alguns metros e começa a sentir dor, queimação ou fraqueza nas pernas, que melhora quando ele <strong>senta ou flexiona o tronco para a frente</strong> (sinal do carrinho de supermercado). Esta característica diferencia a estenose lombar da claudicação vascular.</p>

<h3>Outros sintomas</h3>
<ul>
<li>Dor lombar mecânica;</li>
<li>Formigamento e dormência nos membros inferiores;</li>
<li>Sensação de pernas pesadas ao caminhar;</li>
<li>Em casos avançados, fraqueza muscular e alterações de marcha.</li>
</ul>

<h2>Diagnóstico</h2>
<p>A ressonância magnética é o exame de escolha, mostrando claramente o grau de estreitamento. A tomografia é útil para avaliação óssea, e a eletroneuromiografia auxilia em casos com sintomas bilaterais ou diagnóstico diferencial.</p>

<h2>Tratamento conservador</h2>
<p>Funciona bem em quadros leves a moderados:</p>
<ul>
<li>Fisioterapia com foco em flexão lombar e fortalecimento;</li>
<li>Exercícios aquáticos (excelente opção);</li>
<li>Perda de peso quando aplicável;</li>
<li>Anti-inflamatórios, analgésicos e neuromoduladores;</li>
<li>Bloqueios e infiltrações epidurais guiadas por imagem.</li>
</ul>

<h2>Quando a cirurgia é indicada?</h2>
<p>Quando o tratamento conservador não controla os sintomas, ou quando o paciente apresenta limitação importante para caminhar mesmo distâncias curtas. Déficit neurológico progressivo também é indicação clara.</p>

<h2>Técnicas cirúrgicas modernas</h2>
<h3>Cirurgia endoscópica de coluna</h3>
<p>Permite descompressão eficaz com incisão mínima (8mm), excelente preservação muscular e recuperação rápida — ideal para pacientes idosos.</p>

<h3>Descompressão tubular minimamente invasiva</h3>
<p>Utiliza dilatadores progressivos para acessar a região afetada sem cortar musculatura.</p>

<h3>Descompressão e artrodese</h3>
<p>Quando há instabilidade associada (espondilolistese), pode ser necessário estabilizar o segmento com parafusos pediculares.</p>

<h2>Resultados esperados</h2>
<p>A maioria dos pacientes operados experimenta melhora significativa da capacidade de caminhar e redução importante da dor. Quanto mais precoce a intervenção em casos indicados, melhor o resultado funcional.</p>
"""
    ),
    make(
        "espondilolistese-tratamento",
        "Espondilolistese: Quando uma Vértebra Desliza Sobre a Outra",
        "Conheça os tipos de espondilolistese, sintomas, diagnóstico e tratamentos modernos para essa condição da coluna.",
        "spine", SPINE_IMG, 7, "2026-02-15",
        """
<p>A <strong>espondilolistese</strong> é o deslizamento anterior (ou raramente posterior) de uma vértebra sobre a vértebra logo abaixo. É uma das causas mais comuns de dor lombar crônica em adultos e atletas jovens.</p>

<h2>Tipos principais</h2>
<ul>
<li><strong>Ístmica:</strong> decorre de um defeito na pars interarticularis (espondilólise). Comum em jovens atletas de modalidades que exigem hiperextensão lombar (ginástica, vôlei, mergulho);</li>
<li><strong>Degenerativa:</strong> mais comum em mulheres acima dos 50 anos, geralmente em L4-L5. Decorre da degeneração do disco e das facetas;</li>
<li><strong>Congênita:</strong> presente desde o nascimento;</li>
<li><strong>Traumática ou patológica:</strong> menos frequentes.</li>
</ul>

<h2>Classificação de Meyerding</h2>
<p>Mede o percentual de deslizamento: grau I (até 25%), grau II (25-50%), grau III (50-75%), grau IV (75-100%) e grau V ou espondiloptose (>100%). A maioria dos casos é grau I ou II.</p>

<h2>Sintomas</h2>
<ul>
<li>Dor lombar mecânica que piora ao final do dia;</li>
<li>Dor irradiada para as nádegas e coxas;</li>
<li>Sensação de instabilidade lombar;</li>
<li>Em casos avançados, claudicação neurogênica e déficit neurológico;</li>
<li>Rigidez de musculatura posterior da coxa (isquiotibiais encurtados).</li>
</ul>

<h2>Diagnóstico</h2>
<p>A radiografia em pé e em dinâmica (flexão e extensão) é fundamental para avaliar o grau de deslizamento e a estabilidade. A ressonância magnética complementa a avaliação de discos, raízes nervosas e canal vertebral.</p>

<h2>Tratamento conservador</h2>
<p>Eficaz para a maioria dos pacientes com graus I e II e sem sinais neurológicos:</p>
<ul>
<li>Fisioterapia com foco em estabilização lombar e fortalecimento de core;</li>
<li>Evitar atividades de impacto e hiperextensão;</li>
<li>Pilates clínico e RPG;</li>
<li>Controle de peso e ajustes ergonômicos;</li>
<li>Analgesia e anti-inflamatórios em fases agudas.</li>
</ul>

<h2>Quando operar?</h2>
<ul>
<li>Falha do tratamento conservador por 6 meses;</li>
<li>Progressão do deslizamento;</li>
<li>Déficit neurológico;</li>
<li>Dor incapacitante refratária;</li>
<li>Graus elevados (III a V) sintomáticos.</li>
</ul>

<h2>Cirurgia: o que esperar</h2>
<p>O procedimento padrão é a <strong>artrodese instrumentada</strong> do segmento afetado, frequentemente com redução parcial do deslizamento e descompressão das raízes nervosas. Técnicas minimamente invasivas (MIS-TLIF) oferecem excelentes resultados com menor agressão tecidual.</p>

<h2>Prognóstico</h2>
<p>A maioria dos pacientes operados apresenta excelente recuperação, com retorno à vida ativa em alguns meses. O acompanhamento de longo prazo é importante para monitorar a coluna como um todo.</p>
"""
    ),
    make(
        "artrose-facetaria-tratamento",
        "Artrose Facetária: A Dor que Vem das Pequenas Articulações da Coluna",
        "Aprenda a reconhecer a dor facetária, suas causas e como tratá-la com fisioterapia, bloqueios e radiofrequência.",
        "spine", BACK_IMG, 7, "2026-02-16",
        """
<p>A <strong>artrose facetária</strong> — também chamada de síndrome facetária ou espondiloartrose — é o desgaste das pequenas articulações posteriores da coluna vertebral, denominadas articulações facetárias ou zigapofisárias. É uma das principais causas de dor lombar e cervical em adultos.</p>

<h2>O que são as articulações facetárias?</h2>
<p>Cada vértebra possui duas pequenas articulações na sua parte posterior, que se conectam com a vértebra de cima e a de baixo. Essas articulações guiam e limitam o movimento da coluna. Como qualquer articulação, podem desenvolver artrose ao longo do tempo.</p>

<h2>Causas</h2>
<ul>
<li>Envelhecimento natural (após os 40-50 anos);</li>
<li>Sobrecarga repetitiva (esportes de impacto, trabalho braçal);</li>
<li>Sobrepeso e obesidade;</li>
<li>Sequela de fraturas ou cirurgias prévias;</li>
<li>Desalinhamentos da coluna;</li>
<li>Degeneração discal associada.</li>
</ul>

<h2>Sintomas característicos</h2>
<ul>
<li>Dor lombar ou cervical localizada, paramediana;</li>
<li>Piora ao estender o tronco para trás;</li>
<li>Melhora ao flexionar para frente;</li>
<li>Dor "rasa", profunda, em peso;</li>
<li>Pode irradiar para nádegas, virilha ou parte superior das coxas (dor referida, não radicular);</li>
<li>Rigidez matinal ou após períodos prolongados na mesma posição.</li>
</ul>

<h2>Diagnóstico: clínica + bloqueio teste</h2>
<p>O diagnóstico é primariamente clínico. Exames de imagem mostram o desgaste, mas muitos pacientes assintomáticos têm achados similares. O <strong>bloqueio facetário diagnóstico</strong> guiado por radioscopia é considerado o padrão-ouro: se o paciente melhora significativamente após o bloqueio anestésico, confirma-se a origem facetária da dor.</p>

<h2>Tratamentos eficazes</h2>
<h3>Fisioterapia direcionada</h3>
<p>Exercícios de flexibilização, fortalecimento de core e estabilização lombar são fundamentais. Técnicas como osteopatia e quiropraxia podem auxiliar em pacientes selecionados.</p>

<h3>Medicações</h3>
<p>Anti-inflamatórios, analgésicos e relaxantes musculares em ciclos curtos durante crises. Uso crônico deve ser evitado pelos efeitos colaterais.</p>

<h3>Bloqueios facetários terapêuticos</h3>
<p>Infiltrações com anestésico e corticoide podem oferecer alívio prolongado e auxiliar a fisioterapia.</p>

<h3>Radiofrequência facetária</h3>
<p>Tratamento moderno e altamente eficaz: ondas de radiofrequência desativam os ramos sensitivos que inervam a faceta dolorosa, com alívio que pode durar de 6 meses a 2 anos. Procedimento ambulatorial, minimamente invasivo.</p>

<h2>Cirurgia: quando indicar?</h2>
<p>Reservada para casos com instabilidade associada ou estenose significativa. A artrose facetária isolada raramente exige cirurgia.</p>

<h2>Prevenção</h2>
<p>Atividade física regular, controle de peso, postura adequada e fortalecimento muscular são as melhores estratégias para retardar a progressão da artrose facetária.</p>
"""
    ),
    make(
        "sindrome-do-piriforme-falsa-ciatica",
        "Síndrome do Piriforme: A 'Falsa Ciática' que Confunde o Diagnóstico",
        "Aprenda a diferenciar a síndrome do piriforme da hérnia de disco lombar e conheça os tratamentos mais eficazes.",
        "spine", BACK_IMG, 6, "2026-02-17",
        """
<p>A <strong>síndrome do piriforme</strong> ocorre quando o músculo piriforme, localizado profundamente na região glútea, comprime ou irrita o nervo ciático, gerando sintomas muito semelhantes aos da hérnia de disco lombar — daí o nome popular de "falsa ciática".</p>

<h2>Anatomia: por que isso acontece?</h2>
<p>O músculo piriforme conecta o sacro à parte superior do fêmur. O nervo ciático passa próximo (e em algumas pessoas, atravessa) esse músculo. Quando o piriforme está encurtado, contraturado ou hipertrofiado, pode comprimir o nervo, gerando dor irradiada para a perna.</p>

<h2>Fatores de risco</h2>
<ul>
<li>Sedentarismo e ficar muito tempo sentado (especialmente trabalho remoto);</li>
<li>Corredores e ciclistas com fortalecimento desequilibrado;</li>
<li>Traumas locais (queda sobre a nádega);</li>
<li>Diferenças de comprimento dos membros inferiores;</li>
<li>Postura inadequada e fraqueza glútea.</li>
</ul>

<h2>Sintomas característicos</h2>
<ul>
<li>Dor profunda na região glútea, geralmente unilateral;</li>
<li>Irradiação para a parte posterior da coxa, raramente abaixo do joelho;</li>
<li>Piora ao sentar por longos períodos;</li>
<li>Piora ao subir escadas ou rampas;</li>
<li>Pode haver formigamento, mas raramente déficit motor;</li>
<li>Dor à palpação profunda do músculo piriforme.</li>
</ul>

<h2>Diagnóstico diferencial com hérnia de disco</h2>
<p>A grande dificuldade é diferenciar da ciatalgia por hérnia. Testes específicos (manobra de Pace, FAIR test) ajudam a identificar a origem muscular. A ressonância magnética da coluna costuma ser normal ou com achados não compatíveis com a clínica. Em casos selecionados, a ressonância de pelve com protocolo específico pode evidenciar o piriforme hipertrofiado.</p>

<h2>Tratamento conservador</h2>
<p>É a base do tratamento e funciona em mais de 80% dos casos:</p>
<ul>
<li><strong>Alongamento específico do piriforme:</strong> exercícios diários, com supervisão inicial de fisioterapeuta;</li>
<li>Fortalecimento glúteo, especialmente do médio;</li>
<li>Liberação miofascial (rolinho, bola de tênis);</li>
<li>Anti-inflamatórios em fase aguda;</li>
<li>Modificação de hábitos: levantar a cada 30-50 minutos, ajustes ergonômicos;</li>
<li>Punção seca (dry needling) por profissional habilitado.</li>
</ul>

<h2>Procedimentos intervencionistas</h2>
<p>Quando o tratamento conservador é insuficiente:</p>
<ul>
<li>Infiltração do músculo piriforme guiada por ultrassom;</li>
<li>Aplicação de toxina botulínica para relaxar o músculo (alta taxa de sucesso).</li>
</ul>

<h2>Cirurgia: situação excepcional</h2>
<p>Reservada para casos muito raros e refratários, envolvendo liberação cirúrgica do nervo ciático na região glútea.</p>

<h2>Prevenção</h2>
<p>Manter rotina de alongamento, fortalecimento glúteo equilibrado, evitar ficar sentado por períodos prolongados e ajustar postura no trabalho são fundamentais para prevenir recidivas.</p>
"""
    ),
    make(
        "dor-lombar-na-gestacao-cuidados",
        "Dor Lombar na Gestação: Como Aliviar com Segurança",
        "Saiba o que causa a dor lombar na gravidez, quais cuidados tomar e quando procurar avaliação médica especializada.",
        "prevention", BACK_IMG, 6, "2026-02-18",
        """
<p>A <strong>dor lombar na gestação</strong> atinge cerca de 50 a 70% das gestantes em algum momento da gravidez. Embora seja comum, não deve ser banalizada — existem estratégias seguras e eficazes para alívio.</p>

<h2>Por que a gestação causa dor lombar?</h2>
<ul>
<li><strong>Mudança do centro de gravidade:</strong> o crescimento do útero desloca o centro de gravidade para frente, aumentando a curvatura lombar (hiperlordose);</li>
<li><strong>Hormônio relaxina:</strong> aumenta a frouxidão ligamentar para preparar o parto, afetando articulações sacroilíacas e lombares;</li>
<li><strong>Ganho de peso:</strong> sobrecarga progressiva sobre coluna e articulações;</li>
<li><strong>Distensão da musculatura abdominal:</strong> reduz a estabilização natural da coluna;</li>
<li><strong>Alterações posturais compensatórias.</strong></li>
</ul>

<h2>Tipos de dor</h2>
<ul>
<li><strong>Lombalgia:</strong> dor na região lombar baixa, geralmente bilateral;</li>
<li><strong>Dor sacroilíaca:</strong> mais localizada nas nádegas, comum no terceiro trimestre;</li>
<li><strong>Ciática gestacional:</strong> dor irradiada para a perna, geralmente leve a moderada.</li>
</ul>

<h2>Sinais de alerta que exigem avaliação</h2>
<ul>
<li>Dor intensa que não melhora com repouso;</li>
<li>Irradiação importante com dormência ou fraqueza;</li>
<li>Perda de força nas pernas;</li>
<li>Alterações urinárias ou intestinais;</li>
<li>Dor associada a contrações ou sangramento (procurar obstetra imediatamente).</li>
</ul>

<h2>Estratégias seguras de alívio</h2>
<h3>Atividade física orientada</h3>
<p>Hidroterapia, Pilates para gestantes, ioga adaptada e caminhadas leves têm excelente respaldo científico. Sempre com supervisão profissional especializada em gestantes.</p>

<h3>Postura e ergonomia</h3>
<ul>
<li>Evitar ficar em pé ou sentada por longos períodos;</li>
<li>Usar sapatos confortáveis e estáveis;</li>
<li>Apoiar os pés ao sentar;</li>
<li>Dormir de lado (preferência esquerdo), com travesseiro entre os joelhos.</li>
</ul>

<h3>Fisioterapia obstétrica</h3>
<p>Profissional especializado pode aplicar técnicas seguras de terapia manual, alongamento e mobilizações que reduzem significativamente a dor.</p>

<h3>Cinta gestacional</h3>
<p>Pode auxiliar em casos selecionados, especialmente a partir do segundo trimestre, sob orientação profissional.</p>

<h3>Aplicação de calor local</h3>
<p>Compressas mornas (nunca quentes) ajudam a relaxar a musculatura. Evitar bolsas térmicas no abdome.</p>

<h2>Medicações: cuidado redobrado</h2>
<p>Apenas paracetamol é considerado seguro durante a gestação, sempre com orientação médica. Anti-inflamatórios convencionais devem ser evitados, especialmente no terceiro trimestre.</p>

<h2>O que evitar</h2>
<ul>
<li>Automedicação;</li>
<li>Quiropraxia manipulativa não validada para gestantes;</li>
<li>Posturas inadequadas no trabalho;</li>
<li>Carregar peso excessivo.</li>
</ul>

<h2>Após o parto</h2>
<p>A dor lombar costuma melhorar significativamente nas primeiras semanas. Se persistir além de 3 meses ou houver agravamento, busque avaliação especializada — pode haver alteração estrutural subjacente.</p>
"""
    ),
    make(
        "cirurgia-endoscopica-de-coluna",
        "Cirurgia Endoscópica de Coluna: A Revolução da Cirurgia Minimamente Invasiva",
        "Entenda como a endoscopia de coluna transformou o tratamento de hérnias e estenoses, com recuperação mais rápida e mínima agressão.",
        "spine", SPINE_IMG, 8, "2026-02-19",
        """
<p>A <strong>cirurgia endoscópica de coluna</strong> representa um dos maiores avanços da neurocirurgia moderna. Permite tratar hérnias, estenoses e outras patologias com incisões de apenas 8 milímetros, preservação muscular máxima e recuperação significativamente mais rápida.</p>

<h2>Como funciona a técnica?</h2>
<p>Através de uma pequena incisão, o cirurgião introduz um endoscópio — instrumento com câmera de alta definição e canais de trabalho — diretamente até o local da lesão. Toda a cirurgia é realizada visualizando estruturas com magnificação superior à do microscópio cirúrgico.</p>

<h2>Indicações principais</h2>
<ul>
<li>Hérnia de disco lombar e cervical;</li>
<li>Estenose foraminal e central;</li>
<li>Cistos sinoviais;</li>
<li>Recidiva de hérnia após cirurgia prévia;</li>
<li>Dor radicular refratária ao tratamento conservador;</li>
<li>Em casos selecionados, descompressões e até fusões minimamente invasivas.</li>
</ul>

<h2>Vantagens comprovadas</h2>
<ul>
<li><strong>Incisão de 8 a 10 mm</strong> (vs. 3-5 cm da microcirurgia);</li>
<li>Preservação total da musculatura paravertebral;</li>
<li>Menor sangramento intraoperatório;</li>
<li>Anestesia geral ou raquidiana (alguns casos sob sedação);</li>
<li><strong>Alta hospitalar no mesmo dia ou em 24 horas;</strong></li>
<li>Retorno à vida cotidiana em 1-2 semanas;</li>
<li>Retorno a atividades laborais leves em 2-3 semanas;</li>
<li>Menor risco de fibrose pós-operatória.</li>
</ul>

<h2>Como é a recuperação?</h2>
<p>Diferentemente da cirurgia tradicional, a endoscopia permite caminhada poucas horas após o procedimento. O paciente recebe orientações específicas de fisioterapia precoce, retorno gradual a atividades e acompanhamento ambulatorial frequente nas primeiras semanas.</p>

<h2>Cuidados pós-operatórios</h2>
<ul>
<li>Evitar esforços e cargas pesadas nas primeiras 4-6 semanas;</li>
<li>Iniciar fisioterapia conforme indicação médica;</li>
<li>Manter postura adequada e evitar movimentos bruscos;</li>
<li>Acompanhar consultas de revisão;</li>
<li>Retomar atividade física com orientação progressiva.</li>
</ul>

<h2>Limitações da técnica</h2>
<p>Nem todos os casos são elegíveis. Quadros com grande instabilidade, deformidades complexas ou tumores extensos podem exigir abordagens convencionais. A escolha da técnica deve ser sempre individualizada por especialista experiente em endoscopia de coluna.</p>

<h2>Por que escolher um cirurgião especializado?</h2>
<p>A endoscopia de coluna possui curva de aprendizado significativa. Cirurgiões com <strong>centenas a milhares de procedimentos realizados</strong> apresentam taxas de sucesso superiores a 90% e menor incidência de complicações. Pergunte sempre sobre a experiência específica do profissional na técnica.</p>

<h2>Resultados esperados</h2>
<p>A literatura científica mostra resultados equivalentes ou superiores à microcirurgia tradicional, com vantagens significativas em recuperação, retorno ao trabalho e satisfação do paciente. Para muitos casos, é hoje a técnica de escolha.</p>
"""
    ),
    make(
        "microdiscectomia-cirurgia-hernia-disco",
        "Microdiscectomia: A Cirurgia Padrão-Ouro para Hérnia de Disco",
        "Conheça a microdiscectomia, suas indicações, como é realizada e a recuperação após esse procedimento clássico de coluna.",
        "spine", SPINE_IMG, 7, "2026-02-20",
        """
<p>A <strong>microdiscectomia</strong> é considerada por décadas o padrão-ouro no tratamento cirúrgico da hérnia de disco lombar. Realizada com auxílio de microscópio cirúrgico, oferece excelentes resultados com mínima agressão aos tecidos.</p>

<h2>O que é a microdiscectomia?</h2>
<p>É um procedimento cirúrgico que utiliza um microscópio para visualizar e remover, através de uma pequena incisão de 2 a 3 cm, o fragmento herniado de disco que está comprimindo a raiz nervosa. Diferentemente da discectomia convencional, preserva ao máximo as estruturas vizinhas.</p>

<h2>Quando é indicada?</h2>
<ul>
<li>Hérnia de disco com dor radicular refratária ao tratamento conservador (6-12 semanas);</li>
<li>Déficit motor progressivo;</li>
<li>Dor incapacitante que compromete qualidade de vida;</li>
<li>Síndrome da cauda equina (urgência);</li>
<li>Falha de procedimentos minimamente invasivos prévios.</li>
</ul>

<h2>Como é realizada?</h2>
<h3>Anestesia e posicionamento</h3>
<p>Anestesia geral, com o paciente em decúbito ventral em mesa cirúrgica específica.</p>

<h3>Acesso</h3>
<p>Incisão de 2-3 cm na linha média lombar. Afastamento delicado da musculatura paravertebral. Pequena janela óssea (laminotomia) para acesso ao canal vertebral.</p>

<h3>Descompressão</h3>
<p>Sob magnificação do microscópio, identificação da raiz nervosa, afastamento cuidadoso e remoção do fragmento herniado. Inspeção do disco para evitar recidivas.</p>

<h2>Vantagens da microdiscectomia</h2>
<ul>
<li>Excelente visualização das estruturas neurais;</li>
<li>Taxa de sucesso superior a 90%;</li>
<li>Procedimento bem estabelecido na literatura;</li>
<li>Possibilidade de tratar hérnias complexas;</li>
<li>Recuperação relativamente rápida.</li>
</ul>

<h2>Tempo de internação e recuperação</h2>
<p>Maioria dos pacientes recebe alta em 24-48 horas. A dor radicular costuma melhorar imediatamente. A recuperação completa leva de 4 a 6 semanas, com retorno gradual às atividades.</p>

<h2>Pós-operatório: cuidados essenciais</h2>
<ul>
<li>Caminhar precocemente, ainda no hospital;</li>
<li>Evitar sentar por longos períodos nos primeiros dias;</li>
<li>Não pegar peso superior a 5 kg nas primeiras 4-6 semanas;</li>
<li>Iniciar fisioterapia 2-3 semanas após a cirurgia;</li>
<li>Retorno ao trabalho leve em 2-3 semanas;</li>
<li>Retorno a esportes em 8-12 semanas.</li>
</ul>

<h2>Microdiscectomia vs. Endoscopia: qual escolher?</h2>
<p>Ambas as técnicas têm resultados excelentes. A endoscopia oferece menor agressão tecidual e recuperação mais rápida, enquanto a microdiscectomia possui histórico mais longo e é versátil para casos complexos. A decisão deve ser individualizada pelo neurocirurgião, considerando características da hérnia, anatomia do paciente e experiência do cirurgião.</p>

<h2>Riscos e complicações</h2>
<p>São relativamente baixos (1-3% de complicações significativas), incluindo recidiva da hérnia, infecção, fístula liquórica e lesão neural. A escolha de um cirurgião experiente é crucial para minimizar riscos.</p>
"""
    ),
    make(
        "bloqueio-facetario-procedimento",
        "Bloqueio Facetário: O Que é, Quando é Indicado e Como Funciona",
        "Saiba tudo sobre o bloqueio facetário, procedimento eficaz para dor lombar de origem articular, e como ele pode evitar cirurgias.",
        "spine", BACK_IMG, 6, "2026-02-21",
        """
<p>O <strong>bloqueio facetário</strong> é um procedimento minimamente invasivo que oferece alívio significativo para pacientes com dor lombar ou cervical de origem nas articulações facetárias (zigapofisárias). Pode ter função tanto diagnóstica quanto terapêutica.</p>

<h2>Para que serve o bloqueio facetário?</h2>
<ul>
<li><strong>Diagnóstico:</strong> identifica se a dor realmente vem das facetas (gold standard);</li>
<li><strong>Tratamento:</strong> oferece alívio prolongado em pacientes com artrose facetária;</li>
<li><strong>Auxílio na fisioterapia:</strong> permite que o paciente realize exercícios sem dor.</li>
</ul>

<h2>Quando é indicado?</h2>
<ul>
<li>Dor lombar ou cervical localizada, paramediana;</li>
<li>Piora com extensão do tronco;</li>
<li>Suspeita clínica de dor facetária;</li>
<li>Falha de tratamento conservador inicial;</li>
<li>Diagnóstico diferencial com outras causas de dor.</li>
</ul>

<h2>Como é realizado?</h2>
<h3>Preparo</h3>
<p>Jejum de 4-6 horas. Pode ser realizado em centro cirúrgico ou sala de procedimentos com radioscopia (raio-x intraoperatório) ou tomografia.</p>

<h3>Procedimento</h3>
<ol>
<li>Paciente posicionado em decúbito ventral;</li>
<li>Anestesia local na pele;</li>
<li>Sob orientação de imagem, uma agulha fina é introduzida até a articulação facetária ou seu ramo nervoso;</li>
<li>Injeção de anestésico local e corticoide;</li>
<li>Procedimento dura cerca de 20-30 minutos.</li>
</ol>

<h2>Resultados esperados</h2>
<p>O alívio costuma ser imediato (efeito do anestésico). O efeito prolongado do corticoide aparece em 2-7 dias. A duração varia: alguns pacientes obtêm meses de melhora, outros relatam alívio mais breve. Quando o efeito é importante mas temporário, indica-se a <strong>radiofrequência facetária</strong> como tratamento definitivo.</p>

<h2>Cuidados após o procedimento</h2>
<ul>
<li>Repouso relativo por 24 horas;</li>
<li>Aplicação de gelo no local pode ser útil;</li>
<li>Retorno gradual às atividades normais em 24-48 horas;</li>
<li>Iniciar ou retomar fisioterapia conforme orientação.</li>
</ul>

<h2>Riscos e contraindicações</h2>
<p>O bloqueio facetário é considerado muito seguro, com taxa de complicações inferior a 1%. Possíveis efeitos adversos: dor temporária no local, raramente infecção, sangramento ou reação medicamentosa. Contraindicações incluem infecção ativa, alergias específicas e distúrbios graves de coagulação.</p>

<h2>Radiofrequência: o passo seguinte</h2>
<p>Quando o bloqueio funciona mas não dura, a radiofrequência facetária é a evolução natural. Ondas de radiofrequência criam lesão controlada nos ramos nervosos sensitivos das facetas, oferecendo alívio de 6 meses a 2 anos. Procedimento ambulatorial, com resultados excelentes em pacientes selecionados.</p>

<h2>Bloqueio facetário substitui a cirurgia?</h2>
<p>Para a maioria dos pacientes com dor facetária isolada, sim. A cirurgia fica reservada para casos com instabilidade ou estenose associada. O bloqueio é parte fundamental do arsenal terapêutico moderno em dor de coluna.</p>
"""
    ),
    make(
        "mielopatia-cervical-sinais-tratamento",
        "Mielopatia Cervical: A Compressão Medular que Não Pode Ser Ignorada",
        "Reconheça os sinais da mielopatia cervical, condição grave que requer tratamento cirúrgico precoce para evitar sequelas permanentes.",
        "spine", BRAIN_IMG, 8, "2026-02-22",
        """
<p>A <strong>mielopatia cervical</strong> é uma condição neurológica séria caracterizada pela compressão da medula espinhal na região do pescoço. Sua evolução natural costuma ser progressiva e o tratamento precoce é fundamental para evitar sequelas permanentes.</p>

<h2>O que é a medula espinhal cervical?</h2>
<p>A medula é a estrutura nervosa que transmite informações entre o cérebro e o restante do corpo. Na região cervical, ela controla movimentos e sensibilidade dos membros superiores, inferiores e funções esfincterianas. Sua compressão afeta múltiplas funções neurológicas.</p>

<h2>Causas mais comuns</h2>
<ul>
<li><strong>Espondilose cervical:</strong> degeneração natural com formação de osteófitos e hipertrofia ligamentar (causa mais comum em pessoas acima dos 50 anos);</li>
<li>Hérnias de disco cervicais centrais grandes;</li>
<li>Ossificação do ligamento longitudinal posterior (OLLP);</li>
<li>Estenose congênita do canal cervical;</li>
<li>Traumas cervicais;</li>
<li>Tumores intramedulares ou extramedulares.</li>
</ul>

<h2>Sintomas característicos: o quadro clássico</h2>
<h3>Comprometimento de mãos</h3>
<ul>
<li>Perda de destreza fina (dificuldade para abotoar, escrever, manipular pequenos objetos);</li>
<li>Sensação de "mão desajeitada";</li>
<li>Formigamento em mãos e dedos.</li>
</ul>

<h3>Comprometimento da marcha</h3>
<ul>
<li>Sensação de pernas pesadas, "marcha em bloco";</li>
<li>Desequilíbrio progressivo;</li>
<li>Quedas frequentes em casos avançados.</li>
</ul>

<h3>Outros sinais</h3>
<ul>
<li>Sinal de Lhermitte (sensação de choque ao flexionar o pescoço);</li>
<li>Hiperreflexia (reflexos aumentados);</li>
<li>Sinal de Babinski positivo;</li>
<li>Em casos avançados, alterações esfincterianas.</li>
</ul>

<h2>Por que diagnosticar precocemente?</h2>
<p>A mielopatia tem evolução tipicamente progressiva. Sintomas leves podem se manter estáveis por anos, mas uma vez instalado um déficit significativo, a recuperação completa é improvável mesmo após cirurgia. <strong>O tempo é, literalmente, neurônio.</strong></p>

<h2>Diagnóstico</h2>
<p>A ressonância magnética cervical é o exame padrão-ouro, mostrando a compressão medular e eventualmente alterações no sinal medular (gliose), que indicam sofrimento estabelecido. A tomografia complementa avaliação óssea, e estudos neurofisiológicos podem ser úteis em casos selecionados.</p>

<h2>Tratamento: cirurgia é a regra</h2>
<p>Diferentemente da hérnia de disco simples, a mielopatia cervical sintomática raramente responde apenas ao tratamento conservador. As principais opções cirúrgicas são:</p>

<h3>Discectomia cervical anterior com fusão (ACDF)</h3>
<p>Para compressões focais. Remove disco e osteófitos, com colocação de cage e placa.</p>

<h3>Corpectomia cervical</h3>
<p>Em compressões mais extensas, remove-se parte do corpo vertebral para descompressão ampla.</p>

<h3>Laminoplastia cervical</h3>
<p>Técnica posterior que aumenta o canal vertebral sem fixação, preservando mobilidade.</p>

<h3>Laminectomia com artrodese</h3>
<p>Para casos com múltiplos níveis e instabilidade.</p>

<h2>Recuperação e prognóstico</h2>
<p>Quanto mais precoce a cirurgia, melhor o prognóstico. Sintomas recentes (menos de 6 meses) costumam ter excelente reversibilidade. Sintomas crônicos podem estabilizar mas dificilmente reverterão completamente. Reabilitação fisioterápica é fundamental no pós-operatório.</p>
"""
    ),
    make(
        "fratura-vertebral-osteoporose-tratamento",
        "Fratura Vertebral por Osteoporose: Sintomas e Tratamento Moderno",
        "Saiba como identificar fraturas vertebrais por osteoporose e conheça a vertebroplastia e cifoplastia como tratamentos minimamente invasivos.",
        "spine", BACK_IMG, 7, "2026-02-23",
        """
<p>A <strong>fratura vertebral por osteoporose</strong> é uma das complicações mais comuns e incapacitantes da osteoporose. Frequentemente passa despercebida ou é confundida com simples dor lombar, mas pode ter consequências importantes para a qualidade de vida.</p>

<h2>O que é a osteoporose?</h2>
<p>É uma doença sistêmica caracterizada pela diminuição da densidade mineral óssea, tornando os ossos frágeis e suscetíveis a fraturas. Atinge principalmente mulheres pós-menopausa e idosos de ambos os sexos. Mais de 10 milhões de brasileiros convivem com a doença.</p>

<h2>Como ocorrem as fraturas vertebrais?</h2>
<p>Diferentemente do que muitos imaginam, a maioria das fraturas vertebrais por osteoporose ocorre com <strong>traumas mínimos</strong>: ao levantar um objeto leve, ao tossir vigorosamente, ao espirrar ou simplesmente ao se virar na cama. Em casos mais avançados, podem ocorrer fraturas espontâneas.</p>

<h2>Sintomas característicos</h2>
<ul>
<li>Dor lombar ou torácica de início súbito;</li>
<li>Piora ao sentar, levantar e movimentar-se;</li>
<li>Melhora parcial em decúbito;</li>
<li>Perda de estatura ao longo do tempo;</li>
<li>Cifose progressiva ("corcunda de viúva");</li>
<li>Em alguns casos, dor crônica e limitação funcional persistente;</li>
<li>Raramente, sintomas neurológicos.</li>
</ul>

<h2>Quando suspeitar?</h2>
<ul>
<li>Mulheres acima dos 60 anos com dor lombar de início súbito;</li>
<li>Histórico de fraturas prévias por trauma mínimo;</li>
<li>Diagnóstico prévio de osteoporose;</li>
<li>Uso prolongado de corticoides;</li>
<li>Perda de altura significativa ao longo dos anos.</li>
</ul>

<h2>Diagnóstico</h2>
<p>A radiografia mostra o colapso vertebral. A ressonância magnética é fundamental para diferenciar fraturas <strong>agudas (recentes)</strong> de antigas — informação crucial para decisão terapêutica. A densitometria óssea avalia o grau de osteoporose subjacente.</p>

<h2>Tratamento conservador</h2>
<ul>
<li>Analgesia e repouso relativo na fase aguda;</li>
<li>Uso de coletes ortopédicos por 6-8 semanas;</li>
<li>Mobilização precoce supervisionada;</li>
<li>Fisioterapia gradual;</li>
<li>Tratamento clínico da osteoporose (cálcio, vitamina D, bisfosfonatos, denosumabe).</li>
</ul>

<h2>Tratamentos minimamente invasivos</h2>
<h3>Vertebroplastia</h3>
<p>Injeção de cimento ortopédico (PMMA) percutânea, sob anestesia local, na vértebra fraturada. Estabiliza a fratura e alivia a dor rapidamente. Procedimento ambulatorial, com retorno às atividades em 24-48 horas.</p>

<h3>Cifoplastia</h3>
<p>Variação da vertebroplastia que usa um balão para restaurar parcialmente a altura da vértebra antes da injeção de cimento. Indicada em casos com colapso mais significativo.</p>

<h2>Indicações para os procedimentos percutâneos</h2>
<ul>
<li>Dor refratária a 4-6 semanas de tratamento conservador;</li>
<li>Fraturas agudas (até 6-8 semanas);</li>
<li>Pacientes com qualidade de vida comprometida;</li>
<li>Idosos que toleram mal repouso prolongado.</li>
</ul>

<h2>Prognóstico</h2>
<p>O alívio da dor é tipicamente rápido (24-48 horas após o procedimento) em mais de 90% dos pacientes. O tratamento concomitante da osteoporose é fundamental para evitar novas fraturas. Sem tratamento adequado, o risco de fraturas adicionais aumenta significativamente.</p>

<h2>Prevenção</h2>
<p>Densitometria óssea após os 65 anos (ou mais cedo em casos de risco), suplementação adequada de cálcio e vitamina D, atividade física com carga, e tratamento medicamentoso quando indicado são as melhores estratégias preventivas.</p>
"""
    ),
    make(
        "discopatia-degenerativa-tratamento",
        "Discopatia Degenerativa: O Envelhecimento dos Discos da Coluna",
        "Entenda o que é a discopatia degenerativa, como impacta a vida e quais tratamentos modernos existem para controle dos sintomas.",
        "spine", SPINE_IMG, 7, "2026-02-24",
        """
<p>A <strong>discopatia degenerativa</strong>, ou doença degenerativa do disco, é o processo natural de envelhecimento dos discos intervertebrais — mas que, em alguns pacientes, gera dor significativa e impacto na qualidade de vida.</p>

<h2>O que acontece nos discos com o passar do tempo?</h2>
<p>Os discos intervertebrais funcionam como amortecedores entre as vértebras. Com o envelhecimento, perdem água, elasticidade e altura. O anel fibroso pode desenvolver fissuras, e o núcleo pulposo torna-se menos hidratado e funcional.</p>

<h2>É doença ou envelhecimento normal?</h2>
<p>Ambos. Após os 40 anos, praticamente toda pessoa apresenta algum grau de degeneração discal — muitos completamente assintomáticos. A "discopatia degenerativa" como diagnóstico clínico é reservada para quando esse processo gera sintomas significativos.</p>

<h2>Fatores que aceleram a degeneração</h2>
<ul>
<li>Genética (forte componente hereditário);</li>
<li>Tabagismo (reduz nutrição dos discos);</li>
<li>Sobrepeso e obesidade;</li>
<li>Sedentarismo;</li>
<li>Trabalho braçal com cargas pesadas;</li>
<li>Postura inadequada crônica;</li>
<li>Traumas repetitivos.</li>
</ul>

<h2>Sintomas</h2>
<ul>
<li>Dor lombar ou cervical crônica;</li>
<li>Piora ao sentar por períodos prolongados (a pressão discal é máxima sentado);</li>
<li>Rigidez matinal;</li>
<li>Dor que melhora com movimento leve, piora com sobrecarga;</li>
<li>Em casos avançados, irradiação para membros (quando associada a hérnias ou estenose);</li>
<li>Episódios recorrentes de dor lombar aguda.</li>
</ul>

<h2>Diagnóstico</h2>
<p>A ressonância magnética mostra com clareza a degeneração: perda de sinal nos discos (escurecimento), perda de altura, fissuras anulares, alterações da medula óssea adjacente (alterações de Modic). Importante correlacionar achados com clínica — muitas alterações são incidentais.</p>

<h2>Tratamento conservador: base de tudo</h2>
<h3>Atividade física</h3>
<p>Pilates clínico, hidroterapia, fortalecimento de core e exercícios aeróbicos de baixo impacto têm forte respaldo científico. O movimento é o "alimento" do disco.</p>

<h3>Controle de fatores modificáveis</h3>
<ul>
<li>Cessação do tabagismo (impacto significativo);</li>
<li>Controle de peso;</li>
<li>Ergonomia no trabalho e em casa;</li>
<li>Higiene do sono.</li>
</ul>

<h3>Medicação e fisioterapia</h3>
<p>Anti-inflamatórios em fases agudas, neuromoduladores em casos crônicos, fisioterapia regular e terapias manuais.</p>

<h2>Procedimentos intervencionistas</h2>
<ul>
<li>Bloqueios e infiltrações em casos selecionados;</li>
<li>Tratamentos regenerativos (PRP, células-tronco) — área em estudo, sem indicação consolidada para todos os casos;</li>
<li>Ozonioterapia em pacientes selecionados.</li>
</ul>

<h2>Cirurgia: quando?</h2>
<p>Reservada para casos com sintomas significativos refratários, instabilidade ou compressões neurais associadas. Opções incluem artrodese (fusão) ou artroplastia (prótese de disco), individualizadas por especialista.</p>

<h2>Prognóstico</h2>
<p>Apesar da natureza crônica, a maioria dos pacientes consegue excelente controle dos sintomas com tratamento conservador adequado e mudanças de estilo de vida. A discopatia degenerativa não é uma sentença — é uma condição manejável.</p>
"""
    ),
    make(
        "espondilite-anquilosante-sintomas",
        "Espondilite Anquilosante: A Dor Lombar Inflamatória do Jovem",
        "Aprenda a reconhecer a espondilite anquilosante, doença reumatológica que afeta jovens e exige diagnóstico precoce.",
        "spine", SPINE_IMG, 7, "2026-02-25",
        """
<p>A <strong>espondilite anquilosante</strong> é uma doença inflamatória crônica que afeta primariamente a coluna vertebral e as articulações sacroilíacas. É a representante mais conhecida das espondiloartropatias e tem características muito específicas que a diferenciam das dores mecânicas comuns.</p>

<h2>Quem é afetado?</h2>
<ul>
<li>Predomínio em homens jovens (proporção 3:1);</li>
<li>Início típico entre 15 e 40 anos;</li>
<li>Forte componente genético (associação com HLA-B27);</li>
<li>Histórico familiar é fator de risco importante.</li>
</ul>

<h2>Sintomas característicos da dor inflamatória</h2>
<p>Diferentemente da dor lombar mecânica, a dor inflamatória possui características específicas:</p>
<ul>
<li><strong>Início insidioso</strong> em paciente jovem (menos de 40 anos);</li>
<li><strong>Rigidez matinal</strong> prolongada (mais de 30-60 minutos);</li>
<li><strong>Melhora com exercício, piora com repouso</strong> (oposto da dor mecânica);</li>
<li>Despertar noturno pela dor;</li>
<li>Duração superior a 3 meses;</li>
<li>Dor alternante em nádegas.</li>
</ul>

<h2>Manifestações além da coluna</h2>
<ul>
<li><strong>Uveíte anterior:</strong> inflamação ocular dolorosa, com olho vermelho e fotofobia;</li>
<li>Entesite (inflamação dos tendões, especialmente calcâneo);</li>
<li>Artrite periférica (joelhos, ombros);</li>
<li>Dactilite ("dedo em salsicha");</li>
<li>Associação com doenças inflamatórias intestinais e psoríase;</li>
<li>Em casos avançados, fusão progressiva da coluna ("coluna em bambu" na radiografia).</li>
</ul>

<h2>Diagnóstico precoce: por que é tão importante?</h2>
<p>O atraso médio no diagnóstico ainda é de 6-8 anos. Sintomas precoces são frequentemente confundidos com lombalgia comum. Quanto mais cedo o diagnóstico, melhor o controle da progressão e prevenção de deformidades irreversíveis.</p>

<h2>Como é feito o diagnóstico?</h2>
<ul>
<li>Avaliação clínica detalhada (critérios ASAS);</li>
<li>Ressonância magnética de sacroilíacas (mais sensível em fases iniciais);</li>
<li>Radiografia de sacroilíacas e coluna (mostra alterações em fases mais avançadas);</li>
<li>Pesquisa de HLA-B27 (presente em 90% dos casos);</li>
<li>Marcadores inflamatórios (VHS, PCR);</li>
<li>Avaliação reumatológica especializada.</li>
</ul>

<h2>Tratamento moderno</h2>
<h3>Pilares fundamentais</h3>
<ul>
<li><strong>Exercício físico regular:</strong> talvez a intervenção mais importante. Natação, alongamento, fortalecimento;</li>
<li><strong>Fisioterapia específica:</strong> preservação da mobilidade da coluna;</li>
<li><strong>Anti-inflamatórios não esteroidais</strong> (AINEs): primeira linha medicamentosa;</li>
<li>Cessação do tabagismo (acelera muito a progressão);</li>
<li>Acompanhamento reumatológico regular.</li>
</ul>

<h3>Terapias biológicas</h3>
<p>Em casos refratários aos AINEs, medicamentos biológicos (anti-TNF, anti-IL17) revolucionaram o tratamento, oferecendo controle excelente da doença e melhora significativa da qualidade de vida.</p>

<h2>Papel da neurocirurgia</h2>
<p>Em fases avançadas, pode haver necessidade de cirurgia para corrigir deformidades importantes (osteotomias) ou tratar fraturas, que são mais frequentes devido à rigidez óssea. O tratamento é sempre multidisciplinar (reumatologia + neurocirurgia/ortopedia).</p>

<h2>Vida com espondilite anquilosante</h2>
<p>Com diagnóstico precoce e tratamento adequado, a maioria dos pacientes mantém vida plenamente ativa, com mínima limitação. Os avanços terapêuticos das últimas duas décadas transformaram completamente o prognóstico da doença.</p>
"""
    ),
    make(
        "cifose-postural-hipercifose-tratamento",
        "Cifose Postural: A 'Corcunda' do Século XXI e Como Corrigir",
        "Entenda a hipercifose postural causada pelo uso excessivo de telas e descubra exercícios e tratamentos para correção.",
        "prevention", BACK_IMG, 6, "2026-02-26",
        """
<p>A <strong>cifose postural</strong>, popularmente conhecida como "corcunda" ou "costas curvas", é uma alteração da postura cada vez mais frequente, especialmente em jovens e adultos que passam longas horas em frente a computadores e smartphones — fenômeno hoje chamado de <em>tech neck</em>.</p>

<h2>Cifose normal x hipercifose</h2>
<p>A coluna torácica naturalmente apresenta uma curvatura para frente (cifose) entre 20° e 45°. Quando essa curvatura ultrapassa 45-50°, falamos em <strong>hipercifose</strong>. Em jovens e adultos sem alterações estruturais, geralmente trata-se de uma cifose postural, reversível com tratamento adequado.</p>

<h2>Causas da cifose postural moderna</h2>
<ul>
<li>Uso excessivo de smartphones e tablets (cabeça projetada para frente);</li>
<li>Trabalho prolongado em computadores com monitor abaixo da linha dos olhos;</li>
<li>Sedentarismo e fraqueza da musculatura posterior;</li>
<li>Encurtamento dos músculos peitorais;</li>
<li>Falta de consciência postural;</li>
<li>Em adolescentes, baixa autoestima e tendência a "encolher".</li>
</ul>

<h2>Outras causas de hipercifose</h2>
<ul>
<li><strong>Doença de Scheuermann:</strong> alteração estrutural da adolescência;</li>
<li><strong>Cifose senil:</strong> em idosos, por colapso de discos ou fraturas osteoporóticas;</li>
<li>Sequela de traumas ou cirurgias;</li>
<li>Doenças congênitas raras.</li>
</ul>

<h2>Sintomas associados</h2>
<ul>
<li>Dor cervical e cefaleias frequentes;</li>
<li>Dor entre as escápulas;</li>
<li>Sensação de cansaço postural;</li>
<li>Limitação de extensão da coluna;</li>
<li>Em casos avançados, comprometimento respiratório.</li>
</ul>

<h2>Avaliação</h2>
<p>O exame físico identifica a magnitude da deformidade e se é flexível (reversível) ou rígida. Radiografia panorâmica em pé mensura o ângulo de Cobb. Em casos atípicos, ressonância magnética pode ser solicitada para descartar causas estruturais.</p>

<h2>Tratamento da cifose postural</h2>
<h3>Exercícios essenciais</h3>
<ul>
<li><strong>Alongamento de peitorais:</strong> diariamente, na porta ou na parede;</li>
<li><strong>Fortalecimento da musculatura posterior:</strong> remadas, retração escapular, fortalecimento do trapézio inferior;</li>
<li><strong>Fortalecimento do core:</strong> base para sustentação postural;</li>
<li><strong>Mobilidade da coluna torácica:</strong> exercícios específicos com rolinho ou bola;</li>
<li>Yoga, Pilates clínico e RPG têm excelentes resultados.</li>
</ul>

<h3>Ajustes ergonômicos</h3>
<ul>
<li>Monitor na altura dos olhos;</li>
<li>Pausas a cada 50 minutos;</li>
<li>Uso consciente do celular (elevar à altura dos olhos);</li>
<li>Cadeira com bom suporte lombar.</li>
</ul>

<h3>Consciência postural</h3>
<p>Lembretes, espelhos, aplicativos que vibram quando você se curva — todas essas estratégias ajudam a "reeducar" o cérebro para uma postura mais alinhada.</p>

<h2>Quando procurar especialista?</h2>
<ul>
<li>Cifose rígida ou progressiva;</li>
<li>Dor importante refratária;</li>
<li>Suspeita de doença estrutural;</li>
<li>Comprometimento estético importante;</li>
<li>Sintomas neurológicos.</li>
</ul>

<h2>Tratamento cirúrgico</h2>
<p>Reservado para hipercifoses graves estruturais com importante repercussão funcional ou estética. Procedimentos modernos incluem artrodese instrumentada com técnicas minimamente invasivas em casos selecionados.</p>

<h2>Prevenção: a melhor estratégia</h2>
<p>Educação postural desde a infância, atividade física regular com fortalecimento de coluna, controle do tempo de tela e consciência corporal são fundamentais. A cifose postural é eminentemente prevenível.</p>
"""
    ),
    make(
        "sindrome-dor-miofascial-pontos-gatilho",
        "Síndrome da Dor Miofascial: Conheça os Pontos-Gatilho e Como Tratá-los",
        "Entenda o que são os pontos-gatilho miofasciais, por que causam dor referida e quais tratamentos realmente funcionam.",
        "prevention", BACK_IMG, 6, "2026-02-27",
        """
<p>A <strong>síndrome da dor miofascial</strong> é uma das causas mais comuns — e mais subdiagnosticadas — de dor crônica musculoesquelética. Caracteriza-se pela presença de pontos-gatilho dolorosos em músculos e fáscias, que geram dor local e dor referida em padrões específicos.</p>

<h2>O que são pontos-gatilho?</h2>
<p>Pontos-gatilho (ou trigger points) são nódulos hiperirritáveis em músculos esqueléticos, palpáveis como pequenas "bolinhas" ou "cordas" dolorosas. Quando pressionados, podem gerar dor no próprio local e em regiões distantes (dor referida), seguindo padrões anatômicos previsíveis.</p>

<h2>Fatores que favorecem o aparecimento</h2>
<ul>
<li>Postura inadequada prolongada;</li>
<li>Movimentos repetitivos;</li>
<li>Estresse físico e emocional;</li>
<li>Traumas musculares;</li>
<li>Sedentarismo alternado com esforços intensos;</li>
<li>Distúrbios do sono;</li>
<li>Deficiências nutricionais (vitamina D, magnésio);</li>
<li>Hipotireoidismo.</li>
</ul>

<h2>Sintomas característicos</h2>
<ul>
<li>Dor profunda, em peso ou queimação;</li>
<li>Dor referida em padrões específicos;</li>
<li>Sensação de "nó" ou "tensão" muscular;</li>
<li>Limitação de movimento e força;</li>
<li>Cefaleias tensionais (quando em cervical e trapézio);</li>
<li>Distúrbios do sono pela dor;</li>
<li>Sintomas autonômicos associados (formigamento, sudorese local).</li>
</ul>

<h2>Localização comum dos pontos-gatilho</h2>
<ul>
<li><strong>Trapézio:</strong> causa cefaleias e dor no pescoço;</li>
<li><strong>Quadrado lombar:</strong> dor lombar e referida para nádegas;</li>
<li><strong>Piriforme:</strong> mimetiza ciatalgia;</li>
<li><strong>Glúteo médio:</strong> dor referida para a coxa lateral;</li>
<li><strong>Romboides e escapulares:</strong> dor entre as escápulas;</li>
<li><strong>Esternocleidomastóideo:</strong> cefaleias e tonturas.</li>
</ul>

<h2>Como diferenciar da fibromialgia?</h2>
<p>A síndrome miofascial é <strong>localizada</strong> e tem pontos-gatilho ativos. A fibromialgia é <strong>generalizada</strong> e cursa com fadiga, alterações de sono, alterações cognitivas e múltiplos pontos sensíveis (sem o componente de dor referida típico dos gatilhos miofasciais).</p>

<h2>Diagnóstico</h2>
<p>É essencialmente clínico, baseado em exame físico detalhado. Não há exames de imagem específicos. O médico identifica os pontos-gatilho pela palpação, sua reprodução do padrão de dor referida e a resposta característica à compressão (resposta de contração local — "twitch response").</p>

<h2>Tratamentos eficazes</h2>
<h3>Terapia manual</h3>
<ul>
<li>Liberação miofascial;</li>
<li>Compressão isquêmica dos pontos-gatilho;</li>
<li>Massagem terapêutica especializada;</li>
<li>Mobilização articular.</li>
</ul>

<h3>Punção seca (dry needling)</h3>
<p>Técnica com excelentes resultados: agulhas finas (como de acupuntura) são inseridas diretamente nos pontos-gatilho, "desativando-os". Procedimento de baixo custo e rápido alívio.</p>

<h3>Infiltração com anestésico</h3>
<p>Em pontos-gatilho refratários, pode ser realizada injeção de anestésico local. Toxina botulínica é opção em casos selecionados.</p>

<h3>Exercícios e alongamentos</h3>
<p>Fundamentais para evitar recidiva. Programa supervisionado de fortalecimento e flexibilidade tem impacto significativo.</p>

<h2>Estratégias complementares</h2>
<ul>
<li>Correção postural;</li>
<li>Manejo do estresse (meditação, terapia);</li>
<li>Higiene do sono;</li>
<li>Atividade física regular;</li>
<li>Correção de deficiências nutricionais identificadas;</li>
<li>Hidratação adequada.</li>
</ul>

<h2>Prognóstico</h2>
<p>Com tratamento adequado e mudanças de estilo de vida, a maioria dos pacientes apresenta excelente melhora. A síndrome miofascial é altamente responsiva ao tratamento — desde que diagnosticada e tratada corretamente.</p>
"""
    ),
    make(
        "pilates-rpg-coluna-evidencias-cientificas",
        "Pilates e RPG para Coluna: O Que a Ciência Realmente Diz",
        "Descubra o que pesquisas científicas mostram sobre Pilates clínico e RPG no tratamento e prevenção de problemas de coluna.",
        "prevention", BACK_IMG, 6, "2026-02-28",
        """
<p>O <strong>Pilates clínico</strong> e o <strong>RPG (Reeducação Postural Global)</strong> são duas das técnicas mais populares de exercício terapêutico para problemas de coluna. Mas o que a ciência realmente diz sobre seus benefícios? Vale a pena investir?</p>

<h2>Pilates clínico: princípios e evidências</h2>
<p>Criado pelo alemão Joseph Pilates no início do século XX, o método combina exercícios de fortalecimento, flexibilidade, controle motor e respiração. A versão "clínica" é adaptada para reabilitação e supervisionada por fisioterapeutas.</p>

<h3>O que a pesquisa mostra</h3>
<ul>
<li>Revisões sistemáticas (Cochrane) confirmam que o Pilates é eficaz para dor lombar crônica;</li>
<li>Melhora significativa da função e qualidade de vida;</li>
<li>Resultados comparáveis ou superiores a outras formas de exercício;</li>
<li>Bom perfil de segurança em pacientes selecionados;</li>
<li>Benefícios também documentados para dor cervical crônica.</li>
</ul>

<h3>Pilates de aparelhos vs. de solo</h3>
<p>Ambos têm benefícios, mas o Pilates de aparelhos (Reformer, Cadillac, Chair) permite progressão mais individualizada e assistência em movimentos específicos — vantagem importante em fases iniciais da reabilitação.</p>

<h2>RPG: princípios e evidências</h2>
<p>Desenvolvido pelo francês Philippe Souchard, o RPG é uma técnica de fisioterapia que trabalha o corpo em cadeias musculares, com posturas de alongamento global e respiração específica.</p>

<h3>O que a literatura mostra</h3>
<ul>
<li>Eficácia comprovada em dor lombar crônica e cervicalgia;</li>
<li>Melhora da flexibilidade global e amplitude de movimento;</li>
<li>Bons resultados em alterações posturais (escoliose leve, hipercifose);</li>
<li>Excelente para casos com encurtamentos musculares importantes;</li>
<li>Sessões mais longas (geralmente 1 hora) com poucos exercícios por sessão.</li>
</ul>

<h2>Pilates ou RPG: qual escolher?</h2>
<p>A escolha depende de objetivos, perfil do paciente e disponibilidade de profissionais qualificados:</p>
<ul>
<li><strong>Pilates clínico:</strong> melhor para fortalecimento progressivo, controle motor, atletas e pacientes que querem aliar reabilitação e condicionamento;</li>
<li><strong>RPG:</strong> melhor para casos com importante componente de encurtamentos musculares, alterações posturais estruturais e pacientes que preferem trabalho mais estático.</li>
</ul>

<p>Frequentemente, as duas técnicas se complementam e podem ser combinadas em diferentes fases do tratamento.</p>

<h2>Outras formas de exercício com evidência</h2>
<ul>
<li><strong>Yoga:</strong> bom respaldo científico para dor lombar crônica;</li>
<li><strong>Tai chi e qigong:</strong> benefícios em equilíbrio e dor crônica;</li>
<li><strong>Hidroterapia:</strong> excelente para casos com dificuldade em exercícios em solo;</li>
<li><strong>Musculação tradicional supervisionada:</strong> eficaz se bem orientada;</li>
<li><strong>Caminhada regular:</strong> simples e altamente eficaz.</li>
</ul>

<h2>O segredo: profissional qualificado</h2>
<p>Nenhuma técnica funciona sem profissional capacitado. Procure fisioterapeutas com formação específica e que individualizem o programa às suas necessidades. Aulas em grupo padronizadas raramente trazem os mesmos benefícios.</p>

<h2>Quem deve fazer?</h2>
<ul>
<li>Dor lombar ou cervical crônica;</li>
<li>Pós-operatórios de coluna (com liberação médica);</li>
<li>Hérnias de disco em fase estável;</li>
<li>Prevenção em pacientes com fatores de risco;</li>
<li>Atletas para prevenção de lesões;</li>
<li>Gestantes (com profissional habilitado).</li>
</ul>

<h2>Cuidados e contraindicações</h2>
<p>Casos agudos importantes, instabilidades não diagnosticadas ou sinais de alerta devem ser primeiro avaliados pelo médico. Exercícios mal supervisionados podem agravar quadros existentes.</p>

<h2>Recomendação prática</h2>
<p>A melhor abordagem para a coluna é <strong>combinar técnicas</strong>: avaliação médica especializada + programa de fisioterapia/exercício orientado + ajustes de estilo de vida. Isolar uma única técnica é menos eficaz que uma estratégia multimodal e contínua.</p>
"""
    ),
]

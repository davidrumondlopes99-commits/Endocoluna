// Mapping slug → YouTube video ID for contextual embeds in article pages.
// Falls back to topic-based matching, then to a default video.

const CHANNEL = "drmatheuslopesneuro";

// Real videos from the channel @drmatheuslopesneuro
const VIDEOS = {
  espondilolistese: { id: "oSYlaWKGHFk", title: "Sua coluna está saindo do lugar? Entenda isso agora." },
  estenose:         { id: "5tKKmzTU4Zw", title: "Suas pernas falham ao andar? Pode ser estenose." },
  hernia_rm:        { id: "VvVJIYLU8cw", title: "Ressonância pode enganar? Nem toda hérnia causa dor" },
  desligar_dor:     { id: "NIRrt8uQOps", title: "Como desligar a dor na coluna" },
  sinais_alerta:    { id: "2aNUZmyZ0pg", title: "Dor na coluna: Sinais que não podem esperar" },
  diagnostico:      { id: "iZToD_heajM", title: "Recebeu diagnóstico de Hérnia de Disco ou Estenose? Assista antes de decidir o tratamento" },
  sono_dor:         { id: "jibiGCgOL-0", title: "DOR NA COLUNA ROUBANDO SEU SONO?" },
  guia_sono:        { id: "dYRHtTJtXPc", title: "O Guia Médico do Sono e da Coluna" },
  cirurgia_mis:     { id: "D5wZvIWcVuM", title: "Cirurgia de coluna minimamente invasiva" },
};

// Explicit slug → video mapping (highest priority)
const SLUG_MAP = {
  // Hérnia
  "hernia-de-disco-sintomas-causas-e-quando-a-cirurgia-e-necessaria": VIDEOS.diagnostico,
  "hernia-de-disco-cervical-sintomas-tratamento": VIDEOS.diagnostico,
  "ressonancia-magnetica-coluna-quando-fazer": VIDEOS.hernia_rm,
  "ozonioterapia-para-hernia-de-disco": VIDEOS.diagnostico,
  "microdiscectomia-cirurgia-hernia-disco": VIDEOS.cirurgia_mis,

  // Estenose
  "estenose-de-canal-lombar-sintomas-cirurgia": VIDEOS.estenose,
  "hipertrofia-ligamento-amarelo": VIDEOS.estenose,
  "dor-coluna-em-idosos": VIDEOS.estenose,

  // Espondilolistese
  "espondilolistese-tratamento": VIDEOS.espondilolistese,
  "espondilolise-defeito-pars": VIDEOS.espondilolistese,

  // Cirurgia minimamente invasiva
  "cirurgia-endoscopica-de-coluna": VIDEOS.cirurgia_mis,
  "endoscopia-transforaminal-vs-interlaminar": VIDEOS.cirurgia_mis,
  "cirurgia-robotica-em-coluna": VIDEOS.cirurgia_mis,

  // Dor crônica
  "lombalgia-cronica-causas-e-tratamento": VIDEOS.desligar_dor,
  "nervo-ciatico-inflamado-sintomas-e-tratamento": VIDEOS.desligar_dor,
  "sindrome-do-piriforme-falsa-ciatica": VIDEOS.desligar_dor,
  "neuroestimulacao-medular-dor-cronica": VIDEOS.desligar_dor,
  "failed-back-surgery-syndrome": VIDEOS.desligar_dor,
  "fibromialgia-x-problemas-coluna": VIDEOS.desligar_dor,
  "sindrome-dor-miofascial-pontos-gatilho": VIDEOS.desligar_dor,

  // Sono e coluna
  "colchao-e-travesseiro-ideal-coluna": VIDEOS.sono_dor,
  "postura-home-office-guia-completo": VIDEOS.guia_sono,

  // Sinais de alerta
  "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave": VIDEOS.sinais_alerta,
  "primeiros-sinais-problema-coluna": VIDEOS.sinais_alerta,
  "sindrome-cauda-equina-emergencia": VIDEOS.sinais_alerta,
  "tumor-de-coluna-sinais-alerta": VIDEOS.sinais_alerta,
  "espondilodiscite-infeccao-coluna": VIDEOS.sinais_alerta,
  "dor-lombar-aguda-o-que-fazer-primeiras-48-horas": VIDEOS.sinais_alerta,
};

// Topic groups used to spread videos across remaining articles
const TOPIC_GROUPS = [
  { match: /(disco|hernia|microdis|endoscop|cirurg)/i, video: VIDEOS.diagnostico },
  { match: /(estenose|caminhar|canal|ligamento)/i, video: VIDEOS.estenose },
  { match: /(espondi)/i, video: VIDEOS.espondilolistese },
  { match: /(dor|lombalg|cronic|ciat|nervo)/i, video: VIDEOS.desligar_dor },
  { match: /(sono|colchao|travesseiro|noturna)/i, video: VIDEOS.sono_dor },
  { match: /(sinai|cauda|tumor|infec|emergenc|alerta|primeiros)/i, video: VIDEOS.sinais_alerta },
  { match: /(minimamente|robo|endo)/i, video: VIDEOS.cirurgia_mis },
];

export function getRelatedVideo({ slug, title = "", category = "" }) {
  if (SLUG_MAP[slug]) return SLUG_MAP[slug];

  const haystack = `${slug} ${title} ${category}`.toLowerCase();
  for (const g of TOPIC_GROUPS) {
    if (g.match.test(haystack)) return g.video;
  }
  // default: most popular educational video
  return VIDEOS.desligar_dor;
}

export const YOUTUBE_CHANNEL_URL = `https://www.youtube.com/@${CHANNEL}`;

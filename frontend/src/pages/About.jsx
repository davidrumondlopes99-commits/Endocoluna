import { Award, BookOpen, ShieldCheck, GraduationCap, Microscope, Users } from "lucide-react";

const values = [
  { icon: ShieldCheck, title: "Baseado em evidências", desc: "Cada conteúdo é verificado e referenciado em diretrizes clínicas atualizadas." },
  { icon: BookOpen, title: "Linguagem acessível", desc: "Traduzimos o jargão médico para que pacientes e familiares compreendam." },
  { icon: Microscope, title: "Revisão especializada", desc: "Todos os textos passam por revisão de neurocirurgião com atuação clínica." },
  { icon: Users, title: "Foco no paciente", desc: "Conteúdo desenhado para responder às dúvidas reais do consultório." },
];

export default function About() {
  return (
    <div data-testid="about-page">
      <section className="bg-white border-b border-slate-200">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-20">
          <div className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-3">Sobre o Blog</div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-[#1A365D] tracking-tight leading-[1.05]">
            Ciência <span className="text-[#319795]">acessível</span> em Neurocirurgia e Cirurgia de Coluna.
          </h1>
          <p className="mt-6 text-lg text-slate-600 leading-relaxed">
            O <strong>NeuroSaúde</strong> nasceu da constatação de que existe um abismo entre o que a literatura médica
            produz e o que chega de forma clara à população. Nossa missão é encurtar essa distância — com artigos
            longos, profundos, revisados por especialistas e sempre escritos pensando em quem está diante de um
            diagnóstico ou de uma dúvida importante.
          </p>
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-[#1A365D] mb-10">Nossos valores editoriais</h2>
        <div className="grid sm:grid-cols-2 gap-6">
          {values.map((v, i) => {
            const Icon = v.icon;
            return (
              <div key={i} className="bg-white border border-slate-200 rounded-xl p-6 article-card-hover">
                <div className="w-11 h-11 rounded-xl bg-[#319795]/10 flex items-center justify-center mb-4">
                  <Icon className="w-5 h-5 text-[#319795]" />
                </div>
                <h3 className="text-lg font-bold text-[#1A365D]">{v.title}</h3>
                <p className="mt-2 text-sm text-slate-600 leading-relaxed">{v.desc}</p>
              </div>
            );
          })}
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-slate-200">
        <div className="grid md:grid-cols-12 gap-10 items-start">
          <div className="md:col-span-4">
            <img
              src="https://images.pexels.com/photos/8460157/pexels-photo-8460157.jpeg"
              alt="Dr. Ricardo Almeida"
              className="w-full rounded-2xl border border-slate-200 object-cover aspect-[4/5]"
            />
          </div>
          <div className="md:col-span-8">
            <div className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-2">Editor Médico</div>
            <h2 className="text-3xl sm:text-4xl font-bold text-[#1A365D] tracking-tight">Dr. Ricardo Almeida</h2>
            <p className="mt-1 text-slate-500">Neurocirurgião — CRM-SP 123.456 / RQE 7890</p>

            <p className="mt-6 text-base text-slate-600 leading-relaxed">
              Graduado em Medicina pela Universidade de São Paulo, com residência em Neurocirurgia no Hospital
              das Clínicas e fellowship em Cirurgia Minimamente Invasiva de Coluna. Atua há mais de 15 anos em
              centros de referência, com foco em hérnias de disco, estenoses, aneurismas cerebrais e doenças
              vasculares do sistema nervoso central.
            </p>

            <div className="mt-8 grid grid-cols-3 gap-4">
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <Award className="w-5 h-5 text-[#319795]" />15+
                </div>
                <div className="text-xs text-slate-500 mt-1">Anos de prática</div>
              </div>
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <BookOpen className="w-5 h-5 text-[#319795]" />40+
                </div>
                <div className="text-xs text-slate-500 mt-1">Publicações científicas</div>
              </div>
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <GraduationCap className="w-5 h-5 text-[#319795]" />3
                </div>
                <div className="text-xs text-slate-500 mt-1">Especializações</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#1A365D] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-14 text-center">
          <h3 className="text-2xl sm:text-3xl font-bold">Tem uma dúvida ou sugestão de pauta?</h3>
          <p className="mt-3 text-slate-300 max-w-2xl mx-auto">
            Escreva para a redação. Selecionamos as melhores perguntas dos leitores para transformar em conteúdo.
          </p>
          <a
            href="mailto:contato@neurosaude.com.br"
            data-testid="contact-email"
            className="inline-block mt-6 bg-[#319795] hover:bg-white hover:text-[#1A365D] text-white font-semibold px-7 py-3 rounded-full transition-colors"
          >
            contato@neurosaude.com.br
          </a>
        </div>
      </section>
    </div>
  );
}

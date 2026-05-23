import { Award, BookOpen, ShieldCheck, GraduationCap, Microscope, Users, Instagram, MessageCircle, MapPin, Globe, Youtube } from "lucide-react";
import { SOCIAL_LINKS } from "../lib/socialLinks";
import { SEO } from "../components/SEO";

const values = [
  { icon: ShieldCheck, title: "Baseado em evidências", desc: "Cada conteúdo é verificado e referenciado em diretrizes clínicas atualizadas." },
  { icon: BookOpen, title: "Linguagem acessível", desc: "Traduzimos o jargão médico para que pacientes e familiares compreendam." },
  { icon: Microscope, title: "Revisão especializada", desc: "Todos os textos passam por revisão de neurocirurgião com atuação clínica." },
  { icon: Users, title: "Foco no paciente", desc: "Conteúdo desenhado para responder às dúvidas reais do consultório." },
];

export default function About() {
  return (
    <div data-testid="about-page">
      <SEO
        title="Sobre o Blog"
        description="Conheça o NeuroSaúde, blog médico do Dr. Matheus Lopes (Neurocirurgião, CRM/SP 147238), especialista em coluna e dor, com mais de 1.000 cirurgias endoscópicas realizadas."
      />
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
              src="https://customer-assets.emergentagent.com/job_neuroeduca/artifacts/ec65g3l5_617A9485.JPG"
              alt="Dr. Matheus Lopes"
              className="w-full rounded-2xl border border-slate-200 object-cover aspect-[4/5]"
            />
          </div>
          <div className="md:col-span-8">
            <div className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-2">Editor Médico</div>
            <h2 className="text-3xl sm:text-4xl font-bold text-[#1A365D] tracking-tight">Dr. Matheus Lopes</h2>
            <p className="mt-1 text-slate-500">Neurocirurgião — CRM/SP 147238</p>

            <ul className="mt-6 space-y-3 text-base text-slate-700">
              <li className="flex items-start gap-3">
                <span className="mt-2 w-1.5 h-1.5 rounded-full bg-[#319795] flex-shrink-0" />
                <span><strong className="text-[#1A365D]">Neurocirurgião</strong>, especialista em coluna e dor.</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="mt-2 w-1.5 h-1.5 rounded-full bg-[#319795] flex-shrink-0" />
                <span>Ênfase em <strong className="text-[#1A365D]">cirurgia minimamente invasiva</strong>.</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="mt-2 w-1.5 h-1.5 rounded-full bg-[#319795] flex-shrink-0" />
                <span><strong className="text-[#1A365D]">+ de 1.000 cirurgias endoscópicas</strong> realizadas.</span>
              </li>
            </ul>

            <p className="mt-6 text-base text-slate-600 leading-relaxed">
              Atuação dedicada ao tratamento de hérnias de disco, estenoses, dor crônica e outras patologias
              da coluna, sempre com foco em técnicas modernas, recuperação mais rápida e cuidado individualizado.
            </p>

            <div className="mt-8 grid grid-cols-3 gap-4">
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <Award className="w-5 h-5 text-[#319795]" />1.000+
                </div>
                <div className="text-xs text-slate-500 mt-1">Endoscopias realizadas</div>
              </div>
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <BookOpen className="w-5 h-5 text-[#319795]" />MIS
                </div>
                <div className="text-xs text-slate-500 mt-1">Cirurgia minimamente invasiva</div>
              </div>
              <div className="border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-2 text-[#1A365D] font-bold text-2xl">
                  <GraduationCap className="w-5 h-5 text-[#319795]" />CRM
                </div>
                <div className="text-xs text-slate-500 mt-1">SP 147238</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#1A365D] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
          <div className="text-center mb-8">
            <h3 className="text-2xl sm:text-3xl font-bold">Quer agendar uma consulta?</h3>
            <p className="mt-3 text-slate-300 max-w-2xl mx-auto">
              Entre em contato pelos canais oficiais do Dr. Matheus Lopes.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 gap-4 max-w-2xl mx-auto">
            <a
              href={SOCIAL_LINKS.whatsapp}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="about-whatsapp-cta"
              className="flex items-center gap-3 bg-[#25D366] hover:bg-[#128C7E] text-white font-semibold px-5 py-4 rounded-xl transition-colors"
            >
              <MessageCircle className="w-5 h-5 flex-shrink-0" />
              <div>
                <div className="text-xs uppercase tracking-wider opacity-80">WhatsApp</div>
                <div>Agendar consulta</div>
              </div>
            </a>
            <a
              href={SOCIAL_LINKS.instagram}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="about-instagram-cta"
              className="flex items-center gap-3 bg-white/10 hover:bg-[#319795] text-white font-semibold px-5 py-4 rounded-xl transition-colors"
            >
              <Instagram className="w-5 h-5 flex-shrink-0" />
              <div>
                <div className="text-xs uppercase tracking-wider opacity-80">Instagram</div>
                <div>@drmatheuslopesneuro</div>
              </div>
            </a>
            <a
              href={SOCIAL_LINKS.youtube}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="about-youtube-cta"
              className="flex items-center gap-3 bg-white/10 hover:bg-[#FF0000] text-white font-semibold px-5 py-4 rounded-xl transition-colors"
            >
              <Youtube className="w-5 h-5 flex-shrink-0" />
              <div>
                <div className="text-xs uppercase tracking-wider opacity-80">YouTube</div>
                <div>@drmatheuslopesneuro</div>
              </div>
            </a>
            <a
              href={SOCIAL_LINKS.website}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="about-website-cta"
              className="flex items-center gap-3 bg-white/10 hover:bg-[#319795] text-white font-semibold px-5 py-4 rounded-xl transition-colors"
            >
              <Globe className="w-5 h-5 flex-shrink-0" />
              <div>
                <div className="text-xs uppercase tracking-wider opacity-80">Site oficial</div>
                <div>drmatheuslopes.com.br</div>
              </div>
            </a>
            <a
              href={SOCIAL_LINKS.maps}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="about-address-cta"
              className="flex items-center gap-3 bg-white/10 hover:bg-[#319795] text-white font-semibold px-5 py-4 rounded-xl transition-colors"
            >
              <MapPin className="w-5 h-5 flex-shrink-0" />
              <div>
                <div className="text-xs uppercase tracking-wider opacity-80">Consultório</div>
                <div>Ver endereço no mapa</div>
              </div>
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

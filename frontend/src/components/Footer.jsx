import { Link } from "react-router-dom";
import { Brain, Instagram, Facebook, Linkedin, Youtube, AlertTriangle } from "lucide-react";

export const Footer = () => {
  return (
    <footer data-testid="site-footer" className="bg-[#1A365D] text-white mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        {/* Disclaimer banner */}
        <div
          data-testid="medical-disclaimer"
          className="flex items-start gap-3 bg-white/5 border border-white/10 rounded-xl p-5 mb-10"
        >
          <AlertTriangle className="w-5 h-5 text-[#319795] mt-1 flex-shrink-0" />
          <p className="text-sm text-slate-200 leading-relaxed">
            <strong className="text-white">Aviso Médico:</strong> Todo o conteúdo deste blog tem caráter
            exclusivamente <span className="text-[#319795] font-semibold">educacional e informativo</span> e
            não substitui, em nenhuma hipótese, a consulta presencial com um profissional médico habilitado.
            Diagnósticos e tratamentos devem ser sempre individualizados por especialistas qualificados.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-10">
          <div className="md:col-span-2">
            <div className="flex items-center gap-2.5 mb-4">
              <div className="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center">
                <Brain className="w-5 h-5 text-[#319795]" />
              </div>
              <div className="leading-tight">
                <div className="font-bold text-xl">NeuroSaúde</div>
                <div className="text-[11px] uppercase tracking-[0.18em] text-[#319795] font-semibold">Blog Médico</div>
              </div>
            </div>
            <p className="text-slate-300 text-sm leading-relaxed max-w-md">
              Plataforma editorial dedicada à divulgação de informação científica em Neurocirurgia e
              Cirurgia de Coluna, escrita em linguagem acessível para pacientes e familiares.
            </p>
          </div>

          <div>
            <h4 className="text-sm font-bold uppercase tracking-wider text-white mb-4">Categorias</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li><Link data-testid="footer-cat-brain" to="/categoria/brain" className="hover:text-[#319795] transition-colors">Cérebro</Link></li>
              <li><Link data-testid="footer-cat-spine" to="/categoria/spine" className="hover:text-[#319795] transition-colors">Coluna</Link></li>
              <li><Link data-testid="footer-cat-prevention" to="/categoria/prevention" className="hover:text-[#319795] transition-colors">Prevenção</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-bold uppercase tracking-wider text-white mb-4">Institucional</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li><Link data-testid="footer-about-link" to="/sobre" className="hover:text-[#319795] transition-colors">Sobre o Blog</Link></li>
              <li><Link data-testid="footer-privacy-link" to="/privacidade" className="hover:text-[#319795] transition-colors">Política de Privacidade</Link></li>
              <li><Link data-testid="footer-terms-link" to="/termos" className="hover:text-[#319795] transition-colors">Termos de Uso</Link></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-white/10 mt-10 pt-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <p className="text-xs text-slate-400">
            © {new Date().getFullYear()} NeuroSaúde. Todos os direitos reservados.
          </p>
          <div className="flex items-center gap-3">
            <a data-testid="social-instagram" href="#" aria-label="Instagram" className="w-9 h-9 rounded-full bg-white/5 hover:bg-[#319795] flex items-center justify-center transition-colors">
              <Instagram className="w-4 h-4" />
            </a>
            <a data-testid="social-facebook" href="#" aria-label="Facebook" className="w-9 h-9 rounded-full bg-white/5 hover:bg-[#319795] flex items-center justify-center transition-colors">
              <Facebook className="w-4 h-4" />
            </a>
            <a data-testid="social-linkedin" href="#" aria-label="LinkedIn" className="w-9 h-9 rounded-full bg-white/5 hover:bg-[#319795] flex items-center justify-center transition-colors">
              <Linkedin className="w-4 h-4" />
            </a>
            <a data-testid="social-youtube" href="#" aria-label="YouTube" className="w-9 h-9 rounded-full bg-white/5 hover:bg-[#319795] flex items-center justify-center transition-colors">
              <Youtube className="w-4 h-4" />
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

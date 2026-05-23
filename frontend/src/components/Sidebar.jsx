import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Mail, Award, BookOpen, TrendingUp, Instagram, MessageCircle, Youtube } from "lucide-react";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { toast } from "sonner";
import { fetchMostRead, subscribeNewsletter, CATEGORY_META } from "../lib/api";
import { SOCIAL_LINKS } from "../lib/socialLinks";

const EditorWidget = () => (
  <div data-testid="editor-widget" className="bg-white border border-slate-200 rounded-xl p-6">
    <h4 className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-4">Editor Médico</h4>
    <div className="flex items-start gap-4">
      <img
        src="https://customer-assets.emergentagent.com/job_neuroeduca/artifacts/ec65g3l5_617A9485.JPG"
        alt="Dr. Matheus Lopes"
        className="w-20 h-20 rounded-full object-cover border-2 border-[#319795]/20"
      />
      <div className="flex-1 min-w-0">
        <h5 className="font-bold text-[#1A365D]">Dr. Matheus Lopes</h5>
        <p className="text-xs text-slate-500 mt-0.5">CRM/SP 147238</p>
        <p className="text-xs text-slate-600 mt-2 leading-relaxed">
          Neurocirurgião, especialista em coluna e dor. Ênfase em cirurgia minimamente invasiva.
        </p>
      </div>
    </div>
    <div className="mt-4 pt-4 border-t border-slate-100 grid grid-cols-2 gap-3 text-center">
      <div>
        <div className="flex items-center justify-center gap-1.5 text-[#1A365D]">
          <Award className="w-4 h-4" /> <span className="font-bold">1000+</span>
        </div>
        <div className="text-[11px] text-slate-500 uppercase tracking-wide">Endoscopias</div>
      </div>
      <div>
        <div className="flex items-center justify-center gap-1.5 text-[#1A365D]">
          <BookOpen className="w-4 h-4" /> <span className="font-bold">MIS</span>
        </div>
        <div className="text-[11px] text-slate-500 uppercase tracking-wide">Minimamente invasiva</div>
      </div>
    </div>
    <div className="mt-4 grid grid-cols-3 gap-2">
      <a
        href={SOCIAL_LINKS.instagram}
        target="_blank"
        rel="noopener noreferrer"
        data-testid="editor-instagram-link"
        className="flex items-center justify-center gap-1.5 text-xs font-semibold text-[#319795] hover:text-[#1A365D] border border-[#319795]/30 hover:bg-[#319795]/5 rounded-md py-2 transition-colors"
      >
        <Instagram className="w-3.5 h-3.5" />
      </a>
      <a
        href={SOCIAL_LINKS.youtube}
        target="_blank"
        rel="noopener noreferrer"
        data-testid="editor-youtube-link"
        className="flex items-center justify-center gap-1.5 text-xs font-semibold text-[#FF0000] hover:text-white border border-[#FF0000]/30 hover:bg-[#FF0000] rounded-md py-2 transition-colors"
      >
        <Youtube className="w-3.5 h-3.5" />
      </a>
      <a
        href={SOCIAL_LINKS.whatsapp}
        target="_blank"
        rel="noopener noreferrer"
        data-testid="editor-whatsapp-link"
        className="flex items-center justify-center gap-1.5 text-xs font-semibold text-white bg-[#25D366] hover:bg-[#128C7E] rounded-md py-2 transition-colors"
      >
        <MessageCircle className="w-3.5 h-3.5" />
      </a>
    </div>
  </div>
);

const MostRead = () => {
  const [items, setItems] = useState([]);
  useEffect(() => {
    fetchMostRead(4).then(setItems).catch(() => setItems([]));
  }, []);
  if (!items.length) return null;
  return (
    <div data-testid="most-read-widget" className="bg-white border border-slate-200 rounded-xl p-6">
      <div className="flex items-center gap-2 mb-5">
        <TrendingUp className="w-4 h-4 text-[#319795]" />
        <h4 className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795]">Mais Lidos</h4>
      </div>
      <ol className="space-y-4">
        {items.map((a, idx) => {
          const meta = CATEGORY_META[a.category];
          return (
            <li key={a.id} data-testid={`most-read-item-${a.slug}`}>
              <Link to={`/artigo/${a.slug}`} className="flex gap-3 group">
                <span className="text-3xl font-bold text-slate-200 leading-none w-8 group-hover:text-[#319795] transition-colors">
                  0{idx + 1}
                </span>
                <div className="flex-1 min-w-0">
                  <span
                    className="inline-block text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full text-white mb-1"
                    style={{ backgroundColor: meta?.color || "#319795" }}
                  >
                    {meta?.label || a.category_label}
                  </span>
                  <p className="text-sm font-semibold text-[#1A365D] leading-snug group-hover:text-[#319795] line-clamp-2">
                    {a.title}
                  </p>
                </div>
              </Link>
            </li>
          );
        })}
      </ol>
    </div>
  );
};

const Newsletter = () => {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    if (!email.includes("@")) {
      toast.error("Informe um e-mail válido.");
      return;
    }
    setLoading(true);
    try {
      await subscribeNewsletter({ email });
      toast.success("Inscrição confirmada! Verifique sua caixa de entrada.");
      setEmail("");
    } catch (err) {
      const msg = err?.response?.data?.detail || "Erro ao cadastrar. Tente novamente.";
      toast.error(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      data-testid="newsletter-widget"
      className="rounded-xl p-6 border border-[#319795]/30 bg-gradient-to-br from-[#319795]/5 to-white"
    >
      <div className="w-11 h-11 rounded-xl bg-[#319795] flex items-center justify-center mb-4">
        <Mail className="w-5 h-5 text-white" />
      </div>
      <h4 className="text-lg font-bold text-[#1A365D] leading-snug">
        Receba conteúdos médicos no seu e-mail
      </h4>
      <p className="text-sm text-slate-600 mt-2">
        Um resumo semanal, sem spam, com os principais artigos publicados.
      </p>
      <form onSubmit={submit} className="mt-4 space-y-2">
        <Input
          data-testid="newsletter-email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="seu@email.com"
          required
          className="bg-white border-slate-200"
        />
        <Button
          type="submit"
          data-testid="newsletter-submit"
          disabled={loading}
          className="w-full bg-[#1A365D] hover:bg-[#319795] text-white font-semibold"
        >
          {loading ? "Inscrevendo…" : "Inscrever-se"}
        </Button>
      </form>
      <p className="text-[11px] text-slate-500 mt-3 leading-relaxed">
        Ao se inscrever, você concorda com nossa política de privacidade.
      </p>
    </div>
  );
};

export const Sidebar = () => (
  <aside className="space-y-6">
    <MostRead />
    <EditorWidget />
    <Newsletter />
  </aside>
);

export default Sidebar;

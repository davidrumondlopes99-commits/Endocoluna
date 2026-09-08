import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import { Award, BookOpen, TrendingUp, Instagram, MessageCircle, Youtube, Play, ExternalLink } from "lucide-react";
import { fetchMostRead, fetchYouTubeVideos, CATEGORY_META } from "../lib/api";
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
  const load = useCallback(() => fetchMostRead(4).then(setItems).catch(() => setItems([])), []);
  useEffect(() => {
    load();
  }, [load]);
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
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);

  const load = useCallback(
    () =>
      fetchYouTubeVideos(4)
        .then(setVideos)
        .catch(() => setVideos([]))
        .finally(() => setLoading(false)),
    []
  );
  useEffect(() => {
    load();
  }, [load]);

  return (
    <div
      data-testid="youtube-widget"
      className="rounded-xl p-6 border border-[#FF0000]/20 bg-gradient-to-br from-[#FF0000]/5 to-white"
    >
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-[#FF0000] flex items-center justify-center">
            <Youtube className="w-5 h-5 text-white" />
          </div>
          <div>
            <h4 className="text-sm font-bold text-[#1A365D] leading-tight">Vídeos em destaque</h4>
            <p className="text-[11px] text-slate-500">@drmatheuslopesneuro</p>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="space-y-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="aspect-video bg-slate-100 rounded-lg animate-pulse" />
          ))}
        </div>
      ) : videos.length === 0 ? (
        <p className="text-xs text-slate-500 py-4">Não foi possível carregar os vídeos no momento.</p>
      ) : (
        <ul className="space-y-3">
          {videos.map((v) => (
            <li key={v.id} data-testid={`youtube-video-${v.id}`}>
              <a
                href={v.url}
                target="_blank"
                rel="noopener noreferrer"
                className="group block"
              >
                <div className="relative aspect-video rounded-lg overflow-hidden bg-slate-200">
                  <img
                    src={v.thumbnail}
                    alt={v.title}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                    loading="lazy"
                  />
                  <div className="absolute inset-0 bg-black/30 group-hover:bg-black/10 transition-colors flex items-center justify-center">
                    <div className="w-11 h-11 rounded-full bg-[#FF0000]/95 flex items-center justify-center group-hover:scale-110 transition-transform">
                      <Play className="w-4 h-4 text-white fill-white ml-0.5" />
                    </div>
                  </div>
                </div>
                <p className="mt-2 text-xs font-semibold text-[#1A365D] leading-snug line-clamp-2 group-hover:text-[#FF0000] transition-colors">
                  {v.title}
                </p>
              </a>
            </li>
          ))}
        </ul>
      )}

      <a
        href={SOCIAL_LINKS.youtube}
        target="_blank"
        rel="noopener noreferrer"
        data-testid="youtube-subscribe-cta"
        className="mt-5 w-full inline-flex items-center justify-center gap-2 bg-[#FF0000] hover:bg-[#CC0000] text-white font-semibold text-sm px-4 py-2.5 rounded-md transition-colors"
      >
        <Youtube className="w-4 h-4" /> Inscrever-se no canal
        <ExternalLink className="w-3 h-3 opacity-80" />
      </a>
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

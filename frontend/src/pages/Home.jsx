import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ArrowRight, Clock, Calendar, ShieldCheck, BookOpen, Sparkles } from "lucide-react";
import { fetchArticles, fetchFeatured, CATEGORY_META, formatDate } from "../lib/api";
import { ArticleCard } from "../components/ArticleCard";
import { Sidebar } from "../components/Sidebar";

const Hero = ({ featured }) => {
  if (!featured) return null;
  const meta = CATEGORY_META[featured.category];
  return (
    <section
      data-testid="hero-section"
      className="bg-gradient-to-br from-white via-white to-[#319795]/5 border-b border-slate-200"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
        <div className="grid lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div className="lg:col-span-6 fade-up">
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-[#319795]/10 text-[#319795] text-xs font-bold uppercase tracking-wider mb-6">
              <Sparkles className="w-3.5 h-3.5" />
              Conteúdo científico acessível
            </div>
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-[#1A365D] leading-[1.05] tracking-tight">
              Informação médica que <span className="text-[#319795]">você entende</span> sobre cérebro e coluna.
            </h1>
            <p className="mt-6 text-base sm:text-lg text-slate-600 leading-relaxed max-w-xl">
              Artigos escritos e revisados por neurocirurgiões, com linguagem clara e baseada em evidências
              — para pacientes, familiares e curiosos pela ciência.
            </p>

            <div className="mt-8 flex flex-wrap items-center gap-4">
              <Link
                to={`/artigo/${featured.slug}`}
                data-testid="hero-featured-cta"
                className="inline-flex items-center gap-2 bg-[#1A365D] hover:bg-[#319795] text-white font-semibold px-6 py-3 rounded-full transition-colors"
              >
                Ler artigo em destaque <ArrowRight className="w-4 h-4" />
              </Link>
              <Link
                to="/categoria/spine"
                data-testid="hero-explore-link"
                className="inline-flex items-center gap-2 text-[#1A365D] font-semibold hover:text-[#319795] transition-colors"
              >
                Explorar categorias →
              </Link>
            </div>

            <div className="mt-10 grid grid-cols-3 gap-4 max-w-md">
              <div className="text-center">
                <div className="flex items-center justify-center text-[#319795] mb-1">
                  <ShieldCheck className="w-5 h-5" />
                </div>
                <div className="text-xs text-slate-500 leading-tight">Revisado por especialista</div>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center text-[#319795] mb-1">
                  <BookOpen className="w-5 h-5" />
                </div>
                <div className="text-xs text-slate-500 leading-tight">Linguagem acessível</div>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center text-[#319795] mb-1">
                  <Sparkles className="w-5 h-5" />
                </div>
                <div className="text-xs text-slate-500 leading-tight">Baseado em evidências</div>
              </div>
            </div>
          </div>

          <div className="lg:col-span-6 fade-up-delay-1">
            <Link to={`/artigo/${featured.slug}`} data-testid="hero-featured-card" className="block group">
              <div className="relative rounded-2xl overflow-hidden border border-slate-200 bg-white">
                <div className="aspect-[4/3] overflow-hidden">
                  <img
                    src={featured.image_url}
                    alt={featured.title}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                  />
                </div>
                <div className="absolute top-4 left-4">
                  <span
                    className="inline-flex items-center text-[11px] font-bold uppercase tracking-wider px-3 py-1.5 rounded-full text-white"
                    style={{ backgroundColor: meta?.color || "#319795" }}
                  >
                    Artigo em Destaque
                  </span>
                </div>
                <div className="p-6 lg:p-7">
                  <div className="flex items-center gap-4 text-xs text-slate-500 mb-3">
                    <span className="inline-flex items-center gap-1"><Calendar className="w-3.5 h-3.5" />{formatDate(featured.published_at)}</span>
                    <span className="inline-flex items-center gap-1"><Clock className="w-3.5 h-3.5" />{featured.reading_time} min</span>
                  </div>
                  <h2 className="text-xl lg:text-2xl font-bold text-[#1A365D] leading-tight group-hover:text-[#319795] transition-colors">
                    {featured.title}
                  </h2>
                  <p className="mt-3 text-sm text-slate-600 leading-relaxed line-clamp-3">{featured.excerpt}</p>
                </div>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default function Home() {
  const [articles, setArticles] = useState([]);
  const [featured, setFeatured] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([fetchArticles(), fetchFeatured()])
      .then(([list, feat]) => {
        setArticles(list);
        setFeatured(feat);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div data-testid="home-page">
      <Hero featured={featured} />

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-20">
        <div className="grid lg:grid-cols-12 gap-10">
          <div className="lg:col-span-8">
            <div className="flex items-end justify-between mb-8">
              <div>
                <div className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-2">
                  Publicações Recentes
                </div>
                <h2 className="text-3xl sm:text-4xl font-bold text-[#1A365D] tracking-tight">
                  Últimos Artigos
                </h2>
              </div>
              <Link
                to="/categoria/spine"
                data-testid="see-all-articles-link"
                className="hidden sm:inline-flex items-center gap-1 text-sm font-semibold text-[#319795] hover:text-[#1A365D]"
              >
                Ver todos →
              </Link>
            </div>

            {loading ? (
              <div className="grid sm:grid-cols-2 gap-6">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="bg-white border border-slate-200 rounded-xl h-96 animate-pulse" />
                ))}
              </div>
            ) : (
              <div className="grid sm:grid-cols-2 gap-6" data-testid="articles-grid">
                {articles.map((a, idx) => (
                  <ArticleCard key={a.id} article={a} index={idx} />
                ))}
              </div>
            )}
          </div>

          <div className="lg:col-span-4">
            <Sidebar />
          </div>
        </div>
      </section>
    </div>
  );
}

import { useEffect, useState, useMemo } from "react";
import { useParams, useSearchParams, Link } from "react-router-dom";
import { fetchArticles, CATEGORY_META } from "../lib/api";
import { ArticleCard } from "../components/ArticleCard";
import { Sidebar } from "../components/Sidebar";
import { SEO } from "../components/SEO";

const META = {
  brain: {
    title: "Cérebro & Neurocirurgia",
    desc: "Aneurismas, AVC, tumores cerebrais, dores de cabeça e tudo o que envolve o sistema nervoso central.",
  },
  spine: {
    title: "Coluna Vertebral",
    desc: "Hérnia de disco, estenose, dor lombar, escoliose e cirurgia minimamente invasiva de coluna.",
  },
  prevention: {
    title: "Prevenção & Bem-estar",
    desc: "Postura, ergonomia, exercícios e estratégias para preservar a saúde da sua coluna e do seu cérebro.",
  },
};

export default function Category({ searchMode = false }) {
  const { slug } = useParams();
  const [params] = useSearchParams();
  const q = params.get("q") || "";
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [visibleCount, setVisibleCount] = useState(12);

  useEffect(() => {
    setLoading(true);
    setVisibleCount(12);
    const filters = searchMode ? { q, limit: 100 } : { category: slug, limit: 100 };
    fetchArticles(filters)
      .then(setArticles)
      .finally(() => setLoading(false));
  }, [slug, q, searchMode]);

  const meta = useMemo(() => META[slug] || {
    title: searchMode ? `Resultados para "${q}"` : "Categoria",
    desc: searchMode ? "Artigos encontrados com base na sua busca." : "",
  }, [slug, searchMode, q]);
  const cmeta = CATEGORY_META[slug];

  return (
    <div data-testid={searchMode ? "search-page" : `category-page-${slug}`}>
      <SEO
        title={meta.title}
        description={meta.desc || `Artigos sobre ${meta.title.toLowerCase()} no NeuroSaúde, blog médico do Dr. Matheus Lopes.`}
        noindex={searchMode}
      />
      <section className="bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
          {!searchMode && cmeta && (
            <span
              className="inline-block text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-full text-white mb-4"
              style={{ backgroundColor: cmeta.color }}
            >
              {cmeta.label}
            </span>
          )}
          <h1 className="text-4xl sm:text-5xl font-extrabold text-[#1A365D] tracking-tight">{meta.title}</h1>
          <p className="mt-3 text-base sm:text-lg text-slate-600 max-w-3xl">{meta.desc}</p>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid lg:grid-cols-12 gap-10">
          <div className="lg:col-span-8">
            {loading ? (
              <div className="grid sm:grid-cols-2 gap-6">
                {[1, 2].map((i) => (
                  <div key={i} className="bg-white border border-slate-200 rounded-xl h-96 animate-pulse" />
                ))}
              </div>
            ) : articles.length === 0 ? (
              <div className="bg-white border border-slate-200 rounded-xl p-12 text-center" data-testid="empty-state">
                <h3 className="text-xl font-bold text-[#1A365D] mb-2">Nenhum artigo encontrado</h3>
                <p className="text-slate-600">Tente outra categoria ou volte para a home.</p>
                <Link to="/" className="inline-block mt-4 text-[#319795] font-semibold">← Voltar à home</Link>
              </div>
            ) : (
              <>
                <div className="grid sm:grid-cols-2 gap-6">
                  {articles.slice(0, visibleCount).map((a, i) => (
                    <ArticleCard key={a.id} article={a} index={i} />
                  ))}
                </div>
                {visibleCount < articles.length && (
                  <div className="flex justify-center mt-10">
                    <button
                      onClick={() => setVisibleCount((c) => c + 12)}
                      data-testid="load-more-category"
                      className="inline-flex items-center gap-2 bg-[#1A365D] hover:bg-[#319795] text-white font-semibold px-7 py-3 rounded-full transition-colors"
                    >
                      Ver mais artigos
                      <span className="text-xs opacity-80">({articles.length - visibleCount} restantes)</span>
                    </button>
                  </div>
                )}
              </>
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

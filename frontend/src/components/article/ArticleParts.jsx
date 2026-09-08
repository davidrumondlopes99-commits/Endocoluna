import { useCallback } from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet-async";
import { Share2 } from "lucide-react";

export const ArticleSchemas = ({ breadcrumbSchema, faqSchema }) => {
  if (!breadcrumbSchema && !faqSchema) return null;
  return (
    <Helmet>
      {breadcrumbSchema && <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>}
      {faqSchema && <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>}
    </Helmet>
  );
};

export const ArticleToc = ({ toc }) => {
  if (!toc.length) return null;
  return (
    <nav data-testid="article-toc" className="bg-[#319795]/5 border border-[#319795]/20 rounded-xl p-5 mb-10">
      <h3 className="text-xs font-bold uppercase tracking-[0.18em] text-[#319795] mb-3">Índice do artigo</h3>
      <ol className="space-y-1.5">
        {toc.map((item, i) => (
          <li key={item.id}>
            <a href={`#${item.id}`} className="text-sm text-[#1A365D] hover:text-[#319795] font-medium">
              {i + 1}. {item.text}
            </a>
          </li>
        ))}
      </ol>
    </nav>
  );
};

export const ArticleFooter = ({ category, label }) => {
  const handleShare = useCallback(() => {
    navigator.clipboard?.writeText(window.location.href);
  }, []);

  return (
    <div className="mt-12 pt-8 border-t border-slate-200 flex items-center justify-between">
      <Link to={`/categoria/${category}`} className="text-sm font-semibold text-[#319795] hover:text-[#1A365D]">
        ← Mais artigos em {label}
      </Link>
      <button
        onClick={handleShare}
        data-testid="share-button"
        className="inline-flex items-center gap-2 text-sm font-semibold text-[#1A365D] hover:text-[#319795]"
      >
        <Share2 className="w-4 h-4" /> Compartilhar
      </button>
    </div>
  );
};

export const ArticleSkeleton = () => (
  <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div className="animate-pulse space-y-4">
      <div className="h-8 w-1/3 bg-slate-200 rounded" />
      <div className="h-72 w-full bg-slate-200 rounded-xl" />
      <div className="h-4 w-full bg-slate-200 rounded" />
      <div className="h-4 w-2/3 bg-slate-200 rounded" />
    </div>
  </div>
);

export const ArticleNotFound = () => (
  <div className="max-w-3xl mx-auto px-4 py-24 text-center" data-testid="article-not-found">
    <h2 className="text-3xl font-bold text-[#1A365D] mb-3">Artigo não encontrado</h2>
    <p className="text-slate-600">O artigo solicitado não está disponível.</p>
    <Link to="/" className="inline-block mt-6 text-[#319795] font-semibold">← Voltar à home</Link>
  </div>
);

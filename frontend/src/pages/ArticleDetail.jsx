import { useEffect, useState, useMemo } from "react";
import { useParams, Link } from "react-router-dom";
import { Clock, Calendar, ChevronRight, ArrowLeft, Share2 } from "lucide-react";
import { fetchArticle, CATEGORY_META, formatDate } from "../lib/api";
import { Sidebar } from "../components/Sidebar";
import { SEO } from "../components/SEO";

export default function ArticleDetail() {
  const { slug } = useParams();
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    setLoading(true);
    setError(false);
    fetchArticle(slug)
      .then(setArticle)
      .catch(() => setError(true))
      .finally(() => setLoading(false));
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [slug]);

  const toc = useMemo(() => {
    if (!article?.content_html) return [];
    const parser = new DOMParser();
    const doc = parser.parseFromString(article.content_html, "text/html");
    return Array.from(doc.querySelectorAll("h2")).map((h, i) => ({
      id: `sec-${i}`,
      text: h.textContent,
    }));
  }, [article]);

  const contentWithIds = useMemo(() => {
    if (!article?.content_html) return "";
    let i = 0;
    return article.content_html.replace(/<h2>/g, () => `<h2 id="sec-${i++}">`);
  }, [article]);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="animate-pulse space-y-4">
          <div className="h-8 w-1/3 bg-slate-200 rounded" />
          <div className="h-72 w-full bg-slate-200 rounded-xl" />
          <div className="h-4 w-full bg-slate-200 rounded" />
          <div className="h-4 w-2/3 bg-slate-200 rounded" />
        </div>
      </div>
    );
  }

  if (error || !article) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-24 text-center" data-testid="article-not-found">
        <h2 className="text-3xl font-bold text-[#1A365D] mb-3">Artigo não encontrado</h2>
        <p className="text-slate-600">O artigo solicitado não está disponível.</p>
        <Link to="/" className="inline-block mt-6 text-[#319795] font-semibold">← Voltar à home</Link>
      </div>
    );
  }

  const meta = CATEGORY_META[article.category];

  return (
    <div data-testid="article-detail-page">
      <SEO
        title={article.title}
        description={article.excerpt}
        image={article.image_url}
        type="article"
        article={article}
      />
      {/* Breadcrumb */}
      <div className="bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center gap-2 text-xs text-slate-500">
          <Link to="/" className="hover:text-[#319795]" data-testid="breadcrumb-home">Home</Link>
          <ChevronRight className="w-3.5 h-3.5" />
          <Link to={`/categoria/${article.category}`} className="hover:text-[#319795]" data-testid="breadcrumb-category">
            {meta?.label || article.category_label}
          </Link>
          <ChevronRight className="w-3.5 h-3.5" />
          <span className="truncate text-slate-400">{article.title}</span>
        </div>
      </div>

      {/* Header */}
      <header className="bg-white border-b border-slate-200">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
          <Link to={`/categoria/${article.category}`} className="inline-flex items-center gap-1.5 text-sm font-semibold text-[#319795] hover:text-[#1A365D] mb-4">
            <ArrowLeft className="w-4 h-4" /> {meta?.label || article.category_label}
          </Link>
          <span
            className="inline-block text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-full text-white mb-5"
            style={{ backgroundColor: meta?.color || "#319795" }}
          >
            {meta?.label || article.category_label}
          </span>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#1A365D] leading-[1.1] tracking-tight">
            {article.title}
          </h1>
          <p className="mt-5 text-lg text-slate-600 leading-relaxed max-w-3xl">{article.excerpt}</p>

          <div className="mt-8 flex flex-wrap items-center gap-5 text-sm text-slate-500 border-t border-slate-100 pt-6">
            <div className="flex items-center gap-2">
              <img
                src="https://customer-assets.emergentagent.com/job_neuroeduca/artifacts/idhvttqs_640431106_18364933696205942_4601043174928282564_n.jpg"
                alt={article.author}
                className="w-9 h-9 rounded-full object-cover border border-slate-200"
              />
              <span><span className="text-slate-400">Por</span> <strong className="text-[#1A365D]">{article.author}</strong></span>
            </div>
            <span className="inline-flex items-center gap-1.5"><Calendar className="w-4 h-4" />{formatDate(article.published_at)}</span>
            <span className="inline-flex items-center gap-1.5"><Clock className="w-4 h-4" />{article.reading_time} min de leitura</span>
          </div>
        </div>
      </header>

      {/* Hero image */}
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 -mt-2">
        <div className="aspect-[16/8] rounded-2xl overflow-hidden border border-slate-200">
          <img src={article.image_url} alt={article.title} className="w-full h-full object-cover" />
        </div>
      </div>

      {/* Body */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid lg:grid-cols-12 gap-12">
          <div className="lg:col-span-8">
            {/* TOC */}
            {toc.length > 0 && (
              <nav data-testid="article-toc" className="bg-[#319795]/5 border border-[#319795]/20 rounded-xl p-5 mb-10">
                <h3 className="text-xs font-bold uppercase tracking-[0.18em] text-[#319795] mb-3">Índice do artigo</h3>
                <ol className="space-y-1.5">
                  {toc.map((item, i) => (
                    <li key={item.id}>
                      <a
                        href={`#${item.id}`}
                        className="text-sm text-[#1A365D] hover:text-[#319795] font-medium"
                      >
                        {i + 1}. {item.text}
                      </a>
                    </li>
                  ))}
                </ol>
              </nav>
            )}

            <article
              data-testid="article-content"
              className="prose-article"
              dangerouslySetInnerHTML={{ __html: contentWithIds }}
            />

            <div className="mt-12 pt-8 border-t border-slate-200 flex items-center justify-between">
              <Link to={`/categoria/${article.category}`} className="text-sm font-semibold text-[#319795] hover:text-[#1A365D]">
                ← Mais artigos em {meta?.label}
              </Link>
              <button
                onClick={() => {
                  navigator.clipboard?.writeText(window.location.href);
                }}
                data-testid="share-button"
                className="inline-flex items-center gap-2 text-sm font-semibold text-[#1A365D] hover:text-[#319795]"
              >
                <Share2 className="w-4 h-4" /> Compartilhar
              </button>
            </div>
          </div>

          <div className="lg:col-span-4">
            <Sidebar />
          </div>
        </div>
      </section>
    </div>
  );
}

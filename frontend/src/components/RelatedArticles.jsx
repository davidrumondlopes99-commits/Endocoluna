import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import { ArrowRight, Clock } from "lucide-react";
import { fetchRelatedArticles, CATEGORY_META, formatDate } from "../lib/api";

export const RelatedArticles = ({ slug, category }) => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  const load = useCallback(() => {
    if (!slug) return;
    setLoading(true);
    fetchRelatedArticles(slug, 4)
      .then(setItems)
      .catch(() => setItems([]))
      .finally(() => setLoading(false));
  }, [slug]);

  useEffect(() => {
    load();
  }, [load]);

  if (!loading && items.length === 0) return null;

  const cmeta = CATEGORY_META[category];

  return (
    <section
      data-testid="related-articles"
      className="mt-12 pt-10 border-t border-slate-200"
    >
      <div className="flex items-end justify-between mb-6">
        <div>
          <div className="text-xs uppercase tracking-[0.18em] font-bold text-[#319795] mb-1.5">
            Continue lendo
          </div>
          <h3 className="text-2xl sm:text-3xl font-bold text-[#1A365D] tracking-tight">
            Artigos relacionados em {cmeta?.label || ""}
          </h3>
        </div>
        {category && (
          <Link
            to={`/categoria/${category}`}
            data-testid="related-see-all"
            className="hidden sm:inline-flex items-center gap-1 text-sm font-semibold text-[#319795] hover:text-[#1A365D]"
          >
            Ver todos →
          </Link>
        )}
      </div>

      {loading ? (
        <div className="grid sm:grid-cols-2 gap-4">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="bg-white border border-slate-200 rounded-xl h-32 animate-pulse" />
          ))}
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 gap-4">
          {items.map((a) => (
            <Link
              key={a.id}
              to={`/artigo/${a.slug}`}
              data-testid={`related-article-${a.slug}`}
              className="flex gap-4 bg-white border border-slate-200 hover:border-[#319795] rounded-xl p-3 transition-colors group"
            >
              <div className="w-24 h-24 flex-shrink-0 rounded-lg overflow-hidden bg-slate-100">
                <img
                  src={a.image_url}
                  alt={a.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                  loading="lazy"
                />
              </div>
              <div className="flex-1 min-w-0 flex flex-col justify-between py-1">
                <div>
                  <span
                    className="inline-block text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full text-white mb-1.5"
                    style={{ backgroundColor: CATEGORY_META[a.category]?.color || "#319795" }}
                  >
                    {CATEGORY_META[a.category]?.label || a.category_label}
                  </span>
                  <h4 className="text-sm font-semibold text-[#1A365D] leading-snug group-hover:text-[#319795] line-clamp-2">
                    {a.title}
                  </h4>
                </div>
                <div className="flex items-center gap-3 text-[11px] text-slate-500 mt-2">
                  <span className="inline-flex items-center gap-1">
                    <Clock className="w-3 h-3" /> {a.reading_time} min
                  </span>
                  <span>{formatDate(a.published_at)}</span>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </section>
  );
};

export default RelatedArticles;

import { Link } from "react-router-dom";
import { Clock, Calendar } from "lucide-react";
import { CATEGORY_META, formatDate } from "../lib/api";

export const ArticleCard = ({ article, index = 0 }) => {
  const meta = CATEGORY_META[article.category] || { label: article.category_label, color: "#319795" };
  return (
    <article
      data-testid={`article-card-${article.slug}`}
      className={`article-card-hover bg-white border border-slate-200 rounded-xl overflow-hidden flex flex-col fade-up-delay-${Math.min(index + 1, 3)}`}
    >
      <Link to={`/artigo/${article.slug}`} className="block">
        <div className="aspect-[16/10] overflow-hidden bg-slate-100">
          <img
            src={article.image_url}
            alt={article.title}
            className="w-full h-full object-cover hover:scale-105 transition-transform duration-500"
            loading="lazy"
          />
        </div>
      </Link>
      <div className="p-6 flex flex-col flex-1">
        <div className="flex items-center gap-3 mb-3">
          <span
            data-testid={`category-badge-${article.category}`}
            className="inline-flex items-center text-[11px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full text-white"
            style={{ backgroundColor: meta.color }}
          >
            {meta.label}
          </span>
          <span className="inline-flex items-center gap-1 text-xs text-slate-500">
            <Clock className="w-3.5 h-3.5" />
            {article.reading_time} min de leitura
          </span>
        </div>
        <Link to={`/artigo/${article.slug}`}>
          <h3 className="text-lg md:text-xl font-bold text-[#1A365D] leading-snug hover:text-[#319795] transition-colors line-clamp-3">
            {article.title}
          </h3>
        </Link>
        <p className="mt-3 text-sm text-slate-600 leading-relaxed line-clamp-3 flex-1">
          {article.excerpt}
        </p>
        <div className="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <span className="inline-flex items-center gap-1.5">
            <Calendar className="w-3.5 h-3.5" />
            {formatDate(article.published_at)}
          </span>
          <Link
            to={`/artigo/${article.slug}`}
            data-testid={`read-more-${article.slug}`}
            className="font-semibold text-[#319795] hover:text-[#1A365D]"
          >
            Ler artigo →
          </Link>
        </div>
      </div>
    </article>
  );
};

export default ArticleCard;

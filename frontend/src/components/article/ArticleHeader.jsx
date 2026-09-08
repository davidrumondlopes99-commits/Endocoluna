import { Link } from "react-router-dom";
import { Clock, Calendar, ChevronRight, ArrowLeft } from "lucide-react";
import { formatDate } from "../../lib/api";

const AUTHOR_PHOTO = "https://customer-assets.emergentagent.com/job_neuroeduca/artifacts/ec65g3l5_617A9485.JPG";

export const ArticleBreadcrumb = ({ article, label }) => (
  <div className="bg-white border-b border-slate-200">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center gap-2 text-xs text-slate-500">
      <Link to="/" className="hover:text-[#319795]" data-testid="breadcrumb-home">Home</Link>
      <ChevronRight className="w-3.5 h-3.5" />
      <Link to={`/categoria/${article.category}`} className="hover:text-[#319795]" data-testid="breadcrumb-category">
        {label}
      </Link>
      <ChevronRight className="w-3.5 h-3.5" />
      <span className="truncate text-slate-400">{article.title}</span>
    </div>
  </div>
);

export const ArticleHeader = ({ article, label, color }) => (
  <header className="bg-white border-b border-slate-200">
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
      <Link to={`/categoria/${article.category}`} className="inline-flex items-center gap-1.5 text-sm font-semibold text-[#319795] hover:text-[#1A365D] mb-4">
        <ArrowLeft className="w-4 h-4" /> {label}
      </Link>
      <span
        className="inline-block text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-full text-white mb-5"
        style={{ backgroundColor: color }}
      >
        {label}
      </span>
      <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#1A365D] leading-[1.1] tracking-tight">
        {article.title}
      </h1>
      <p className="mt-5 text-lg text-slate-600 leading-relaxed max-w-3xl">{article.excerpt}</p>

      <div className="mt-8 flex flex-wrap items-center gap-5 text-sm text-slate-500 border-t border-slate-100 pt-6">
        <div className="flex items-center gap-2">
          <img src={AUTHOR_PHOTO} alt={article.author} className="w-9 h-9 rounded-full object-cover border border-slate-200" />
          <span><span className="text-slate-400">Por</span> <strong className="text-[#1A365D]">{article.author}</strong></span>
        </div>
        <span className="inline-flex items-center gap-1.5"><Calendar className="w-4 h-4" />{formatDate(article.published_at)}</span>
        <span className="inline-flex items-center gap-1.5"><Clock className="w-4 h-4" />{article.reading_time} min de leitura</span>
      </div>
    </div>
  </header>
);

export const ArticleHeroImage = ({ article }) => (
  <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 -mt-2">
    <div className="aspect-[16/8] rounded-2xl overflow-hidden border border-slate-200">
      <img src={article.image_url} alt={article.title} className="w-full h-full object-cover" />
    </div>
  </div>
);

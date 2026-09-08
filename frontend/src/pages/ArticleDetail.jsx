import { useEffect, useState, useMemo, useCallback } from "react";
import { useParams } from "react-router-dom";
import { fetchArticle, CATEGORY_META } from "../lib/api";
import { Sidebar } from "../components/Sidebar";
import { SEO } from "../components/SEO";
import { ArticleVideo } from "../components/ArticleVideo";
import { RelatedArticles } from "../components/RelatedArticles";
import { ArticleBreadcrumb, ArticleHeader, ArticleHeroImage } from "../components/article/ArticleHeader";
import { ArticleSchemas, ArticleToc, ArticleFooter, ArticleSkeleton, ArticleNotFound } from "../components/article/ArticleParts";
import { getRelatedVideo } from "../lib/youtubeMap";
import { buildToc, sanitizeContent, buildFaqSchema, buildBreadcrumbSchema } from "../lib/articleSchema";

const useArticle = (slug) => {
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    setError(false);
    try {
      setArticle(await fetchArticle(slug));
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [slug]);

  useEffect(() => {
    load();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [load]);

  return { article, loading, error };
};

export default function ArticleDetail() {
  const { slug } = useParams();
  const { article, loading, error } = useArticle(slug);
  const html = article?.content_html;

  const toc = useMemo(() => buildToc(html), [html]);
  const contentHtml = useMemo(() => ({ __html: sanitizeContent(html) }), [html]);
  const faqSchema = useMemo(() => buildFaqSchema(html), [html]);
  const breadcrumbSchema = useMemo(() => buildBreadcrumbSchema(article), [article]);
  const relatedVideo = useMemo(
    () => (article ? getRelatedVideo({ slug: article.slug, title: article.title, category: article.category_label }) : null),
    [article]
  );

  if (loading) return <ArticleSkeleton />;
  if (error || !article) return <ArticleNotFound />;

  const meta = CATEGORY_META[article.category];
  const label = meta?.label || article.category_label;
  const color = meta?.color || "#319795";

  return (
    <div data-testid="article-detail-page">
      <SEO title={article.title} description={article.excerpt} image={article.image_url} type="article" article={article} />
      <ArticleSchemas breadcrumbSchema={breadcrumbSchema} faqSchema={faqSchema} />
      <ArticleBreadcrumb article={article} label={label} />
      <ArticleHeader article={article} label={label} color={color} />
      <ArticleHeroImage article={article} />

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid lg:grid-cols-12 gap-12">
          <div className="lg:col-span-8">
            <ArticleToc toc={toc} />
            <article data-testid="article-content" className="prose-article" dangerouslySetInnerHTML={contentHtml} />
            <ArticleVideo video={relatedVideo} />
            <RelatedArticles slug={article.slug} category={article.category} />
            <ArticleFooter category={article.category} label={label} />
          </div>
          <div className="lg:col-span-4">
            <Sidebar />
          </div>
        </div>
      </section>
    </div>
  );
}

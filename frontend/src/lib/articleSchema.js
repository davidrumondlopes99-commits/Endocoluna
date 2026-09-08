import DOMPurify from "dompurify";

// Allowlist for article HTML: keeps the tags actually used in articles + id anchors for TOC
const SANITIZE_CONFIG = {
  ALLOWED_TAGS: ["p", "h2", "h3", "h4", "ul", "ol", "li", "strong", "em", "b", "i", "br", "a", "blockquote"],
  ALLOWED_ATTR: ["id", "href", "title", "target", "rel"],
};

const parseHtml = (html) => new DOMParser().parseFromString(html, "text/html");

export const buildToc = (html) => {
  if (!html) return [];
  return Array.from(parseHtml(html).querySelectorAll("h2")).map((h, i) => ({
    id: `sec-${i}`,
    text: h.textContent,
  }));
};

export const sanitizeContent = (html) => {
  if (!html) return "";
  let i = 0;
  const withIds = html.replace(/<h2>/g, () => `<h2 id="sec-${i++}">`);
  return DOMPurify.sanitize(withIds, SANITIZE_CONFIG);
};

const firstParagraphAfter = (el) => {
  let sibling = el.nextElementSibling;
  while (sibling && sibling.tagName !== "P") sibling = sibling.nextElementSibling;
  return sibling ? (sibling.textContent || "").trim() : "";
};

export const buildFaqSchema = (html) => {
  if (!html) return null;
  const faqs = Array.from(parseHtml(html).querySelectorAll("h2"))
    .map((h2) => ({ question: (h2.textContent || "").trim(), answer: firstParagraphAfter(h2) }))
    .filter(({ question, answer }) => question && answer.length > 30)
    .map(({ question, answer }) => ({
      "@type": "Question",
      name: question,
      acceptedAnswer: { "@type": "Answer", text: answer },
    }));
  if (faqs.length < 2) return null;
  return { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: faqs };
};

export const buildBreadcrumbSchema = (article) => {
  if (!article || typeof window === "undefined") return null;
  const origin = window.location.origin;
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: [
      { "@type": "ListItem", position: 1, name: "Home", item: `${origin}/` },
      { "@type": "ListItem", position: 2, name: article.category_label, item: `${origin}/categoria/${article.category}` },
      { "@type": "ListItem", position: 3, name: article.title, item: window.location.href },
    ],
  };
};

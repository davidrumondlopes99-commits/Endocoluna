import { Helmet } from "react-helmet-async";

const SITE_NAME = "EndoColuna Brasil";
const DEFAULT_DESC =
  "Blog médico especializado em Neurocirurgia e Cirurgia de Coluna. Conteúdo educacional baseado em evidências, escrito por Dr. Matheus Lopes (CRM/SP 147238).";
const DEFAULT_IMAGE =
  "https://static.prod-images.emergentagent.com/jobs/11721837-3a81-4cef-8d93-7d18b3b33d31/images/82ba2b39d6ef16938189865504baf2209e615eabc1a3c89c7102af011648bfdc.png";

export const SEO = ({
  title,
  description = DEFAULT_DESC,
  image = DEFAULT_IMAGE,
  type = "website",
  article = null,
  noindex = false,
}) => {
  const fullTitle = title ? `${title} | ${SITE_NAME}` : `${SITE_NAME} — Blog de Neurocirurgia e Cirurgia de Coluna`;
  const url = typeof window !== "undefined" ? window.location.href : "";
  const canonical = typeof window !== "undefined" ? window.location.origin + window.location.pathname : "";

  return (
    <Helmet>
      <title>{fullTitle}</title>
      <meta name="description" content={description} />
      {noindex && <meta name="robots" content="noindex,nofollow" />}
      <link rel="canonical" href={canonical} />

      {/* Open Graph */}
      <meta property="og:type" content={type} />
      <meta property="og:title" content={fullTitle} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content={image} />
      <meta property="og:url" content={url} />
      <meta property="og:site_name" content={SITE_NAME} />
      <meta property="og:locale" content="pt_BR" />

      {/* Twitter */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={fullTitle} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={image} />

      {/* Article-specific Open Graph */}
      {article && (
        <>
          <meta property="article:author" content={article.author} />
          <meta property="article:published_time" content={article.published_at} />
          <meta property="article:section" content={article.category_label} />
        </>
      )}

      {/* JSON-LD structured data */}
      {article ? (
        <script type="application/ld+json">
          {JSON.stringify({
            "@context": "https://schema.org",
            "@type": "MedicalWebPage",
            mainEntityOfPage: { "@type": "WebPage", "@id": url },
            headline: title,
            description,
            image,
            datePublished: article.published_at,
            dateModified: article.published_at,
            author: {
              "@type": "Person",
              name: article.author,
              jobTitle: "Neurocirurgião",
              identifier: "CRM/SP 147238",
            },
            publisher: {
              "@type": "Organization",
              name: SITE_NAME,
              logo: {
                "@type": "ImageObject",
                url: image,
              },
            },
            about: {
              "@type": "MedicalCondition",
              name: article.category_label,
            },
            inLanguage: "pt-BR",
          })}
        </script>
      ) : (
        <script type="application/ld+json">
          {JSON.stringify({
            "@context": "https://schema.org",
            "@type": "MedicalOrganization",
            name: SITE_NAME,
            description: DEFAULT_DESC,
            url: typeof window !== "undefined" ? window.location.origin : "",
            medicalSpecialty: ["Neurosurgery", "SpineSurgery"],
            employee: {
              "@type": "Physician",
              name: "Dr. Matheus Lopes",
              identifier: "CRM/SP 147238",
              medicalSpecialty: ["Neurosurgery", "SpineSurgery"],
            },
          })}
        </script>
      )}
    </Helmet>
  );
};

export default SEO;

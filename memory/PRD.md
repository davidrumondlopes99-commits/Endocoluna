# NeuroSaúde – Blog de Neurocirurgia e Cirurgia de Coluna

## Problem Statement (original)
Create a modern, clean, multi-page blog application in Brazilian Portuguese, specialized in Neurosurgery and Spine Surgery, designed to attract organic search traffic. Header with Categories dropdown (Brain/Spine/Prevention), About link, and Search. Hero with featured article. Article grid with cards. Sidebar with Most Read, Editor widget, and Newsletter signup. Footer with educational disclaimer and social links. Palette: Deep Navy (#1A365D), Soft Teal (#319795), light gray (#F7FAFC). Typography: Montserrat/Inter. Three long-form articles (1500+ words each) on Hérnia de Disco, Aneurisma Cerebral, and Dor nas Costas (Red Flags).

## User Personas
- Pacientes e familiares buscando explicações claras sobre diagnósticos neurocirúrgicos.
- Profissionais de saúde em formação procurando referência didática.
- Público geral pesquisando sintomas (tráfego orgânico via SEO).

## Architecture
- **Backend**: FastAPI + Motor (MongoDB), endpoints sob `/api`. Seed automático de 3 artigos na inicialização.
- **Frontend**: React 19 + react-router-dom v7, Tailwind + Shadcn/UI, Lucide-React, Sonner para toasts. Tipografia Montserrat (UI) + Lora (corpo dos artigos).
- **Rotas**: `/`, `/artigo/:slug`, `/categoria/:slug`, `/buscar`, `/sobre`.

## What's been implemented (2026-05-23 / MVP)
- Backend API: list/featured/most-read/detail/categories/newsletter (com duplicate 409 e validação de email).
- Seed automático de 3 artigos PT-BR (~1500-1800 palavras cada) com HTML estruturado.
- Frontend: Header sticky com dropdown de categorias, busca, mobile menu; Footer navy com disclaimer médico e links sociais.
- Home com Hero + Grid + Sidebar (Most Read, Editor, Newsletter).
- Página de artigo com índice (TOC) gerado a partir dos H2s, breadcrumb, share button, prose tipografada (Lora).
- Página de categoria e de busca (rota /buscar).
- Página About com bio do editor e valores editoriais.
- Toast notifications (sonner) na assinatura da newsletter.
- 100% dos testes backend e frontend passaram (iteração 1).

## Core Requirements (static)
- Conteúdo SEMPRE em Brasileiro Português.
- Estilo editorial (blog) — não SaaS landing.
- Disclaimer médico em todas as páginas (footer).
- Acessibilidade: WCAG AA (navy + teal contraste OK), data-testid em todos os elementos interativos.

## Prioritized Backlog
### P1
- CMS leve no admin (proteger com auth) para criar/editar artigos sem deploy.
- Página de artigo: leitor de progresso (scroll bar) + estimativa de leitura dinâmica.
- SEO: meta tags dinâmicas (react-helmet), sitemap.xml, schema.org Article JSON-LD.
- Suporte a comentários (Disqus ou nativo com moderação).

### P2
- Newsletter real (integração com Resend/SendGrid).
- Página de busca com filtros (categoria + ordenação).
- Compartilhamento social com OG tags por artigo.
- Modo escuro opcional (light/dark theme switch).
- Mais artigos (objetivo: 20+ artigos por categoria para SEO).

### P3
- Analytics (Google Analytics 4 / Plausible).
- Banner de cookies / LGPD.
- Sistema de tags secundárias (além de categoria).

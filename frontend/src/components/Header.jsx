import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Search, Brain, Activity, Shield, Menu, X } from "lucide-react";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "./ui/dropdown-menu";

const categories = [
  { slug: "brain", label: "Cérebro", icon: Brain, desc: "Neurocirurgia e doenças do encéfalo" },
  { slug: "spine", label: "Coluna", icon: Activity, desc: "Cirurgia de coluna e patologias vertebrais" },
  { slug: "prevention", label: "Prevenção", icon: Shield, desc: "Saúde, ergonomia e bem-estar" },
];

export const Header = () => {
  const navigate = useNavigate();
  const [query, setQuery] = useState("");
  const [mobileOpen, setMobileOpen] = useState(false);

  const onSearch = (e) => {
    e.preventDefault();
    const q = query.trim();
    if (!q) return;
    navigate(`/buscar?q=${encodeURIComponent(q)}`);
    setMobileOpen(false);
  };

  return (
    <header
      data-testid="site-header"
      className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          <Link to="/" data-testid="logo-link" className="flex items-center gap-2.5 group">
            <div className="w-10 h-10 rounded-xl bg-[#1A365D] flex items-center justify-center group-hover:bg-[#319795] transition-colors">
              <Brain className="w-5 h-5 text-white" />
            </div>
            <div className="leading-tight">
              <div className="font-bold text-[#1A365D] text-xl tracking-tight">NeuroSaúde</div>
              <div className="text-[11px] uppercase tracking-[0.18em] text-[#319795] font-semibold">Blog Médico</div>
            </div>
          </Link>

          <nav className="hidden lg:flex items-center gap-1">
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <button
                  data-testid="nav-categories-trigger"
                  className="px-4 py-2 text-sm font-semibold text-[#1A365D] hover:text-[#319795] transition-colors rounded-md"
                >
                  Categorias
                </button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="start" className="w-72">
                <DropdownMenuLabel className="text-[#1A365D]">Áreas de Conhecimento</DropdownMenuLabel>
                <DropdownMenuSeparator />
                {categories.map((c) => {
                  const Icon = c.icon;
                  return (
                    <DropdownMenuItem
                      key={c.slug}
                      data-testid={`nav-category-${c.slug}`}
                      onClick={() => navigate(`/categoria/${c.slug}`)}
                      className="flex items-start gap-3 py-3 cursor-pointer"
                    >
                      <Icon className="w-5 h-5 text-[#319795] mt-0.5" />
                      <div>
                        <div className="font-semibold text-[#1A365D]">{c.label}</div>
                        <div className="text-xs text-slate-500">{c.desc}</div>
                      </div>
                    </DropdownMenuItem>
                  );
                })}
              </DropdownMenuContent>
            </DropdownMenu>

            <Link
              to="/sobre"
              data-testid="nav-about-link"
              className="px-4 py-2 text-sm font-semibold text-[#1A365D] hover:text-[#319795] transition-colors rounded-md"
            >
              Sobre o Blog
            </Link>
          </nav>

          <form onSubmit={onSearch} className="hidden md:flex items-center gap-2" data-testid="search-form">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
              <Input
                data-testid="search-input"
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Buscar artigos…"
                className="pl-9 w-56 lg:w-72 bg-slate-50 border-slate-200 focus-visible:ring-[#319795]"
              />
            </div>
            <Button
              type="submit"
              data-testid="search-submit"
              className="bg-[#1A365D] hover:bg-[#319795] text-white font-semibold"
            >
              Buscar
            </Button>
          </form>

          <button
            data-testid="mobile-menu-toggle"
            className="lg:hidden p-2 text-[#1A365D]"
            onClick={() => setMobileOpen((v) => !v)}
            aria-label="Abrir menu"
          >
            {mobileOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {mobileOpen && (
          <div className="lg:hidden pb-4 border-t border-slate-100 pt-4" data-testid="mobile-menu">
            <form onSubmit={onSearch} className="flex gap-2 mb-4">
              <Input
                data-testid="mobile-search-input"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Buscar artigos…"
                className="bg-slate-50"
              />
              <Button type="submit" className="bg-[#1A365D] text-white">Ir</Button>
            </form>
            <div className="space-y-1">
              {categories.map((c) => (
                <Link
                  key={c.slug}
                  to={`/categoria/${c.slug}`}
                  onClick={() => setMobileOpen(false)}
                  data-testid={`mobile-category-${c.slug}`}
                  className="block px-3 py-2 rounded-md text-[#1A365D] font-semibold hover:bg-slate-50"
                >
                  {c.label}
                </Link>
              ))}
              <Link
                to="/sobre"
                onClick={() => setMobileOpen(false)}
                data-testid="mobile-about-link"
                className="block px-3 py-2 rounded-md text-[#1A365D] font-semibold hover:bg-slate-50"
              >
                Sobre o Blog
              </Link>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;

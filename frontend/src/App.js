import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "sonner";

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Home from "@/pages/Home";
import ArticleDetail from "@/pages/ArticleDetail";
import Category from "@/pages/Category";
import About from "@/pages/About";

function App() {
  return (
    <div className="App min-h-screen flex flex-col bg-[#F7FAFC]">
      <BrowserRouter>
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/artigo/:slug" element={<ArticleDetail />} />
            <Route path="/categoria/:slug" element={<Category />} />
            <Route path="/buscar" element={<Category searchMode />} />
            <Route path="/sobre" element={<About />} />
          </Routes>
        </main>
        <Footer />
      </BrowserRouter>
      <Toaster position="top-right" richColors />
    </div>
  );
}

export default App;

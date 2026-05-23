import { MessageCircle } from "lucide-react";
import { SOCIAL_LINKS } from "../lib/socialLinks";

export const WhatsAppButton = () => (
  <a
    href={SOCIAL_LINKS.whatsapp}
    target="_blank"
    rel="noopener noreferrer"
    data-testid="floating-whatsapp-button"
    aria-label="Agendar consulta no WhatsApp"
    className="fixed bottom-6 right-6 z-40 flex items-center gap-2 bg-[#25D366] hover:bg-[#128C7E] text-white font-semibold pl-4 pr-5 py-3 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105"
  >
    <MessageCircle className="w-5 h-5" />
    <span className="hidden sm:inline text-sm">Agendar consulta</span>
  </a>
);

export default WhatsAppButton;

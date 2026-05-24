import { Youtube, Play } from "lucide-react";
import { YOUTUBE_CHANNEL_URL } from "../lib/youtubeMap";

export const ArticleVideo = ({ video }) => {
  if (!video) return null;
  return (
    <section
      data-testid="article-video-embed"
      className="my-12 rounded-2xl overflow-hidden border border-[#FF0000]/15 bg-gradient-to-br from-[#FF0000]/5 via-white to-[#319795]/5"
    >
      <div className="grid md:grid-cols-12 gap-0">
        <div className="md:col-span-7 relative bg-black">
          <div className="relative aspect-video">
            <iframe
              src={`https://www.youtube-nocookie.com/embed/${video.id}?rel=0&modestbranding=1`}
              title={video.title}
              loading="lazy"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="absolute inset-0 w-full h-full"
              data-testid={`youtube-iframe-${video.id}`}
            />
          </div>
        </div>
        <div className="md:col-span-5 p-6 lg:p-8 flex flex-col justify-center">
          <div className="inline-flex items-center gap-2 text-[#FF0000] text-xs font-bold uppercase tracking-wider mb-3">
            <Youtube className="w-4 h-4" />
            Vídeo do Dr. Matheus Lopes
          </div>
          <h3 className="text-xl lg:text-2xl font-bold text-[#1A365D] leading-tight">
            {video.title}
          </h3>
          <p className="mt-3 text-sm text-slate-600 leading-relaxed">
            Aprofunde o conteúdo deste artigo assistindo à explicação em vídeo —
            direto, prático e em linguagem acessível.
          </p>
          <a
            href={YOUTUBE_CHANNEL_URL}
            target="_blank"
            rel="noopener noreferrer"
            data-testid="article-video-channel-cta"
            className="mt-5 inline-flex items-center gap-2 self-start bg-[#FF0000] hover:bg-[#CC0000] text-white font-semibold text-sm px-5 py-2.5 rounded-full transition-colors"
          >
            <Play className="w-4 h-4 fill-white" />
            Ver mais vídeos no canal
          </a>
        </div>
      </div>
    </section>
  );
};

export default ArticleVideo;

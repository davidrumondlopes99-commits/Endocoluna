import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

export const api = axios.create({ baseURL: API });

export const fetchArticles = async ({ category, q, limit } = {}) => {
  const params = {};
  if (category) params.category = category;
  if (q) params.q = q;
  if (limit) params.limit = limit;
  const { data } = await api.get("/articles", { params });
  return data;
};

export const fetchArticle = async (slug) => {
  const { data } = await api.get(`/articles/${slug}`);
  return data;
};

export const fetchFeatured = async () => {
  const { data } = await api.get("/articles/featured");
  return data;
};

export const fetchMostRead = async (limit = 4) => {
  const { data } = await api.get("/articles/most-read", { params: { limit } });
  return data;
};

export const fetchCategories = async () => {
  const { data } = await api.get("/categories");
  return data;
};

export const subscribeNewsletter = async (payload) => {
  const { data } = await api.post("/newsletter", payload);
  return data;
};

export const fetchYouTubeVideos = async (limit = 6) => {
  const { data } = await api.get("/youtube/videos", { params: { limit } });
  return data;
};

export const CATEGORY_META = {
  brain: { label: "Cérebro", color: "#319795" },
  spine: { label: "Coluna", color: "#2C7A7B" },
  prevention: { label: "Prevenção", color: "#1A365D" },
};

export const formatDate = (iso) => {
  if (!iso) return "";
  const d = new Date(iso);
  return d.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
};

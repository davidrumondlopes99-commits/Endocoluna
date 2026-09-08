# ==== Build stage ====
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies (cache-friendly)
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --network-timeout 600000

# Copy source
COPY . .

# Backend URL is empty by default => frontend uses relative /api routed by Nginx.
# Override with --build-arg REACT_APP_BACKEND_URL=https://your.domain to bake a full URL.
ARG REACT_APP_BACKEND_URL=""
ENV REACT_APP_BACKEND_URL=$REACT_APP_BACKEND_URL

RUN yarn build

# ==== Runtime stage (Nginx) ====
FROM nginx:1.27-alpine AS runtime

# Copy built static files
COPY --from=builder /app/build /usr/share/nginx/html

# Custom nginx config with SPA fallback + /api proxy
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget -qO- http://127.0.0.1/ >/dev/null 2>&1 || exit 1

CMD ["nginx", "-g", "daemon off;"]

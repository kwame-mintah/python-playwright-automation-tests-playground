# Use official lightweight Nginx image
FROM nginx:alpine3.23

# Remove default nginx site
RUN rm -rf /usr/share/nginx/html/*

# Copy static files into nginx
COPY index.html /usr/share/nginx/html/

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:alpine

# Copy static website files to nginx html serving directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

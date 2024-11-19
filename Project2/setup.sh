
---

### 2. **setup.sh** - Shell Script (For Running Containers)

Since you’re not using Docker Compose, your **setup.sh** file will have the commands to manually set up the containers. Here's the updated version of `setup.sh`:

```bash
#!/bin/bash
# Setup script for running WordPress and MySQL containers

echo "Creating network..."
docker network create wordpress-network

echo "Running MySQL container..."
docker run -d -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wpdb -v sqlvol:/var/lib/sql --name mystore mysql

echo "Running WordPress container..."
docker run -d --name wp --link mystore:mysql -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=password -e WORDPRESS_DB_NAME=wpdb -p 80:80 wordpress

echo "Access WordPress at http://your-ec2-public-ip"

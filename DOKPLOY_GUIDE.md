# Pasos para Desplegar en Dokploy (CD)

## 1. Preparar GitHub
```bash
cd flaskcrud
git add .
git commit -m "Preparado para Dokploy"
git push origin main
```

## 2. Configurar en Dokploy

### 2.1 Crear Proyecto
1. Ve a tu panel de Dokploy
2. Crea un nuevo **Project**
3. Nombre: `Flask CRUD`

### 2.2 Crear Servidor
1. Ve a **Servers**
2. Agrega tu VPS/MV con la IP y credenciales SSH
3. Instala Dokploy Agent si no está instalado

### 2.3 Crear Base de Datos
1. Ve a **Databases** en el proyecto
2. Crea una base de datos MySQL:
   - Database Type: `MySQL`
   - Database Name: `flaskcrud`
   - Username: `dokploy`
   - Password: `[genera una segura]`

### 2.4 Crear Deployment
1. Ve a **Deployments** en el proyecto
2. Crea nuevo **Static Deployment** o **Docker Compose**
3. Configura:
   - **Repository**: `https://github.com/TU_USER/flaskcrud`
   - **Branch**: `main`
   - **Build Type**: `Docker Compose`
   
4. En variables de entorno agrega:
   ```
   MYSQL_HOST=tu-db-host
   MYSQL_USER=dokploy
   MYSQL_PASSWORD=tu_password
   MYSQL_DB=flaskcrud
   MYSQL_PORT=3306
   DOMAIN=tu-dominio.com
   ```

### 2.5 Configurar Dominio (Opcional)
1. En el deployment, ve a **Domain**
2. Agrega tu dominio o subdominio
3. Habilita SSL automático con Let's Encrypt

## 3. Deploy Automático (CD)
Dokploy automáticamente:
- Detectará push al branch `main`
- Ejecutará `docker-compose build`
- Desplegará el contenedor
- Configurará Traefik con SSL

## 4. Verificar
```bash
# Ver logs
docker-compose logs -f

# Ver contenedores
docker ps
```

## Estructura Esperada en Dokploy
```
flaskcrud/
├── Dockerfile          # Build de producción
├── docker-compose.yml  # Definición de servicios
├── app/                # Código de la aplicación
├── sql/
│   └── init.sql        # Schema de BD
├── requirements.txt
└── .env.example        # Variables de entorno
```

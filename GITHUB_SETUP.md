# 📚 Guía: Subir a GitHub Pages

Esta guía te ayudará a publicar tu Libro de Amor en GitHub Pages.

## Paso 1: Crear un repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Haz clic en el icono **+** en la esquina superior derecha
3. Selecciona **New repository**
4. Rellena los datos:
   - **Repository name:** `love-book`
   - **Description:** "Un libro digital romántico con 200 razones para amar"
   - **Visibility:** Selecciona **Public**
   - ☑️ Marca **Add a README file** (opcional, ya tienes uno)
5. Haz clic en **Create repository**

## Paso 2: Configurar Git en tu computadora

Si es la primera vez usando Git, abre PowerShell y configura:

```powershell
git config --global user.name "YakuzaMeen"
git config --global user.email "u202212214@upc.edu.pe"
```

## Paso 3: Subir el proyecto

En PowerShell, navega a la carpeta del proyecto:

```powershell
cd C:\Users\rodrs\Love_Book
```

Inicializa el repositorio Git:

```powershell
git init
git add .
git commit -m "Proyecto: Libro de Amor - 200 razones para amar"
```

Conecta con el repositorio remoto (reemplaza USERNAME con tu usuario):

```powershell
git branch -M main
git remote add origin https://github.com/YakuzaMeen/love-book.git
git push -u origin main
```

Si te pide contraseña, usa un **Personal Access Token** en lugar de tu contraseña:

1. Ve a GitHub > Settings > Developer settings > Personal access tokens
2. Genera un nuevo token con permiso `repo`
3. Cópialo y úsalo como contraseña en Git

## Paso 4: Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Haz clic en **Settings**
3. En el menú lateral, selecciona **Pages**
4. En **Source**, selecciona:
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Haz clic en **Save**

## Paso 5: ¡Listo!

En unos segundos, tu sitio estará disponible en:

```
https://YakuzaMeen.github.io/love-book/
```

GitHub te mostrará la URL exacta en la sección de Pages.

## Hacer cambios en el futuro

Si necesitas actualizar el contenido:

```powershell
# Haz tus cambios en los archivos

# Después, sube los cambios:
git add .
git commit -m "Descripción del cambio"
git push
```

## Comandos Git útiles

```powershell
# Ver estado del repositorio
git status

# Ver historial de cambios
git log

# Descargar cambios del repositorio remoto
git pull

# Ver rama actual
git branch
```

## Solución de problemas

### Error: "fatal: not a git repository"
Asegúrate de estar en la carpeta correcta y haber ejecutado `git init`

### Error: "authentication failed"
Usa un Personal Access Token en lugar de contraseña

### Los cambios no aparecen en el sitio
- Espera 2-5 minutos (GitHub tarda en desplegar)
- Limpia la caché del navegador (Ctrl + Shift + Delete)
- Verifica que la rama sea `main` en GitHub Pages Settings

---

¡Tu libro de amor ya estará en línea! 💕

# 🎨 Guía de Personalización

## Personalizar el Proyecto

El proyecto es 100% personalizable. Aquí te muestro cómo hacer cambios comunes:

---

## 1️⃣ Cambiar el Nombre en la Propuesta

**Archivo:** `script.js`

**Busca:**
```javascript
¿Me permitas a mí, Rodrigo Sosa, ser tu novio?
```

**Reemplaza con tu nombre:**
```javascript
¿Me permitas a mí, [Tu Nombre], ser tu novio/novia?
```

---

## 2️⃣ Cambiar los Colores Principales

**Archivo:** `style.css`

**Rosa Principal (#ff69b4):**
```css
/* Cambiar en: */
.swiper-button-next, .swiper-button-prev { color: #tu-color; }
.page-number { color: #tu-color; }
.page-heart { /* color auto*/ }
```

**Rosa Oscuro (#ff1493):**
```css
.special-page { border: 3px solid #tu-color; }
.special-page .page-text { color: #tu-color; }
.proposal-page { background: linear-gradient(135deg, #color1 0%, #tu-color 100%); }
```

**Ejemplos de colores románticos:**
- `#FF1493` - Rosa profundo
- `#FFB6C1` - Rosa claro
- `#FF69B4` - Rosa medio (actual)
- `#FF0080` - Magenta
- `#E91E63` - Rosa tropical
- `#C2185B` - Rosa oscuro
- `#F48FB1` - Rosa pálido

---

## 3️⃣ Cambiar las Fuentes

**Archivo:** `index.html`

**Fuente Romántica (Dancing Script):**
```html
<!-- Cambiar esta línea -->
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Lora:ital@0;1&display=swap" rel="stylesheet">

<!-- Por ejemplo, para Playfair Display: -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lora:ital@0;1&display=swap" rel="stylesheet">
```

**Luego en `style.css`, actualiza:**
```css
.page-number {
    font-family: 'Playfair Display', cursive; /* Cambiar aquí */
}
```

**Fuentes recomendadas:**
- Dancing Script (actual)
- Playfair Display
- Great Vibes
- Allura
- Satisfy
- Pacifico

---

## 4️⃣ Cambiar el Texto del Modal de Respuesta

**Archivo:** `script.js`

**Busca:**
```javascript
modalText.textContent = 'Ahora oficialmente eres mi novia ❤️';
```

**Personaliza el mensaje:**
```javascript
modalText.textContent = 'Tu mensaje personalizado aquí ❤️';
```

---

## 5️⃣ Cambiar el Texto de Botones

**Archivo:** `script.js`

**Busca esta sección:**
```javascript
// Botón 1: Sí
const btn1 = document.createElement('button');
btn1.classList.add('proposal-btn');
btn1.textContent = 'Sí 💖'; // Cambiar aquí

// Botón 2: Obvio que sí
const btn2 = document.createElement('button');
btn2.classList.add('proposal-btn');
btn2.textContent = 'Obvio que sí 💕'; // Cambiar aquí
```

---

## 6️⃣ Cambiar la Página Especial (Razón 201)

**Archivo:** `script.js`

**Busca:**
```javascript
const specialPage = "La única razón por la que podría dejarte es si mi corazón dejara de latir, porque mientras viva, siempre voy a elegirte a ti.";
```

**Personaliza con tu mensaje:**
```javascript
const specialPage = "Tu mensaje especial aquí...";
```

---

## 7️⃣ Cambiar la Propuesta Completa

**Archivo:** `script.js`

**Busca:**
```javascript
const proposalText = `Después de 200 razones para amarte…
y una sola imposible para dejarte…

Hoy no te prometo perfección.
Te prometo intención, respeto, lealtad y ganas reales de construir algo bonito contigo.

Y con todo esto…

¿Me permitas a mí, Rodrigo Sosa, ser tu novio?`;
```

**Personaliza completamente:**
```javascript
const proposalText = `Tu propuesta aquí...
Puedes usar saltos de línea con Ctrl+Enter`;
```

---

## 8️⃣ Cambiar la Cantidad de Razones

Si quieres menos o más de 200 razones:

**En `script.js`:**
```javascript
const reasons = [
    "Tu sonrisa",
    "Tu apoyo",
    // ... agrega o elimina razones aquí
    "Tú"
];
```

**Nota:** El código se adapta automáticamente, solo tienes que cambiar la cantidad de elementos en el array.

---

## 9️⃣ Agregar Animaciones Personalizadas

**Archivo:** `style.css`

**Agregar una animación personalizada:**
```css
@keyframes myAnimation {
    0% {
        /* estado inicial */
        transform: scale(1);
    }
    100% {
        /* estado final */
        transform: scale(1.1);
    }
}

.my-element {
    animation: myAnimation 2s ease-in-out;
}
```

---

## 🔟 Cambiar el Fondo

**Archivo:** `style.css`

**Actual:**
```css
body {
    background: linear-gradient(135deg, #fff5f7 0%, #ffe4e9 100%);
}
```

**Cambiar a un color sólido:**
```css
body {
    background: #fff5f7;
}
```

**Cambiar a gradiente diferente:**
```css
body {
    background: linear-gradient(135deg, #FFE4E9 0%, #FFB6C1 100%);
}
```

---

## 1️⃣1️⃣ Cambiar el Título de la Página

**Archivo:** `index.html`

**Busca:**
```html
<title>Libro de Amor - 200 Razones para Amarte</title>
```

**Personaliza:**
```html
<title>Tu título aquí</title>
```

---

## 1️⃣2️⃣ Cambiar los Emojis

Puedes cambiar los emojis en varios lugares:

**En `style.css`:**
```css
body::before {
    content: '♥ ♥ ♥'; /* Cambiar símbolos aquí */
}
```

**En `script.js`:**
```javascript
pageHeart.textContent = '💕'; /* Cambiar emoji de corazón */

// En la función de corazones flotantes:
heart.textContent = '💗'; /* Cambiar emoji */
```

**Emojis románticos disponibles:**
- ❤️ Corazón rojo
- 💕 Dos corazones
- 💗 Corazón latiendo
- 💖 Corazón brillante
- 💝 Corazón con regalo
- 💘 Cupido
- 💞 Corazones giratorios
- 🌹 Rosa
- ✨ Brillo
- ⭐ Estrella

---

## 📋 Checklist de Personalización Común

- [ ] Cambiar nombre en propuesta
- [ ] Personalizar colores
- [ ] Cambiar fuentes
- [ ] Personalizar mensaje de respuesta
- [ ] Cambiar botones
- [ ] Actualizar razón 201
- [ ] Personalizar propuesta
- [ ] Cambiar título de la página
- [ ] Actualizar emojis

---

## 💡 Tips Extra

1. **Mantén backups**: Antes de hacer cambios grandes, copia los archivos originales
2. **Prueba localmente**: Abre index.html en tu navegador después de cada cambio
3. **Usa colores complementarios**: Usa [coolors.co](https://coolors.co) para encontrar paletas
4. **Sé coherente**: Mantiene la misma temática en todo el proyecto
5. **Móvil primero**: Prueba tus cambios en móvil, que es el principal uso

---

**¡Diviértete personalizando! Este proyecto es tuyo. 💕**

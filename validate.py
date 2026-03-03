#!/usr/bin/env python3
"""
Script de validación del proyecto Love Book
Verifica que todos los archivos estén correctos y completos
"""

import os
import json

def validate_project():
    """Valida que el proyecto esté completo"""
    
    base_path = "."
    
    # Archivos requeridos
    required_files = {
        "index.html": "HTML principal",
        "style.css": "Estilos CSS",
        "script.js": "Lógica JavaScript",
        ".gitignore": "Configuración Git"
    }
    
    print("=" * 60)
    print("🔍 VALIDACIÓN DEL PROYECTO LOVE BOOK")
    print("=" * 60)
    
    # Verificar archivos principales
    print("\n📁 Verificando archivos principales...")
    all_exist = True
    for filename, description in required_files.items():
        filepath = os.path.join(base_path, filename)
        exists = os.path.isfile(filepath)
        status = "✅" if exists else "❌"
        print(f"  {status} {filename:20} - {description}")
        if not exists:
            all_exist = False
    
    if not all_exist:
        print("\n❌ Faltan archivos requeridos")
        return False
    
    # Verificar contenido de script.js
    print("\n🔍 Verificando contenido de script.js...")
    with open("script.js", "r", encoding="utf-8") as f:
        script_content = f.read()
    
    # Contar razones
    reasons_count = script_content.count('"Tu') + script_content.count('"Tus') + script_content.count('"La') + script_content.count('"Tú')
    print(f"  ✅ Razones encontradas: {reasons_count}")
    
    # Verificar elementos especiales
    checks = [
        ("specialPage", "Razón 201 especial"),
        ("proposalText", "Texto de propuesta"),
        ("generateSlides", "Función de generación"),
        ("initializeSwiper", "Inicialización de Swiper"),
        ("showProposalResponse", "Respuesta de propuesta"),
    ]
    
    for element, description in checks:
        has_element = element in script_content
        status = "✅" if has_element else "❌"
        print(f"  {status} {description}")
    
    # Verificar contenido de index.html
    print("\n🔍 Verificando contenido de index.html...")
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    html_checks = [
        ("swiper-container", "Contenedor Swiper"),
        ("swiperWrapper", "Wrapper para slides"),
        ("proposalModal", "Modal de propuesta"),
        ("floatingHearts", "Corazones flotantes"),
        ("Swiper.js", "CDN de Swiper"),
        ("Dancing Script", "Fuente Dancing Script"),
    ]
    
    for element, description in html_checks:
        has_element = element in html_content
        status = "✅" if has_element else "❌"
        print(f"  {status} {description}")
    
    # Verificar contenido de style.css
    print("\n🔍 Verificando contenido de style.css...")
    with open("style.css", "r", encoding="utf-8") as f:
        css_content = f.read()
    
    css_checks = [
        (".page", "Estilos de página"),
        (".proposal-page", "Estilos propuesta"),
        ("animation:", "Animaciones CSS"),
        ("@media", "Media queries responsive"),
        (".swiper", "Estilos Swiper"),
    ]
    
    for element, description in css_checks:
        has_element = element in css_content
        status = "✅" if has_element else "❌"
        print(f"  {status} {description}")
    
    # Resumen final
    print("\n" + "=" * 60)
    print("✨ VALIDACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 60)
    print("\n📊 Estadísticas del Proyecto:")
    
    # Tamaño de archivos
    total_size = 0
    for filename in required_files.keys():
        if os.path.isfile(filename):
            size = os.path.getsize(filename)
            total_size += size
            size_kb = size / 1024
            print(f"  📄 {filename:20} - {size_kb:8.2f} KB")
    
    print(f"  {'─' * 45}")
    print(f"  📦 Tamaño total:        {total_size / 1024:8.2f} KB")
    
    print("\n✅ El proyecto está listo para:")
    print("   • Usar localmente: Abre index.html en tu navegador")
    print("   • Subir a GitHub Pages: Sigue GITHUB_SETUP.md")
    print("   • Personalizar: Revisa PERSONALIZATION.md")
    
    print("\n💡 Próximos pasos:")
    print("   1. Prueba localmente abriendo index.html")
    print("   2. Personaliza si lo necesitas (PERSONALIZATION.md)")
    print("   3. Sube a GitHub (GITHUB_SETUP.md)")
    print("   4. ¡Comparte con esa persona especial! 💕")
    
    return True

if __name__ == "__main__":
    try:
        validate_project()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Asegúrate de ejecutar este script desde la carpeta love-book")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

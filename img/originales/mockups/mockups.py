"""Registro de mockups: páginas (8.7, en paginas.py) y guía de estilos (8.8)."""
from base import ROJO, icono, slider
from paginas import (estructura, inicio, base, aro, pedalera, dash_galeria, dash_editor,
                     ingeniero_avisos, ingeniero_estrategia, sesiones, analisis, ajustes)


# ---------------------------------------------------------------- 8.8
def _html(cuerpo, ancho):
    from base import CSS
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div style="padding:20px;width:{ancho}px">{cuerpo}</div></body></html>'


def paleta():
    marca = [("Crema", "#F2EAE3", "PMS 9244 C", "#131211"), ("Gris cálido", "#D0C9C3", "PMS Warm Gray 2 U", "#131211"),
             ("Rojo", "#FF073A", "PMS 185 C", "#fff"), ("Casi negro", "#131211", "PMS Neutral Black C", "#F2EAE3"),
             ("Negro", "#000000", "PMS 6 C", "#F2EAE3")]
    fila_marca = "".join(f'<div style="flex:1;border-radius:10px;overflow:hidden;border:1px solid #ccc"><div style="height:110px;background:{h};color:{t};padding:10px;font-weight:700;font-size:16px">{nom}</div>'
                         f'<div style="padding:8px 10px;font-size:12px"><b>{h}</b><br>{pms}</div></div>' for nom, h, pms, t in marca)
    roles = [("FONDO", "#0d0c0b", "#E4DAD2", "Fondo de página"), ("PANEL", "#1c1a19", "#F2EAE3", "Islas y tarjetas"),
             ("PANEL_ALTO", "#262322", "#E6DCD4", "Sub-islas, controles"), ("BORDE", "#3a3634", "#C9BFB7", "Bordes y rejillas"),
             ("TEXTO", "#F2EAE3", "#131211", "Tinta principal"), ("TEXTO_SUAVE", "#D0C9C3", "#6b635c", "Tinta secundaria"),
             ("DESACTIVADO", "#6f6a66", "#A79E96", "Controles inactivos"), ("BARRA", "#000000", "#131211", "Barra lateral y pie")]
    tabla_roles = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:4px 0;border-bottom:1px solid #eee">'
                          f'<code style="width:120px;font-size:12px">{r}</code><span style="width:150px;font-size:12px;color:#666">{d}</span>'
                          f'<span style="flex:1;height:30px;border-radius:6px;background:{o};border:1px solid #bbb;color:#888;font-size:11px;display:flex;align-items:center;padding-left:8px">{o}</span>'
                          f'<span style="flex:1;height:30px;border-radius:6px;background:{c};border:1px solid #bbb;color:#888;font-size:11px;display:flex;align-items:center;padding-left:8px">{c}</span></div>'
                          for r, o, c, d in roles)
    estados = [("Verde OK", "#2eb857", "Conectado, configurado"), ("Morado", "#9D00FF", "Vuelta más rápida"),
               ("Amarillo boxes", "#f2c230", "Vuelta con parada"), ("Naranja aviso", "#e0a63a", "Atención"),
               ("Azul info", "#6aa9ff", "Información")]
    fila_est = "".join(f'<div style="flex:1;display:flex;align-items:center;gap:8px"><span style="width:34px;height:34px;border-radius:8px;background:{h};flex:none"></span>'
                       f'<div style="font-size:12px"><b>{nom}</b> {h}<br><span class="suave">{d}</span></div></div>' for nom, h, d in estados)
    fam = [("Pista", "#4a90e2"), ("Coche", "#e8892b"), ("Conducción", "#a066e0"), ("Estrategia", "#d9a21b"), ("Tiempo", "#1fa6b8"), ("Radio", "#2eb857")]
    fila_fam = "".join(f'<div style="flex:1;display:flex;align-items:center;gap:8px"><span style="width:34px;height:34px;border-radius:8px;background:{h}"></span><div style="font-size:12px"><b>{nom}</b><br>{h}</div></div>' for nom, h in fam)
    cuerpo = f"""<div class="h2" style="margin-bottom:10px">a) Paleta principal</div><div style="display:flex;gap:12px">{fila_marca}</div>
<div class="h2" style="margin:22px 0 10px">b) Colores de estado</div><div style="display:flex;gap:10px">{fila_est}</div>
<div class="h2" style="margin:22px 0 10px">c) Colores de las familias de avisos</div><div style="display:flex;gap:10px">{fila_fam}</div>"""
    return _html(cuerpo, 1060), (1100, 430)


def niveles_prueba():
    """8.9: los cuatro niveles de prueba, del más automático al más real."""
    niveles = [
        ("1", "Pruebas automáticas", "Cada cambio, en segundos",
         ["Lógica de la aplicación sin interfaz", "Lectura de la telemetría de cada juego", "Reglas del ingeniero y estrategia",
          "Espejo del protocolo firmware ↔ aplicación"], "Sin hardware ni juego", "#4a90e2"),
        ("2", "Integración continua", "Cada envío al repositorio",
         ["Compila los tres firmwares", "Comprueba las versiones", "Ejecuta todas las pruebas automáticas",
          "Publica el instalador solo con una etiqueta de versión"], "Servidor de GitHub Actions", "#1fa6b8"),
        ("3", "Pruebas en banco", "Cada versión de firmware",
         ["Protecciones de la base ante golpes y bloqueos", "Ruido y respuesta de los pedales", "Luces, botones y pantalla del aro",
          "Herramientas de diagnóstico en paralelo"], "Periféricos reales, sin juego", "#e8892b"),
        ("4", "Validación en pista", "Cada versión publicada",
         ["Sesiones largas con los simuladores", "Equipo completo funcionando a la vez", "Consumo de CPU y refresco del dash",
          "Registro de la sesión para revisarla después"], "Equipo y juegos reales", ROJO),
    ]
    cols = "".join(
        f'<div style="flex:1;display:flex;flex-direction:column;border:1.5px solid {c};border-radius:12px;overflow:hidden">'
        f'<div style="background:{c};color:#fff;padding:10px 14px"><div style="font-size:30px;font-weight:700;line-height:1">{num}</div>'
        f'<div style="font-size:17px;font-weight:700;margin-top:4px">{tit}</div><div style="font-size:12px;opacity:.9">{cuando}</div></div>'
        f'<div style="padding:12px 14px;display:flex;flex-direction:column;gap:8px;flex:1">'
        + "".join(f'<div style="font-size:13px;display:flex;gap:6px"><span style="color:{c};font-weight:700">•</span><span>{x}</span></div>' for x in items)
        + f'<div style="margin-top:auto;font-size:12px;color:#777;border-top:1px solid #ddd;padding-top:8px">{donde}</div></div></div>'
        for num, tit, cuando, items, donde, c in niveles)
    flecha = ('<div style="display:flex;align-items:center;gap:10px;margin-top:14px;font-size:13px;color:#555">'
              '<span>Más rápido y frecuente</span><div style="flex:1;height:3px;background:linear-gradient(90deg,#4a90e2,#1fa6b8,#e8892b,#FF073A);position:relative">'
              '<span style="position:absolute;right:-4px;top:-6px;border-left:10px solid #FF073A;border-top:7.5px solid transparent;border-bottom:7.5px solid transparent"></span></div>'
              '<span>Más cercano al uso real</span></div>')
    cuerpo = f'<div style="display:flex;gap:14px">{cols}</div>{flecha}'
    return _html(cuerpo, 1100), (1140, 345)


def tipografia():
    """Escala tipográfica con muestras reales en Roboto (px = pt x 2,4 para que se lean en el PDF)."""
    pesos = "".join(
        f'<div style="flex:1;border:1px solid #ddd;border-radius:10px;padding:12px 16px">'
        f'<div style="font-size:12px;color:#888">Roboto {nom} · {w}</div>'
        f'<div style="font-weight:{w};font-size:38px;color:#222">Aa</div>'
        f'<div style="font-weight:{w};font-size:14px;color:#444">ABCDEFGHIJKLMNÑ abcdefghijklmnñ<br>0123456789 · 1:58.412 · 41.6 kg</div></div>'
        for nom, w in [("Regular", 400), ("Medium", 500), ("Bold", 700)])
    escala = [("Título de página", "14 pt · semi-negrita", 14, 600, "Ingeniero de pista", "#222"),
              ("Pestañas y títulos de tarjeta", "13 pt · negrita", 13, 700, "Configuración &nbsp; Freno", "#222"),
              ("Texto general", "10 pt · regular", 10, 400, "Fuerza máxima del volante &nbsp; 11.2 A", "#333"),
              ("Texto secundario", "10 pt · regular", 10, 400, "Se aplicará al volver a abrir la aplicación.", "#8a8178"),
              ("Barra de título", "9 pt · regular", 9, 400, "VH SimGrid", "#333"),
              ("Botones de píldora", "9 pt · negrita", 9, 700, '<span class="pill" style="font-size:inherit;padding:6px 26px">Calibrar</span>', "#333"),
              ("Botones pequeños y preajustes", "8 pt · negrita", 8, 700, '<span class="pill mini" style="font-size:inherit">Mín</span> <span class="pill mini on" style="font-size:inherit">900</span>', "#333"),
              ("Insignia de ayuda", "7 pt · negrita", 7, 700, 'Zona muerta <span class="ayuda" style="width:22px;height:22px;font-size:inherit">!</span>', "#333")]
    filas = "".join(
        f'<div style="display:flex;align-items:center;gap:20px;padding:10px 0;border-bottom:1px solid #eee">'
        f'<div style="width:270px;flex:none"><div style="font-weight:700;font-size:14px">{uso}</div><div style="font-size:12px;color:#888">{med}</div></div>'
        f'<div style="font-size:{pt * 2.4:.0f}px;font-weight:{w};color:{c}">{txt}</div></div>'
        for uso, med, pt, w, txt, c in escala)
    cuerpo = (f'<div class="h2" style="margin-bottom:10px">a) Familia Roboto</div><div style="display:flex;gap:12px">{pesos}</div>'
              f'<div class="h2" style="margin:22px 0 4px">b) Escala tipográfica</div>{filas}')
    return _html(cuerpo, 1060), (1100, 705)


def iconografia():
    grupos = [("Navegación", ["inicio", "volante_ffb", "volante", "pedalera", "dash", "engineer", "tipo_traza", "ajustes"]),
              ("Acciones", ["anadir", "lapiz", "copiar", "papelera", "exportar", "importar", "deshacer", "rehacer", "lupa", "filtro", "recargar", "play", "parar", "movil"]),
              ("Curvas de pedal", ["curva_lineal", "curva_progresiva", "curva_suave", "curva_agresiva", "curva_en_s", "curva_s_invertida"]),
              ("Elementos del dash", ["tipo_texto", "tipo_gauge_dial", "tipo_gauge_arco", "tipo_gauge_lineal", "tipo_led_barra", "tipo_shift_light", "tipo_neumaticos", "tipo_mapa_pista", "tipo_delta_tiempo", "tipo_standings", "tipo_video", "tipo_pagina_web"]),
              ("Clima y coche", ["clima_seco", "clima_mojado", "clima_lluvia", "coche_gt", "coche_formula", "casco"])]
    fam = [("familia_spotter", "#4a90e2"), ("familia_rivales", "#4a90e2"), ("familia_gomas", "#e8892b"), ("familia_presiones", "#e8892b"),
           ("familia_danos", "#e8892b"), ("familia_ritmo", "#a066e0"), ("familia_entrenador", "#a066e0"), ("familia_combustible", "#d9a21b"),
           ("familia_estrategia", "#d9a21b"), ("familia_boxes", "#d9a21b"), ("familia_tiempo", "#1fa6b8"), ("familia_resultado", "#2eb857")]
    celda = lambda ic, col, fondo="": (f'<div style="width:78px;display:flex;flex-direction:column;align-items:center;gap:6px">'
                                       f'<div style="width:48px;height:48px;border-radius:10px;display:flex;align-items:center;justify-content:center;{fondo}">{icono(ic, col, 28)}</div>'
                                       f'<span style="font-size:10px;color:#666;text-align:center;word-break:break-all">{ic}</span></div>')
    cuerpo = ""
    for t, lista in grupos:
        cuerpo += f'<div class="h3" style="margin:12px 0 8px;color:#222">{t}</div><div style="display:flex;flex-wrap:wrap;gap:8px">' + "".join(celda(i, "#333", "background:#efefef") for i in lista) + "</div>"
    cuerpo += '<div class="h3" style="margin:12px 0 8px;color:#222">Familias de avisos (con el color de su tema)</div><div style="display:flex;flex-wrap:wrap;gap:8px">' + "".join(celda(i, c, f"background:{c}33") for i, c in fam) + "</div>"
    cuerpo += ('<div class="h3" style="margin:16px 0 8px;color:#222">El mismo SVG recoloreado según el estado y el modo</div><div style="display:flex;gap:18px;align-items:center">'
               + f'<div style="background:#1c1a19;padding:10px;border-radius:10px">{icono("volante", "#F2EAE3", 34)}</div>'
               + f'<div style="background:#1c1a19;padding:10px;border-radius:10px">{icono("volante", ROJO, 34)}</div>'
               + f'<div style="background:#F2EAE3;padding:10px;border-radius:10px;border:1px solid #ccc">{icono("volante", "#131211", 34)}</div>'
               + f'<div style="background:#F2EAE3;padding:10px;border-radius:10px;border:1px solid #ccc">{icono("volante", ROJO, 34)}</div>'
               + f'<div style="background:#1c1a19;padding:10px;border-radius:10px">{icono("volante", "#6f6a66", 34)}</div>'
               + '<span class="suave" style="font-size:12px">oscuro · oscuro activo · claro · claro activo · desactivado</span></div>')
    return _html(cuerpo, 1200), (1240, 900)


def componentes():
    celda = lambda t, cuerpo: f'<div class="col" style="gap:10px;align-items:flex-start"><div class="h3" style="color:#222">{t}</div>{cuerpo}</div>'
    cuerpo = f"""<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px 40px">
{celda("Botón píldora", '<div style="display:flex;gap:8px;flex-wrap:wrap"><span class="pill">Normal</span><span class="pill" style="background:#FF073A;border-color:#FF073A;color:#fff">Encima</span><span class="pill off">Desactivado</span></div>')}
{celda("Botón principal y mini", '<div style="display:flex;gap:8px;align-items:center"><span class="pill primario">Reproducir</span><span class="pill mini">Mín</span><span class="pill mini on">900</span></div>')}
{celda("Indicador de estado", '<div style="display:flex;gap:16px"><span class="estado ok">Conectado</span><span class="estado ko">Desconectado</span><span class="estado" style="color:#e0a63a">Esperando</span></div>')}
{celda("Pestañas de sección", '<div class="tabs" style="height:46px;gap:26px;padding:0 20px"><span class="tab activo" style="font-size:15px">Activa</span><span class="tab" style="font-size:15px">Otra</span><span class="tab" style="font-size:15px">Otra</span></div>')}
{celda("Subpestañas", '<div class="subtabs"><span class="activo">Carrera</span><span>Reglamento</span><span>Tandas</span></div>')}
{celda("Interruptor", '<div style="display:flex;gap:14px;align-items:center"><span class="toggle si"></span> sí <span class="toggle"></span> no</div>')}
{celda("Deslizador con valor editable", '<div style="width:320px">' + slider("Fuerza máxima", 65, "11.2 A") + '</div>')}
{celda("Desplegable", '<div class="combo" style="width:240px">Como el general</div>')}
{celda("Insignia de ayuda", '<div>Zona muerta <span class="ayuda">!</span> <span class="suave" style="font-size:12px">&#8594; explicación al pasar el ratón</span></div>')}
{celda("Isla (tarjeta)", '<div class="isla" style="width:300px;height:90px"><div class="h3">Título de isla</div></div>')}
{celda("Sub-isla", '<div class="isla" style="width:300px;padding:10px"><div class="subisla">Fila dentro de una isla</div></div>')}
{celda("Lectura en vivo", '<div class="barra" style="width:300px"><i style="width:52%;background:#FF073A"></i><span>41.6 kg (52 %)</span></div>')}
{celda("Preajuste", '<div style="display:flex;gap:6px">' + "".join(f'<span style="border:1px solid #c4c4c4;border-radius:5px;padding:3px;background:#fff">{icono(p, "#666", 22)}</span>' for p in ["curva_lineal", "curva_progresiva", "curva_suave"]) + '</div>')}
{celda("Barra de perfil", '<div style="display:flex;gap:8px;align-items:center"><span class="check si"></span> Auto <div class="combo" style="width:110px">GT3</div><span class="pill mini">Guardar</span></div>')}
{celda("Puntos de paso (asistente)", '<div style="display:flex;gap:8px;align-items:center"><span style="width:10px;height:10px;border-radius:50%;background:#FF073A"></span><span style="width:10px;height:10px;border-radius:50%;background:#FF073A"></span><span style="width:26px;height:10px;border-radius:5px;background:#FF073A"></span><span style="width:10px;height:10px;border-radius:50%;background:#ccc"></span><span style="width:10px;height:10px;border-radius:50%;background:#ccc"></span></div>')}
</div>"""
    return _html(cuerpo, 1160), (1200, 560)


MOCKUPS = {
    "ui-estructura": estructura, "ui-inicio": inicio, "ui-base": base, "ui-aro": aro, "ui-pedalera": pedalera,
    "ui-dash-galeria": dash_galeria, "ui-dash-editor": dash_editor,
    "ui-ingeniero-avisos": ingeniero_avisos, "ui-ingeniero-estrategia": ingeniero_estrategia,
    "ui-sesiones": sesiones, "ui-analisis": analisis, "ui-ajustes": ajustes,
    "estilo-paleta": paleta, "pruebas-niveles": niveles_prueba, "estilo-tipografia": tipografia, "estilo-iconos": iconografia, "estilo-componentes": componentes,
}

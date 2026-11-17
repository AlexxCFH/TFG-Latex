"""Mockups de las páginas (8.7). Las llamadas numeradas van en línea, junto al elemento."""
from base import ROJO, cabecera_periferico, icono, m, n, slider, tabs, ventana

VENTANA = (1276, 836)

GIROS = ["360", "540", "720", "900", "1080"]


def _giros():
    return '<div style="display:flex;gap:6px">' + "".join(
        f'<span class="pill mini{" on" if g == "900" else ""}">{g}</span>' for g in GIROS) + "</div>"


# ---------------------------------------------------------------- 8.7.1
def estructura():
    cont = f"""
<div class="cabecera"><span class="h1">Nombre de la página</span><span class="estado ok">Estado</span>
<span class="pill">Acción principal</span>
<div class="perfil"><span class="check si"></span> Automático <span style="margin-left:8px">Perfil</span>
<div class="combo" style="width:200px">Perfil activo</div><span class="pill">Guardar</span><span class="pill">Nuevo</span><span class="pill">Borrar</span></div></div>
{tabs(["Sección 1", "Sección 2", "Sección 3"], 0)}
<div class="fila" style="flex:1">
  <div class="isla col" style="flex:1"><div class="h3">Isla de contenido</div>
    {slider("Ajuste", 40, "40")}{slider("Ajuste", 65, "65")}{slider("Ajuste", 20, "20")}</div>
  <div class="isla col" style="flex:1"><div class="h3">Isla de contenido</div>
    {slider("Ajuste", 55, "55")}{slider("Ajuste", 30, "30")}</div>
  <div class="isla col" style="flex:1"><div class="h3">Isla de contenido</div>
    <div class="ph x" style="flex:1"></div></div>
</div>"""
    extra = "".join([
        '<div class="region" style="left:20px;top:20px;width:1240px;height:32px"></div>',
        '<div class="region" style="left:20px;top:52px;width:70px;height:740px"></div>',
        '<div class="region" style="left:110px;top:58px;width:1130px;height:52px"></div>',
        '<div class="region" style="left:110px;top:118px;width:1130px;height:72px"></div>',
        '<div class="region" style="left:110px;top:196px;width:1130px;height:580px"></div>',
        '<div class="region" style="left:20px;top:792px;width:1240px;height:28px"></div>',
        n(1, 600, 23), n(2, 42, 470), n(3, 1236, 71), n(4, 1236, 141), n(5, 1236, 470), n(6, 600, 795),
    ])
    return ventana(cont, activo=-1, extra=extra), VENTANA


# ---------------------------------------------------------------- 8.7.2
def inicio():
    portadas = []
    for i, (nombre, estado) in enumerate([("Assetto Corsa", "No instalado"), ("ACC", "Configurado"),
                                          ("AC EVO", "No instalado"), ("iRacing", "Sin configurar"),
                                          ("Automobilista 2", "No instalado")]):
        color = "#2eb857" if estado == "Configurado" else ("#e0a63a" if estado == "Sin configurar" else "#666")
        marca = m(2) if i == 1 else ""
        portadas.append(f'<div class="ph x" style="width:206px;height:120px;flex:none;padding-bottom:8px">'
                        f'<span style="position:absolute;top:44px;font-size:14px;color:#777">{nombre}</span>'
                        f'<span style="color:{color};font-weight:700;display:flex;align-items:center">{estado}{marca}</span></div>')
    pedales = "".join(
        f'<div style="display:flex;align-items:center;gap:12px"><span style="width:80px">{p}</span>'
        f'<div class="barra" style="flex:1"><i style="width:{v}%;background:{c}"></i><span>{v}%</span></div>'
        f'<span class="pill mini off">Mín</span><span class="pill mini off">Máx</span>{m(6) if p == "Freno" else "<span style=width:32px></span>"}</div>'
        for p, v, c in [("Embrague", 0, "#4a90e2"), ("Freno", 38, ROJO), ("Acelerador", 72, "#2eb857")])
    cab = lambda t, k: (f'<div style="display:flex;align-items:center;gap:12px;align-self:stretch"><span class="h2">{t}</span>'
                        f'<span class="estado ok">Conectado</span><span class="pill">Desconectar</span>{m(k) if k else ""}'
                        f'<span style="margin-left:auto;font-size:20px;color:#666">&#8942;</span></div>')
    cont = f"""
<div class="h2">Lanzador de juegos {m(1)}</div>
<div style="display:flex;gap:12px;overflow:hidden">{''.join(portadas)}</div>
<div style="height:6px;width:420px;background:#cfcfcf;border-radius:3px"></div>
<div class="h2" style="margin-top:4px">Tus dispositivos</div>
<div class="fila" style="flex:1">
  <div class="isla col" style="flex:1;align-items:center">
    {cab("Volante", 3)}
    <div style="font-size:26px;font-weight:700;color:#666;margin-top:6px">-34°</div>
    <div style="transform:rotate(-34deg)">{icono("volante", "#777", 140)}</div>
    <span class="pill">Mover al 0</span>
    <div class="suave">Ángulo máximo de giro</div>
    <div style="display:flex;align-items:center">{_giros()}{m(4)}</div>
    <div style="align-self:stretch">{slider("", 62, "900°", ayuda=False)}</div>
  </div>
  <div class="col" style="flex:1;gap:20px">
    <div class="isla col">{cab("Base", 0)}
      {slider("Fuerza máxima del volante", 70, "11.2 A", ayuda=False, marca=m(5))}</div>
    <div class="isla col" style="flex:1;gap:14px">{cab("Pedales", 0)}
      <div style="display:flex;gap:16px;align-items:center;flex:1">{icono("pedalera", "#777", 110)}<div class="col" style="flex:1;gap:14px">{pedales}</div></div>
    </div>
  </div>
</div>"""
    return ventana(cont, activo=0, juego="Assetto Corsa Competizione detectado"), VENTANA


# ---------------------------------------------------------------- 8.7.3
def base():
    sens = "".join(slider(t, p, v, marca=m(4) if i == 0 else "") for i, (t, p, v) in enumerate([
        ("Fuerza máxima del volante", 70, "11.2 A"), ("Suavizado de la señal del juego", 20, "2"),
        ("Refuerzo de las fuerzas pequeñas", 10, "5 %"), ("Forma de la respuesta de fuerza", 50, "1.00"),
        ("Dureza del tope de giro", 80, "80 %")]))
    efectos = "".join(slider(t, p, v) for t, p, v in [
        ("Amortiguación propia del volante", 15, "15 %"), ("Efecto muelle pedido por el juego", 100, "100 %"),
        ("Amortiguación pedida por el juego", 100, "100 %"), ("Fricción pedida por el juego", 100, "100 %"),
        ("Inercia pedida por el juego", 100, "100 %"), ("Suavidad del motor a baja velocidad", 30, "30 %"),
        ("Centrado suave en el escritorio", 20, "20 %")])
    mant = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;gap:8px">'
                   f'<span>{t}</span><span class="pill" style="width:100px;flex:none">{b}</span></div>'
                   for t, b in [("Reinicio suave de la base", "Reiniciar"),
                                ("Restablecer y recalibrar la base", "Iniciar"),
                                ("Calibrar la suavidad del motor (anti-cogging)", "Calibrar")])
    cont = f"""{cabecera_periferico("VH Grid DD15", "GT3")}
{tabs(["Configuración", "Ecualizador FFB", "Curva FFB base", "Varios"], 0, marca=2)}
<div class="fila" style="flex:1">
  <div class="isla col" style="flex:1;align-items:center;min-width:0"><div class="h3" style="align-self:flex-start">Rango de dirección {m(3)}</div>
    {icono("volante", "#777", 110)}<div style="font-size:22px;font-weight:700;color:#666">0°</div>
    <div style="display:flex;gap:8px"><span class="pill">Mover al 0</span><span class="pill">Establecer centro</span></div>
    <div class="suave">Ángulo máximo de giro <span class="ayuda">!</span></div>
    {_giros()}
    <div style="align-self:stretch">{slider("", 62, "900°", ayuda=False)}</div>
    <div class="col" style="align-self:stretch;margin-top:auto;gap:12px"><div class="h3">Mantenimiento {m(5)}</div>{mant}<div class="suave" style="font-size:12px">calibrado · 2026-10-12</div></div>
  </div>
  <div class="isla col" style="flex:1;gap:14px;min-width:0"><div class="h3">Sensación FFB</div>{sens}
    <div style="display:flex;gap:10px;align-items:center"><span class="check"></span> Suavizar entre muestras del juego</div></div>
  <div class="isla col" style="flex:1;gap:12px;min-width:0"><div class="h3">Efectos base {m(6)}</div>{efectos}</div>
</div>"""
    return ventana(cont, activo=1), VENTANA


# ---------------------------------------------------------------- 8.7.4
def aro():
    colores = ["#2eb857"] * 8 + ["#f2c230"] * 6 + [ROJO] * 6 + ["#4a90e2"] * 4
    leds = "".join(f'<div style="width:30px;height:30px;border-radius:50%;background:{c if i < 15 else "#d6d6d6"};'
                   f'border:1px solid #bbb"></div>' for i, c in enumerate(colores))
    filas = [("RPM", "Barra de RPM", "1-24", "#2eb857"), ("Bandera", "Azul", "1-3, 22-24", "#4a90e2"),
             ("Bandera", "Amarilla", "1-3, 22-24", "#f2c230"), ("Coche", "Límite de foso", "1-24", "#9D00FF"),
             ("Coche", "ABS activo", "1-2", "#e0a63a"), ("Coche", "TC activo", "23-24", "#1fa6b8")]
    tabla = "".join(
        f'<div class="subisla" style="display:flex;align-items:center;gap:14px">'
        f'<span class="toggle si" style="transform:scale(.8)"></span><span style="width:90px;color:#777">{g}</span>'
        f'<span style="flex:1;font-weight:500">{e}{m(5) if i == 0 else ""}</span><span style="width:110px">LEDs {r}</span>'
        f'<span style="width:22px;height:22px;border-radius:5px;background:{c}"></span>'
        f'<div class="combo" style="width:130px;padding:4px 10px">Parpadeo</div></div>' for i, (g, e, r, c) in enumerate(filas))
    cont = f"""{cabecera_periferico("VH Formula Apex", "Por defecto")}
{tabs(["Configuraciones generales", "Configuración de las RPM", "Asignación de luces"], 2, marca=2)}
<div class="isla col"><div class="h3">Vista previa {m(3)}</div><div style="display:flex;justify-content:space-between;padding:10px 20px">{leds}</div></div>
<div class="fila" style="flex:1">
  <div class="isla col" style="flex:2;gap:10px"><div style="display:flex;align-items:center"><span class="h3">Efectos</span>
    <span style="margin-left:auto">{m(4)}</span><span class="pill">+ Añadir efecto</span></div>{tabla}</div>
  <div class="isla col" style="flex:1;gap:12px"><div class="h3">Qué está pasando {m(6)}</div>
    <div class="subisla col" style="gap:6px"><div><b>Juego:</b> ACC</div><div><b>RPM:</b> 7 850 / 8 400</div>
    <div><b>Marcha:</b> 4</div><div><b>Bandera:</b> ninguna</div><div><b>Activo ahora:</b> Barra de RPM</div></div>
    <div style="margin-top:auto;display:flex;gap:8px;flex-wrap:wrap;align-items:center">{m(7)}<span class="pill">Probar luces</span><span class="pill">Apagar luces</span><span class="pill">Simular</span></div>
  </div>
</div>"""
    return ventana(cont, activo=2, juego="Assetto Corsa Competizione detectado"), VENTANA


# ---------------------------------------------------------------- 8.7.5
def _curva(puntos, color):
    w, h = 300, 220
    pts = " ".join(f"{20 + x * (w - 30) / 100:.0f},{h - 20 - y * (h - 30) / 100:.0f}" for x, y in puntos)
    circ = "".join(f'<circle cx="{20 + x * (w - 30) / 100:.0f}" cy="{h - 20 - y * (h - 30) / 100:.0f}" r="6" fill="#fff" stroke="{color}" stroke-width="2"/>' for x, y in puntos)
    rej = "".join(f'<line x1="{20 + i * (w - 30) / 4:.0f}" y1="10" x2="{20 + i * (w - 30) / 4:.0f}" y2="{h - 20}" stroke="#d6d6d6" stroke-dasharray="3 3"/>' for i in range(5))
    rej += "".join(f'<line x1="20" y1="{10 + i * (h - 30) / 4:.0f}" x2="{w - 10}" y2="{10 + i * (h - 30) / 4:.0f}" stroke="#d6d6d6" stroke-dasharray="3 3"/>' for i in range(5))
    return (f'<svg width="{w}" height="{h}">{rej}<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.5"/>'
            f'{circ}<text x="{w/2}" y="{h-4}" font-size="11" fill="#777" text-anchor="middle">Recorrido (%)</text>'
            f'<text x="10" y="{h/2}" font-size="11" fill="#777" transform="rotate(-90 10 {h/2})" text-anchor="middle">Salida (%)</text></svg>')


def pedalera():
    def columna(nombre, color, puntos, lectura, zm, pos, marcas):
        presets = "".join(f'<span style="border:1px solid #c4c4c4;border-radius:5px;padding:3px;background:#fff">{icono(p, "#666", 22)}</span>'
                          for p in ["curva_lineal", "curva_progresiva", "curva_suave"])
        mk = lambda k: m(k) if k in marcas else ""
        return f"""<div class="isla col" style="flex:1;gap:10px;align-items:stretch;min-width:0">
  <div style="display:flex;align-items:center;gap:8px"><span style="width:9px;height:9px;border-radius:50%;background:{color}"></span>
    <span style="font-size:17px;font-weight:700">{nombre}</span>{mk(3)}<span style="margin-left:auto" class="check"></span> Invertir <span class="ayuda">!</span></div>
  <div style="display:flex;align-items:center;gap:8px">Preajustes: {presets}<span class="ayuda">!</span>{mk(4)}</div>
  <div style="display:flex;justify-content:center;position:relative">{_curva(puntos, color)}<span style="position:absolute;right:-8px;top:45%">{mk(5)}</span></div>
  {slider("Zona muerta", zm, str(zm), ayuda=True)}
  <div style="display:flex;align-items:center"><div class="barra" style="flex:1"><i style="width:{pos}%;background:{color}"></i><span>{lectura}</span></div>{mk(6)}</div>
  <div style="display:flex;justify-content:center;align-items:center"><span class="pill">Calibrar</span>{mk(7)}</div></div>"""
    traza = ('<svg width="100%" height="80" viewBox="0 0 1000 90" preserveAspectRatio="none">'
             '<polyline points="0,80 120,80 160,10 300,10 330,80 520,80 560,20 640,20 660,80 1000,80" fill="none" stroke="#2eb857" stroke-width="2"/>'
             '<polyline points="0,80 320,80 340,30 380,22 430,60 480,80 650,80 670,15 720,40 760,80 1000,80" fill="none" stroke="' + ROJO + '" stroke-width="2"/>'
             '<polyline points="0,80 60,80 70,12 100,12 110,80 1000,80" fill="none" stroke="#4a90e2" stroke-width="2"/></svg>')
    cont = f"""{cabecera_periferico("VH Axis", "GT3")}
<div class="isla col" style="gap:4px"><div class="h3">Traza de pedales {m(2)}</div>{traza}</div>
<div class="fila" style="flex:1">
{columna("Embrague", "#4a90e2", [(0, 0), (20, 5), (35, 15), (50, 50), (65, 85), (80, 95), (100, 100)], "0 %", 2, 0, ())}
{columna("Freno", ROJO, [(0, 0), (17, 12), (33, 28), (50, 46), (67, 65), (83, 83), (100, 100)], "41.6 kg (52 %)", 0, 52, (3, 4, 5, 6, 7))}
{columna("Acelerador", "#2eb857", [(0, 0), (17, 17), (33, 33), (50, 50), (67, 67), (83, 83), (100, 100)], "73 %", 6, 73, ())}
</div>"""
    return ventana(cont, activo=3, juego="Assetto Corsa Competizione detectado"), VENTANA


# ---------------------------------------------------------------- 8.7.6
def _mini_dash(marcha="4", rpm="7850", alto=150, grande=62):
    return f"""<div style="background:#3a3a3a;border-radius:6px;height:{alto}px;position:relative;color:#eee;font-family:Roboto">
<div style="position:absolute;left:10px;top:8px;right:10px;height:10px;background:linear-gradient(90deg,#2eb857 0 45%,#f2c230 45% 75%,{ROJO} 75%);border-radius:3px;opacity:.85"></div>
<div style="position:absolute;left:50%;top:{alto * 0.2:.0f}px;transform:translateX(-50%);font-size:{grande}px;font-weight:700">{marcha}</div>
<div style="position:absolute;left:12px;top:40px;font-size:11px;color:#aaa">VEL</div><div style="position:absolute;left:12px;top:54px;font-size:22px;font-weight:700">187</div>
<div style="position:absolute;right:12px;top:40px;font-size:11px;color:#aaa">DELTA</div><div style="position:absolute;right:12px;top:54px;font-size:22px;font-weight:700;color:#2eb857">-0.32</div>
<div style="position:absolute;left:12px;bottom:12px;font-size:16px">1:58.412</div><div style="position:absolute;right:12px;bottom:12px;font-size:16px">{rpm}</div>
</div>"""


def dash_galeria():
    nombres = ["AMR23 - Formula Alpha 23", "Aston Martin Vantage AMR GT3", "BMW M4 GT3", "Ferrari 296 GT3",
               "Ferrari 488 GT3", "Ferrari F1", "RaceLogic"]
    tarjetas = [f'<div class="isla" style="border:2px dashed #aaa;display:flex;flex-direction:column;align-items:center;'
                f'justify-content:center;gap:8px;height:206px"><span style="font-size:34px;color:#666">+</span>'
                f'<b>Crear un dash nuevo {m(5)}</b></div>']
    for i, nom in enumerate(nombres):
        sel = ' marco-rojo' if i == 0 else ''
        tarjetas.append(f'<div class="isla{sel}" style="padding:10px;height:206px;display:flex;flex-direction:column;gap:10px">'
                        f'{_mini_dash(str(i % 6 + 1))}<b style="text-align:center">{nom}{m(6) if i == 0 else ""}</b></div>')
    cont = f"""<div class="cabecera"><span class="h1">AMR23</span><span class="estado ok">Reproduciendo</span>{m(1)}
<div class="perfil" style="gap:14px">{m(2)}{icono("vista_carrusel", "#666", 20)}<span style="background:#ddd;border-radius:6px;padding:4px">{icono("vista_cuadricula", "#333", 20)}</span>{icono("vista_lista", "#666", 20)}
<span style="margin-left:10px">Pantalla</span><div class="combo" style="width:260px">Pantalla del aro — 800×480</div>{m(3)}
{icono("exportar", "#555", 22)}{icono("importar", "#555", 22)}{icono("movil", "#555", 22)}{m(4)}</div></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;align-content:start;flex:1;padding:4px 30px 0 30px;overflow:hidden">{''.join(tarjetas)}</div>
<div style="display:flex;justify-content:center;gap:12px;align-items:center"><span class="pill">Editar</span><span class="pill primario">Detener</span>{m(7)}</div>"""
    return ventana(cont, activo=4, juego="Assetto Corsa Competizione detectado"), VENTANA


def dash_editor():
    caja = "".join(f'<div style="display:flex;align-items:center;gap:8px;padding:3px 0">{icono(ic, "#555", 16)}{t}</div>' for ic, t in [
        ("tipo_texto", "Texto"), ("tipo_imagen", "Imagen"), ("tipo_rectangulo", "Rectángulo"), ("tipo_elipse", "Elipse"),
        ("tipo_boton", "Botón"), ("tipo_shift_light", "Luz de cambio"), ("tipo_video", "Vídeo"),
        ("tipo_pagina_web", "Página web"), ("tipo_gauge_lineal", "Gauge lineal"), ("tipo_gauge_dial", "Gauge circular"),
        ("tipo_gauge_arco", "Gauge de arco"), ("tipo_led_barra", "Barra segmentada"), ("tipo_neumaticos", "Neumáticos"),
        ("tipo_traza", "Traza"), ("tipo_delta_tiempo", "Delta de tiempo"), ("tipo_mapa_pista", "Mapa de pista"),
        ("tipo_standings", "Posiciones"), ("tipo_widget", "Widget (otro dash)")])
    jer = "".join(f'<div style="display:flex;align-items:center;gap:8px;padding:4px 0">{icono("tipo_widget", "#666", 16)}'
                  f'<span style="flex:1">{t}</span>{icono("lapiz", "#777", 15)}{icono("candado_abierto", "#777", 15)}'
                  f'{icono("ojo_abierto" if v else "ojo_cerrado", "#777", 15)}</div>'
                  for t, v in [("Barra de RPM", 1), ("Marcha", 1), ("Velocidad", 1), ("Delta", 1), ("Tiempo de vuelta", 1),
                               ("Aviso de frenada", 0), ("Aviso de boxes", 0)])
    herramientas = "".join(icono(i, "#555", 18) for i in [
        "rejilla", "guias", "iman", "alinear_izq", "alinear_centro_h", "alinear_der", "alinear_arriba",
        "alinear_centro_v", "alinear_abajo", "distribuir_h", "distribuir_v", "orden_adelante", "orden_atras",
        "candado", "papelera", "deshacer", "rehacer"])
    pantallas = "".join(f'<div style="width:150px;flex:none;text-align:center">{_mini_dash(str(i + 3), alto=110, grande=44)}<div style="margin-top:4px">{p}</div></div>'
                        for i, p in enumerate(["PAGE 1", "PAGE 2", "SETUP"]))
    props = "".join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid #ddd;padding:3px 0"><span class="suave">{k}</span><span>{v}</span></div>'
                    for k, v in [("Nombre", "Marcha"), ("X / Y", "350 / 120"), ("Ancho / Alto", "100 / 140"), ("Texto", "[Gear]"),
                                 ("Fuente", "Roboto Bold 120"), ("Color", "Calculado  fx"), ("Visible si", "siempre")])
    cont = f"""
<div style="display:flex;align-items:center;gap:22px;margin:-12px -26px 0 -26px;padding:6px 10px;background:#e8e8e8;border-bottom:1px solid #d0d0d0">
  <span class="pill">&#8592; Cerrar editor</span><span>Archivo</span><span>Dash</span><span>Editar</span><span>Elementos</span><span>Herramientas</span>{m(1)}
  <b style="margin-left:auto;font-size:16px">AMR23 - Formula Alpha 23</b></div>
<div style="display:flex;align-items:center;gap:12px;margin:-12px -26px 0 -26px;padding:6px 10px;background:#efefef;border-bottom:1px solid #d0d0d0">
  <span>&#9656; Probar dash</span><div class="combo" style="width:150px;padding:4px 10px">Pantalla del aro</div>
  <span>Overlay transparente</span><div style="display:flex;gap:12px;align-items:center">{herramientas}</div>{m(2)}
  <span style="margin-left:auto">– 100 % +</span><span>800×480 px</span></div>
<div class="fila" style="flex:1;gap:12px;margin:0 -16px -12px -16px;min-height:0">
  <div class="isla col" style="width:210px;gap:2px;padding:10px 12px"><b style="margin-bottom:6px">Caja de herramientas {m(3)}</b>
    <div class="combo" style="padding:4px 8px;margin-bottom:6px;color:#999">Buscar elemento…</div>{caja}</div>
  <div class="col" style="flex:1;gap:10px;min-width:0">
    <div style="display:flex;gap:8px;align-items:center">{''.join(f'<span class="pill mini{" on" if i == 0 else ""}" style="border-radius:6px">{p}</span>' for i, p in enumerate(["PAGE 1", "PAGE 2", "SETUP"]))}
      <span class="suave" style="margin-left:12px">Botones del aro: &lt; Sin asignar &nbsp; &gt; Sin asignar</span>{m(4)}</div>
    <div style="background:#d9d9d9;flex:1;display:flex;align-items:center;justify-content:center;border-radius:8px;gap:10px">
      <div style="width:460px;height:276px;outline:2px dashed #888">{_mini_dash(alto=276, grande=120)}</div>{m(5)}</div>
    <div class="isla col" style="gap:8px;padding:10px 12px"><b>Pantallas {m(6)}</b><div style="display:flex;gap:14px">{pantallas}</div></div>
  </div>
  <div class="col" style="width:290px;gap:10px">
    <div class="isla col" style="gap:2px;padding:10px 12px"><b style="margin-bottom:6px">Jerarquía de pantalla {m(7)}</b>
      <div class="combo" style="padding:4px 8px;margin-bottom:4px;color:#999">Buscar…</div>{jer}</div>
    <div class="isla col" style="flex:1;gap:8px;padding:10px 12px"><b>Propiedades {m(8)}</b>{props}</div>
  </div>
</div>"""
    return ventana(cont, activo=4, sidebar=False), VENTANA


# ---------------------------------------------------------------- 8.7.7
FAMILIAS = {"Spotter": ("familia_spotter", "#4a90e2"), "Combustible": ("familia_combustible", "#d9a21b"),
            "Ritmo": ("familia_ritmo", "#a066e0"), "Gomas": ("familia_gomas", "#e8892b"),
            "Coche": ("familia_coche", "#e8892b"), "Daños": ("familia_danos", "#e8892b"),
            "Presiones": ("familia_presiones", "#e8892b"), "Rivales": ("familia_rivales", "#4a90e2"),
            "Estrategia": ("familia_estrategia", "#d9a21b"), "Tiempo": ("familia_tiempo", "#1fa6b8"),
            "Conducción": ("familia_conduccion", "#a066e0"), "Vuelta": ("familia_vuelta", "#a066e0"),
            "Entrenador": ("familia_entrenador", "#a066e0"), "Boxes": ("familia_boxes", "#d9a21b"),
            "Parte": ("familia_parte", "#2eb857"), "Resultado": ("familia_resultado", "#2eb857")}


def ingeniero_avisos():
    nivel = {"Spotter": "Hablador", "Entrenador": "Silenciado", "Rivales": "Seco"}

    def familia(nom, marcas=()):
        ic, c = FAMILIAS[nom]
        niv = nivel.get(nom, "Como el general")
        return (f'<div class="subisla" style="display:flex;align-items:center;gap:10px;padding:6px 14px">'
                f'<span style="background:{c}33;border-radius:6px;padding:4px">{icono(ic, c, 18)}</span>'
                f'<b style="font-size:16px">{nom}</b>{m(4) if 4 in marcas else ""}<span style="margin-left:auto">{m(5) if 5 in marcas else ""}</span>'
                f'<div class="combo" style="width:170px;padding:5px 10px">{niv}</div>'
                f'<span style="color:#666">&#8964;</span></div>')
    abierta = ('<div class="subisla col" style="gap:6px;padding:8px 14px;grid-column:1 / span 2">'
               f'<div style="display:flex;align-items:center;gap:10px"><span style="background:#d9a21b33;border-radius:6px;padding:4px">{icono("familia_combustible", "#d9a21b", 18)}</span>'
               f'<b style="font-size:16px">Combustible</b>{m(6)}<div class="combo" style="margin-left:auto;width:170px;padding:5px 10px">Como el general</div><span style="color:#666">&#8963;</span></div>'
               + "".join(f'<div style="display:flex;align-items:center;gap:12px;padding-left:44px"><span class="toggle{" si" if s else ""}" style="transform:scale(.7)"></span><span>{t}</span></div>'
                         for t, s in [("Vueltas de gasolina restantes", 1), ("Aviso de reserva", 1), ("Cuánto echar en la parada", 1), ("Consumo de la última vuelta", 0)])
               + "</div>")
    orden = ["Spotter", "Rivales", "Ritmo", "Gomas", "Coche", "Daños", "Presiones", "Estrategia", "Tiempo", "Entrenador"]
    grid = familia("Spotter", (4, 5)) + familia("Rivales") + abierta + "".join(familia(x) for x in orden[2:])
    cont = f"""<div class="cabecera"><span class="h1">Ingeniero de pista</span><span class="estado ok">Activo</span><span class="pill">Apagar</span>{m(1)}</div>
{tabs(["Voz", "Avisos", "Estrategia"], 1, marca=2)}
<div class="isla col" style="flex:1;gap:10px;overflow:hidden">
  <div class="subisla" style="display:flex;align-items:center;gap:12px;padding:6px 14px"><span style="background:{ROJO}33;border-radius:6px;padding:4px">{icono("engineer", ROJO, 18)}</span>
    <b style="font-size:17px">Personalidad</b>{m(3)}<div class="combo" style="margin-left:auto;width:170px;padding:5px 10px">Normal</div></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:9px 20px">{grid}</div>
</div>"""
    return ventana(cont, activo=5), VENTANA


def ingeniero_estrategia():
    def opcion(num, txt, extra_, sel):
        borde = f"border:2px solid {ROJO}" if sel else "border:1px solid #d0d0d0"
        return (f'<div class="subisla" style="width:130px;{borde};padding:8px 12px"><div><b style="font-size:22px">{num}</b> '
                f'<span style="font-size:11px">{txt}</span>{" ★" if sel else ""}</div><div style="font-weight:700;color:{"#2eb857" if sel else "#444"}">{extra_}</div>'
                f'<div style="height:5px;background:#4a90e2;border-radius:3px;margin-top:6px"></div></div>')
    tile = lambda t, v, u: (f'<div style="flex:1;padding:4px 8px;min-width:0"><div style="font-size:10px;font-weight:700;color:#666">{t} <span class="ayuda">!</span></div>'
                            f'<div style="font-size:20px;font-weight:700">{v}</div><div style="font-size:11px;color:#777">{u}</div></div>')
    grafica = lambda tit, val, pts: (f'<div class="subisla col" style="flex:1;gap:2px;padding:8px 12px;min-width:0"><div style="display:flex;font-size:10px;font-weight:700">{tit}<span style="margin-left:auto">{val}</span></div>'
                                     f'<svg height="80" width="100%" viewBox="0 0 400 90" preserveAspectRatio="none"><rect x="185" y="0" width="30" height="90" fill="#f2c23055"/>'
                                     f'<polyline points="{pts}" fill="none" stroke="#4a90e2" stroke-width="2"/></svg></div>')
    cont = f"""<div class="cabecera"><span class="h1">Ingeniero de pista</span><span class="estado ok">Activo</span><span class="pill">Apagar</span></div>
{tabs(["Voz", "Avisos", "Estrategia"], 2)}
<div class="fila" style="flex:1;min-height:0">
  <div class="col" style="width:280px;flex:none"><div style="display:flex;align-items:center;gap:6px"><span class="h2">Estrategias</span>{m(1)}
    <span style="margin-left:auto;display:flex;gap:6px">{icono("anadir", "#555", 20)}{icono("play", "#555", 20)}{icono("copiar", "#555", 20)}{icono("papelera", "#555", 20)}</span></div>
    <div class="combo" style="border-radius:999px;color:#999">Buscar estrategia…</div>
    <div class="isla col" style="flex:1;padding:8px;gap:8px">
      <div class="subisla marco-rojo"><b>Sprint Barcelona 60 min</b><div style="font-size:11px">Ferrari 296 GT3 · Barcelona</div></div>
      <div class="subisla"><b>Spa 24 h · equipo</b><div style="font-size:11px">Ferrari 296 GT3 · Spa</div></div>
      <div class="subisla"><b>Monza 2 h</b><div style="font-size:11px">McLaren 720S GT3 · Monza</div></div></div></div>
  <div class="isla col" style="flex:1;gap:9px;min-width:0">
    <div style="display:flex;align-items:center;gap:10px"><span class="h2">Sprint Barcelona 60 min</span>{icono("lapiz", "#555", 18)}<span class="pill off">Guardada</span>
      <span style="margin-left:auto">{m(2)}</span><span class="pill">Medir en pista</span><span class="ayuda">!</span></div>
    <div class="suave" style="margin-top:-8px">Ferrari 296 GT3 · Barcelona</div>
    <div style="display:flex;gap:10px;align-items:center">{opcion(1, "parada", "Mejor", True)}{opcion(2, "paradas", "+36.2 s", False)}{opcion(3, "paradas", "+69.2 s", False)}
      <div class="subisla" style="width:110px;height:72px;border:1.5px dashed #aaa;display:flex;align-items:center;justify-content:center;font-size:28px;color:#777">+</div>{m(3)}</div>
    <div style="display:flex;gap:12px;font-size:12px;align-items:center"><span>&#9632; Formación</span><span style="color:#4a90e2">&#9632; Piloto 1</span><span style="color:#2eb857">&#9632; Piloto 2</span>{m(4)}</div>
    <div style="display:flex;height:34px;border-radius:8px;overflow:hidden;color:#fff;font-weight:700;font-size:12px;position:relative;flex:none">
      <div style="width:2%;background:#f2c230"></div><div style="width:52%;background:#4a90e2;display:flex;align-items:center;justify-content:center">17 v · Piloto 1 · 94 L</div>
      <div style="width:46%;background:#2eb857;display:flex;align-items:center;justify-content:center">16 v · Piloto 2 · 50 L</div>
      <div style="position:absolute;left:52%;top:4px;width:26px;height:26px;border-radius:50%;background:#333;border:2px solid #fff;font-size:10px;display:flex;align-items:center;justify-content:center">P1</div></div>
    <div style="display:flex;gap:12px;align-items:center">{grafica("GASOLINA EN EL DEPÓSITO", "mín. 8.0 L", "0,5 200,50 215,10 400,85")}{grafica("RITMO PREVISTO", "media 1:52.2", "0,80 200,20 215,85 400,30")}{m(5)}</div>
    <div class="subtabs" style="align-items:center"><span class="activo">Carrera</span><span>Reglamento</span><span>Tandas</span><span>Clasificación</span>{m(6)}</div>
    <div style="display:flex;gap:12px;align-items:center">
      <div class="subisla col" style="flex:1;gap:2px;min-width:0"><div style="font-size:10px;font-weight:700">CARRERA &nbsp;<span class="pill mini on">Tiempo</span> <span class="pill mini">Vueltas</span></div>
        <div style="display:flex">{tile("DURACIÓN", "1 h", "horas y minutos")}{tile("RITMO", "1:50.1", "por vuelta")}</div></div>
      <div class="subisla col" style="flex:2;gap:2px;min-width:0"><div style="font-size:10px;font-weight:700">GASOLINA &nbsp;<span class="pill mini on">Conservadora</span> <span class="pill mini">Equilibrada</span> <span class="pill mini">Agresiva</span></div>
        <div style="display:flex">{tile("CONSUMO", "2.60", "litros / vuelta")}{tile("DEPÓSITO", "120", "litros")}{tile("RESERVA", "8.0", "litros al llegar")}{tile("REPOSTAJE", "2.0", "litros / segundo")}</div></div>
      {m(7)}
    </div>
  </div>
</div>"""
    return ventana(cont, activo=5, juego="Assetto Corsa Competizione detectado"), VENTANA


# ---------------------------------------------------------------- 8.7.8
def sesiones():
    filas = [("Spa · Ferrari 296 GT3", "Carrera · 12/10/2026 23:25 · 3 vueltas", "2:28.765", False, True),
             ("Nürburgring 24h · Ferrari 296 GT3", "Práctica libre · 12/10/2026 22:07 · 3 vueltas", "8:59.766", True, False),
             ("Zolder · Ferrari 296 GT3", "Práctica libre · 12/10/2026 19:05 · 1 vuelta", "1:30.214", False, False),
             ("Paul Ricard · Ferrari 296 GT3", "Carrera · 12/10/2026 18:46 · 8 vueltas", "1:58.985", True, False),
             ("Paul Ricard · Ferrari 296 GT3", "Carrera · 12/10/2026 18:28 · 8 vueltas", "2:00.172", False, False),
             ("Monza · McLaren 720S GT3 Evo", "Clasificación · 14/09/2026 10:21 · 5 vueltas", "1:47.330", False, False)]
    lista = "".join(
        f'<div class="isla{" marco-rojo" if sel else ""}" style="display:flex;align-items:center;gap:16px;padding:8px">'
        f'<div class="ph" style="width:110px;height:64px;align-items:center">{icono("tipo_mapa_pista", "#888", 34)}</div>'
        f'<div class="col" style="gap:8px"><b>{t}{m(2) if sel else ""}</b><span class="suave">{s}</span></div>'
        f'<span style="margin-left:auto">{m(3) if (mej and i == 1) else ""}</span><b style="font-size:17px;color:{"#9D00FF" if mej else "#333"}">{tiempo}</b>'
        f'{icono("papelera", "#777", 20) if sel else "<span style=width:20px></span>"}</div>'
        for i, (t, s, tiempo, mej, sel) in enumerate(filas))
    datos = lambda tit, pares: (f'<b style="margin-top:6px">{tit}</b><div class="isla col" style="gap:6px;padding:10px 14px">'
                                + "".join(f'<div style="display:flex"><span>{k}</span><b style="margin-left:auto;{st}">{v}</b></div>' for k, v, st in pares) + "</div>")
    cont = f"""<div class="cabecera"><span class="h1">Sesiones</span><span class="suave">56 de 56</span></div>
<div style="display:flex;justify-content:center;gap:16px;align-items:center;margin-top:-6px">
  <div class="combo" style="width:420px;border-radius:999px;color:#999">{icono("lupa", "#888", 16)}<span style="margin-right:auto">Buscar sesión…</span></div>
  {icono("filtro", "#555", 20)}{icono("recargar", "#555", 20)}{m(1)}</div>
<div class="fila" style="flex:1;overflow:hidden">
  <div class="col" style="flex:1;gap:10px">{lista}</div>
  <div class="col" style="width:370px;gap:6px">
    <div class="isla" style="display:flex;gap:12px;height:240px"><div class="col" style="flex:1"><b style="font-size:17px">Spa {m(4)}</b>
      <svg viewBox="0 0 100 140" height="170"><path d="M30 10 L60 50 L70 90 L85 120 L60 130 L50 100 L30 110 L15 125 L20 95 L40 70 Z" fill="none" stroke="#555" stroke-width="3"/><line x1="33" y1="20" x2="40" y2="14" stroke="{ROJO}" stroke-width="3"/></svg></div>
      <div class="col" style="gap:6px;margin-top:30px;width:140px">{''.join(f'<div style="display:flex"><span>{k}</span><b style="margin-left:auto">{v}</b></div>' for k, v in [("Longitud", "6.95 km"), ("Curvas", "19"), ("Sesiones", "5"), ("Vueltas", "3"), ("Clima", "Seco")])}</div></div>
    {datos("TIEMPOS " + m(5), [("Mejor vuelta", "2:28.640", "color:#9D00FF"), ("Ritmo", "2:33.016", "")])}
    {datos("CONDICIONES INICIALES", [("Asfalto", "óptima", ""), ("Pista", "39 °C", ""), ("Aire", "31 °C", "")])}
    {datos("SESIÓN", [("Coche", "Ferrari 296 GT3", ""), ("Tipo", "Carrera", ""), ("Su mejor vuelta", "2:28.765", "")])}
  </div>
</div>"""
    return ventana(cont, activo=6), VENTANA


def analisis():
    canales = [("Velocidad", "SpeedKmh", 110, "0,100 80,20 160,28 200,90 260,95 330,20 480,18 520,85 600,88 700,12 820,30 860,92 1000,45"),
               ("Régimen", "Rpms", 55, "0,50 80,8 85,32 160,8 200,45 260,48 330,12 335,32 480,8 520,40 600,45 700,8 820,16 860,45 1000,20"),
               ("Marcha", "Gear", 40, "0,35 80,35 80,22 160,22 160,12 200,12 200,35 330,35 330,18 520,18 520,35 700,35 700,8 1000,8"),
               ("Freno", "Brake", 40, "0,38 160,38 165,4 200,6 210,38 480,38 485,4 520,15 525,38 820,38 825,4 860,8 865,38 1000,38"),
               ("Gas", "Throttle", 40, "0,4 155,4 160,38 210,38 230,4 475,4 480,38 525,38 540,4 815,4 820,38 865,38 880,4 1000,4")]
    color = {"Brake": ROJO, "Throttle": "#2eb857"}
    trazas = "".join(
        f'<div style="background:#efefef;border-top:1px solid #ddd;position:relative;height:{h + 24}px">'
        f'<div style="position:absolute;left:8px;top:3px">{nom}</div><div style="position:absolute;left:180px;top:3px;color:{color.get(c, "#555")}">{c}</div>'
        f'<svg style="position:absolute;left:60px;top:20px" width="1030" height="{h}" viewBox="0 0 1000 {h}" preserveAspectRatio="none">'
        f'<polyline points="{p}" fill="none" stroke="#bbb" stroke-width="2" transform="translate(12,2)"/>'
        f'<polyline points="{p}" fill="none" stroke="{color.get(c, "#333")}" stroke-width="2"/></svg></div>'
        for nom, c, h, p in canales)
    cont = f"""<div class="cabecera"><span class="pill">&#8249; Sesiones</span>{m(1)}<span class="h1">Análisis</span>
<span class="suave" style="font-size:14px">Assetto Corsa Competizione · Ferrari 296 GT3 · Spa</span></div>
{tabs(["Base", "Vehículo", "Suspensión", "Circuito"], 0, marca=2)}
<div class="subtabs" style="padding-left:14px;align-items:center"><span class="activo">COMPARE</span><span>DELTA</span><span>DRIVER</span><span>WHEELSPD</span><span>US-OS</span><span>FUERZAS</span><span>RPM HISTO</span><span>SUSP HISTO</span>{m(3)}</div>
<div style="display:flex;align-items:center;gap:12px"><span>&#8249;</span><span class="pill" style="border-radius:6px">V2 &nbsp;2:28.765</span><span>&#8250;</span>
  <span class="suave">frente a</span><span class="pill" style="border-radius:6px;border-color:#9D00FF;color:#9D00FF">V3 &nbsp;2:28.640</span>{m(4)}
  <span style="margin-left:auto;display:flex;gap:14px;font-size:12px"><span style="color:{ROJO}">&#9632; Vuelta no válida</span><span style="color:#d9a21b">&#9632; Parada en boxes</span><span style="color:#9D00FF">&#9632; Vuelta más rápida</span></span></div>
<div style="display:flex;align-items:center;gap:4px"><div style="background:#efefef;border-radius:8px;font-size:11px;font-weight:700;flex:1">
  <div style="display:flex;align-items:center;height:22px"><span style="width:60px;padding-left:6px">VUELTA</span><div style="flex:1;display:flex;gap:2px;padding-right:4px"><div style="flex:1;background:#d0d0d0;text-align:center">V1</div><div style="flex:1;outline:2px solid #444;text-align:center">V2 2:28.765</div><div style="flex:1;background:#9D00FF55;text-align:center">V3 2:28.640</div></div></div>
  <div style="display:flex;align-items:center;height:20px"><span style="width:60px;padding-left:6px">SECTOR</span><div style="flex:1;display:flex;gap:2px;padding-right:4px">{''.join(f'<div style="flex:1;background:{c};text-align:center">{s}</div>' for s, c in [("S1 +0.08", "#f2c23066"), ("S2 -0.21", "#2eb85766"), ("S3 +0.01", "#d0d0d0")])}</div></div>
  <div style="display:flex;align-items:center;height:20px"><span style="width:60px;padding-left:6px">CURVA</span><div style="flex:1;display:flex;gap:2px;padding-right:4px">{''.join('<div style="flex:1;background:#dadada;text-align:center">C' + str(i) + '</div>' for i in range(1, 20))}</div></div></div>{m(5)}</div>
<div style="display:flex;align-items:center;gap:4px;flex:1;min-height:0"><div style="flex:1;border-radius:8px;overflow:hidden;position:relative">{trazas}
  <div style="position:absolute;left:520px;top:0;bottom:0;border-left:1.5px dashed {ROJO}"></div>
  <div style="position:absolute;left:506px;top:40px">{m(7)}</div></div>{m(6)}</div>
<div style="display:flex;justify-content:space-between;padding:0 34px 0 70px;font-size:11px;color:#666;margin-top:-8px"><span>0:00.000</span><span>0:37.191</span><span>1:14.382</span><span>1:51.574</span><span>2:28.765</span></div>"""
    return ventana(cont, activo=6), VENTANA


# ---------------------------------------------------------------- 8.7.9
def ajustes():
    izquierda = "".join(
        f'<div style="display:flex;align-items:center;gap:14px"><div class="col" style="gap:3px;flex:1"><span>{t}{m(2) if i == 1 else ""}</span>'
        f'<span class="suave" style="font-size:12px">{d}</span></div>{c}</div>'
        for i, (t, d, c) in enumerate([
            ("Idioma", "Se aplicará al volver a abrir la aplicación.", '<div class="combo" style="width:200px">Español</div>'),
            ("Modo oscuro", "Desactívalo para usar la paleta en claro.", '<span class="toggle si"></span>'),
            ("Continúa ejecutándose en segundo plano al cerrar", "Al cerrar la ventana sigue en el área de notificación.", '<span class="toggle"></span>'),
            ("Reconectar los periféricos automáticamente", "El volante y la pedalera se conectan solos al detectarse.", '<span class="toggle si"></span>'),
            ("Arrancar con Windows", "Abrir la aplicación al iniciar sesión.", '<span class="toggle"></span>'),
            ("Arrancar minimizado en la bandeja", "Al abrirse queda en el área de notificación.", '<span class="toggle"></span>'),
            ("Buscar actualizaciones al arrancar", "Avisa con una franja arriba si hay versión nueva.", '<span class="toggle si"></span>'),
            ("Abrir en la última página visitada", "Al arrancar vuelve a la última página.", '<span class="toggle si"></span>'),
            ("Notificaciones de la aplicación", "Avisos desde el área de notificación.", '<span class="toggle si"></span>')]))
    grupo = lambda t, cuerpo: f'<div class="col" style="gap:8px"><b>{t}</b>{cuerpo}</div>'
    pills = lambda *bs: '<div style="display:flex;gap:8px;flex-wrap:wrap">' + "".join(f'<span class="pill">{b}</span>' for b in bs) + "</div>"
    derecha = (grupo("Grabaciones de sesión " + m(3), '<div style="display:flex;gap:10px;align-items:center"><span class="suave">Cuántas</span><div class="combo" style="width:150px">Sin límite</div><span class="suave">Espacio</span><div class="combo" style="width:150px">Sin límite</div></div>'
                     + '<div style="display:flex;gap:10px;align-items:center"><span class="pill">Borrar sesiones</span><span class="suave">68 grabaciones · 213 MB</span></div>')
               + grupo("Puesta a punto " + m(4), pills("Menú del dash", "Asistente de configuración"))
               + grupo("Actualizaciones y copias " + m(5), pills("Buscar actualizaciones") + pills("Exportar copia", "Importar copia"))
               + grupo("Carpetas " + m(6), pills("Grabaciones", "Perfiles", "Registro", "Diagnóstico"))
               + grupo("Sobre la aplicación", '<div style="display:flex"><span>Versión</span><span style="margin-left:auto">0.11.0</span></div><div style="display:flex"><span>Contacto</span><span style="margin-left:auto">correo · LinkedIn · GitHub</span></div>'))
    cont = f"""<div class="cabecera"><span class="h1">Configuración del sistema</span></div>
{tabs(["Aplicación", "Telemetría"], 0, marca=1)}
<div class="isla fila" style="flex:1;gap:0">
  <div class="col" style="flex:1;gap:18px;padding-right:24px;border-right:1px solid #d6d6d6">{izquierda}</div>
  <div class="col" style="flex:1;gap:22px;padding-left:24px">{derecha}</div>
</div>"""
    return ventana(cont, activo=7), VENTANA

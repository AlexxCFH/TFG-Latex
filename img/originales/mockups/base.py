"""Piezas comunes de los mockups de la interfaz de VH SimGrid (capítulo 8.7-8.8).

Cada mockup es un HTML que Chrome sin ventana convierte en PNG (render.py).
Estilo de wireframe: grises neutros, el rojo de la marca solo para lo activo y
para los números de las llamadas, que el texto del capítulo referencia.
"""
import os
import re

RAIZ_APP = r"C:\Users\Alejandro\Desktop\Nueva carpeta\ui\configurador"
ICONOS = os.path.join(RAIZ_APP, "assets", "iconos")
FUENTES = os.path.join(RAIZ_APP, "assets", "fuentes").replace("\\", "/")

ROJO = "#FF073A"


def icono(nombre, color="#555", lado=24):
    """SVG real de assets/iconos recoloreado (vienen pintados en crema)."""
    ruta = os.path.join(ICONOS, nombre + ".svg")
    with open(ruta, encoding="utf-8") as f:
        svg = f.read()
    svg = re.sub(r"<\?xml[^>]*>", "", svg)
    svg = svg.replace("#F2EAE3", color).replace("#f2eae3", color)
    svg = re.sub(r"<svg ", f'<svg style="width:{lado}px;height:{lado}px;display:block" ', svg, count=1)
    svg = re.sub(r'\swidth="[\d.]+"', "", svg, count=1)
    svg = re.sub(r'\sheight="[\d.]+"', "", svg, count=1)
    return svg


CSS = f"""
@font-face {{ font-family: Roboto; src: url('file:///{FUENTES}/Roboto-Regular.ttf'); font-weight: 400; }}
@font-face {{ font-family: Roboto; src: url('file:///{FUENTES}/Roboto-Medium.ttf'); font-weight: 500; }}
@font-face {{ font-family: Roboto; src: url('file:///{FUENTES}/Roboto-Bold.ttf'); font-weight: 700; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #ffffff; font-family: Roboto, sans-serif; color: #333; font-size: 13px; }}
.lienzo {{ position: relative; padding: 18px; }}
.ventana {{ position: relative; width: 1240px; height: 800px; border: 2px solid #444; border-radius: 6px;
           overflow: hidden; display: flex; flex-direction: column; background: #fafafa; }}
.titlebar {{ height: 32px; background: #3a3a3a; color: #eee; display: flex; align-items: center;
            padding: 0 12px; font-size: 12px; gap: 8px; flex: none; }}
.titlebar .logo {{ font-weight: 700; color: {ROJO}; font-style: italic; }}
.titlebar .ctrl {{ margin-left: auto; display: flex; gap: 22px; color: #ccc; font-size: 14px; }}
.cuerpo {{ flex: 1; display: flex; min-height: 0; }}
.sidebar {{ width: 70px; background: #e2e2e2; border-right: 1px solid #c8c8c8; display: flex;
           flex-direction: column; align-items: center; padding-top: 14px; gap: 20px; flex: none; }}
.sidebar .marca {{ font-weight: 700; font-style: italic; font-size: 22px; color: #555; margin-bottom: 6px; }}
.sidebar .item {{ position: relative; width: 70px; display: flex; justify-content: center; }}
.sidebar .item.activo::before {{ content: ''; position: absolute; left: 0; top: 2px; bottom: 2px; width: 3px; background: {ROJO}; }}
.sidebar .abajo {{ margin-top: auto; margin-bottom: 16px; }}
.pagina {{ flex: 1; padding: 12px 26px 22px 26px; display: flex; flex-direction: column; gap: 12px; min-width: 0; }}
.footer {{ height: 28px; background: #3a3a3a; color: #ddd; font-size: 11px; display: flex;
          align-items: center; padding: 0 12px; flex: none; }}
.footer .centro {{ margin: 0 auto; }}
.footer .logo {{ font-weight: 700; color: {ROJO}; font-style: italic; }}
.cabecera {{ display: flex; align-items: center; gap: 14px; min-height: 40px; }}
.h1 {{ font-size: 21px; font-weight: 700; color: #222; }}
.h2 {{ font-size: 17px; font-weight: 700; color: #222; }}
.h3 {{ font-size: 14px; font-weight: 500; color: #555; }}
.suave {{ color: #888; }}
.estado {{ font-size: 14px; display: inline-flex; align-items: center; gap: 6px; }}
.estado::before {{ content: ''; width: 7px; height: 7px; border-radius: 50%; background: currentColor; }}
.ok {{ color: #2eb857; }} .ko {{ color: {ROJO}; }}
.pill {{ border: 1.5px solid #444; border-radius: 999px; padding: 6px 20px; font-size: 12px; font-weight: 700;
        color: #333; background: #fff; white-space: nowrap; display: inline-block; text-align: center; }}
.pill.primario {{ background: {ROJO}; border-color: {ROJO}; color: #fff; padding: 8px 30px; }}
.pill.off {{ border-color: #c4c4c4; color: #b0b0b0; background: #f0f0f0; }}
.pill.mini {{ padding: 3px 12px; font-size: 11px; }}
.pill.on {{ background: #444; color: #fff; }}
.perfil {{ margin-left: auto; display: flex; align-items: center; gap: 10px; font-size: 14px; color: #666; }}
.check {{ width: 16px; height: 16px; border: 1.5px solid #999; border-radius: 3px; display: inline-block; background: #fff; }}
.check.si {{ background: {ROJO}; border-color: {ROJO}; }}
.combo {{ border: 1px solid #bbb; border-radius: 6px; background: #fff; padding: 8px 12px; display: flex;
         align-items: center; justify-content: space-between; gap: 18px; font-size: 13px; color: #444; }}
.combo::after {{ content: ''; width: 7px; height: 7px; border-right: 2px solid #666; border-bottom: 2px solid #666;
                transform: rotate(45deg) translateY(-3px); }}
.tabs {{ background: #ececec; border-radius: 12px; height: 62px; display: flex; justify-content: center;
        align-items: center; gap: 46px; flex: none; }}
.tab {{ font-size: 18px; font-weight: 500; color: #555; padding: 8px 10px; }}
.tab.activo {{ color: {ROJO}; border-bottom: 3px solid {ROJO}; }}
.subtabs {{ display: flex; gap: 26px; font-size: 14px; color: #555; }}
.subtabs .activo {{ color: #222; border-bottom: 2px solid {ROJO}; padding-bottom: 6px; }}
.isla {{ background: #efefef; border: 1px solid #dadada; border-radius: 12px; padding: 16px 18px; }}
.subisla {{ background: #e4e4e4; border: 1px solid #d2d2d2; border-radius: 10px; padding: 10px 14px; }}
.fila {{ display: flex; gap: 20px; }}
.col {{ display: flex; flex-direction: column; gap: 10px; }}
.ayuda {{ display: inline-flex; width: 13px; height: 13px; border-radius: 50%; border: 1px solid #999;
         font-size: 8px; font-weight: 700; align-items: center; justify-content: center; color: #777;
         vertical-align: middle; margin-left: 4px; }}
.slider {{ display: flex; align-items: center; gap: 12px; }}
.slider .riel {{ flex: 1; height: 4px; background: #cfcfcf; border-radius: 2px; position: relative; }}
.slider .riel i {{ position: absolute; left: 0; top: 0; bottom: 0; background: #888; border-radius: 2px; }}
.slider .riel b {{ position: absolute; top: -7px; width: 18px; height: 18px; border-radius: 50%; background: #fff;
                  border: 2px solid #777; margin-left: -9px; }}
.slider .valor {{ width: 70px; border: 1px solid #ccc; background: #fff; border-radius: 4px; text-align: center;
                 padding: 4px 0; font-size: 12px; color: #555; }}
.toggle {{ width: 46px; height: 24px; border-radius: 12px; background: #cfcfcf; position: relative; flex: none; }}
.toggle::after {{ content: ''; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px; border-radius: 50%; background: #fff; }}
.toggle.si {{ background: {ROJO}; }}
.toggle.si::after {{ left: 25px; }}
.ph {{ background: #dcdcdc; border: 1px solid #c4c4c4; border-radius: 8px; position: relative; overflow: hidden;
      display: flex; align-items: flex-end; justify-content: center; color: #555; font-size: 12px; font-weight: 500; }}
.ph.x {{ background: linear-gradient(to top right, transparent calc(50% - 1px), #c4c4c4, transparent calc(50% + 1px)),
                     linear-gradient(to top left, transparent calc(50% - 1px), #c4c4c4, transparent calc(50% + 1px)), #e3e3e3; }}
.barra {{ height: 26px; border-radius: 13px; background: #e2e2e2; border: 1px solid #d0d0d0; position: relative;
         overflow: hidden; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; }}
.barra i {{ position: absolute; left: 0; top: 0; bottom: 0; opacity: .55; }}
.barra span {{ position: relative; }}
.n {{ position: absolute; width: 26px; height: 26px; border-radius: 50%; background: {ROJO}; color: #fff;
     font-weight: 700; font-size: 14px; display: flex; align-items: center; justify-content: center;
     box-shadow: 0 0 0 3px #fff; z-index: 10; }}
.ni {{ display: inline-flex; width: 24px; height: 24px; border-radius: 50%; background: {ROJO}; color: #fff;
      font-weight: 700; font-size: 13px; align-items: center; justify-content: center; flex: none;
      vertical-align: middle; margin: 0 4px; box-shadow: 0 0 0 2px #fff; font-style: normal; }}
.marco-rojo {{ outline: 2.5px solid {ROJO}; outline-offset: -1px; }}
.region {{ position: absolute; border: 2px dashed {ROJO}; border-radius: 8px; z-index: 9; }}
.leyenda {{ position: absolute; background: #fff; color: {ROJO}; font-weight: 700; font-size: 13px; padding: 2px 8px;
           border: 1.5px solid {ROJO}; border-radius: 6px; z-index: 10; white-space: nowrap; }}
"""

SIDEBAR = ["inicio", "volante_ffb", "volante", "pedalera", "dash", "engineer", "tipo_traza"]


def ventana(contenido, activo=0, extra="", juego="Ningún simulador detectado", sidebar=True):
    items = []
    for i, nombre in enumerate(SIDEBAR):
        color = ROJO if i == activo else "#555"
        cls = "item activo" if i == activo else "item"
        items.append(f'<div class="{cls}">{icono(nombre, color, 30)}</div>')
    cls_aj = "item abajo activo" if activo == 7 else "item abajo"
    items.append(f'<div class="{cls_aj}">{icono("ajustes", ROJO if activo == 7 else "#555", 30)}</div>')
    barra = (f'<div class="sidebar"><div class="marca">VH</div>{"".join(items)}</div>' if sidebar else "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="lienzo"><div class="ventana">
  <div class="titlebar"><span class="logo">VH</span> VH SimGrid<span class="ctrl"><span>&#8211;</span><span>&#9633;</span><span>&#10005;</span></span></div>
  <div class="cuerpo">{barra}<div class="pagina">{contenido}</div></div>
  <div class="footer"><span>Versión 0.11.0 &nbsp;|&nbsp; Copyright © 2026 VH SimGrid</span><span class="centro">{juego}</span><span class="logo">VH</span></div>
</div>{extra}</div></body></html>"""


def n(numero, x, y):
    """Llamada numerada en coordenadas del lienzo (x, y en px desde la esquina)."""
    return f'<div class="n" style="left:{x}px;top:{y}px">{numero}</div>'


def m(numero):
    """Llamada numerada en línea, pegada al elemento que señala."""
    return f'<span class="ni">{numero}</span>'


def slider(etiqueta, pos, valor, ayuda=True, marca=""):
    a = ('<span class="ayuda">!</span>' if ayuda else "") + marca
    return (f'<div class="col" style="gap:4px"><div>{etiqueta}{a}</div><div class="slider">'
            f'<div class="riel"><i style="width:{pos}%"></i><b style="left:{pos}%"></b></div>'
            f'<div class="valor">{valor}</div></div></div>')


def cabecera_periferico(nombre, perfil, conectado=True, marca=1):
    est = '<span class="estado ok">Conectado</span>' if conectado else '<span class="estado ko">Desconectado</span>'
    boton = "Desconectar" if conectado else "Conectar"
    return f"""<div class="cabecera"><span class="h1">{nombre}</span>{est}<span class="pill">{boton}</span>
<div class="perfil">{m(marca) if marca else ""}<span class="check si"></span> Automático <span class="ayuda">!</span>
<span style="margin-left:8px">Perfil</span><div class="combo" style="width:200px">{perfil}</div>
<span class="pill">Guardar</span><span class="pill">Nuevo</span><span class="pill">Borrar</span></div></div>"""


def tabs(nombres, activo=0, marca=None):
    pre = m(marca) if marca else ""
    return f'<div class="tabs">{pre}' + "".join(
        f'<span class="tab{" activo" if i == activo else ""}">{t}</span>' for i, t in enumerate(nombres)) + "</div>"

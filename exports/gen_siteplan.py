# -*- coding: utf-8 -*-
"""Схема за разпределение на парцела — ферма 30 000 носачки (свободно отглеждане).
Ревизия 2: по-големи халета (18×90 m) + разделени сондаж (чиста зона, СОЗ) и
торохранилище (мръсна зона, отделен портал, ~200 m отстояние)."""
from PIL import Image, ImageDraw, ImageFont
import math

ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIALB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def F(sz, bold=False): return ImageFont.truetype(ARIALB if bold else ARIAL, sz)

S = 2.5
LEFT, TOP = 80, 165
PW, PH = int(605*S), int(300*S)
CW, CH = LEFT + PW + 600, TOP + PH + 175

def MX(x): return LEFT + x*S
def MY(y): return TOP + (300 - y)*S
def box(x0, y0, x1, y1): return [MX(x0), MY(y1), MX(x1), MY(y0)]

img = Image.new("RGB", (CW, CH), "white")
d = ImageDraw.Draw(img)

C = dict(range1="#CFE8B6", range2="#C2E3A4", core="#ECE5D3", road="#D8C19E",
         house="#3F6FB0", wgarden="#9CC3E6", tech="#C0504D", manure="#8C6D31",
         silo="#9AA0A6", entry="#ED7D31", water="#2E9BD6", park="#B8BCC2",
         shelter="#4E7A33", text="#1F2933", fence="#5A4632", arrow="#1F2933",
         soz="#1C9BD6", dirty="#7A4A1E")

def dashed(p0, p1, dash=16, gap=11, fill="#000", width=3):
    x0,y0=p0; x1,y1=p1; dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy)
    if L==0: return
    ux,uy=dx/L,dy/L; n=0.0
    while n<L:
        a=(x0+ux*n,y0+uy*n); m=min(n+dash,L); b=(x0+ux*m,y0+uy*m)
        d.line([a,b], fill=fill, width=width); n+=dash+gap

def dashed_circle(cx, cy, r, fill, width=2, seg=16):
    pts=[]; n=64
    for i in range(n+1):
        a=2*math.pi*i/n; pts.append((cx+r*math.cos(a), cy+r*math.sin(a)))
    for i in range(0,n,2):
        d.line([pts[i],pts[i+1]], fill=fill, width=width)

def ctext(cx,cy,s,font,fill="#000",anchor="mm"): d.text((cx,cy),s,font=font,fill=fill,anchor=anchor)

def badge(x,y,num):
    px,py=MX(x),MY(y); r=15
    d.ellipse([px-r,py-r,px+r,py+r], fill="#222", outline="white", width=2)
    ctext(px,py,str(num),F(20,True),"white")

# ---- 1. zone fills ----
d.rectangle(box(0,0,605,300), fill=C["core"])
d.rectangle(box(100,0,605,120), fill=C["range1"])
d.rectangle(box(100,180,605,300), fill=C["range2"])
for xx in (268,437):
    dashed((MX(xx),MY(120)),(MX(xx),MY(0)), fill="#7AA15A", width=2)
    dashed((MX(xx),MY(300)),(MX(xx),MY(180)), fill="#6E9A50", width=2)
for (xx,lab) in ((184,"1A"),(352,"1B"),(521,"1C")): ctext(MX(xx),MY(95),lab,F(19,True),"#3C5A24")
for (xx,lab) in ((184,"2A"),(352,"2B"),(521,"2C")): ctext(MX(xx),MY(205),lab,F(19,True),"#3C5A24")

# ---- 2. roads / lanes ----
d.rectangle(box(0,146,100,154), fill=C["road"])
d.rectangle(box(100,144,206,156), fill=C["road"])
d.rectangle(box(96,0,104,300), fill=C["road"])

# ---- 3. CLEAN core (SW): borehole, parking, filter, packing ----
# borehole + tank + СОЗ ring (clean, far south-west)
d.rectangle(box(20,42,34,72), fill=C["water"], outline="#1c6e99", width=2)        # 8 borehole
d.ellipse([MX(35),MY(70),MX(49),MY(54)], fill=C["water"], outline="#1c6e99", width=2)  # tank
dashed_circle(MX(30),MY(56),58, fill=C["soz"], width=2)                            # СОЗ пояс I
ctext(MX(30),MY(56)-66,"СОЗ",F(16,True),C["soz"])
d.rectangle(box(8,82,40,116), fill=C["park"], outline="#6b6f74", width=2)          # 9 parking
d.rectangle(box(5,124,40,172), fill=C["entry"], outline="#7a3d12", width=2)        # 1 entrance/filter
d.rectangle(box(50,108,94,185), fill=C["tech"], outline="#7a2f2d", width=2)        # 2 packing/technology

# ---- 4. DIRTY zone (NW corner): manure store, far from borehole ----
d.rectangle(box(46,246,94,292), fill=C["manure"], outline="#5e4820", width=2)      # 7 manure store
# separate dirty gate on north boundary above manure
d.line([(MX(56),MY(300)),(MX(80),MY(300))], fill="white", width=7)
ctext(MX(68),MY(300)-16,"Мръсен портал (тор)",F(16,True),C["dirty"])

# ---- 5. houses 18 × 90 m (central band y120–180), winter gardens, silos ----
d.rectangle(box(110,120,200,126), fill=C["wgarden"], outline="#5a8bbf", width=2)   # WG1 (south)
d.rectangle(box(110,126,200,144), fill=C["house"], outline="#26456e", width=2)     # House 1
d.rectangle(box(110,156,200,174), fill=C["house"], outline="#26456e", width=2)     # House 2
d.rectangle(box(110,174,200,180), fill=C["wgarden"], outline="#5a8bbf", width=2)   # WG2 (north)
for xx in range(116,198,9):
    d.line([(MX(xx),MY(120)),(MX(xx),MY(118))], fill="#26456e", width=3)           # popholes -> Range1
    d.line([(MX(xx),MY(180)),(MX(xx),MY(182))], fill="#26456e", width=3)           # popholes -> Range2
for (sx,sy) in ((104,132),(108,132),(104,168),(108,168)):
    d.ellipse([MX(sx)-7,MY(sy)-7,MX(sx)+7,MY(sy)+7], fill=C["silo"], outline="#6b6f74", width=2)
d.text((MX(124),MY(135)),"ХАЛЕ 1 · 15 000",font=F(18,True),fill="white",anchor="lm")
d.text((MX(124),MY(165)),"ХАЛЕ 2 · 15 000",font=F(18,True),fill="white",anchor="lm")

# ---- 6. shelters ----
def tree(x,y):
    px,py=MX(x),MY(y); r=6
    d.ellipse([px-r,py-r,px+r,py+r], fill=C["shelter"], outline="#2f4d1f", width=2)
for (x,y) in [(150,55),(220,80),(300,45),(370,75),(450,55),(530,80),(580,40),
              (150,245),(220,220),(300,255),(370,225),(450,250),(530,220),(580,255)]: tree(x,y)

# ---- 7. badges ----
badge(22,148,1); badge(72,147,2); badge(118,135,3); badge(118,165,4)
badge(186,123,5); badge(186,177,5); badge(106,150,6); badge(70,269,7)
badge(45,57,8); badge(24,99,9); badge(350,40,10); badge(350,260,11)
badge(203,150,12); badge(150,40,13)

# ---- 8. perimeter fence + clean gate ----
for (a,b) in [((0,0),(605,0)),((605,0),(605,300)),((605,300),(0,300)),((0,300),(0,0))]:
    dashed((MX(a[0]),MY(a[1])),(MX(b[0]),MY(b[1])), dash=14, gap=9, fill=C["fence"], width=3)
d.line([(MX(0),MY(143)),(MX(0),MY(157))], fill="white", width=6)
ctext(MX(-3),MY(150),"Портал / КПП",F(17,True),C["text"],anchor="rm")

# ---- 9. dimensions ----
yb=MY(0)+46
d.line([(MX(0),yb),(MX(605),yb)], fill=C["text"], width=2)
for xx in (0,605): d.line([(MX(xx),yb-7),(MX(xx),yb+7)], fill=C["text"], width=2)
for xx in (100,200,300,400,500):
    d.line([(MX(xx),yb-5),(MX(xx),yb+5)], fill="#888", width=1); ctext(MX(xx),yb+16,str(xx),F(15),"#666")
ctext(MX(302),yb+34,"≈ 605,20 m  (дълга ос)",F(21,True),C["text"])
lab=Image.new("RGBA",(260,30),(0,0,0,0)); ld=ImageDraw.Draw(lab)
ld.text((130,15),"≈ 300,00 m",font=F(21,True),fill=C["text"],anchor="mm")
lab=lab.rotate(90,expand=True); img.paste(lab,(LEFT-58,TOP+PH//2-130),lab)

# ---- 10. north arrow ----
nx,ny=MX(560),MY(245); ang=math.radians(28); ln=58
tipx,tipy=nx+ln*math.sin(ang), ny-ln*math.cos(ang)
d.line([(nx,ny),(tipx,tipy)], fill=C["arrow"], width=5)
d.polygon([(tipx,tipy),
           (tipx-12*math.cos(ang)-7*math.sin(ang),tipy-12*math.sin(ang)+7*math.cos(ang)),
           (tipx+7*math.cos(ang)-12*math.sin(ang),tipy+7*math.sin(ang)+12*math.cos(ang))], fill=C["arrow"])
ctext(tipx+9,tipy-6,"С",F(24,True),C["arrow"])

# ---- 11. scale bar ----
sbx,sby=LEFT,TOP+PH+92
for i,seg in enumerate([(0,50),(50,100)]):
    fillc=C["text"] if i%2==0 else "white"
    d.rectangle([sbx+seg[0]*S,sby,sbx+seg[1]*S,sby+12], fill=fillc, outline=C["text"], width=2)
for v in (0,50,100): ctext(sbx+v*S,sby+26,str(v),F(15),C["text"])
ctext(sbx+118,sby+26,"m",F(15),C["text"],anchor="lm")

# ---- 12. title ----
ctext(LEFT,34,"СХЕМА ЗА РАЗПРЕДЕЛЕНИЕ НА ПАРЦЕЛА",F(38,True),C["text"],anchor="lm")
ctext(LEFT,74,"Ферма за 30 000 кокошки носачки · свободно отглеждане (яйце код 1)",F(23),"#444",anchor="lm")
ctext(LEFT,104,"Ориентировъчно ~18 ha · 2 халета × 15 000 (18 × 90 m) · изгон 2×6 ha · СХЕМАТИЧНО — подлежи на геодезично заснемане",
      F(18),"#777",anchor="lm")

# ---- 13. legend ----
LX=LEFT+PW+34; ly=TOP-6
ctext(LX,ly,"ЛЕГЕНДА",F(28,True),C["text"],anchor="lm"); ly+=44
items=[("1","Вход · санитарен филтър · биосигурност",C["entry"]),
       ("2","Технологична сграда (грейдер,\nопаковане, хладен склад)",C["tech"]),
       ("3","Хале 1 — 15 000 · 18 × 90 m (волиера)",C["house"]),
       ("4","Хале 2 — 15 000 · 18 × 90 m (волиера)",C["house"]),
       ("5","Зимна градина (Kaltscharraum)",C["wgarden"]),
       ("6","Фуражни силози",C["silo"]),
       ("7","Закрито торохранилище (мръсна зона)",C["manure"]),
       ("8","Сондаж + резервоар (чиста зона, в СОЗ)",C["water"]),
       ("9","Паркинг / весова",C["park"]),
       ("10","Изгон 1 ≈ 6 ha — паркети 1A/1B/1C",C["range1"]),
       ("11","Изгон 2 ≈ 6 ha — паркети 2A/2B/2C",C["range2"]),
       ("12","Обслужваща алея / вътр. път",C["road"]),
       ("13","Заслони / сянка в паркетите",C["shelter"])]
for num,txt,col in items:
    d.rectangle([LX,ly-13,LX+26,ly+13], fill=col, outline="#555", width=2)
    d.ellipse([LX+3,ly-10,LX+23,ly+10], fill="#222"); ctext(LX+13,ly,num,F(15,True),"white")
    lines=txt.split("\n")
    for i,t in enumerate(lines):
        ctext(LX+38, ly-7+i*22 if len(lines)>1 else ly, t, F(20), C["text"], anchor="lm")
    ly += 30 + (22 if len(lines)>1 else 0)

ly+=8; d.line([(LX,ly),(LX+560,ly)],fill="#bbb",width=2); ly+=22
ctext(LX,ly,"Чисто / мръсно зониране и вода:",F(19,True),C["text"],anchor="lm"); ly+=26
notes1=["Сондажът (8) е в чиста зона (ЮЗ), в санитарно-охранителна",
        "   зона (СОЗ, пояс I ограден ≥ 10 m; Наредба № 3/2000) и на",
        "   ~200 m от торохранилището (7) — мин. 50 m норма.",
        "Торохранилището (7) е в мръсна зона (С) с отделен портал,",
        "   по посока на вятъра, далеч от опаковането и водата."]
for t in notes1: ctext(LX,ly,t,F(17),"#333",anchor="lm"); ly+=24
ly+=6
notes2=["— — —  Периметрова ограда 1,80 m + ел. жица",
        "Халета: 2 × 18 × 90 m = 2 × 1 620 m² (~9 нос./m² под;",
        "   ~4,6/m² използваема при волиера; норма ≤ 9/m² използваема).",
        "Изгон: ≤ 2 500 нос./ha (4 m²/нос.); радиус ≤ 150 m (350 m с ≥4 заслона/ha).",
        "Биосигурност: ≥ 1 500 m от др. птицеферми/населено място (Наредба 44/2006).",
        "Ориентация: халета по дългата ос (изток–запад) за по-малко слънце.",
        "Тор: ~24 t N/год. → ~141 ha за разпръскване (нитрати)."]
for t in notes2: ctext(LX,ly,t,F(17),"#333",anchor="lm"); ly+=24

img.save("/Users/kirilg/Documents/Claude/Projects/chicken-farm/chicken-farm/exports/site-plan.png", dpi=(150,150))
print("saved", img.size)

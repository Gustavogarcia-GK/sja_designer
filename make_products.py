from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math
from pathlib import Path
OUT=Path('/mnt/data/sja_site/assets'); OUT.mkdir(exist_ok=True)
W,H=1000,700
try:
    font_b=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',34)
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24)
    small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
except: font_b=font=small=None

def base(title):
    im=Image.new('RGB',(W,H),(235,233,230)); d=ImageDraw.Draw(im)
    # subtle tabletop gradient
    for y in range(H):
        c=int(242-(y/H)*22); d.line((0,y,W,y),fill=(c,c,c-2))
    d.rectangle((0,0,W,78),fill=(24,24,24)); d.text((35,20),'SJA DESIGNER',font=font_b,fill='white')
    d.text((W-330,25),title,font=small,fill=(220,220,220))
    return im

def shadow_layer(im, box, radius=24, offset=(10,14), alpha=90):
    x0,y0,x1,y1=box; sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    ox,oy=offset; sd.rounded_rectangle((x0+ox,y0+oy,x1+ox,y1+oy),radius=radius,fill=(0,0,0,alpha)); sh=sh.filter(ImageFilter.GaussianBlur(14)); im.paste(sh,(0,0),sh)

def label(d,xy,text,size=18): d.text(xy,text,font=small,fill=(70,70,70))
def save(im,name): im.save(OUT/name,quality=92,optimize=True)

# magnet
im=base('Ímã de Geladeira'); shadow_layer(im,(270,170,730,560),30)
d=ImageDraw.Draw(im); d.rounded_rectangle((270,170,730,560),30,fill=(250,250,248),outline=(190,190,190),width=3)
d.rounded_rectangle((310,210,690,520),20,fill=(30,30,30)); d.text((370,310),'SJA',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',90),fill='white'); d.text((455,410),'Designer',font=font,fill=(190,190,190)); label(d,(335,580),'Ímã personalizado com marca SJA Designer'); save(im,'ima-geladeira.jpg')

# invitation
im=base('Convite Personalizado'); shadow_layer(im,(190,150,810,570),18); d=ImageDraw.Draw(im); d.rounded_rectangle((190,150,810,570),18,fill=(253,250,245),outline=(210,200,190),width=3)
d.text((330,205),'CONVITE',font=font_b,fill=(30,30,30)); d.text((365,265),'Seu momento',font=font,fill=(100,100,100)); d.text((345,320),'merece ser especial',font=font_b,fill=(25,25,25)); d.line((300,395,700,395),fill=(150,150,150),width=2); d.text((330,430),'Criado pela SJA Designer',font=small,fill=(90,90,90)); save(im,'convite-personalizado.jpg')

# planner
im=base('Planner'); shadow_layer(im,(260,130,740,585),12); d=ImageDraw.Draw(im); d.rounded_rectangle((260,130,740,585),12,fill=(45,45,45)); d.rectangle((285,155,715,555),fill=(248,247,243)); d.text((330,195),'PLANNER',font=font_b,fill=(30,30,30)); d.text((335,245),'SJA DESIGNER',font=small,fill=(100,100,100));
for yy in [315,365,415,465,515]: d.line((330,yy,665,yy),fill=(185,185,185),width=2)
for xx in [400,510,620]: d.line((xx,300,xx,530),fill=(205,205,205),width=2)
save(im,'planner.jpg')

# bookmark
im=base('Marca Página'); shadow_layer(im,(390,120,610,600),8); d=ImageDraw.Draw(im); d.rounded_rectangle((390,120,610,600),8,fill=(28,28,28)); d.polygon([(390,600),(500,545),(610,600)],fill=(235,233,230)); d.text((420,225),'SJA',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',58),fill='white'); d.text((425,305),'Designer',font=font,fill=(190,190,190)); d.line((455,370,545,370),fill=(190,190,190),width=2); d.text((422,405),'MARCA',font=small,fill='white'); d.text((422,435),'PÁGINA',font=small,fill='white'); save(im,'marca-pagina.jpg')

# catalog
im=base('Catálogo'); shadow_layer(im,(220,125,780,590),8); d=ImageDraw.Draw(im); d.rounded_rectangle((220,125,780,590),8,fill=(250,250,248)); d.rectangle((220,125,500,590),fill=(28,28,28)); d.text((285,230),'SJA',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',80),fill='white'); d.text((290,330),'CATÁLOGO',font=font_b,fill='white');
for x in [535,645]:
    d.rounded_rectangle((x,190,x+90,310),8,fill=(220,220,220)); d.rounded_rectangle((x,340,x+90,460),8,fill=(205,205,205))
d.text((535,500),'Produtos & soluções',font=small,fill=(70,70,70)); save(im,'catalogo.jpg')

# menu
im=base('Cardápio'); shadow_layer(im,(230,130,770,580),10); d=ImageDraw.Draw(im); d.rounded_rectangle((230,130,770,580),10,fill=(255,252,246)); d.text((380,180),'CARDÁPIO',font=font_b,fill=(30,30,30)); d.text((420,230),'SJA DESIGNER',font=small,fill=(100,100,100));
for i,y in enumerate([300,355,410,465]):
    d.ellipse((285,y,335,y+50),fill=(215,210,200)); d.text((355,y+10),f'Item personalizado {i+1}',font=small,fill=(55,55,55)); d.text((660,y+10),'R$ --',font=small,fill=(55,55,55))
save(im,'cardapio.jpg')

# boxes
im=base('Caixas Personalizadas'); d=ImageDraw.Draw(im); shadow_layer(im,(260,250,520,540),12); shadow_layer(im,(480,190,760,500),12); d=ImageDraw.Draw(im); d.polygon([(260,250),(390,185),(520,250),(390,315)],fill=(45,45,45)); d.polygon([(260,250),(390,315),(390,540),(260,465)],fill=(30,30,30)); d.polygon([(390,315),(520,250),(520,465),(390,540)],fill=(65,65,65)); d.text((315,340),'SJA',font=font_b,fill='white'); d.text((320,385),'DESIGNER',font=small,fill=(200,200,200)); d.polygon([(480,190),(620,125),(760,190),(620,255)],fill=(240,240,238)); d.polygon([(480,190),(620,255),(620,500),(480,435)],fill=(220,220,218)); d.polygon([(620,255),(760,190),(760,435),(620,500)],fill=(250,250,248)); d.text((560,315),'SJA',font=font_b,fill=(30,30,30)); save(im,'caixas-personalizadas.jpg')

# folder
im=base('Folder'); d=ImageDraw.Draw(im); shadow_layer(im,(160,150,840,570),8); d=ImageDraw.Draw(im); d.polygon([(160,150),(840,150),(760,570),(240,570)],fill=(252,252,250)); d.line((500,150,500,570),fill=(200,200,200),width=3); d.rectangle((160,150,840,235),fill=(30,30,30)); d.text((390,175),'SJA DESIGNER',font=font_b,fill='white'); d.text((245,285),'FOLDER PERSONALIZADO',font=font_b,fill=(40,40,40)); d.text((245,335),'Comunicação • Divulgação • Marca',font=small,fill=(90,90,90)); d.line((245,385,735,385),fill=(180,180,180),width=2); save(im,'folder.jpg')

# calendar
im=base('Calendário'); shadow_layer(im,(230,125,770,585),10); d=ImageDraw.Draw(im); d.rounded_rectangle((230,125,770,585),10,fill=(252,252,250)); d.rectangle((230,125,770,225),fill=(30,30,30)); d.text((420,155),'CALENDÁRIO',font=font_b,fill='white'); d.text((410,255),'SJA DESIGNER',font=font,fill=(50,50,50));
for r in range(4):
  for c in range(3):
    x=275+c*160; y=325+r*55; d.rounded_rectangle((x,y,x+125,y+38),5,fill=(238,238,235),outline=(200,200,200));
save(im,'calendario.jpg')

# receipt
im=base('Recibo'); shadow_layer(im,(330,120,670,600),4); d=ImageDraw.Draw(im); d.rectangle((330,120,670,600),fill=(255,255,252),outline=(190,190,190),width=2); d.text((405,165),'SJA',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',55),fill=(25,25,25)); d.text((385,230),'RECIBO',font=font_b,fill=(35,35,35)); d.line((375,295,625,295),fill=(170,170,170),width=2); d.text((375,325),'Recebi de: __________________',font=small,fill=(80,80,80)); d.text((375,375),'Valor: R$ ________________',font=small,fill=(80,80,80)); d.text((375,425),'Referente a: ______________',font=small,fill=(80,80,80)); d.line((375,510,625,510),fill=(160,160,160),width=2); d.text((430,530),'SJA Designer',font=small,fill=(80,80,80)); save(im,'recibo.jpg')

# other: branded pen
im=base('Outros Produtos'); d=ImageDraw.Draw(im); shadow_layer(im,(190,315,810,390),28); d=ImageDraw.Draw(im); d.rounded_rectangle((190,315,810,390),35,fill=(30,30,30)); d.rounded_rectangle((735,330,790,375),12,fill=(120,120,120)); d.polygon([(790,330),(860,352),(790,375)],fill=(45,45,45)); d.text((420,330),'SJA DESIGNER',font=font_b,fill='white'); d.rectangle((230,305,280,400),fill=(210,210,210)); d.text((350,465),'Exemplo de brinde personalizado',font=font,fill=(55,55,55)); save(im,'outros-produtos.jpg')

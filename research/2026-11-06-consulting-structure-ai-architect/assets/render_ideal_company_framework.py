from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import unicodedata
ROOT=Path(__file__).parent
FONTS=list(Path('/System/Library/Fonts').glob('*.ttc'))
def font(n,bold=False):
    key=unicodedata.normalize('NFD','ヒラギノ角ゴシック W'+('6' if bold else '3'))
    return ImageFont.truetype(str(next(p for p in FONTS if key in unicodedata.normalize('NFD',p.stem))),n)
W,H=2250,1260
INK='#173249'; TEAL='#147F8B'; BG='#F3F6F9'; MUTED='#566B7C'
im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
def text(x,y,s,size=36,bold=False,color=INK):
    d.text((x,y),s,font=font(size,bold),fill=color)
def center(x,y,s,size=36,bold=False,color=INK):
    f=font(size,bold);b=d.textbbox((0,0),s,font=f)
    d.text((x-(b[2]-b[0])/2,y-(b[3]-b[1])/2-b[1]),s,font=f,fill=color)
def box(rect,fill,outline=None,width=2,radius=20):
    d.rounded_rectangle(rect,radius=radius,fill=fill,outline=outline,width=width)
def arrow(x1,y1,x2,y2,color=TEAL,width=7):
    d.line((x1,y1,x2,y2),fill=color,width=width)
    d.polygon([(x2,y2),(x2-19,y2-13),(x2-19,y2+13)],fill=color)
text(65,45,'理想の企業像｜AとBを両方満たす環境',61,True)
text(68,139,'A：①に軸足を置き、②〜④につながる　　B：全社レベルの変革を支援する',35,color=MUTED)
box((65,220,2185,370),'#E4EFF0')
text(95,245,'B｜変革の対象範囲：全社',44,True)
text(95,315,'業務・組織・意思決定の変革を、実際の案件・事例から確認する',35)
box((65,420,2185,900),'#FFFFFF')
text(95,445,'A｜①を軸足に、②〜④にも関与できる',43,True)
x=[95,715,1205,1695]; width=[560,430,430,430]
labels=[['① 方針・構想策定','構想・方針を考える'],['② 設計','技術的な判断'],['③ 導入・実行','実装への参加'],['④ 定着・運用・改善','継続的な関与']]
for i,(left,w,lines) in enumerate(zip(x,width,labels)):
    top=590
    box((left,top,left+w,top+175),'#ECF4F5',TEAL,3)
    center(left+w/2,top+54,lines[0],35 if i<3 else 30,True)
    center(left+w/2,top+120,lines[1],32)
    if i<3:arrow(left+w+10,top+88,x[i+1]-15,top+88)
box((95,522,350,574),INK,radius=10)
center(222,548,'志向の軸足',32,True,'#FFFFFF')
d.line((2110,790,2110,832,375,832,375,790),fill=TEAL,width=6)
d.polygon([(375,780),(362,803),(388,803)],fill=TEAL)
center(1240,862,'実装・運用の知見を、構想・方針へ戻す',34,True,TEAL)
box((65,950,2185,1175),'#E8EDF4')
text(95,978,'「自分が関われるか」は、構想と実装がつながる環境から間接的に考える',40,True)
text(95,1055,'同じ案件・目標での協働　／　工程間の連動　／　技術の知見が構想に反映される',34)
text(95,1126,'企業全体の提供範囲と、本人の担当保証は分けて扱う。',30,color=MUTED)
im.save(ROOT/'ideal-company-framework.png')
print('Created ideal-company framework diagram.')

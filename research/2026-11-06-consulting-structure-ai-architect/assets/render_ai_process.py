from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import unicodedata, json
ROOT=Path(__file__).parent
FONTS=list(Path('/System/Library/Fonts').glob('*.ttc'))
def font(size,bold=False):
    key=unicodedata.normalize('NFD','ヒラギノ角ゴシック W'+('6' if bold else '3'))
    return ImageFont.truetype(str(next(p for p in FONTS if key in unicodedata.normalize('NFD',p.stem))),size)
INK='#152F44'; BG='#F2F6F8'; MUTED='#526878'
CONFIG=json.loads((ROOT.parent/'comparison.json').read_text())
COL={int(k):v['color'] for k,v in CONFIG['A']['palette'].items()}
im=Image.new('RGB',(2250,1160),BG);d=ImageDraw.Draw(im)
def txt(x,y,s,size=36,bold=False,color=INK):
    d.text((x,y),s,font=font(size,bold),fill=color)
def centered(x,y,s,size=36,bold=False,color=INK):
    f=font(size,bold);b=d.textbbox((0,0),s,font=f)
    d.text((x-(b[2]-b[0])/2,y-(b[3]-b[1])/2-b[1]),s,font=f,fill=color)
txt(65,40,'A｜工程の範囲と関与の程度',61,True)
txt(68,135,'色が付く工程の広がり＝範囲　／　色の濃さ＝関与の程度',35,color=MUTED)
left=65;labelw=570;cw=385;top=225;head=104;rh=151
LABELS={'strategy':'戦略コンサル','general':'総合コンサル','it':'ITコンサル','sier':'SIer'}
cats=[LABELS[k] for k in CONFIG['category_order']]
rows=['① 方針・構想策定','② 設計','③ 導入・実行','④ 定着・運用・改善']
levels=[row['degree'] for row in CONFIG['A']['rows']]
centered(left+labelw/2,top+head/2,'支援工程',43,True)
for j,cat in enumerate(cats):
    x=left+labelw+j*cw
    d.rounded_rectangle((x+6,top,x+cw-6,top+head-6),radius=15,fill=INK)
    centered(x+cw/2,top+head/2-3,cat,39,True,'#FFFFFF')
for i,(row,vals) in enumerate(zip(rows,levels)):
    y=top+head+i*rh
    d.rounded_rectangle((left,y+5,left+labelw-4,y+rh-5),radius=15,fill='#FFFFFF')
    txt(left+25,y+48,row,39,True)
    for j,level in enumerate(vals):
        x=left+labelw+j*cw
        d.rounded_rectangle((x+6,y+5,x+cw-6,y+rh-5),radius=15,fill=COL[level])
d.rounded_rectangle((65,962,2185,1108),radius=18,fill='#E7EEF1')
for x,key,label in [(95,4,'非常に強い'),(630,3,'強い'),(1165,2,'中程度'),(1700,1,'限定的')]:
    d.rounded_rectangle((x,988,x+76,1040),radius=7,fill=COL[key])
    txt(x+96,994,label,34,True)
txt(95,1067,'①は同程度と仮定。②〜④は関与の程度の暫定評価。白色は範囲外。判定理由と例外は詳細ページへ。',30,color=MUTED)
im.save(ROOT/'ai-process-involvement.png')
print('Created four-level involvement heatmap.')

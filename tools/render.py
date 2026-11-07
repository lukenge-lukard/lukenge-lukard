"""Rebuild the README animation. Requires Pillow: python -m pip install Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
font = ImageFont.truetype(FONT, 19)
small = ImageFont.truetype(FONT, 15)
BG, FG, DIM, GREEN = '#0d1117', '#c9d1d9', '#8b949e', '#9ece8b'
EVENTS = [
 ('2022', 'Added temporary fix', 'remove next sprint'),
 ('2023', 'Replaced frontend', 'temporary fix retained'),
 ('2024', 'Migrated database', 'temporary fix retained'),
 ('2025', 'Rebuilt backend', 'temporary fix retained'),
 ('2026', 'Tried removing temporary fix', 'everything stopped'),
 ('2026', 'Restored temporary fix', 'architecture decision'),
]
def frame(step):
 im=Image.new('RGB',(1000,490),BG); d=ImageDraw.Draw(im)
 d.rounded_rectangle((1,1,998,488),radius=8,outline='#30363d',width=2)
 d.line((1,47,998,47),fill='#30363d',width=1)
 d.text((25,15),'system.log',font=small,fill=DIM)
 for i,(year,action,note) in enumerate(EVENTS[:step+1]):
  color=GREEN if i==5 else FG
  d.text((26,76+i*37),year+'  '+action,font=font,fill=color)
  if i==step: d.text((96,318), '# '+note,font=small,fill=GREEN if i==5 else DIM)
 for x,label in [(30,'frontend'),(290,'backend'),(550,'database')]:
  d.rectangle((x,374,x+175,413),outline='#484f58')
  d.text((x+14,384),label,font=small,fill=DIM)
  d.line((x+87,414,x+87,440,850,440,850,413),fill=GREEN,width=2)
 d.rectangle((768,374,970,413),outline=GREEN,width=2)
 d.text((783,384),'temporary fix',font=small,fill=GREEN)
 d.rectangle((27,455,36,473),fill=GREEN)
 return im
if __name__=='__main__':
 frames=[frame(i) for i in range(len(EVENTS))]
 frames[0].save(ROOT/'assets/temporary-fix.gif',save_all=True,append_images=frames[1:],duration=[1600,1300,1300,1300,2000,3800],loop=0,optimize=True,disposal=2)
 frames[-1].save(ROOT/'assets/temporary-fix.png')
 print('Rendered',len(frames),'frames')

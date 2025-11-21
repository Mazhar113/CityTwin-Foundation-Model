import torch.nn as nn
import torch

class SmallCNN(nn.Module):
    def __init__(self,out_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3,16,3,padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16,32,3,padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Flatten(), nn.Linear(32*16*16,out_dim)
        )
    def forward(self,x):
        return self.net(x)

class FoundationSmall(nn.Module):
    def __init__(self):
        super().__init__()
        self.img = SmallCNN(128)
        self.ts = nn.Linear(12,64)
        self.txt = nn.Linear(16,64)
        self.ctx = nn.Linear(8,8)
        self.fuse = nn.Linear(128+64+64+8,256)
        self.head = nn.Linear(256,1)
    def forward(self,img,ts,txt,ctx):
        img_e = self.img(img)
        ts_e = self.ts(ts)
        txt_e = self.txt(txt.float())
        ctx_e = self.ctx(ctx)
        x = torch.cat([img_e,ts_e,txt_e,ctx_e], dim=-1)
        fused = self.fuse(x)
        return self.head(fused).squeeze(-1), fused

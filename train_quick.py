# quick single-step smoke test
import torch, numpy as np
from src.utils.model_small import FoundationSmall
import torch.nn.functional as F

def quick():
    m = FoundationSmall(); m.train()
    imgs = torch.tensor(np.random.rand(2,3,64,64).astype('float32'))
    ts = torch.tensor(np.random.rand(2,12).astype('float32'))
    txt = torch.tensor(np.random.randint(0,1000,size=(2,16)).astype('int64'))
    ctx = torch.tensor(np.random.rand(2,8).astype('float32'))
    labels = torch.tensor(np.random.rand(2,1).astype('float32'))
    preds, fused = m(imgs, ts, txt, ctx)
    loss = F.mse_loss(preds, labels.squeeze(-1))
    loss.backward()
    torch.save(m.state_dict(), 'model_checkpoint.pt')
    print('ok', loss.item())

if __name__ == '__main__': quick()

# small local training loop on synthetic data
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
from src.utils.model_small import FoundationSmall
import torch.nn.functional as F

class SyntheticDataset(Dataset):
    def __init__(self,n=128): self.n=n
    def __len__(self): return self.n
    def __getitem__(self,idx):
        import numpy as np
        return np.random.rand(3,64,64).astype('float32'), np.random.rand(12).astype('float32'), np.random.randint(0,1000,size=(16,)).astype('int64'), np.random.rand(8).astype('float32'), np.random.rand(1).astype('float32')

def collate(batch):
    import torch
    imgs = torch.tensor([b[0] for b in batch])
    ts = torch.tensor([b[1] for b in batch])
    txt = torch.tensor([b[2] for b in batch])
    ctx = torch.tensor([b[3] for b in batch])
    labels = torch.tensor([b[4] for b in batch]).float()
    return imgs, ts, txt, ctx, labels

if __name__ == '__main__':
    ds = SyntheticDataset(); dl = DataLoader(ds, batch_size=8, collate_fn=collate)
    m = FoundationSmall(); opt = torch.optim.AdamW(m.parameters(), lr=1e-4)
    for epoch in range(1):
        for imgs, ts, txt, ctx, labels in dl:
            preds, fused = m(imgs, ts, txt, ctx)
            loss = F.mse_loss(preds, labels.squeeze(-1))
            opt.zero_grad(); loss.backward(); opt.step()
    torch.save(m.state_dict(), 'model_checkpoint.pt')
    print('saved')

# ViT and transformer text encoder integration
from timm import create_model
from transformers import AutoModel, AutoTokenizer
import torch.nn as nn

class ViTEncoder(nn.Module):
    def __init__(self, name='vit_base_patch16_224', out_dim=768):
        super().__init__(); self.backbone = create_model(name, pretrained=True, num_classes=out_dim)
    def forward(self,x): return self.backbone(x)

class TextEncoder(nn.Module):
    def __init__(self, name='distilbert-base-uncased', out_dim=768):
        super().__init__(); self.model = AutoModel.from_pretrained(name); self.proj = nn.Linear(self.model.config.hidden_size,out_dim)
    def forward(self, input_ids, attention_mask=None):
        out = self.model(input_ids=input_ids, attention_mask=attention_mask)[0]
        return self.proj(out.mean(dim=1))

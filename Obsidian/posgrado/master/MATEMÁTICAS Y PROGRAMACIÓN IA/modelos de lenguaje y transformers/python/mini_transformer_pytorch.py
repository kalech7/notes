"""Mini Transformer causal educativo.

Requiere PyTorch. Mantiene las formas visibles y usa la primitiva SDPA actual.
No incluye RoPE ni KV cache para conservar el foco en el bloque Transformer.
"""

from __future__ import annotations

import torch
from torch import Tensor, nn
from torch.nn import functional as F


class CausalSelfAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int) -> None:
        super().__init__()
        if d_model % num_heads != 0:
            raise ValueError("d_model debe ser divisible por num_heads")
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: Tensor) -> Tensor:
        batch, seq_len, d_model = x.shape
        qkv = self.qkv(x)
        qkv = qkv.reshape(batch, seq_len, 3, self.num_heads, self.head_dim)
        q, k, v = qkv.unbind(dim=2)
        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        attended = F.scaled_dot_product_attention(
            q,
            k,
            v,
            dropout_p=0.0,
            is_causal=True,
        )
        attended = attended.transpose(1, 2).contiguous()
        attended = attended.reshape(batch, seq_len, d_model)
        return self.out(attended)


class SwiGLU(nn.Module):
    def __init__(self, d_model: int, d_ff: int) -> None:
        super().__init__()
        self.gate = nn.Linear(d_model, d_ff, bias=False)
        self.up = nn.Linear(d_model, d_ff, bias=False)
        self.down = nn.Linear(d_ff, d_model, bias=False)

    def forward(self, x: Tensor) -> Tensor:
        return self.down(F.silu(self.gate(x)) * self.up(x))


class TransformerBlock(nn.Module):
    def __init__(self, d_model: int, num_heads: int, d_ff: int) -> None:
        super().__init__()
        self.attn_norm = nn.RMSNorm(d_model)
        self.attn = CausalSelfAttention(d_model, num_heads)
        self.ffn_norm = nn.RMSNorm(d_model)
        self.ffn = SwiGLU(d_model, d_ff)

    def forward(self, x: Tensor) -> Tensor:
        x = x + self.attn(self.attn_norm(x))
        x = x + self.ffn(self.ffn_norm(x))
        return x


class MiniLM(nn.Module):
    def __init__(
        self,
        vocab_size: int = 32,
        d_model: int = 24,
        num_heads: int = 4,
        d_ff: int = 64,
        num_layers: int = 2,
    ) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.blocks = nn.ModuleList(
            TransformerBlock(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        )
        self.final_norm = nn.RMSNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)
        self.lm_head.weight = self.embedding.weight

    def forward(self, token_ids: Tensor) -> Tensor:
        x = self.embedding(token_ids)
        for block in self.blocks:
            x = block(x)
        return self.lm_head(self.final_norm(x))


def next_token_loss(logits: Tensor, token_ids: Tensor) -> Tensor:
    predictions = logits[:, :-1, :].contiguous()
    targets = token_ids[:, 1:].contiguous()
    return F.cross_entropy(
        predictions.reshape(-1, predictions.size(-1)),
        targets.reshape(-1),
    )


if __name__ == "__main__":
    torch.manual_seed(7)
    model = MiniLM()
    batch = torch.randint(0, 32, (3, 8))
    logits = model(batch)
    loss = next_token_loss(logits, batch)
    loss.backward()

    assert logits.shape == (3, 8, 32)
    assert loss.ndim == 0
    assert model.embedding.weight.grad is not None
    print("tokens:", tuple(batch.shape))
    print("logits:", tuple(logits.shape))
    print("loss:", round(loss.item(), 4))
    print("gradiente embedding:", tuple(model.embedding.weight.grad.shape))
